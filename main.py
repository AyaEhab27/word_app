from fastapi import FastAPI, UploadFile, File, Form
from utils.speech_to_text import convert_audio_to_text
from utils.language_detection import detect_language
from utils.text_processing import clean_and_split_text
from utils.glb_mapping import get_animation_links
from utils.cloudinary_helper import upload_to_cloudinary
import os

app = FastAPI()

@app.post("/translate/")
async def translate_text(text: str = Form(None), audio: UploadFile = File(None)):
    if not text and not audio:
        return {"error": "يجب إدخال نص أو ملف صوتي"}

    if audio:
        audio_bytes = await audio.read()
        text = convert_audio_to_text(audio_bytes)
        if not text:
            return {"error": "تعذر تحويل الصوت إلى نص"}

    language = detect_language(text)
    cleaned_text = clean_and_split_text(text, language)
    animation_urls = get_animation_links(cleaned_text, language)
    
    # حفظ الروابط في Cloudinary مع الحفاظ على نفس الاسم
    cloudinary_urls = []
    for url in animation_urls:
        try:
            # استخراج اسم الملف من الرابط
            filename = os.path.basename(url).split('?')[0]  # إزالة أي query parameters
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