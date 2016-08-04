from sys import argv
from os.path import exists

script, from_file, to_file = argv



in_file = open(from_file)
indata = in_file.read()

print "Ready, hit RETURN to continue, CTRL-C to fuck this program up."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Copyed from %s to %s" % (from_file, to_file);
print "The output file was %d bytes long" % len(to_file)
print "The input file was %d bytes long" % len(indata)
out_file.close()
in_file.close()