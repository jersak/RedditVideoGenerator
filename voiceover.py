import pyttsx3
from gtts import gTTS

voiceoverDir = "Voiceovers"

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    # engine = pyttsx3.init()
    # engine.setProperty('rate', 125)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[2].id)
    # engine.save_to_file(text, filePath)
    # engine.runAndWait()

    tts = gTTS(text, lang='en')
    tts.save(filePath)
    return filePath