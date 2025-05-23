from langdetect import detect
import re

def detect_language(text):
    try:
        
        cleaned_text = re.sub(r'[ًٌٍَُِّْءؤئ]', '', text)
        
        
        if any('\u0600' <= char <= '\u06FF' for char in cleaned_text):
            return "ar"
            
        
        lang = detect(cleaned_text)
        return "ar" if lang == "ar" else "en"
    except:
        
        if any('\u0600' <= char <= '\u06FF' for char in text):
            return "ar"
        return "en"
