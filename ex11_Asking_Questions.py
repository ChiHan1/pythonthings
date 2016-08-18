print "How old are you?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "how much do you weigh?",
#had one space too many between the equals and raw_input which cuased a crash.
weight = raw_input() 


print "So, you are %r old, %s tall and %r fat." % (age, height, weight)