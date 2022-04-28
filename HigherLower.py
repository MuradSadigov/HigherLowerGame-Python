import random
from art import *
from gameData import *
import os

def get_data_A():
    get_a = random.randint(0, 49)
    return get_a

def get_data_B():
    get_b = random.randint(0, 49)
    return get_b

def comparison(follow_A, follow_B):
    if follow_A == follow_B:
        get_data_A()
        get_data_B()
        comparison(follow_A=follow_A, follow_B=follow_B)
    elif follow_A > follow_B:
        return "A"
    elif follow_B > follow_A:
        return "B"

follower = ""
score = 0

a = get_data_A()
Dict_A = data[a]
print(logo)
def menu(data, score, a, Dict_A):
    
    #Data of A
    name_A = Dict_A["name"]
    follow_A = Dict_A["follower_count"]
    # print(follow_A)
    desc_A = Dict_A["description"]
    coun_A = Dict_A["country"]
    print(f"Compare A: {name_A}, a {desc_A}, from {coun_A}.")
    
    print(vs)

    #Data of B
    Dict_B = data[get_data_B()]
    name_B = Dict_B["name"]
    follow_B = Dict_B["follower_count"]
    # print(follow_B)
    desc_B = Dict_B["description"]
    coun_B = Dict_B["country"]
    print(f"Against B: {name_B}, a {desc_B}, from {coun_B}.")

    
    #User choice
    follower = input("Who has more followers? Type 'A' or 'B': ")

    #Comparison between comparison() and user
    #if A is greater than B
    if comparison(follow_A=follow_A, follow_B=follow_B) == "A" and follower == "A":
        score += 1
        os.system('clear')
        print(f"You are right! Current score: {score}")
        ##Changing data between A and B
        menu(data, score, a, Dict_A)
    #if B is Greater than A
    elif comparison(follow_A=follow_A, follow_B=follow_B) == "B" and follower == "B":
        score += 1
        os.system('clear')
        print(f"You are right! Current score: {score}")
        ##Changing data between A and B
        del Dict_A
        Dict_A = Dict_B
        menu(data, score, a, Dict_A)
    else:
        os.system('clear')
        print(f"Sorry, that's wrong. Final score: {score}")
        a = str(input("Do you wanna start playing again?: Type 'yes' or 'no': "))
        if a == "no" or a == "NO" or a == "n":
            exit
        elif a == "yes" or a == "Yes" or a == "y":
            os.system('clear')
            score = 0
            menu(data, score, a, Dict_A)

    
menu(data, score, a, Dict_A)
