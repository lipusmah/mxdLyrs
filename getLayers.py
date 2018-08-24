import arcpy  
import Tkinter as tk
import tkFileDialog
import time
import os

"""
Script: 
Opens tkinter open file window for selecting mxd file. It lists
parent layers; layer name ; source directory as a CSV file.

Script uses bat file for lunching and will use ArcGis python interpreter
usually saved in c/Python27/ArcGIS....

Path to mentioned interpreter has to be specified in bat file.

bat file is by default writen for arcgis 10.4


Blaz Lipus

"""
class lyrExtractor:

    def __init__(self):
        print("\n")
        root = tk.Tk()
        root.withdraw()
        self.mxd_path = tkFileDialog.askopenfilename()
        self.out_dir = tkFileDialog.askdirectory()

        #pridobi txt file name in path
        if self.mxd_path.split(".")[-1] != "mxd":
            print("Selected file is not *.mxd file or was the file 'open' operation canceled before selecting.")
            print("Rerun and select *.mxd file.")
            raise WrongFileError
        
    def extract(self):
        start = time.time()

        print("Starting *.lyr extracting procedure for all layers in selected mxd file...\n")
        
        mxd = arcpy.mapping.MapDocument(self.mxd_path)  
        print("Starting process on file: {}\n".format(self.mxd_path))
        
        layers = arcpy.mapping.ListLayers(mxd)      
        for lyr in layers:
            fn = self.out_dir+"/"+str(lyr)+".lyr"
            lyr.saveACopy(fn)

        stop = time.time()
        
        print("Process took {} sec and successfully finished!!\n".format(round(stop-start, 3)) )
        
        print("Lyrs file saved in:  {}".format(self.out_dir))

class WrongFileError(Exception):
    pass

if __name__ == "__main__":
    ex = lyrExtractor()
    ex.extract()
