# -*- coding: utf-8 -*-
# Write/read a CSV file
import csv            # For reading and writing csv data
import numpy as np    # For extended calculation
import pandas as pd

# Write out ndarray in a csv format
def csv_writer(output_path, data_array, title_array, indexflag=False):
    df = pd.DataFrame()

    for i, title in enumerate(title_array):
        df[title] = data_array[:, i]
    
    df.to_csv(output_path, index = indexflag)
    return True

# Load CSV data as a ndarray
class CSVHandler:

    # Constructor
    def __init__(self, filename):
        self.__filename = filename # csv file name (private in each instance)
        self.points = [] # point cloud data 
        self.rowsize = 0 #    row size of csv table
        self.colsize = 0 # column size of csv table

    # load csv data as a ndarray
    def read_csv(self, ignore_row_num, get_info=False):
        try:
            with open(self.__filename, encoding = "utf_8_sig") as f:
                _reader = csv.reader(f)
                self.points = [row for row in _reader]
            self.points = np.matrix(self.points)          # convert to np.matrix type for easier slicing.
            self.points = self.points[ignore_row_num:, :] # remove the titie row, in concrete terms, Row No.1 ~ No.ignore_row_num (0 means "ignore nothing")
            self.points = self.points.astype(np.float64)  # change type from str to float64
            self.rowsize = self.points.shape[0]
            self.colsize = self.points.shape[1]
        except:
            print(f"Error loading {self.__filename}")
            return False

        if get_info: # if necessary, output infomation about CSV
            self.get_info()
        return True

    # simply output CSV data info
    # Arguments: none, Return value: none
    def get_info(self):
        print("\n########## CSV Data Info ##########")
        print(f"CSV filename: {self.__filename}")
        print(f"row   size  : {self.rowsize}")
        print(f"colum size  : {self.colsize}")
        print(f"points: \n{self.points}")
        print("#####################################\n")
