print("Hello! Welcome to your personal EKG monitor.")
print("Here, you will be recording your pulse and finding out your BPM.")
print("To start, enter your age and then enter if you are recording your resting or moving heart rate.")
print("Then, feel your pulse with one hand and start pressing the spacebar everytime you feel a pulse.")
print("Enjoy!\n")

# # Testing Code
age = input("Enter your age: ")
age = int(age)
# if (age < 10):
    # print("You are too young to use this app!")
heartType = input("Are you recording your resting and moving heart rate? (Please type \"R\" for resting and \"M\" for moving). ")

BPM = 300

low = True

def determine_heart_cond(age, heartType, BPM):
    if (heartType == "R"):
        if (age >= 10):
            if (BPM  >= 60 and BPM <= 100): 
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 100):
                low = False
    elif (heartType == "M"):
        if (age >= 20):
            if (BPM  >= 100 and BPM <= 170):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 170):
                low = False
        elif (age >= 30):
            if (BPM  >= 95 and BPM <= 162):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 162):
                low = False
        elif (age >= 35):
            if (BPM  >= 93 and BPM <= 157):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 157):
                low = False
        elif (age >= 40):
            if (BPM  >= 90 and BPM <= 153):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 153):
                low = False
        elif (age >= 45):
            if (BPM  >= 88 and BPM <= 149):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 149):
                low = False
        elif (age >= 50):
            if (BPM  >= 85 and BPM <= 145):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 145):
                low = False
        elif (age >= 55):
            if (BPM  >= 83 and BPM <= 140):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 140):
                low = False
        elif (age >= 60):
            if (BPM  >= 80 and BPM <= 136):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 136):
                low = False
        elif (age >= 65):
            if (BPM  >= 78 and BPM <= 132):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 132):
                low = False
        elif (age >= 70):
            if (BPM  >= 75 and BPM <= 128):
                print("Congrats! You have a healthy heart rate.")
            elif (BPM >= 128):
                low = False
    return low

def high_and_low(low):
    if (low == True):
        print("\nYour heart rate is too low! Please do the following to increase heart rate:")
        print("Exercise \nGet more sleep \nIf your BPM is still too low, please go see a doctor")
    else:
        print("\nYour heart rate is too high! Please do the following to decrease heart rate:")
        print("Meditate \nTake deep breaths \nExercise more often \nStart a healthier diet")
        print("If you are still worried, please go see a doctor")

# test
low = determine_heart_cond(age, heartType, BPM)
high_and_low(low)

