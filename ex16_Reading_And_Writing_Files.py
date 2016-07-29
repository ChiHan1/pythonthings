#from sys import argv

#script, filename = argv


print "What file would you like to change or create?"
filename = raw_input("> ")


print "We're going to erase the contents of %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "To continue, press RETURN."

raw_input("?")

print "Opening the file..."

#Opens the file with a write parameter and stores it in the target variable. 
target = open(filename, 'w')

print "Truncating the file. Goodbye!"

#Sets all data in the file to 0. 
target.truncate()

print "Now I'm going to ask you for three lines to write to the file."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.close()

print "Lets read the file."

#Stores data in filename into readfile... not sure why I need this ....
readfile = filename

#Opens the file associated with the variable readfile and stores it in lol.
lol = open(readfile)

#Prints the lol variable with the read parameter.
print lol.read()



print "And finally, we close it"
target.close()

