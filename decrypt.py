import copy
import keysched as ks

key_sched=ks.keyscheduling()


def circulant( arr,  n):
   
    c = [[0 for i in range(n)] for j in range(n)]
    for k in range(n):
        c[k][0] = arr[k]

    for  i in range(1,n):
        for j in range(n):
            if (j - 1 >= 0):
                c[j][i] = c[j - 1][i - 1]
            else:
                c[j][i] = c[n - 1][i - 1]
             
    result = [[c[j][i] for j in range(len(c))] for i in range(len(c[0]))]

    return result
    
M01 = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
M11 = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
M21 = [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
M31 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
mk01=circulant(M01,32)
mk11=circulant(M11,32)
mk21=circulant(M21,32)
mk31=circulant(M31,32)

def addrndkey(k,state):
    result=[[0 for i in range(32)]for j in range(4)]
    for i in range(4):
        for j in range(32):
            result[i][j] = k[i][j] ^ state[i][j]
    return result
    
def invmixrows(A,B):
    result = [[0] for i in range(32)]
    
    s=[]
    for i in B:
        s.append([B[i]])
#     print(s)
    for i in range(len(A)):
#         print(A[i])
        for j in range(len(s[0])):
            for k in range(len(s)):
                u=copy.deepcopy(result[i][j])
                result[i][j] = u^(A[i][k]^s[k][j])

    final=[]
#     print(result)
    for i in range(32):
        final.append(result[i][0])
    
    return final
    
def invsbox(sbox,state):
    for i in range(32):
        x=""
        for j in range(4):
            x+=str(state[j][i])
#         print(int(x,2))
        z=sbox.index(x)
        y=str(bin(z)[2:])
#         print(y)
        for k in range(0):
            state[k][i]=int(y[k])
    return state
    
inp = input("Enter the cipher text: ")
cipher_text=[[0 for i in range(32)]for j in range(4)]
ind=0
for i in range(4):
    for j in range(32):
        cipher_text[i][j]=int(inp[ind])
        ind+=1
Sbox = ['0010', '1101', '0011', '1001', '0111', '1011', '1010', '0110', '1110', '0000', '1111', '0100', '1000', '0101', '0001',
'1100']
cipher_text=addrndkey(key_sched[14],cipher_text)
for i in range(13,-1,-1):
    cipher_text[0]=invmixrows(mk01,cipher_text[0])
    cipher_text[1]=invmixrows(mk11,cipher_text[1])
    cipher_text[2]=invmixrows(mk21,cipher_text[2])
    cipher_text[3]=invmixrows(mk31,cipher_text[3])
    
    cipher_text=invsbox(Sbox,cipher_text)
    
    cipher_text=addrndkey(key_sched[i],cipher_text)

bin_str=""
text=""
x=0
# print(cipher_text)
for i in range(4):
    for j in range(32):
        bin_str+=str(cipher_text[i][j])
        x+=1
        if x==8:
            # print(int(bin_str,2))
            text+=chr(int(bin_str,2))
            bin_str=""
            x=0
            
print(text)