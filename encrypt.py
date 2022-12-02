import copy
import keysched as ks

key_sch=ks.keyscheduling()
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

M0 = [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]
M1 = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1]
M2 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1]
M3 = [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1]
mk0=circulant(M0,32)
mk1=circulant(M1,32)
mk2=circulant(M2,32)
mk3=circulant(M3,32)

def addrndkey(k,state):
    result=[[0 for i in range(32)]for j in range(4)]
    for i in range(4):
        for j in range(32):
            result[i][j] = k[i][j] ^ state[i][j]
    return result
    
def subbytes(sbox,state):
    for i in range(32):
        x=""
        for j in range(4):
            x+=str(state[j][i])
#         print(int(x,2))
        y=sbox[int(x,2)]
        
        for k in range(4):
            state[k][i]=int(y[k])
    return state
    

def mixrows(A,B):
     
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
    
    
def encr_pm():    
    Sbox = ['0010', '1101', '0011', '1001', '0111', '1011', '1010', '0110', '1110', '0000', '1111', '0100', '1000', '0101', '0001',
    '1100']
    message=input("Enter the message:")
    in_bin=""
    for i in message:
        x=ord(i)
    #     print(format(x, '#010b'))
        in_bin+=str(format(x, '#010b')[2:])
    print(len(in_bin))
    if len(in_bin)<128:
        in_bin="1"+in_bin.zfill(127)
    
    
    input_state=[[0 for i in range(32)]for j in range(4)]
    # # print(key_bin,'\n',key_state,len(key_bin))
    
    x=0
    for i in range(4):
        for j in range(32):
            input_state[i][j]=int(in_bin[x])
            x+=1
    
    # print(input_state)
    print()
    
    for i in range(14):
        input_state=addrndkey(key_sch[i],input_state)
    #     print(input_state)
    
    #     print()
        input_state=subbytes(Sbox,input_state)
    #     print(input_state)
    #     print()
        input_state[0]=mixrows(mk0,input_state[0])
    #     print(input_state[0])
        input_state[1]=mixrows(mk1,input_state[1])
    #     print(input_state[1])
        input_state[2]=mixrows(mk2,input_state[2])
    #     print(input_state[2])
        input_state[3]=mixrows(mk3,input_state[3])
    #     print(input_state[3])
    #     print()
    input_state=addrndkey(key_sch[14],input_state)
    r=""
    for i in range(4):
        for j in range(32):
            r+=str(input_state[i][j])
    return r
    
    
print(encr_pm())