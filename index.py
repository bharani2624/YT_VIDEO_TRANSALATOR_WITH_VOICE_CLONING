from flask import Flask,render_template,request
from pytube import YouTube
from modules.helperFunctions import *
from modules.voiceCloning import *
from modules.voice_cloning import *
from pytube import extract
from modules.combined import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download',methods=['POST'])

def download():
    if request.method=='POST':
        yt_link=request.form['ytlink']
        lan_sel=request.form['language']
        Download(yt_link,lan_sel)
        return "Downloaded"
 
def Download(Link,lan):
    id=extract.video_id(Link)
    target_audience=lan
    print(target_audience)
    installVideo(Link)
    get_transcript(id,"data/transcript.txt")
    extract_audio("videos/Original_video","audios/sample.mp3")

    detect_pauses("audios/sample.mp3")

    get_translation("data/transcript.txt","data/translated_transcript.txt",target_audience)

    tts("data/translated_transcript.txt","audios/VoiceOver.mp3","audios/sample.mp3")

    muted_audio=mute_time_frames("audios/VoiceOver.mp3",detect_pauses("audios/sample.mp3"))

    output_file_path="audios/output.mp3"
    muted_audio.export(output_file_path, format="mp3")
    
    replace_audio("videos/Original_Video", "audios/output.mp3", "videos/Final_Video.mp4")    




if __name__ == '__main__':
    app.run(debug=True)


