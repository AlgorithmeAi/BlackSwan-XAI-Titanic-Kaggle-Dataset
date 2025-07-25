from algorithmeai.titanic import my_graphic_function, my_function, get_feature_importance, datapoint_to_csv

PASSENGER = {"Pclass" : int(input("What's you passenger class? (1/2/3)")), "Name" : str(input("What's your name? (text field)")), "Sex" : str(input("What's your gender? (male/female)")), "Age" : int(input("What's your Age? (0-99)")), "SibSp" : int(input("How many Siblings did you had onboard? (0-42)")), "Parch" : float(input("How many Parents / Childrens with you? (0-42)")), "Ticket" : str(input("What's written on your ticket?")), "Fare" : float(input("How much did you pay to get onboard?")), "Cabin" : str(input("What's written on your cabin?")), "Embarked" : str(input("Where did you get onboard? (C = Cherbourg, Q = Queenstown, S = Southampton)"))}
import json
print("### YOU ###")
print(json.dumps(PASSENGER, indent=2))

if "y" in str(input("Do you hearby validate the following informations? (y/n)")):
    print("### ROW JSON FOR RAG ANALYSIS ###")
    print(json.dumps(my_graphic_function(PASSENGER), indent=2))
    print("### What are your chances of survival ###")
    print(my_function(PASSENGER) * 100, " % (knowing the optimal threshold is above 64%)")
    print("### What mattered in the making of this confidence probability ###")
    print(json.dumps(get_feature_importance(PASSENGER), indent=2))
    print("### The Existing Passenger you made Algorithme.Ai think of ###")
    print(datapoint_to_csv(PASSENGER))
    
    
