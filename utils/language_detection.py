from langdetect import detect
import re

def detect_language(text):
    try:
        # تنظيف النص من التشكيل والهمزات
        cleaned_text = re.sub(r'[ًٌٍَُِّْءؤئ]', '', text)
        
        # إذا كان النص يحتوي على أحرف عربية، نرجح أنه عربي
        if any('\u0600' <= char <= '\u06FF' for char in cleaned_text):
            return "ar"
            
        # إذا لم يكن هناك أحرف عربية، نستخدم الكشف التلقائي
        lang = detect(cleaned_text)
        return "ar" if lang == "ar" else "en"
    except:
        # إذا فشل الكشف، نعود للتحقق من الأحرف العربية
        if any('\u0600' <= char <= '\u06FF' for char in text):
            return "ar"
        return "en"