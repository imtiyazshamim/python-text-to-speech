import pyttsx3
kitty =pyttsx3.init()
speech= input("say something:  ")
kitty.say(speech)
kitty.runAndWait()