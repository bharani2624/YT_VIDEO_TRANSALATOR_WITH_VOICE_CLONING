from googletrans import Translator
from gtts import gTTS
import os

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def translate_to_telugu(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='te')
    return translated_text.text

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    os.system("mpg123 output.mp3")  # You may need to change the command based on your operating system

if __name__ == "__main__":
    file_path = 'data/transcript.txt'  # Replace this with the path to your text file
    content = read_text_file(file_path)
    if content:
        print("Original Content:")
        print(content)
        
        translated_content = translate_to_telugu(content)
        print("\nTranslated Content:")
        print(translated_content)

        text_to_speech(translated_content, language='te')
