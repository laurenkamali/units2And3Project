'''
Name: Lauren Kamali
Date: 1/24/25
Assignment: Unit 2 and 3 Project
'''

def get_season(userMonth, userDay):
    if (userMonth == "March" and userDay >= 20) or userMonth in ["April", "May"] or (userMonth == "June" and userDay <= 20):
        return "Spring"
    elif (userMonth == "June" and userDay >= 21) or userMonth in ["July", "August"] or (userMonth == "September" and userDay <= 21):
        return "Summer"
    elif (userMonth == "September" and userDay >= 22) or userMonth in ["October", "November"] or (userMonth == "December" and userDay <= 20):
        return "Fall"
    else:
        return "Winter"

userMonth = input("Enter the name of the month: ").capitalize()  
try:
    userDay = int(input("Enter the day (1-31): ")) 
    season = get_season(userMonth, userDay)
    print(f"The season on {userMonth} {userDay} is {season}.") 
except ValueError:
    print("Invalid day. Please enter a number.")