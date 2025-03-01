'''Name: Nan Xiao
DS5010
ICE 06'''
from collective_impurity_entropy import CollectiveImpurityEntropy
from collective_impurity_gini import CollectiveImpurityGini
from config import PIVOTS
from Record import Record
class TreeNode:
    def __init__(self, records, pivot_choices):
        self.records_1d = records
        self.pivot_choices = pivot_choices.copy()# because we need to edit the dictionary constantly, so we are making a copy of it
        self.children = []
        self.label_to_apply = None # predicted label 
        self.partition_logic = None # which partition strategy to choose
        self.low_count = 0
        self.high_count = 0
        self._count_labels() # ensures count are always correct at initialization
    
    def _count_labels(self):
        for record in self.records_1d:
            if record.actual_label == 'High Risk':
                self.high_count += 1
            if record.actual_label == 'Low Risk':
                self.low_count += 1
        # not necessary return low_count, high_count
    
    def is_homogenous(self):
        return self.low_count == len(self.records_1d) or self.high_count == len(self.records_1d)#check if the dataset has been homogenous already

        
    def grow_tree(self, strategy, i = 0): # calculator which strategy
        indent = "    " * i
        print(f"Growing tree at depth {i} with {len(self.records_1d)} records")
        print(f"  - Low Risk count: {self.low_count}")
        print(f"  - High Risk count: {self.high_count}")
        
        if self.is_homogenous() or len(self.pivot_choices) == 0:
            if self.high_count == 0 :
                self.label_to_apply = 'Low Risk'     
            if self.low_count == 0 or len(self.pivot_choices) == 0:
                self.label_to_apply = 'High Risk'
                #print (f"{indent} Leaf Node --> {self.label_to_apply} ")
                return       
        # are we done spliiting?
        partitions = self.find_best_partition(self.records_1d,strategy)
        if any(len(sublist) == 0 for sublist in partitions):
            #print(f"{indent}, Stopping recursion due to empty partition.")  
            return 
        print(f"{indent} Splitting on: {self.best_label}")  
        for sublist in partitions:
            #print(f"{indent} Branch {i+1} ({len(sublist)} records)")
            child = TreeNode(sublist,self.pivot_choices) # make a treenode
            self.children.append(child)# put that treenode into self.children
            #print("\t"*i, "recursing with: ",self.records_1d, i+1) #x-1 --> the popped labels
            child.grow_tree(strategy, i+1) # for each tree node in children
        if i >= 20:
            # print("\t"*i, "hit too many recursive steps- terminating")
            return None

    
    def find_best_partition(self,records_1d, strategy): #an object (of either InformationGain or CollectiveImpurity)
        '''For each lambda in PIVOTS, try partitioning the 
        record list using that lambda, then use the object's calculate function to evaluate the quality.'''
        #print out which key partition was the best
        self.best_label = None
        best_score = float('inf') # the lower the better
        best_records_split = []
        for key , lam in self.pivot_choices.items():  
            partitions = self.make_partition(records_1d, key)
            left_size = len(partitions[0])
            right_size = len(partitions[1])
            # print(f"Trying partion on {key}")
            # print(f"  - Left partition size (below {key}: {left_size})")
            # print(f"  - Right partition size (below {key}: {right_size})")
            
            if left_size == 0 or right_size == 0:
                # print(f" XX Skipping{key}, results in empty partition!")
                continue
            score = strategy.calculate(partitions)
            # print(f"Entropy score for the partition is {score}")
            # print(f"current best score is  {best_score}")
            if score < best_score:
                best_score = score
                self.partition_logic = lam
                self.best_label = key
                best_records_split = partitions
                # print("found best label", self.best_label)
                
                #print(f"Node Data: {[record.attrs for record in self.records_1d]}")
                #print(f"Recursing with best label: {self.best_label}, remaining pivots: {list(self.pivot_choices.keys())}")
        if self.best_label is not None:
            self.pivot_choices.pop(self.best_label,None)
        print("---")
        return best_records_split


    def make_partition(self,records_1d,key):
        ''' subdivide our list of records based on one of our keys.'''
        left_split = []
        right_split = []
        for record in records_1d:
            if self.pivot_choices[key](record):
                left_split.append(record)
            else:
                right_split.append(record)
            
        return left_split, right_split
    
    def __repr__(self):
        return f"TreeNode({self.best_label}, {len(self.records_1d)} records)"
    
    def classify_record_single(self, record_object):
        """
        classifies a single record object
        Param: record_object - an object of the record class
        returns: that record object with the predicted_label field set
        """
        if len(self.children) == 0:
            record_object.predicted_label = self.label_to_apply
            return record_object
        else:
            if self.partition_logic(record_object) == True:
                child = self.children[0]
            else:
                child = self.children[1]
            child.classify_record_single(record_object)


    def classify_records(self, record_list):
        """
        classifies a list of record objects
        """
        for record_object in record_list:
            self.classify_record_single(record_object)
        return record_list