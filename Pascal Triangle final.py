# Pascal's Triangle

def pascal_rows(n):
    li = [[1]]
    for i in range(n-1):
        li_now = []
        li_prev = li[i]
        for j in range(len(li_prev)-1):
            li_now.append(li_prev[j] + li_prev[j+1])
            
        li_now.insert(0, 1)
        li_now.insert(len(li_now), 1)
        
        li.append(li_now)
    
    li_str = []
    for row in li:
        s_0 = ""
        for num in row:
            s_0 += str(num) + " "
        s = s_0[:len(s_0)-1]
        li_str.append(s)
    
    max_length = len(li_str[len(li_str)-1])
    for string in li_str:
        space_count = (max_length-len(string))//2
        space = " "*space_count
        print(space + string)

pascal_rows(15)
