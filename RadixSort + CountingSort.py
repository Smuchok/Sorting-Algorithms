# Taras Smuk IST-21
def CountingSort(A):
    # C= []
    k= max(A)
    C= [0]*(k+1)
    B= [None]*len(A)    # для результату

    # print(' C  =', C,    '\n B=', B)

    for i in range(len(A)):
        # print(' i=', i)
        C[ A[i] ] += 1
        # print(C)
    # print(" C' =", C)

    for j in range(1, k+1): # не включати C[0] елемент!
        # print(' j=', j)
        C[j]= C[j] + C[j-1]
        # print(C)
    # print(" C''=", C)

    i= len(A)
    for lorem in range(len(A)):
        i = i-1
        # print(' i=', i)

        B[ C[ A[i] ]-1 ] = A[i]
        C[ A[i] ] = C[ A[i] ] - 1
        # print('B=', B, '\nC=', C)

    return A, C, B

def RadixSort(A, d):
    for i in range(d):
        print('\n','_'*10, 'Radix:', i, '_'*10)
        R= CountingSort(A)[2]
        print(R)
    return R

print('='*50)
# A= [2,5,3,0,2,3,0,3]
A= [329,457,657,839,436,720,355]

d= len( str(max(A)) )
print(A, end='\n\n')

# Z= CountingSort(A)
Z= RadixSort(A, d)

print('\n', Z)
print('='*50)
