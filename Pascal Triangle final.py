
rows = int(input("Enter the number of rows: "))

space_li = []
space = ""
space_li.append(space)

for z in range(1, rows):
    space += " "
    space_li.append(space)
    

def print_list(li):
    pos = rows - len(li)
    spacing = space_li[pos]
    string = ""
    for item in li:
        string += str(item) + " "
    print(spacing + string)


print_list([1])

li = [1, 1]
print_list(li)

for i in range(rows-2):
    
    length = len(li)    
    li_2 = []
    for m in range(length):
        if m == 0 or m == length-1:
            li_2.append(1)    
        if m < length - 1:
            li_2.append(li[m] + li[m+1])
           
    li = li_2
    print_list(li)



