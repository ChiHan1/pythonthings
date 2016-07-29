#A string variable that equals a numerical format variable. 
x = "There are %d types of people." % 10
#String Variable 
binary = "binary"
#String Variable
do_not = "don't"
#A String Variable contating two string format variables. (binary, do_not)
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

yes = "yes"
no = "no"


funny =  input('Was that funny? ')
#print funny


if funny == yes:
	print "GOOD!"
elif funny == no:
	print "ASS"
else:
	print " It's yes or no"





#Print of a raw format variable. 
#print "I said: %r" % x
#print "I also said: '%s'." % y

#hilarious = False
#joke_evaluation = "Isn't that joke so funny?! %r"

#print joke_evaluation % hilarious

#w = "This is the left side of..."
#e = "a string with a right side."

#print w + e

