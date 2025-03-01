'''Name: Nan Xiao
DS5010
ICE06'''
from Record import Record
class ParentStrategy:
    def probability(self, sublist, label): # probability measures the occurance of the target variable out of the total list
        '''return the probability of that label within that list.
        For example, if I had 10 record objects, and 3 were labeled "Low Risk", this method should return 0.3 (3/10). '''
        count = 0 
        for record in sublist: # go over the records to check if the label matches
            if record.actual_label == label: 
                count += 1 # if so, occurance count + 1
        #debug: print(f"in parentstrategy: Label {label}: Count = {count}, Total = {len(sublist)}, Probability = {count / len(sublist)}")
        return count/len(sublist) if sublist else 0 # in the certain partition sublist, count the possibility of occurance of that certain label
    