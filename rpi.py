import speech_recognition as sr
from adafruit_servokit import ServoKit
import time
import cv2
# Initialize recognizer class (for recognizing speech)
recognizer = sr.Recognizer()


# Create a PCA9685 instance, assuming default address of 0x40
kit = ServoKit(channels=16, address=0x41)
kit.servo[0].set_pulse_width_range(500, 2500)
kit.servo[1].set_pulse_width_range(500, 2500)
kit.servo[2].set_pulse_width_range(500, 2500) 
# Set the servo on channel 0 to 90 degrees (mid-point)


import subprocess
import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

def capture_image(image_name='image.jpg'):
    cam = cv2.VideoCapture(1)

    while True:
        ret, image = cam.read()
        cv2.imshow('Imagetest',image)
        k = cv2.waitKey(1)
        if k != -1:
            break
    cv2.imwrite('/home/vanshksingh/testimage.jpg', image)
    cam.release()
    cv2.destroyAllWindows()
        
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",google_api_key="AIzaSyCbwAj_jEB4q4TP2xF9eCt63TF7zYLIxSk")
                                                            # example
    message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": "Write a two to four word description of the file",
                },
                {"type": "image_url", "image_url": "/home/vanshksingh/testimage.jpg"},
            ]
        )
    response = llm.invoke([message])
    return response.content


# Function to continuously listen for any spoken commands
def listen_for_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Now listening for a command...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Command detected: {command}")
            return command
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            return None

# Function to listen continuously for the wake word
def listen_for_wake_word():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for wake word 'Hey Buddy'...")
        try:
            command = recognizer.recognize_google(recognizer.listen(source, timeout=5, phrase_time_limit=5)).lower()
            if "hey buddy" in command:
                print("Wake word detected!")
                return True
            return False
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            return False

# Function to process commands and control the servo
def process_command(command):
    if "i have a fever" in command:
        print("Moving servo to 20 degrees for 'I have a fever'.")
        kit.servo[0].angle = 180
        kit.servo[1].angle = 150
        kit.servo[2].angle = 80
    elif "i am feeling unwell" in command:
        print("Moving servo to 100 degrees for 'I am feeling unwell'.")
        kit.servo[0].angle = 90
        kit.servo[1].angle = 60
        kit.servo[2].angle = 75
    elif "what is this" in command:
        
        # Capture the image and get description
        print(capture_image('capture_image.jpg'))
        
        
    print("Returning servo to 0 degrees.")
    time.sleep(2)

    kit.servo[0].angle = 0
    kit.servo[1].angle = 0
    kit.servo[2].angle = 0

# Function to retry command recognition
def retry_command(retries=5):
    for _ in range(retries):
        command = listen_for_command()
        if command and any(phrase in command for phrase in ["i have a fever", "i am feeling unwell","what is this"]):
            process_command(command)
            return True
        print("Command not recognized. Retrying...")
    return False

# Main function to keep the mic on after the wake word is detected
def main():
    while True:
        # Listen for the wake word first
        if listen_for_wake_word():
            # Once the wake word is detected, keep listening for further commands
            if retry_command():
                print("Returning to wake word listening...")

if _name_ == "_main_":
    main()
