#Running Conversion Calculator
#Author: Yash Hooda
#Date Created: 02/11/2023
#This Python Program calculates the Running pace, distance, or time and predicts race time. It can also predict your running training paces. 
# You can also calculate V02 max in this project.


import math

print('Welcome to the Running Conversion Calculator! This project predicts your running pace, distance, or time based on your preferences.')
print('You can also predict your race time and training paces!')

#method to calculate intended pace, distance, or time based on your preferences
def calculate(goal):
    if(goal == 'pace'):
        #pace calculator method to calculate average pace from time and distance
        def pace_calculator(time_in_minutes, distance_in_miles):
            pace = time_in_minutes / distance_in_miles
            return pace
        #take time and distance input from user to calculate pace
        time = float(input("Enter the total time in minutes: "))
        distance = float(input("Enter the distance in miles: "))
         #print out average pace from time and distance
        average_pace = pace_calculator(time, distance)
        print("Your average pace is {:.2f} minutes per mile.".format(average_pace))
        
    #if you want to calculate running distance from pace and time
    elif(goal == 'distance'):
        #distance calculator method 
        def distance_calculator(average_pace, time_in_minutes):
            distance_in_miles = time_in_minutes/average_pace 
            return distance_in_miles
        #take pace and time input from user to calculate distance
        pace = float(input("Enter your running pace: "))
        time = float(input("Enter the total time in minutes: "))
        #print out total running distance from pace and time
        total_distance = distance_calculator(pace, time)
        print("Your total distance is {:.2f} miles.".format(total_distance))
        
    #if you want to calculate total running time from pace and distance
    elif(goal == 'time'):
        #time calculator method
        def time_calculator(average_pace, total_distance):
            time_in_minutes = total_distance * average_pace
            return time_in_minutes
        #take pace and distance input from user to calculate total time
        pace = float(input("Enter your running pace: "))
        distance = float(input("Enter the total distance in miles: "))
        #print out total running time from pace and distance
        total_time = time_calculator(pace, distance)
        print("Your total time is {:.2f} minutes.".format(total_time))
        
    else:
        #if user choice is invalid, print error message
        print("Sorry, your choice is invalid. Please try again later.")
        exit(1)
        
#Ask the user what they want to calculate, running distance, running pace, or running time? 
choice = input("What do you want to calculate?: ")
#Call the calculate function to start program execution
calculate(choice)

#Ask user if they want to predict race times or not
choice2 = input("Do you want to predict your race times? (y/n): ")
if choice2 == "y":
    
    #Enter current running time and current running distance
    runningtime = input("Enter your current running time (in minutes): ")
    runningdistance = input("Enter your current running distance (in miles): ")
    #Enter your goal race distance (in miles)
    predictedracedistance = input("Enter your goal race distance (in miles): ")
    #Calculate your predicted race time 
    predictedracetime = float(runningtime) * pow(float(predictedracedistance)/float(runningdistance), 1.06)
    predictedracetime = str(predictedracetime)
    predictedracedistance = str(predictedracedistance)
    
    print("Your predicted race time for " + predictedracedistance + " miles is " + predictedracetime + " minutes.")
    print(" ")
    
    #print('Would you like to calculate your training paces?')
    
    
else:
    #Print new line
    print(' ')
    
#Calculate training paces
choice3 = input('Do you want to calculate your training paces? (y/n): ')
if choice3 == "y":
    #Use 1 mile race time to calculate training paces using statistics and data analaysis
    predictedracetime = float(predictedracetime)
    predictedracetime = float(runningtime) * pow(float(1)/float(runningdistance), 1.06)
    #print out and predict training paces using stats
    print('Your training paces are the following: ')
    easyrunpace = 1.50 * predictedracetime
    print('Your Easy Run Pace is: ' + str(easyrunpace) + " minutes per mile")
    temporunpace = 1.25 * predictedracetime
    print('Your Tempo Run Pace is: ' + str(temporunpace) + " minutes per mile")
    v02maxrunpace = 1.35 * predictedracetime
    print('Your V02 Max Run Pace is: ' + str(v02maxrunpace) + " minutes per mile")
    speedrunpace = 1.10 * predictedracetime
    print('Your Speed Run Pace is: ' + str(speedrunpace) + " minutes per mile")
    longrunpace = 1.55 * predictedracetime
    print('Your Long Run Pace is: ' + str(longrunpace) + " minutes per mile")
    print(' ')
    
    
    
#Calculate V02 max levels 
choice4 = input('Do you want to know your VO2 max levels? (y/n): ')
if choice4 == "y":
    #Use predicted 1.5 mile race time to calculate V02 max 
    predictedracetime = float(runningtime) * pow(float(1.5)/float(runningdistance), 1.06)
    testcompletiontime = predictedracetime
    
    #Ask for gender 
    choice5 = input('What is your gender? (Enter M for Male, F for Female): ')
    if choice5 == "M":
        gender = 1
    elif choice5 == "F":
        gender = 0
    
    #Enter body weight
    choice6 = input('Please enter your body weight (in pounds): ')
    choice6 = float(choice6)
    bodyweight = choice6
    #Calculate V02 max
    v02max = 88.02 + (3.716 * gender) - (0.0753 * bodyweight) - (2.767 * testcompletiontime)
    v02max = str(v02max)
    #Predict V02 max with 90% confidence level
    print('Your v02max is estimated to be: ' + v02max + ' mlkg')
    print('DISCLAIMER: Please understand that this test has an accuracy prediction of 90% and a standard error of 2.8 mlkg. This test is not 100% accurate.')
    print('Thank you for using Running Conversion Calculator! Good luck on your running and THE GRIND NEVER STOPS!')
            
else:
    #Ending message for program
    print('Thank you for using Running Conversion Calculator! Good luck on your running and THE GRIND NEVER STOPS!')
