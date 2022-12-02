import copy
def col_diff(keybef):
    m=[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
    for i in range(32):
        xor=0
        for j in range(4):
            for k in range(4):
                xor=(xor)^(m[j][k]^keybef[k][i])

            keybef[j][i]=xor
    return keybef

def row1(A,B):
     
    result = [[0] for i in range(32)]
    s=[]
    for i in range(len(B)):
        s.append([B[i]])
#     print(s)
#     print(A)
    for i in range(len(A)):
        for j in range(len(s[0])):
            for k in range(len(s)):
                u=copy.deepcopy(result[i][j])
#                 print((A[i][k] ^ s[k][j]),u ^ (A[i][k] ^ s[k][j]))
                result[i][j] = (u ^ (A[i][k] * s[k][j]))
                
#         print(result[i][j])

    final=[]
#     print(result)
    for i in range(32):
        final.append(result[i][0])
    
    return final
    
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
    
def row_diff(key_state):
    
    l=[1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0]
    mk=circulant(l,32)
    key_state[0]=row1(mk,key_state[0])
    key_state[1]=key_state[1][8:]+key_state[1][0:8]
    key_state[2]=key_state[2][15:]+key_state[2][0:15]
    key_state[3]=key_state[3][18:]+key_state[3][0:18]
    
    return key_state

def con_add(key_state,x):
    con = [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
    for i in range(8):
        key_state[3][i]^=con[i]
    for i in range(8,16):
        key_state[2][i]^=con[i]
    for i in range(16,24):
        key_state[1][i]^=con[i]
    for i in range(24,28):
        key_state[0][i]^=con[i]
    u=bin(x)[2::].zfill(4)
    for i in range(4):
        key_state[0][28+i]^=int(u[i])
    return key_state

def keyscheduling():
    key=input("Enter the key in hex(32 length):")

    key_bin=bin(int(key,16))[2::].zfill(128)
    key_state=[[0 for i in range(32)]for j in range(4)]
    # print(key_bin,'\n',key_state,len(key_bin))

    x=0
    for i in range(4):
        for j in range(32):
            key_state[i][j]=int(key_bin[x])
            x+=1
    # print(key_state)

    key_list=[key_state]
    for rnd in range(14):            
        key_state=col_diff(key_state)
        key_state=row_diff(key_state)
        key_state=con_add(key_state,rnd)
    #     print(key_state)
        k = copy.deepcopy(key_state)
        key_list.append(k)

    
    return key_list
    
# print(keyscheduling())