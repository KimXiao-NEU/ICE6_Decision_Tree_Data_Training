'''Name: Nan Xiao
DS5010
ICE 06'''
import csv
import statistics
from Record import Record
from collective_impurity_entropy import CollectiveImpurityEntropy
from collective_impurity_gini import CollectiveImpurityGini
from config import PIVOTS
from Treenode import TreeNode

def _generate_attrs(row):# each row would be a dictionary value
    return {key.replace(' ', ''): value for key, value in row.items() if key != "Assessment"} 
# key.strip() only removes leading and trailing spaces, while key.replace(" ", "") removes all spaces within the string.

def _get_class(row):
    """
    training_data1.csv stores an assessment as 1 of 2 strings: "Low Risk" or "high Risk".  This function converts it to an int
    Param row: dict representing a single row of our csv.
    Returns: either 0 or 1 if Assessment is correctly formatted.  Raises exception if data is invalid
    """
    #if row['Assessment'] == "Low Risk":
    #    return 0
    #elif row['Assessment'] == "High Risk":
    #    return 1
    #raise TypeError("Assessment " + row["Assessment"] + " is invalid.  Must be either `Low Risk` or `High Risk`")
    return row['Assessment']

def _make_record(row):
    attrs = _generate_attrs(row)
    actual_label = _get_class(row)
    return Record(attrs, actual_label)

def make_records(filepath): 
   with open(filepath, newline='', mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        records = []
        for row in reader:
            records.append(_make_record(row))
        return records 
'''treat all of the different attributes for a single row as a list and set it to the attrs attribute in record.  
Then use the "Assessment" column to assign the "actual_label" attr in Record.'''

file = 'sufficiently_noisy_data-1.csv'
file_check = 'checking_data.csv'
actual_file = 'ICE6TrainingDataFile.csv'
record_list = make_records(actual_file)
strategy = CollectiveImpurityEntropy()
#Then make an object of TreeNode called root that takes in that list of records and the PIVOTS data structure.
root = TreeNode(record_list,PIVOTS.copy())
root.grow_tree(strategy)
test_record_list = make_records('test_data.csv')
rec = root.classify_records(test_record_list)

# accuracy calculation
acc = sum([1 for r in rec if r.actual_label == r.predicted_label])/len(rec)
print(f"{acc:.3f}")

correct_count = 0
incorrect_count = 0
total_count = len(rec)

for r in rec:
    print(f"Record ID: {r.attrs.get('ID', 'Unknown')}, Actual: {r.actual_label}, Predicted: {r.predicted_label}")
    if r.actual_label == r.predicted_label:
        correct_count += 1
    else:
        incorrect_count += 1
        print(f" -- Mismatch: Actual = {r.actual_label}, Predicted = {r.predicted_label}")

acc = correct_count / total_count
print(correct_count)
print(incorrect_count)
print(f"\nTotal correct: {correct_count}/{total_count}")
print(f"Calculated Accuracy: {acc:.3f}")
'''
age_mean = statistics.mean(int(r.attrs["Age"]) for r in record_list)

blood_mean = statistics.mean(int(r.attrs['SystolicBloodPressure']) for r in record_list)

cholestrol_mean =  statistics.mean(int(r.attrs['TotalCholesterol']) for r in record_list)

HDL_mean = statistics.mean(int(r.attrs['HDLcholesterol']) for r in record_list)
print(f"Average Col data: age = {age_mean:.1f} , blood = {blood_mean:.1f}, total chol = {cholestrol_mean:.1f}, HDL = {HDL_mean:.1f} ")
'''