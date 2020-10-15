# Run the command below if package not installed
# pip install pyttsx3

# Importing pyttsx3
import pyttsx3

engine = pyttsx3.init()  # object creation

""" Setting Up Of Voice """

""" RATE """
rate = engine.getProperty('rate')  # getting details of current speaking rate
print("Rate: ", rate)  # printing current voice rate
engine.setProperty('rate', 200)  # setting up new voice rate

""" VOLUME """
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print("Volume: ", volume)  # printing current volume level
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

""" VOICE """
voices = engine.getProperty('voices')  # getting details of current voice
for voice in voices:  # list of language packs available in system
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

""" Speaking """
engine.say("Hello! Myself Chiranjib. Welcome to 30 Days of AIML. My current voice is " + str(
    voice.name) + ",speaking rate " + str(rate) + "and current volume is " + str(
    volume))
engine.runAndWait()
engine.stop()

"""Saving to a file"""
engine.save_to_file("Hello! Myself Chiranjib. Welcome to 30 Days of AIML.", "Output.mp3")
engine.runAndWait()
print("\nAudio Saved!")
