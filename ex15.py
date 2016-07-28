# A system(package) specific parameter to require command line arguments.
from sys import argv

#Arguments created for module argv. This line has two, arg to display the 
#script file name, and arg to require a filename when the script is run. 
#It doesn't have to be a filename, but for the program to function it must.
script, filename = argv

#Opens the filename provided by the user and then creates an object that contains what
#was in the file. The object is then connected to the variable txt. 
txt = open(filename)

print "Here's your file %r:" % filename

#The object can be changed with different parameters. The parameter ".read()" sends the
#object with no parameters. 
print txt.read()


#This block of code is very similar to the first half. 
#Its main difference is it prompts the user for the file name. 
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
