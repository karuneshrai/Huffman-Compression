def tree(tn,s,dic,dic1):
    if tn not in dic:
        dic1[tn]=s
    else:
        a=dic[tn][0];b=dic[tn][1]
        return [tree(a,(s+'0'),dic,dic1),tree(b,(s+'1'),dic,dic1)]
def sort(data_items):
    for i in range(len(data_items)):
        for j in range(len(data_items)-1):
            if data_items[j][1]>data_items[j+1][1]:
                data_items[j+1],data_items[j]=data_items[j],data_items[j+1]
    return data_items
def compress(file):
    file=open(file)
    data1=file.read()
    text=''
    data1=data1.lower()
    my_text="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(data1)):
        if data1[i] not in my_text:
        
            data1=data1.replace(data1[i]," ")
    aa=data1.split()  
    
        
    for i in range(len(aa)):
        text=text+aa[i]+" "
    
    
    
    import string
    ss=string.ascii_letters+' '
    data={}
    for i in data1:
        if i.isupper():
                i=i.lower()
        if i in ss and i not in data:
            data[i]=1
        elif i in ss and i in data:
            data[i]+=1
    data_items=list(data.items())
    for i in range(len(data_items)):
        data_items[i]=list(data_items[i])
    data_items=sort(data_items)
    dic={}
    for i in range(len(data_items)-1):
        name=data_items[0][0]+data_items[1][0]
        we=data_items[0][1]+data_items[1][1]
        a=data_items.pop(0)
        b=data_items.pop(0)
        dic[name]=[a[0],b[0]]
        data_items.append([name,we])
        data_items=sort(data_items)
    dic1={}
    file.close()
    
    (tree(name,'',dic,dic1))
    
    ft=""
    for i in range(len(text)):
        if (text[i])!="0" and (text[i])!="1":
           ft=ft+dic1[text[i]]
    g=open('Novel_Compressed.txt','w+')
    g.write('')
    g=open('Novel_Compressed.txt','a')
    g.write(str(dic1))
    rem=10-((len(ft)+1)%10)
    g.write(str(rem))
    ft=ft+('0'*(rem))
    for i in range(int(len(ft)/10)):
        x=int((10*i))
        #print(chr(int(ft[x:x+9],2)),end='')
        g.write(chr(int(ft[x:x+10],2)))
    g.close()
compress(input('File to Compess: '))