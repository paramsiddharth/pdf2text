import pyttsx3 # Speech synthesis

def text_to_speech():
    with open('./out/output.txt', 'r') as pages:
        content = pages.read()

    # Initialize the TTS object
    speaker = pyttsx3.init()

    # Pronounce the text
    speaker.say(content)
    speaker.runAndWait()
