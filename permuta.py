def permuta(s,l,p):    
    if (l == ''):
        return p
    else:
        r = []
        for w in p:            
            for c in l:
                m = l
                w = w + c
                m.remove(c)
                r = append(permuta(s,m,p))
               

    return r
   
   
s = input('Palavra para permutação: ')
p = permuta(s,s,[])
print(p)
