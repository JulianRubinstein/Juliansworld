import timeit

global p
p=1

def printboard(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print ("--------------------")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print ("|", end="")
            
            if j == 8 :
                print(str(board[i][j]) + "|")
            else:
                print(str(board[i][j]) + " " , end= "")
                   
def checkifvalid(i1,j1):
    for k in range (0,9):
        if k!=i1:
            if s[i1][j1] == s[k][j1]:
                return False
    for k in range (0,9):
        if k!=j1:
            if  s[i1][j1] == s[i1][k]:
                return False
    for i in range(i1-i1%3,i1+(3-i1%3)):
        for j in range(j1-j1%3,j1+(3-j1%3)):
            if i!=i1 or j!=j1:
                if  s[i1][j1] == s[i][j]:
                    return False
    return True

def producenumber(i1,j1):
    global p
    prev=s[i1][j1]
    for k in range(1,10):
        s[i1][j1]=k
        if checkifvalid(i1,j1) == True:
            p=1
            return True
    s[i1][j1]=0
    p=0
    return False

def backproducenumber(i1,j1):
    global p
    prev=s[i1][j1]
    for k in range(prev+1,10):
        s[i1][j1]=k
        if checkifvalid(i1,j1) == True:
            p=1
            return True
    s[i1][j1]=0
    p=0
    return False

global s
global f
global sres
    
def restart():
    global s
    s=sres

sres= [[7, 0, 0, 0, 0, 4, 3, 0, 0], 
     [0, 0, 3, 0, 0, 1, 5, 0, 6], 
     [0, 0, 6, 0, 0, 0, 0, 7, 8], 
     [0, 8, 0, 0, 7, 0, 0, 0, 0], 
     [9, 0, 0, 0, 0, 0, 0, 0, 2], 
     [0, 0, 0, 0, 9, 0, 0, 5, 0], 
     [3, 6, 0, 0, 0, 0, 7, 0, 0], 
     [4, 0, 5, 9, 0, 0, 6, 0, 0], 
     [0, 0, 9, 8, 0, 0, 0, 0, 5]]

s=sres


f = [[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]]

A =     [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]


for i in range(9):
    for j in range(9):
        if (s[i][j])!=0:
            f[i][j]=1

#printboard(s)           
#
#start = timeit.default_timer()
#
#t=solve()
#
#stop = timeit.default_timer()
#
#print("\n")
#
#print('Time: ', stop - start) 
#
#print("\n")
#
#printboard(s)
#
#print(t)



