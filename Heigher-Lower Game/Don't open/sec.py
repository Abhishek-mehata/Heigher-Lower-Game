import database
import gamelogo
import random
print(gamelogo.game_logo)




d1=random.choice(database.data)
d2=random.choice(database.data)
fcn1=0
fcn2=0
def func1(dictionary):
    for i in dictionary:
        value=dictionary[i]
        if i=="follower-count":
            print(value)
            return value
def func2(dictionary):
    for i in dictionary:
        value=dictionary[i]
        if i=="follower-count":
            print(value)
            return value
r2=func2(d2)
r1=func1(d1)

def game():
    # print
    for i in d1:
        d=[]
        value=d1[i]
        d=d+value  
