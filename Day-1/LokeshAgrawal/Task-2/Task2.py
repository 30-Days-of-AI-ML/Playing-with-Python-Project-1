# -------------------------------------------------------------Using gTTS and playsound module--------------------------------------------------------------

# importing gTTS and playsound module
from gtts import gTTS
from playsound import playsound

# enter our text that we want to convert into speech
text_val = 'Hello, My name is Lokesh Agrawal'
language = 'en'

# making object of gTTs and saving our speech
obj = gTTS(text = text_val, lang = language , slow= False)
obj.save("exam.mp3")

# playing our speech using playsound module
playsound("exam.mp3")


# -----------------------------------------------------------------Using pypiwin32 module-----------------------------------------------------------------------

# importing win32com.client and making object of it 
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    # taking user input 
    s = input("Enter your word you want to say: \n")
    speaker.Speak(s)
    
    # taking user choice
    print("Do you want to change the text-to-speech?\n")
    print("Press--\n\t\t","1 for again\n\t\t","2 for quit")
    user_choice = input("Enter any key mentioned above: \n")
    if user_choice == '1':
        continue
    elif user_choice == '2':
        break
    else:
        print("Please,Enter valid input!")
        continue
