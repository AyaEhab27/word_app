import json
import os
from pathlib import Path
from utils.cloudinary_helper import upload_to_cloudinary
import re


MAPPINGS_DIR = Path(__file__).parent.parent / "mappings"


def load_json(file_name):
    file_path = MAPPINGS_DIR / file_name
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)

ARABIC_NUMERALS_MAP = {
    '٠': '0',
    '١': '1',
    '٢': '2',
    '٣': '3',
    '٤': '4',
    '٥': '5',
    '٦': '6',
    '٧': '7',
    '٨': '8',
    '٩': '9'
}

def normalize_numerals(text):
    return ''.join(ARABIC_NUMERALS_MAP.get(char, char) for char in text)

def get_animation_links(words, lang):
    result = []
    for word in words:
        
        if lang == "ar":
            word = normalize_numerals(word)
        
        

mappings = {
    "ar_letters": load_json("arabic_letters.json"),
    "en_letters": load_json("english_letters.json"),
    "ar_words": load_json("arabic_words.json"),
    "en_words": load_json("english_words.json"),
    "ar_numbers": load_json("arabic_numbers.json"),
    "en_numbers": load_json("english_numbers.json")
}


def get_animation_links(words, lang):
    result = []
    word_map = mappings[f"{lang}_words"]
    number_map = mappings[f"{lang}_numbers"]
    letter_map = mappings[f"{lang}_letters"]

    
    full_text = ' '.join(words)
    remaining_text = full_text
    
    
    while remaining_text:
        found_phrase = None
        max_length = 0
        
        
        for phrase in word_map:
            if remaining_text.lower().startswith(phrase.lower()):
                if len(phrase) > max_length:
                    max_length = len(phrase)
                    found_phrase = phrase
        
        if found_phrase:
            
            result.append(word_map[found_phrase]["url"])
            
            remaining_text = remaining_text[len(found_phrase):].strip()
        else:
            
            next_word = remaining_text.split(' ')[0]
            normalized_word = normalize_numerals(next_word) if lang == "ar" else next_word.lower()
            word_found = False
            
            
            for key in word_map:
                if normalized_word == key.lower():
                    result.append(word_map[key]["url"])
                    word_found = True
                    break
            
           
            if not word_found and normalized_word in number_map:
                result.append(number_map[normalized_word]["url"])
                word_found = True
            
            
            if not word_found:
                for char in next_word:
                    char_normalized = normalize_numerals(char) if lang == "ar" else char.lower()
                    char_found = False
                    
                    
                    if lang == "ar":
                        if char == 'ة':
                            for letter_key in letter_map:
                                if 'ه' == letter_key:
                                    result.append(letter_map[letter_key]["url"])
                                    char_found = True
                                    break
                        elif char == 'ه':
                            for letter_key in letter_map:
                                if 'ه' == letter_key:
                                    result.append(letter_map[letter_key]["url"])
                                    char_found = True
                                    break
                    
                    if not char_found:
                        for letter_key in letter_map:
                            if char_normalized == letter_key.lower():
                                result.append(letter_map[letter_key]["url"])
                                char_found = True
                                break
                    
                    if not char_found and lang == "ar":
                        clean_char = re.sub(r'[ًٌٍَُِّْ]', '', char)
                        if clean_char and clean_char != char:
                            clean_char = handle_arabic_special_chars(clean_char)
                            for letter_key in letter_map:
                                if clean_char.lower() == letter_key.lower():
                                    result.append(letter_map[letter_key]["url"])
                                    break
            
            
            remaining_text = remaining_text[len(next_word):].strip()

    return result

def handle_arabic_special_chars(char):
    """معالجة خاصة للحروف العربية مثل الهاء والتاء المربوطة"""
    if char == 'ة':
        return 'ه'  # يمكنك تغيير هذا إذا كنت تريد التعامل مع التاء المربوطة بشكل منفصل
    return char
