print("Hello! Welcome to your personal EKG monitor.")
print("Here, you will be recording your pulse and finding out your BPM.")
print("To start, enter your age and then enter if you are recording your resting or moving heart rate.")
print("Then, feel your pulse with one hand and start pressing the spacebar everytime you feel a pulse.")
print("Enjoy!")

age = input("Enter your age: ")
age = int(age)
heartType = input("Are you recording your resting or moving heart rate? (Please type \"R\" for resting or \"M\" for moving). ")

BPM = 100

if (heartType == "R"):
    if (age >= 20):
        if (BPM  >= 60 or BPM <= 100): 
            print("Congrats! You have a healthy heart rate.")
elif (heartType == "M"):
    if (age >= 20):
        if (BPM  >= 100 or BPM <= 170):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 30):
        if (BPM  >= 95 or BPM <= 162):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 35):
        if (BPM  >= 93 or BPM <= 157):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 40):
        if (BPM  >= 90 or BPM <= 153):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 45):
        if (BPM  >= 88 or BPM <= 149):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 50):
        if (BPM  >= 85 or BPM <= 145):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 55):
        if (BPM  >= 83 or BPM <= 140):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 60):
        if (BPM  >= 80 or BPM <= 136):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 65):
        if (BPM  >= 78 or BPM <= 132):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")
    elif (age >= 70):
        if (BPM  >= 75 or BPM <= 128):
            print("Congrats! You have a healthy heart rate.")
        else:
            print("You are out of shape! Please do the following to achieve a healthy heart rate:")