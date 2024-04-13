# Display welcome messgae to user
#print("Hello! Welcome to your personal EKG monitor.")
#print("Here, you will be recording your pulse and finding out your BPM.")
#print("To start, enter your age and then enter if you are recording your resting or moving heart rate.")
#print("Then, feel your pulse with one hand and start pressing the spacebar everytime you feel a pulse.")
#print("Enjoy!\n")

# Testing Code
#age = int(input("Enter your age: "))

#while (age < 10):
#    age = int(input("\nYou are too young to use this app!\nPlease enter a valid age: "))

# input validation for heartType (no longer needed because of drop down menu)
# heartType = input("Are you recording your resting and moving heart rate? (Please type \"R\" for resting and \"M\" for moving). ")
# while ((heartType != "R") and (heartType != "r") and (heartType != "M") and (heartType != "m")):
    # heartType = input("Invalid input. Please enter \"R\" for resting or \"M\" for moving. ")

# test data
#heartType = "Resting"
# Replace with actual BPM data
#BPM = 100

# Function to determine if heart rate is healthy or not
def determine_heart_cond(age, heartType, BPM):
    age=int(age)
    if (heartType == "Resting"):
        if (age >= 10):
            if (BPM  >= 60 and BPM <= 100): 
                healthy = True
            else:
                healthy = False
    elif (heartType == "Moving"):
        if (age >= 20):
            if (BPM  >= 100 and BPM <= 170):
                healthy = True
            else:
                healthy = False
        elif (age >= 30):
            if (BPM  >= 95 and BPM <= 162):
                healthy = True
            else:               
                healthy = False
        elif (age >= 35):
            if (BPM  >= 93 and BPM <= 157):
                healthy = True
            else:               
                healthy = False
        elif (age >= 40):
            if (BPM  >= 90 and BPM <= 153):
                healthy = True
            else:              
                healthy = False
        elif (age >= 45):
            if (BPM  >= 88 and BPM <= 149):
                healthy = True
            else:                
                healthy = False
        elif (age >= 50):
            if (BPM  >= 85 and BPM <= 145):
                healthy = True
            else:               
                healthy = False
        elif (age >= 55):
            if (BPM  >= 83 and BPM <= 140):
                healthy = True
            else:                
                healthy = False
        elif (age >= 60):
            if (BPM  >= 80 and BPM <= 136):
                healthy = True
            else:                
                healthy = False
        elif (age >= 65):
            if (BPM  >= 78 and BPM <= 132):
                healthy = True
            else:                
                healthy = False
        elif (age >= 70):
            if (BPM  >= 75 and BPM <= 128):
                healthy = True
            else:                
                healthy = False
    return healthy

# Function to provide health advice based on heart rate
def advice(healthy):
    if (healthy == True):
        print("\nCongrats! You have a healthy heart rate.")
    else:
        print("\nYour heart rate is abnormal for your age.\nPlease continue recording data and consult a medical professional")

# # Test heart rate and provide advice
# healthy = determine_heart_cond(age, heartType, BPM)
# advice(healthy)

# # Inform user that data has been recorded
# print("\nYour data has been recorded.")

