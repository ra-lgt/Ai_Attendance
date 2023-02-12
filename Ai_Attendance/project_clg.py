#imports
import pyaudio
import speech_recognition as sr
import pyttsx3 as speech
import cv2 as cv
import face_recognition
from datetime import *
import os
#define_start
speech=speech.init()
speech.setProperty('rate',150)
recon=sr.Recognizer()
#define_end
                                                                
names=["Abhirami","Ajay","Kishore","Sampath","Mohan","Selva"]    #namelist
text="" #Ajay 

####################################Manual validation################################

def manual_validation():
    print("\nstart your 1st letter as capital don't provide your initial")
    speech.say("start your 1st letter as capital don't provide your initial")
    speech.runAndWait()
    
    user_name=input()
    if(user_name in names):
        global text
        text=text+user_name
        webcam()
    else:
        print("Your name is not found in the namelist please contact the admin")

#####################################choice################################

def name():
    print("What is your name\n")
    speech.say("what is your name")  #gets input(voice) from user
    speech.runAndWait()
    
    print("you can use voice assist or also manual validation\n")
    speech.say("you can use voice assist or also manual validation")
    speech.runAndWait()
    
    print("press 1 if you need voice assist or press 2 for manual validation\n")
    speech.say("press 1 if you need voice assist or press 2 for manual validation")
    speech.runAndWait()
    
    
    user_choice=int(input())
    
    if(user_choice==1):
        validation_name()
    
    elif(user_choice==2):
        manual_validation()
    
    else:
        print("Invalid choice")

####################################attendance####################################

def attendance():
    
    with open('F:\\visual_studio_codes\\python\\attendance.txt','r+') as myfile:
        
        data=myfile.read()
        today=date.today()
        Time=datetime.now().time()
        
        myfile.write("Name:{name}  Date:{date}  Time:{time}\n".format(name=text,date=today,time=Time))
        myfile.truncate()
        cv.destroyAllWindows()
        exit()
##################################image_validateion################################

def validation():
    try:
        data=face_recognition.load_image_file("F:\\visual_studio_codes\\python\\known_faces\\%s.jpg"%text)
        validation=face_recognition.load_image_file("F:\\visual_studio_codes\\python\\%s.jpg"%text)
    
        lst1=face_recognition.face_encodings(validation)[0]
        lst=face_recognition.face_encodings(data)[0]
    
        result=face_recognition.compare_faces([lst1],lst)
        if(result[0]==True):

            print("Your attendance is added successfully")
            os.remove("F:\\visual_studio_codes\\python\\%s.jpg"%text)
            attendance()
        else:
            print("Your face doesn't match")
    except:
        print("try again")
#####################################webcam##########################################

def webcam():
    cam=cv.VideoCapture(0)
    
    while True:
        
        sussess,frame=cam.read()
        
        cv.imshow('camera',frame)
        key_press=cv.waitKey(10)
        
        if(key_press==13):
            cv.imwrite('%s.jpg'%text,frame) #Ajay.jpg

        elif(key_press==27): #esc
            validation()
        elif(key_press==80):  #q
            cv.destroyAllWindows()
        else:
            continue

###################################voice_assist_validation######################

def validation_name():
    
    print("\nSpeak now.....")
    
    with sr.Microphone() as voice:   #opens microphone from system
        audio=recon.listen(voice)   
    
    try:
        text_lst=recon.recognize_google(audio)
        
                
        if(text_lst in names):         #validation
            global text
            text=text+text_lst
            print("hi",text)
            webcam()
        
        else:
            print("you said",text_lst)
            print("Your name is not found in the namelist either try again or please contact the admin")
    
    except:
        print("Try again")
        validation_name()

name()

###########################################code_ends################################################3