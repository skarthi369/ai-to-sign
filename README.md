# Speech-to-Sign-Language-Translator (ISL)

**An application which takes in live speech or audio recording as input, converts it into text and displays the relevant Indian Sign Language images or GIFs.**

**An application which takes in live speech or audio recording as input, converts it into text and displays the relevant Indian Sign Language images or GIFs.**

## Features
- Front-end using EasyGui and Streamlit
- Speech input through microphone using PyAudio
- Speech recognition using Google Speech API and Sphinx (for offline use)
- Text Preprocessing using NLP
- Dictionary based Machine Translation
- Interactive web interface

## Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/skarthi369/ai-to-sign.git
cd ai-to-sign
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

You can run the application in three different ways:

1. Using Streamlit interface (Recommended):
```bash
streamlit run main3.py
```

2. Using the basic interface:
```bash
python main1.py
```

3. Using the alternative interface:
```bash
python main2.py
```

### Usage Instructions
1. Launch the application using any of the methods above
2. When using the speech input:
   - Hit the record button to start taking speech input
   - Speak clearly into your microphone
   - The application will process your speech and show the corresponding signs
   - Say "goodbye" to exit the application
3. When using text input:
   - Type your text in the input field
   - The application will show the corresponding signs


**Sign language is a visual language that is used by deaf people as their mother tongue. Unlike acoustically conveyed sound patterns, sign language uses body language and manual communication to fluidly convey the thoughts of a person. Due to considerable time required in learning the Sign Language,  it becomes difficult to communicate with these specially abled people, and thus creates a communication gap.**

## Objective
**This Audio to Sign Language converter aims at :**
- Providing information access and services to deaf people in Indian sign language.
- Developing a scalable project which can be extended to capture whole vocabulary of ISL through manual and non-manual signs

It can be developed as a desktop or mobile application to enable specially abled people to communicate easily and effectively with others

**Sign language is a visual language that is used by deaf people as their mother tongue. Unlike acoustically conveyed sound patterns, sign language uses body language and manual communication to fluidly convey the thoughts of a person. Due to considerable time required in learning the Sign Language, people find it difficult to communicate with these specially abled people, creating a communication gap. Thus, we propose an application which takes in live speech or audio recording as input, converts it into text and displays the relevant Indian Sign Language images or GIFs.**

## Algorithm
Audio to Sign Language Translator
1. Start
2. Getting the Speech
   1. Listen for 1 second and calibrate the energy threshold for ambient noise
levels.
   2. Listen the Speech using Microphone.
Now the energy threshold is already set to a good value, and we can
reliably catch speech right away.
3. Recognise the Speech.
4. Convert Speech to Text.
   1. Make the Text to lowercase for further manipulation.
5. Detected Text
   1. If “goodbye” then exit.
   2.Else if Detected Text in predefined Dictionary Words. Display
respective GIFs of the Phrase.
   3. Else Count the Letters of the Word/Phrase.
      1. Display the Visual of the phrase with some delay of Actions.
   4. Continue all the steps from Step 3, and continue till the Speech Ends.
6. If Error in Step 2, That is if no Speech Detected then display error message
“Could not listen”.

**Due to considerable time required in learning the Sign Language, people find it difficult to communicate with these specially abled people, creating a communication gap. Thus the Audio to Sign Language converter is important and significant because it helps in providing information access and services to deaf people in Indian sign language and develops a scalable project which can be extended to capture whole vocabulary of ISL through manual and non-manual signs. It also can be developed as a desktop or mobile application to enable specially abled people to communicate easily and effectively with others.**


