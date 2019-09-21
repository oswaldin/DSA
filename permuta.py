def letras(s):
    a = []
    for l in s:
        a.append(l)
    return a

def permuta(l,p):     
    if (l == []):
        return p
    else:
        r = []
        np = []
        for c in l:            
            m = l + []          
            if (p==[]):
                w = '' + c
                m.remove(c)                            
                np.append(w)                
                r = r + permuta(m,[w])                     
            else:
                for w in p:
                    w = w + c + ''                    
                    m.remove(c)
                    np.append(w)           
                    r = r + permuta(m,[w])    
    return r
   
def limpa(a):
    for e in a:
        if a.count(e) > 1:
            a.remove(e)
    return a

s = input('Palavra para permutação: ')
pmt = permuta(letras(s),[])
pmt = limpa(pmt)
print('================================\n', len(pmt), 'anagramas possíveis\n================================')
print(pmt)
