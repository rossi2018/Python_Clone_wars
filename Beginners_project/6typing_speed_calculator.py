#Typing speed calculator to calculate the speed of word you type per second and number of wrong words

import time
import random

#Steps to make typing speed calculator
#part one
#Make a list that consist of strings of sentences i.e three or more than three
#use random.choce function to pick a sentence from any of the three or more sentence
#Print out the selected sentence that was generated using random.choice in a variable
#The next step will be to print out input that will contain where the user need to type the corresponding sentence 


#Part two will be to write a function that will calculate the speed of the typing using the formular
#speed=distance/time where we have three parameter:start time,end time and length of the sentence(which is the distance)
#to get the time we need the start time and end time using epoch time 
#after that, return the speed using round function to 2 decimal place

#Part three creat a function that will count for the errors when typing 
#the function will have two argument: length of the saved word and user input(to see if it correspond with saved word)
#use for loop to loop throgh each user input word if it corresponds to save word
#Initialize error 
#encounterd index error when using if statement when input is not equal to output
#Have to use try and except to campture the error 

#Lastly called out the  two functions 

def speed_of_typing(start_time,end_time,sentence_length):
    total_time=round(end_time-start_time,2)
    speed=len(sentence_length)/total_time
    return round(speed)

def error_count(saved_sentences,user_input):
    error=0
    for words in range(len(saved_sentences)):
        try:
            if  saved_sentences[words] != user_input[words]:
                error=error+1
        except:
            error=error+1
    return error


stord_sentences=[
"Netflix is running down that hill.Netflix wants what Disney and HBO have franchises so popular that fans get tattoos of them",
"The Marvel Cinematic Universe keeps expanding.In 2008, the Marvel Cinematic Universe (MCU) had its own Big Bang with the launch of Iron Man",
"Just realizing that it’s basically the middle of August and we still don’t have a definitive “Song of the Summer” for everyone to rally around"] 


if __name__=="__main__":
    while True:
        continue_playin=input("Do you want to play: yes or no \n")
        if continue_playin=="yes":
            sentence=random.choice(stord_sentences)
            print("--------------------------------------Welcom to typing speed------------------------------------------------------------------")
            print(sentence)
            print("")


            time_start=time.time()
            typing_input=input("Enter the corresponding character that display above ^^ below  \n")
            time_end=time.time()

            print("Your speed is {} w/s" .format(speed_of_typing(time_start,time_end,typing_input)))
            print("Error encountered while typing is {} count(s)".format(error_count(sentence,typing_input)))
        elif continue_playin=="no":
            print("Thanks you ")
            break
        else:
            print("Wrong input")    
        
