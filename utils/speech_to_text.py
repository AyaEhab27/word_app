import speech_recognition as sr
from pydub import AudioSegment
import io

def convert_audio_to_text(audio_bytes):
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    audio = audio.set_channels(1).set_frame_rate(16000)
    recognizer = sr.Recognizer()
    with sr.AudioFile(io.BytesIO(audio.export(format="wav").read())) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data, language="ar-EG")
        except:
            try:
                return recognizer.recognize_google(audio_data, language="en-US")
            except:
                return ""