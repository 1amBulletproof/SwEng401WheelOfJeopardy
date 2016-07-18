#!/usr/bin/python27
# Path to python

# Written by Brandon Tarney
# 12.20.14
# program purpose: Create file manipulation classes...these classes will use REGEX, data structures & File reading/writing

from os import listdir 															# need package to find all csv files in given directory
import csv 																		# need to read csv's
																	# For testing purposes
import Tkinter														# for selecting the document to use
from tkFileDialog import askopenfilename

class FileComparisonGUI(Tkinter.Tk):
	def __init__(self, parent=None):
		Tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid() # packing/geometry method

		#Labels
		self.ReqLabel = Tkinter.Label(self,  text ="Requirements CSV File Selected (CSV)")
		self.ReqLabel.grid(column = 0, row = 1, sticky = "N", padx = 20, pady = 10)

		self.SigLabel = Tkinter.Label(self,  text ="Signals CSV File Selected (CSV)")
		self.SigLabel.grid(column = 2, row = 1, sticky = "N", padx = 20, pady = 10)

		#buttons
		self.ReqFileButton = Tkinter.Button(self, text = "Choose the Requirements File (CSV)", command = self.Choose_Requirements_File)
		self.ReqFileButton.grid(column = 0, row = 0, sticky = "S", padx = 20, pady = 10)

		self.SigFileButton = Tkinter.Button(self, text = "Choose the Signals File (CSV)", command = self.Choose_Signals_File)
		self.SigFileButton.grid(column = 2, row = 0, sticky = "S", padx = 20, pady = 10)

		self.QuitButton = Tkinter.Button(self, text = "QUIT", command = self.quit)
		self.QuitButton.grid(column = 1, row = 4, padx = 30, pady = 15)

	def Choose_Requirements_File(self):
		name = askopenfilename()
		name_string = str(name)
		self.ReqLabel["text"] = name_string

	def Choose_Signals_File(self):
		name = askopenfilename()
		name_string = str(name)
		self.SigLabel["text"] = name_string

if __name__ == "__main__":
	FCapp = FileComparisonGUI(None)
	FCapp.title('FILE COMPARISON APP v. 1.0')
	FCapp.geometry()
	FCapp.mainloop()
