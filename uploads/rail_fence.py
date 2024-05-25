def rail_fence_enc(txt, rails):
    enc = [['' for i in range(4)] for j in range(len(txt))]
    y=0
    x = 0
    inc=True
    for i in txt:
        for j in range(rails):
            if j==y:
                enc[x][j] = i
        x+=1
        if y == rails-1:
            inc=False
        if y == 0:
            inc = True
        if inc:
            y+=1
        else:
            y-=1
    finalEncrypted = []
    for i in range(rails):
        for j in range(len(txt)):
            if enc[j][i]!='':
                finalEncrypted.append(enc[j][i])
    
    
    finalEncrypted = ''.join(finalEncrypted)
    return finalEncrypted

def rail_fence_dec(txt, rails):
    enc = [['' for i in range(4)] for j in range(len(txt))]
    y=0
    x = 0
    inc=True
    for i in txt:
        for j in range(rails):
            if j==y:
                enc[x][j] = i
        x+=1
        if y == rails-1:
            inc=False
        if y == 0:
            inc = True
        if inc:
            y+=1
        else:
            y-=1
    finalEncrypted = []
    for i in range(rails):
        for j in range(len(txt)):
            if enc[j][i]!='':
                finalEncrypted.append(enc[j][i])
    
    
    finalEncrypted = ''.join(finalEncrypted)
    return finalEncrypted



print(rail_fence_enc('THISISASECRET',4))