
def shirts_and_pants(shirts_amount, pants_amount):
	print "You have %d of shirts." % shirts_amount
	print "You have %d of pants." % pants_amount
	if shirts_amount > pants_amount:
			print "You have right amount of shirts.\n"
	else:
			print "YOU NEED MORE SHIRTS!!!\n"



#6	
shirts_and_pants(((shirts*32)/4),(((pants*2)*3)))			
#5
shirts = 400
pants = 231
shirts_and_pants(shirts,pants)		
#4
shirts_and_pants(27%6, 27/9)
#3
shirts_and_pants(17, 8)
#2
print "Enter number of shirts and pants."
shirts_and_pants(int(raw_input("> ")),int(raw_input("> ")))
#1
print "Enter in Shirt amount."
number_shirts = int(raw_input("> "))
print "Enter in Pant amount."
number_pants = int(raw_input("> " ))
shirts_and_pants(number_shirts,number_pants)




#does't work
#shirts2 = 123123123
#pants2 = 321321321
#shirts_and_pants('%d, %d ' % (shirts2, pants2))