'''Name: Nan Xiao
DS5010
HW05'''
class Record:
    def __init__(self, input_values, actual_label): #dictionary
        # create a tuple of values to represent x (that always starts with out bias value)
        
        self.attrs = input_values
        self.actual_label = actual_label
        self.predicted_label = None

    def __str__(self):
        return f"Record(attrs = {self.attrs}, actual = {self.actual_label}, predicted = {self.predicted_label}"