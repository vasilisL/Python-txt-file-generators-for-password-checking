#Greek phone number list generator

string=''
FILE = open("pl.txt","w")
total_items = 0

for x in range(6900000000, 7000000000):
    string = string + str(x) + '\n'
    total_items += 1

FILE.write(string)

string=''
FILE.close()
print "DONE!Total items in list: ", total_items
