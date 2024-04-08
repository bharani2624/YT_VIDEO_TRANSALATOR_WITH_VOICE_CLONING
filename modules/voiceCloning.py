from elevenlabs import clone, generate, set_api_key, save, Voices, Voice
from dotenv import dotenv_values
from os import listdir, system

import requests

if not '.env' in listdir('.'):
    api_key = "48702b94422c22f25396461d9d1410af"

def voiceOverNoClone(transcript:str, output_file:str):
    set_api_key(api_key)
    print("Generating a Voice Over...")
    audio = generate(text=transcript)
    save(audio, output_file)
    
def voiceOver(transcript:str, output_file:str):
    set_api_key(api_key)
    print("Generating a Voice Over...")
    voice = clone(
        name="Antonio",
        files=["audios/sample.mp3"],
        model='eleven_multilingual_v2'
    )
    audio = generate(text=transcript, voice=voice)
    save(audio, output_file)

def delete_cloned_voice():
       
    HEADERS = {
        "Accept": "application/json",
        "xi-api-key": api_key
    }

    voices = Voices.from_api()
    URL = f"https://api.elevenlabs.io/v1/voices/{voices[0].voice_id}"
    
    response = requests.delete(URL, headers=HEADERS)

    print(response)