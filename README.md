#Running Conversion Calculator
#Author: Yash Hooda
#Date Created: 02/11/2023
#This Python Program calculates the Running pace, distance, or time and predicts race time. It can also predict your running training paces.

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
    
    runningtime = input("Enter your current running time (in minutes): ")
    runningdistance = input("Enter your current running distance (in miles): ")
    predictedracedistance = input("Enter your goal race distance (in miles): ")
    predictedracetime = float(runningtime) * pow(float(predictedracedistance)/float(runningdistance), 1.06)
    predictedracetime = str(predictedracetime)
    predictedracedistance = str(predictedracedistance)
    
    print("Your predicted race time for " + predictedracedistance + " miles is " + predictedracetime + " minutes.")
    print(" ")
    
    #print('Would you like to calculate your training paces?')
    
    
else:
    print(' ')
    
choice3 = input('Do you want to calculate your training paces? (y/n): ')
if choice3 == "y":
    
    predictedracetime = float(predictedracetime)
    predictedracetime = float(runningtime) * pow(float(1)/float(runningdistance), 1.06)
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
    
    print('Thank you for using Running Conversion Calculator! Good luck on your running and THE GRIND NEVER STOPS!')
    
else:
    print('Thank you for using Running Conversion Calculator! Good luck on your running and THE GRIND NEVER STOPS!')
    

            
        
