def Decompress(file):
    g=open(file)
    data=g.read()
    dic='';i=0
    while i<(len(data)):
        dic=dic+data[i]
        if data[i]=='}':
            break
        i+=1
    dic=eval(dic)
    key=[i for i in dic];items=[dic[i] for i in dic]
    data=data[i+1:]
    rem=data[0]
    data=data[1:]
    h=open('Decompressed.txt','w+');h.write('')
    h=open('Decompressed.txt','a');w='';enc=''
    for i in range(len(data)):
        enc=enc+("{0:010b}".format(ord(data[i])))
        #print((ord(data[i])))
    enc=enc[:len(enc)-int(rem)]
    for i in range(len(enc)):
        w=w+enc[i]
        if w in items:
            h.write(key[items.index(w)])
            w=''
    h.close()
Decompress(input('File to Decompress: '))
