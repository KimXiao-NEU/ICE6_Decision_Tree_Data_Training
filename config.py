'''Name: Nan Xiao
DS5010
ICE06
A huge dictionary --> PIVOTS'''

'''PIVOTS will just be a dictionary of strings mapping to lambda definitions.
Each key will be the name of one of our attributes (use the headers from the csv). '''
PIVOTS = { #can't just import the make_records()function or the variables, causing cyclical import problems in Python
    'Age_Mean': lambda r: int(r.attrs["Age"]) <= 63.92, # age col Mean63.92
    #'Age_mode': lambda r: int(r.attrs["Age"]) <= 82, #age col mode number
    #'Age_retire': lambda r: int(r.attrs["Age"]) <= 65, # retirement age
    'SystolicBloodPressure_Mean': lambda r: int(r.attrs['SystolicBloodPressure']) >= 157.04, #blood presure col mean157.04
    #'SystolicBloodPressure_Mode': lambda r: int(r.attrs['SystolicBloodPressure']) >= 160, # blood presure col mode number
    'OnHypertensionMedication': lambda r: r.attrs['OnHypertensionMedication']== "TRUE",
    'HasDiabetes':lambda r: r.attrs['HasDiabetes'] == "TRUE",
    "IsSmoker": lambda r: r.attrs["IsSmoker"] == "TRUE",
    'TotalCholesterol_Mean': lambda r: int(r.attrs['TotalCholesterol']) >= 177.78,#Total Cholesterol col mean177.78
    #'TotalCholesterol_Mode': lambda r: int(r.attrs['TotalCholesterol']) >= 242, # Total Cholesterol col mode
    'HDLcholesterol_Mean': lambda r: int(r.attrs['HDLcholesterol']) >= 51.27, # HDL Cholesterol col mean 51.27
    #'HDLcholesterol_Mode': lambda r: int(r.attrs['HDLcholesterol']) >= 64, # HDL col Mode number
    'IsAfricanAmerican': lambda r: r.attrs['IsAfricanAmerican'] == "TRUE",
    'Gender': lambda r: r.attrs["Gender"] == "Male"
}
### References
'''
- Cleveland Clinic. "Cholesterol Numbers: What Do They Mean?" Accessed February 24, 2025. https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean.
  - Used for Total Cholesterol 3-way split thresholds: <200 mg/dL (healthy), 200–239 mg/dL (borderline), ≥240 mg/dL (high).
'''


