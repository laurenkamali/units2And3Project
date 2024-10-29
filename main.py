'''
Name: Lauren Kamali
Date: 10/28/24
Assignment: Unit 2 and 3 Project
'''

userMonth = input("Enter the name of the month: ")
userDay = int(input("Enter the day (1-31): ")) 

def get_season(userMonth, userDay):
    if (userMonth == "March" and userDay >= 20) or userMonth in ["April", "May"] or (userMonth == "June" and userDay <= 14):
        return "Spring"
    elif (userMonth == "June" and userDay >= 15) or userMonth in ["July", "August"] or (userMonth == "September" and userDay <= 21):
        return "Summer"
    elif (userMonth == "September" and userDay >= 22) or userMonth in ["October", "November"] or (userMonth == "December" and userDay <= 20):
        return "Fall"
    else:
        return "Winter"


print(f"{userMonth} {userDay} is in {get_season(userMonth, userDay)}")







