list1=[9,80,16,67,35] #list is a collection of items
s=0                     #defining variable sum "S"
for i in list1:         #creating a loop for each list item
    s=s+i               #adding 0 to the list item (or 1)
    if s!=i:            # to avoid first item printed
        print(s)        #print the sum "s"
        s=i             #storing the previous value of i in s
print(list1[0]+s)       #print the sum of the last + first list item