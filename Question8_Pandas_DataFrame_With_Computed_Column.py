import pandas as pd
#creating a data set with a dictionary:
data_columns =  {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210]
}

#creating the data frame:
data_frame = pd.DataFrame(data_columns)
data_frame["BxC"] = data_frame["B"] * data_frame["C"]

#pringint out the new data frame
print(data_frame)
