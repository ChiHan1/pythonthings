print "what file would you like to read?"
readfile = raw_input("> ")


lol = open(readfile)

print lol.read()