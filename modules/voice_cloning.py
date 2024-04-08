from elevenlabs import generate, play,save,clone
import os

def tts(text_file_path,output_file_path,sample_path):
    with open(text_file_path,'r',encoding="utf-8") as file:
        text=file.read()
    Voice=clone(api_key="e64474999e93f4094cad148c7fe513e2",
                name="ABD",
                files=[sample_path])    
    audio=generate(api_key="e64474999e93f4094cad148c7fe513e2",
                   text=text,
                   voice=Voice,
                   model="eleven_multilingual_v2")  
    save(audio,output_file_path)
    print(f"VoiceOver.mp3 is successfully saved in {output_file_path}")

