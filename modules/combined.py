import librosa
import numpy as np
from pydub import AudioSegment

def detect_pauses(audio_file_path, threshold_db=-40, window_length=0.1, hop_length=512):
    y, sr = librosa.load(audio_file_path, sr=None)
    energy = librosa.feature.rms(y=y, frame_length=int(sr * window_length), hop_length=hop_length)
    energy_db = librosa.amplitude_to_db(energy, ref=np.max)
    pause_indices = np.where(energy_db < threshold_db)[1]
    pause_timeframes = []
    current_start = None
    for idx in pause_indices:
        if current_start is None:
            current_start = idx * hop_length / sr
        elif idx == pause_indices[-1] or idx != pause_indices[np.where(pause_indices == idx)[0][0] + 1] - 1:
            pause_timeframes.append((current_start, (idx + 1) * hop_length / sr))
            current_start = None
    return pause_timeframes

def mute_time_frames(audio_file_path, pause_timeframes):
    audio = AudioSegment.from_file(audio_file_path)
    muted_audio = audio
    for start_time, end_time in pause_timeframes:
        start_index = int(start_time * 1000)
        end_index = int(end_time * 1000)
        muted_audio = muted_audio[:start_index] + AudioSegment.silent(duration=end_index-start_index) + muted_audio[end_index:]
    return muted_audio

# if __name__ == "__main__":
#     audio_file_path = "sample.mp3"
#     pause_timeframes = detect_pauses(audio_file_path)
#     muted_audio = mute_time_frames("VoiceOver.mp3", pause_timeframes)
#     output_file_path = "output.mp3"
#     muted_audio.export(output_file_path, format="mp3")


