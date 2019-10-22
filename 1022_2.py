# coding: utf-8


a = input("Player1:")
b = input("Player2:")

c = a.lower()
d = b.lower()

words =["蛋糕","大便","你吃","我吃"]

def game(a,b):
    if c==words[0] and d==words[2]:
        print("Player1 win!")
    elif c==words[0] and d==words[3]:
        print("Player2 win!")
    elif c==words[1] and d==words[2]:
        print("Player2 win!")
    elif c==words[1] and d==words[3]:
        print("Player1 win!")
    elif c==words[2] and d==words[0]:
        print("Player2 win!")
    elif c==words[2] and d==words[1]:
        print("Player1 win!")
    elif c==words[3] and d==words[0]:
        print("Player1 win!")
    elif c==words[3] and d==words[1]:
        print("Player2 win!")
    else:
        print("No winner!")
    
    
game(a,b)
