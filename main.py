#code with harry
# def sum(a, b, c ):
#     return a + b + c
# # def sum1(a, b):
# #     return a + b 

# def printBoard(xState, zState):
#     zero = 'X' if xState[0] else ('O' if zState[0] else 0)
#     one = 'X' if xState[1] else ('O' if zState[1] else 1)
#     two = 'X' if xState[2] else ('O' if zState[2] else 2)
#     three = 'X' if xState[3] else ('O' if zState[3] else 3)
#     four = 'X' if xState[4] else ('O' if zState[4] else 4)
#     five = 'X' if xState[5] else ('O' if zState[5] else 5)
#     six = 'X' if xState[6] else ('O' if zState[6] else 6)
#     seven = 'X' if xState[7] else ('O' if zState[7] else 7)
#     eight = 'X' if xState[8] else ('O' if zState[8] else 8)
#     print(f"{zero} | {one} | {two} ")
#     print(f"--|---|---")
#     print(f"{three} | {four} | {five} ")
#     print(f"--|---|---")
#     print(f"{six} | {seven} | {eight} ") 

# def checkWin(xState, zState):
#     wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#     for win in wins:
#         if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
#             print("X Won the match")
#             return 1
#         if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
#             print("O Won the match")
#             return 0
#         # else:
#         #     print("Draw the match")
#         #     return 1
        
        
        
            
#     return -1
    
# if __name__ == "__main__":
#     xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     turn = 1 # 1 for X and 0 for O
#     print("Welcome to Tic Tac Toe")
#     while(True):
#         printBoard(xState, zState)
#         if(turn == 1):
#             print("X's Chance")
#             value = int(input("Please enter a value: "))
#             xState[value] = 1
#         else:
#             print("O's Chance")
#             value = int(input("Please enter a value: "))
#             zState[value] = 1
#         cwin = checkWin(xState, zState)
#         if(cwin != -1):
#             print("Match over")
#             break
        
#         turn = 1 - turn

#code with sparsh


def sum(a,b,c):
    return a+b+c

def printboard(lis,lst):
    print()
    
    zero="x" if lis[0] else ("0" if lst[0] else 0)
    one="x" if lis[1] else ("0" if lst[1] else 1)
    two="x" if lis[2] else ("0" if lst[2] else 2)
    three="x" if lis[3] else ("0" if lst[3] else 3)
    four="x" if lis[4] else ("0" if lst[4] else 4)
    five="x" if lis[5] else ("0" if lst[5] else 5)
    six="x" if lis[6] else ("0" if lst[6] else 6)
    seven="x" if lis[7] else ("0" if lst[7] else 7)
    eight="x" if lis[8] else ("0" if lst[8] else 8)
    

    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")



def check(lis,lst):
    possiblties=[[0,1,2],[2,5,8],[6,7,8],[3,4,5],[0,3,6],[0,4,8],[2,4,6],[1,4,7]]
    for num in possiblties:
        if (sum(lis[num[0]],lis[num[1]],lis[num[2]])==3):
            print("X's win the match")
            return 1
        
        if (sum(lst[num[0]],lst[num[1]],lst[num[2]])==3):
            print("0's win the match")
            return 0
        
        if((c==5 or c==4) and (c1==5 or c1==4)):
            print("Draw the match")
            return 2
        
    return -1    


lis=[0,0,0,0,0,0,0,0,0]
lst=[0,0,0,0,0,0,0,0,0]
c=0
c1=0

print("Welcome to Tic Tak Toe Game")
tune=1
while 1:
    #print("Welcome to Tic Tak Toe Game")
  
    printboard(lis,lst)
    if (tune==1):
        print("X's chance")
        num_bari=int(input("choice the number"))
        lis[num_bari]=1
        c=c+1
    else:
        print("0's chance")
        num_bari=int(input("choice the number"))
        lst[num_bari]=1
        c1=c1+1
    tune=1-tune
    var=check(lis,lst)
    
    if(var!=-1):
        print("Match  is over")
        break

