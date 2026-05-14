import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

print("Available Voices:")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name}, {voice.id}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("All systems are functional")

