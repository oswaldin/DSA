def permuta(l,p):     
    if (l == []):
        return p
    else:
        r = []        
        for c in l:            
            m = l + []          
            for w in p:
                w = w + c + ''                    
                m.remove(c)                
                r = r + permuta(m,[w])    
    return r
   
def limpa(a):
    for e in a:
        if a.count(e) > 1:
            for x in range(a.count(e)-1): a.remove(e)
    return a

s = input('Palavra para permutação: ')
pmt = permuta(list(s),[''])
pmt = limpa(pmt)
print('================================\n', len(pmt), 'anagramas possíveis\n================================')
print(pmt)
