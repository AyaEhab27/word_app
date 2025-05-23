import re


def clean_and_split_text(text, lang):
    if lang == "ar":
        
        text = re.sub(r'[ًٌٍَُِّْ]', '', text)
        text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
        
        text = text.replace('ى', 'ي')
    else:
        text = re.sub(r'[^\w\s]', '', text)
        text = text.lower()
    
    return text.strip().split()
