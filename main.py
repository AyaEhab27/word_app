from fastapi import FastAPI, UploadFile, File, Form
from utils.speech_to_text import convert_audio_to_text
from utils.language_detection import detect_language
from utils.text_processing import clean_and_split_text
from utils.glb_mapping import get_animation_links
from utils.cloudinary_helper import upload_to_cloudinary
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate/")
async def translate_text(text: str = Form(None), audio: UploadFile = File(None)):
    if not text and not audio:
        return {"error": "Enter text or voice"}

    if audio:
        audio_bytes = await audio.read()
        text = convert_audio_to_text(audio_bytes)
        if not text:
            return {"error": "Error in text or voice"}

    language = detect_language(text)
    cleaned_text = clean_and_split_text(text, language)
    animation_urls = get_animation_links(cleaned_text, language)
    
    
    cloudinary_urls = []
    for url in animation_urls:
        try:
            
            filename = os.path.basename(url).split('?')[0]  
            cloudinary_url = upload_to_cloudinary(url, public_id=filename)
            cloudinary_urls.append(cloudinary_url)
        except Exception as e:
            cloudinary_urls.append(f"Error uploading {url}: {str(e)}")
    
    return {
        "input_text": text,
        "language": language,
        "original_links": animation_urls,
        "cloudinary_links": cloudinary_urls
    }
