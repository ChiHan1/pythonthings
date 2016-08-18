formatter = "%r %r %r %r"

#Inputs 1 for the first  %r then 2 for the second and soforth
print formatter % (1, 2, 3, 4)
#Inputs "one" for the first %r then "two" for the second and soforth.
print formatter % ("one", "two", "three", "four")
#Inputs True for the first r% then False for the second and soforth.
print formatter % (True, False, False, True)

print formatter % ( formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)