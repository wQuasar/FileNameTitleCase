# Python script to change all the filenames in a folder to title case

import os

# Gets the list of files in folder and then renames them to title case
def changeNamesToTitleCase():
	file_names = os.listdir(".")

	for file_name in file_names:
		if (file_name != "FileNameTitleCase.py"):
			new_name = file_name.title()

			# Only change name if there is an actual change
			if (file_name != new_name):
				print (file_name + " -> " + new_name)
				os.rename(file_name, new_name)
			else:
				print (file_name + " -> NO CHANGE")


# Main edit function
def init():
	print ("** KEEP BACKUPS YOU PUNK! **\n")
	input("Press ENTER to continue...")

	print ("----- BEGIN PROCESSING -----\n")
	changeNamesToTitleCase()
	print ("\n----- END PROCESSING ----- ")

# Self start
init()