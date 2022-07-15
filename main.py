# l=[1,2,3,4]
# count=len(l)
# i=0
# print(count)
# while count>0:
#     print(l[i])
#     i=i+1
#     count=count-1

# # for item in l:
# #     count=count+1
# #     print(count)
# # else:
# #     print("done")
import random
ans = 'y'
while ans == 'y' or ans == 'Y':
    def gameWin(comp, you):
        if comp == 's':
            if you == 'w':
                return False
            elif you == 's':
                return False
            else:
                return True
        if comp == 'w':
            if you == 'w':
                return False
            elif you == 's':
                return False
            else:
                return True
        if comp == 'g':
            if you == 'w':
                return False
            elif you == 'g':
                return False
            else:
                return True
    print("\t\t\t WELCOME TO THE GAME!!\t\t\t")
    print("\t\t\t SNAKE WATER & GUN!!\t\t\t")
    print("COMPUTER'S TURN")
    randno = random.randint(1, 3)
    if randno == 1:
        comp = 's'
    elif randno == 2:
        comp = 'w'
    else:
        comp = 'g'
    you = input("YOUR TURN: Snake(s), Water(w), Gun(g)?")
    a = gameWin(comp, you)
    if a == False:
        print("You loose, try again :(")
    else:
        print("You Win!!! :)")
    ans = input("Do You Want To Continue?? Y/y|N/n ")
