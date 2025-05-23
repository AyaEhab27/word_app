import re

# def clean_and_split_text(text, lang):
#     if lang == "ar":
#         text = re.sub(r'[ًٌٍَُِّْ]', '', text)  # إزالة التشكيل
#         text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
#         text = text.replace('ة', 'ه').replace('ى', 'ي')
#         text = text.strip()
#     else:
#         text = re.sub(r'[^\w\s]', '', text)  # إزالة علامات الترقيم
#         text = text.lower().strip()  # توحيد الحروف الصغيرة
    
#     # إرجاع الجملة كاملة ثم الكلمات المفردة إذا كانت جملة
#     words = text.split()
#     return [text] + words if len(words) > 1 else words


# def clean_and_split_text(text, lang):
#     if lang == "ar":
#         text = re.sub(r'[ًٌٍَُِّْ]', '', text)
#         text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
#         text = text.replace('ة', 'ه').replace('ى', 'ي')
#     else:
#         text = re.sub(r'[^\w\s]', '', text)
#         text = text.lower()
    
#     # إرجاع الكلمات المفردة فقط (بدون الجملة الكاملة)
#     return text.strip().split()

def clean_and_split_text(text, lang):
    if lang == "ar":
        # إزالة التشكيل فقط مع الحفاظ على الهاء والتاء المربوطة
        text = re.sub(r'[ًٌٍَُِّْ]', '', text)
        text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
        # لا نغير 'ة' إلى 'ه' هنا لأننا نريد التعرف على الكلمات كما هي في JSON
        text = text.replace('ى', 'ي')
    else:
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
    
    return text.strip().split()