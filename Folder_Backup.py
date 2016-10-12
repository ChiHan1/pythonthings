import shutil
from sys import argv
import errno

def copyDirectory(src, dst):
	try: 
		shutil.copytree(src, dst)
	
	except OSError as e:
		if e.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
		
		else:
			print ('Directory not copied. Error: %s' % e)



script, sour, dest = argv


copyDirectory(sour, dest)

print "This is %s " % script
print "The source path is %s\nThe destination path is %s " % (sour, dest)



