import random
import gamelogo
import database
import os
print(gamelogo.game_logo)
# print(account_1)
# print(account_2)

score=0
def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return (f"{name} a {description}, from {country}")


def check_answer(guess, follower1, follower2):
    if follower1 < follower2:
        if guess == 1:
            return False
        elif guess == 2:
            return True
    elif follower1 > follower2:
        if guess == 1:
            return True
        elif guess == 2:
            return False
        

account_2 = random.choice(database.data)
continue_flag=True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(database.data)
    while account_1==account_2:
        account_2 = random.choice(database.data)
    print(f'compare 1: ({display_accountinfo(account_1)})')
    print(gamelogo.vs)
    print(f"Compare 2: ({display_accountinfo(account_2)})")
    guess = int(input("Who Has more followers in social media? Type 1 or Type 2="))
    followers_count1 = account_1["follower-count"]
    followers_count2 = account_2["follower-count"]
    is_correct=check_answer(guess, followers_count1, followers_count2)
    os.system("CLS")
    print(gamelogo.game_logo)
    if is_correct==True:
        score=score+1
        print(f"You are right your score is: {score}")
    else:
        print(f"You are wrong.Your final score is: {score}")
        continue_flag=False




# import gamelogo
# import database
# import random
# print(gamelogo.game_logo)
# score=0
# def check_ans(guess,follower_account_1,follower_account_2):
#     if follower_account_1<follower_account_2:
#         if guess==1:
#             # print()
#             return False
#         else:
#             return True
#     elif follower_account_1>follower_account_2:
#         if guess==1:
#             return True
#         else:
#             return False

# def display_accountinfo(account):
#     i=1
#     name=account["name"]
#     description=account["description"]
#     country=account["country"]
#     # while i==2 and i==1:
#     #     i=2
#     #     print(f" Compare {i}name:{name}, {description}, country:{country} {gamelogo.vs}")
#     return(f"name:{name}, a {description}, from {country} ")
# account_1=random.choice(database.data)
# account_2=random.choice(database.data)
# print(f"Compare 1: {display_accountinfo(account_1)}")
# # print({gamelogo.vs})
# print(f"Compare 2: {display_accountinfo(account_2)}")

# guess=int(input("Who has more folowers? 1 or 2="))
# follower_account_1=account_1["follower_count"]
# follower_account_2=account_2["follower_count"]
# is_correct=check_ans(guess,follower_account_1,follower_account_2)
# if is_correct==True:
#     score=score+1
#     print(f"your guess is correct.Your score is {score}")
# else:
#     print(f"Yu are wrong. our final score is {score}")