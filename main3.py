import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image, ImageTk
import string
from itertools import count
import os

# Initialize recognizer and set up Streamlit interface
r = sr.Recognizer()

isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
           'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 
           'do you have money', 'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 
           'dont worry', 'flower is beautiful', 'good afternoon', 'good evening', 'good morning', 'good night', 
           'good question', 'had your lunch', 'happy journey', 'hello what is your name', 'how many people are there in your family', 
           'i am a clerk', 'i am bore doing nothing', 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 
           'i dont understand anything', 'i go to a theatre', 'i love to shop', 'i had to say something but i forgot', 
           'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
           'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later', 
           'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 
           'shall I help you', 'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 
           'there was traffic jam', 'wait I am thinking', 'what are you doing', 'what is the problem', 'what is todays date', 
           'what is your father do', 'what is your job', 'what is your mobile number', 'what is your name', 'whats up', 
           'when is your interview', 'when we will go', 'where do you stay', 'where is the bathroom', 'where is the police station', 
           'you are wrong', 'address', 'agra', 'ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 
           'banaras', 'banglore', 'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut',
           'crocodile','dasara', 'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 
           'grapes', 'gujrat', 'hello', 'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 
           'kerala', 'krishna', 'litre', 'mango', 'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 
           'orange', 'pakistan', 'pass', 'police station', 'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 
           'saturday', 'september', 'shop', 'sleep', 'southafrica', 'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 
           'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village', 'voice', 'wednesday', 'weight','please wait for sometime',
           'what is your mobile number','what are you doing','are you busy']

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
       'x', 'y', 'z']

def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write("Listening for your command...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            st.write("You said:", command)
            return command
        except sr.UnknownValueError:
            st.write("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            st.write("Sorry, there was an error with the speech recognition service.")
            return None

def display_sign_language(command):
    # Display GIF for recognized command if it exists
    if command in isl_gif:
        gif_path = f"ISL_Gifs/{command}.gif"
        if os.path.exists(gif_path):
            st.image(gif_path)
    # Otherwise, display image for the letter
    else:
        for char in command:
            if char in arr:
                img_path = f'letters/{char}.jpg'
                if os.path.exists(img_path):
                    img = Image.open(img_path)
                    st.image(img, caption=f"Sign for {char.upper()}")

# Main Streamlit App
def main():
    st.title("Hearing Impairment Assistant")
    
    if st.button('Start Listening'):
        command = recognize_speech()
        if command:
            display_sign_language(command)

    st.write("Try saying something like 'hello' or 'goodbye' to see how the assistant reacts.")

if __name__ == "__main__":
    main()
