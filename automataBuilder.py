def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string
    print(str1)   
    return str1  

fname = 'legal.txt'

out = open('out.txt','w')

total = 0

with open(fname) as f:
    content = f.readlines()

x = listToString(content)

for parts in x:
    parts = parts.replace("\n", "")
    out.write(parts)
    #print(parts)
out.write('\n')
# out.write(str(total))
out.close()
f.close()

        