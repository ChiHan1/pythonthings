from sys import argv

script, input_file = argv

#Function to read a variable, (f)
def print_all(f): 
	print f.read()
	f.seek(-20,1)
#Sets the file postion(where to start reading or writing)at 0 for any variable sent to the function.
#The whence is default at the absolute file postion, or at the start. 
#It does not return a value.
#Example output:
			#Evil
			#Trumps
			#Good
#For instance, parameters f.seek(0) will read the file from the start at position 0 which is the e in evil.
#If it is f.seek(-20,2) it will read at the end of the file first and go backwards, so to start at -20, it will read -20 position from the end of file which is the e in evil. 


#A function with two variables. First is a regular varible for a line number, but could be anything.
#The second is for reading a line. 
def print_a_line(line_count, f):
	print line_count, f.readline()
	
#Opens the file into an object represented by current_file.
current_file = open(input_file)


print "First let's print the whole file: \n and fastforward to the beginning \n"
#This will read the file out to the user then position the back to the start of the file. 
print_all(current_file)



print "Let's print three lines:"
#Creates a variable equal to 1.
current_line = 1
#Uses the read function to print the variable current_file(1) and then read the line that is equal to 1.
print_a_line(current_line, current_file)

#A reconfigured variable that is equal to 2. (1+1)
#current_line = current_line + 1
current_line += 1
#Uses the readline function to print the variable current_line(2) 
print_a_line(current_line, current_file)

#A reconfigured variable that is equal to 3. (2+1)
current_line += 1
#Uses the read function to print the variable current_file(3) and then read the line that is equal to 3.
print_a_line(current_line, current_file)

current_file.close()