import os 
print("Which directory would you like to save this file?")
directory = input()
if os.path.isdir(directory):
	print("What is the file name?")
	file_name = input()
	print("What is your name")
	name = input()
	print("What is your address?")
	address = input()
	print("What is your phone number?")
	phone_number = input()
	with open(os.path.join(directory,file_name), 'w') as fileHandle:# w is for writing
 		fileHandle.write(f"{name},{address},{phone_number}.") # write into the file
	print("Your file has been created.")
else:
	print("This is not a valid directory.")

	


