#date list generator

string=''
FILE = open("bdl.txt","w")
item_count = 0

for d in range(01, 32):
    for m in range(01, 13):
        for y in range(1939 , 2020):
            string = string + str(d) + str(m) + str(y)
            item_count += 1
FILE.write(string+'\n')

string=''
FILE.close()
print 'Total items in list', item_count
