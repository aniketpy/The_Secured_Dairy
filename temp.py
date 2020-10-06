import random
al=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
  'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ','a', 'b',
   'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
     'w', 'x', 'y', 'z']
lst=['w', 'L', 'Y', 'c', 'A', 'm', 'C', 'r', 'v',
 'z', 'R', 'F', 's', 'k', ' ', 'Z', 't', 'i', 'n',
  'D', 'j', 'J', 'V', 'E', 'e', 'u', 'S', 'h', 'B',
   'M', 'b', 'l', 'O', 'U', 'a', 'H', 'y', 'X', 'f',
    'W', 'T', 'P', 'p', 'N', 'Q', 'o', 'd', 'K', 'g',
     'q', 'I', 'G', 'x']



def encrypt(b):
    str1=""
    for i in b:
        if i in al:
            poss=al.index(i)
            newposs=lst[poss]
            str1=str1+newposs
        else :
            str1=str1+i
    return str1

def decrypt(str1):
    b=""
    for i in str1:
        if i in al:
            poss=lst.index(i)
            b=b+al[poss]
        else:
            b=b+i
    return(b)

b="str1=str1+newposs"
a=encrypt(b)
print(a)
print(decrypt(a))