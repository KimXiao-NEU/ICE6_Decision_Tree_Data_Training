'''Name: Nan Xiao
DS5010
ICE06'''
import math
from ParentStrategy import ParentStrategy
class CollectiveImpurityEntropy(ParentStrategy):
    def __init__(self):
        super().__init__()
    '''calculates the weighted sum of a partition using the Entropy calculation
    Entropy can be more sensitive to small changes outside of a dominant class'''
    def entropy(self, sublist): 
        if not sublist:
            return 0
        prob = self.probability(sublist, 'Low Risk') 
        q = 1 - prob  # Store `1 - prob` instead of recomputing it
        return -sum(p * math.log2(p) for p in (prob, q) if p > 0) # note that prob is always less than 1 and log2 of prob will be negative.
    
    def calculate(self,lists):
        #computes weighted entropy sum across all subsets --> score
        total_records = sum(len(sublist)for sublist in lists) # the total number of records in the csv file
        if total_records == 0:
            return 0
        weighted_entropy = 0
        for sublist in lists:
            weighted_entropy +=  len(sublist)/total_records * self.entropy(sublist) # use weighted 
            # DebuggingL print(f"each sublist the weighted_entropy{weighted_entropy}")
        return weighted_entropy
            

        