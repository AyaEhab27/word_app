import json
import os
from pathlib import Path
from utils.cloudinary_helper import upload_to_cloudinary
import re

# مسار مجلد mappings
MAPPINGS_DIR = Path(__file__).parent.parent / "mappings"

# أولاً: تعريف الدالة load_json قبل استخدامها
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
        # معالجة الأرقام العربية
        if lang == "ar":
            word = normalize_numerals(word)
        
        # باقي الكود...
# ثانياً: تحميل mappings باستخدام الدالة التي أصبحت معرّفة الآن
mappings = {
    "ar_letters": load_json("arabic_letters.json"),
    "en_letters": load_json("english_letters.json"),
    "ar_words": load_json("arabic_words.json"),
    "en_words": load_json("english_words.json"),
    "ar_numbers": load_json("arabic_numbers.json"),
    "en_numbers": load_json("english_numbers.json")
}

# def get_animation_links(words, lang):
#     result = []
#     word_map = mappings[f"{lang}_words"]
#     number_map = mappings[f"{lang}_numbers"]
#     letter_map = mappings[f"{lang}_letters"]

#     # أولاً: محاولة العثور على الجملة الكاملة
#     full_phrase = ' '.join(words)
#     normalized_phrase = normalize_numerals(full_phrase) if lang == "ar" else full_phrase.lower()
    
#     # البحث في الكلمات الكاملة
#     found_in_dict = False
#     for key in word_map:
#         if normalized_phrase == key.lower():
#             result.append(word_map[key]["url"])
#             found_in_dict = True
#             break

#     # إذا وجدنا الجملة كاملة، نعود بالنتيجة
#     if found_in_dict:
#         return result

#     # إذا لم نجد الجملة كاملة، نبحث في كل كلمة على حدة
#     for word in words:
#         normalized_word = normalize_numerals(word) if lang == "ar" else word.lower()
#         word_found = False

#         # البحث في الكلمات المفردة
#         for key in word_map:
#             if normalized_word == key.lower():
#                 result.append(word_map[key]["url"])
#                 word_found = True
#                 break

#         # إذا لم توجد الكلمة، البحث في الأرقام
#         if not word_found and normalized_word in number_map:
#             result.append(number_map[normalized_word]["url"])
#             word_found = True

#         # إذا لم توجد كلمة أو رقم، تقسيم الكلمة إلى حروف
#         if not word_found:
#             for char in word:
#                 char_normalized = normalize_numerals(char) if lang == "ar" else char.lower()
#                 char_found = False
                
#                 # البحث في الحروف
#                 for letter_key in letter_map:
#                     if char_normalized == letter_key.lower():
#                         result.append(letter_map[letter_key]["url"])
#                         char_found = True
#                         break
                
#                 if not char_found and lang == "ar":
#                     # محاولة إزالة التشكيل إذا كان حرف عربي
#                     clean_char = re.sub(r'[ًٌٍَُِّْ]', '', char)
#                     if clean_char and clean_char != char:
#                         for letter_key in letter_map:
#                             if clean_char.lower() == letter_key.lower():
#                                 result.append(letter_map[letter_key]["url"])
#                                 break

#     return result


# def get_animation_links(words, lang):
#     result = []
#     word_map = mappings[f"{lang}_words"]
#     number_map = mappings[f"{lang}_numbers"]
#     letter_map = mappings[f"{lang}_letters"]

#     # أولاً: محاولة العثور على الجملة الكاملة
#     full_phrase = ' '.join(words)
#     normalized_phrase = normalize_numerals(full_phrase) if lang == "ar" else full_phrase.lower()
    
#     # البحث في الكلمات الكاملة (مع مراعاة الهاء والتاء المربوطة)
#     found_in_dict = False
#     for key in word_map:
#         if normalized_phrase == key.lower():
#             result.append(word_map[key]["url"])
#             found_in_dict = True
#             break

#     if found_in_dict:
#         return result

#     # إذا لم نجد الجملة كاملة، نبحث في كل كلمة على حدة
#     for word in words:
#         normalized_word = normalize_numerals(word) if lang == "ar" else word.lower()
#         word_found = False

#         # البحث في الكلمات المفردة (مع مراعاة الهاء والتاء المربوطة)
#         for key in word_map:
#             if normalized_word == key.lower():
#                 result.append(word_map[key]["url"])
#                 word_found = True
#                 break

#         # إذا لم توجد الكلمة، البحث في الأرقام
#         if not word_found and normalized_word in number_map:
#             result.append(number_map[normalized_word]["url"])
#             word_found = True

#         # إذا لم توجد كلمة أو رقم، تقسيم الكلمة إلى حروف
#         if not word_found:
#             for char in word:
#                 char_normalized = normalize_numerals(char) if lang == "ar" else char.lower()
#                 char_found = False
                
#                 # البحث في الحروف (مع معالجة خاصة للهاء والتاء المربوطة)
#                 if lang == "ar":
#                     # معالجة خاصة للتاء المربوطة والهاء
#                     if char == 'ة':
#                         # حاول البحث عن 'ه' إذا لم تجد 'ة'
#                         for letter_key in letter_map:
#                             if 'ه' == letter_key:
#                                 result.append(letter_map[letter_key]["url"])
#                                 char_found = True
#                                 break
#                     elif char == 'ه':
#                         for letter_key in letter_map:
#                             if 'ه' == letter_key:
#                                 result.append(letter_map[letter_key]["url"])
#                                 char_found = True
#                                 break
                
#                 if not char_found:
#                     for letter_key in letter_map:
#                         if char_normalized == letter_key.lower():
#                             result.append(letter_map[letter_key]["url"])
#                             char_found = True
#                             break
                
#                 if not char_found and lang == "ar":
#                     # محاولة إزالة التشكيل إذا كان حرف عربي
#                     clean_char = re.sub(r'[ًٌٍَُِّْ]', '', char)
#                     if clean_char and clean_char != char:
#                         for letter_key in letter_map:
#                             if clean_char.lower() == letter_key.lower():
#                                 result.append(letter_map[letter_key]["url"])
#                                 break

#     return result




# def get_animation_links(words, lang):
#     result = []
#     word_map = mappings[f"{lang}_words"]
#     number_map = mappings[f"{lang}_numbers"]
#     letter_map = mappings[f"{lang}_letters"]

#     # قائمة لتخزين الكلمات المجمعة المؤقتة
#     temp_phrase = []
    
#     for word in words:
#         normalized_word = normalize_numerals(word) if lang == "ar" else word.lower()
#         found = False

#         # إضافة الكلمة الحالية إلى العبارة المؤقتة
#         temp_phrase.append(normalized_word)
#         current_phrase = ' '.join(temp_phrase)

#         # البحث عن العبارة الحالية في القاموس
#         for key in word_map:
#             if current_phrase == key.lower():
#                 result.append(word_map[key]["url"])
#                 temp_phrase = []  # إعادة تعيين العبارة المؤقتة
#                 found = True
#                 break

#         if found:
#             continue

#         # إذا لم يتم العثور على العبارة، نبحث في الكلمة المفردة
#         for key in word_map:
#             if normalized_word == key.lower():
#                 # إذا كانت هناك كلمات متراكمة في العبارة المؤقتة
#                 if temp_phrase[:-1]:  # إذا كان هناك كلمات سابقة
#                     # معالجة الكلمات السابقة كحروف
#                     for prev_word in temp_phrase[:-1]:
#                         for char in prev_word:
#                             # معالجة خاصة للتاء المربوطة والهاء
#                             processed_char = handle_arabic_special_chars(char)
#                             # البحث عن الحرف في letter_map
#                             for letter_key in letter_map:
#                                 if processed_char == letter_key.lower():
#                                     result.append(letter_map[letter_key]["url"])
#                                     break
                
#                 result.append(word_map[key]["url"])
#                 temp_phrase = []
#                 found = True
#                 break

#         if not found and normalized_word in number_map:
#             # معالجة أي كلمات متراكمة كحروف
#             if temp_phrase[:-1]:
#                 for prev_word in temp_phrase[:-1]:
#                     for char in prev_word:
#                         processed_char = handle_arabic_special_chars(char)
#                         for letter_key in letter_map:
#                             if processed_char == letter_key.lower():
#                                 result.append(letter_map[letter_key]["url"])
#                                 break
            
#             result.append(number_map[normalized_word]["url"])
#             temp_phrase = []
#             found = True

#         if not found and not temp_phrase:
#             # إذا لم تكن هناك كلمات متراكمة، نتعامل مع الكلمة كحروف
#             for char in word:
#                 processed_char = handle_arabic_special_chars(char)
#                 char_normalized = normalize_numerals(processed_char) if lang == "ar" else processed_char.lower()
#                 char_found = False
                
#                 for letter_key in letter_map:
#                     if char_normalized == letter_key.lower():
#                         result.append(letter_map[letter_key]["url"])
#                         char_found = True
#                         break
                
#                 if not char_found and lang == "ar":
#                     clean_char = re.sub(r'[ًٌٍَُِّْ]', '', char)
#                     if clean_char and clean_char != char:
#                         clean_char = handle_arabic_special_chars(clean_char)
#                         for letter_key in letter_map:
#                             if clean_char.lower() == letter_key.lower():
#                                 result.append(letter_map[letter_key]["url"])
#                                 break

#     # معالجة أي كلمات متبقية في العبارة المؤقتة
#     if temp_phrase:
#         for word in temp_phrase:
#             for char in word:
#                 processed_char = handle_arabic_special_chars(char)
#                 char_normalized = normalize_numerals(processed_char) if lang == "ar" else processed_char.lower()
#                 char_found = False
                
#                 for letter_key in letter_map:
#                     if char_normalized == letter_key.lower():
#                         result.append(letter_map[letter_key]["url"])
#                         char_found = True
#                         break
                
#                 if not char_found and lang == "ar":
#                     clean_char = re.sub(r'[ًٌٍَُِّْ]', '', char)
#                     if clean_char and clean_char != char:
#                         clean_char = handle_arabic_special_chars(clean_char)
#                         for letter_key in letter_map:
#                             if clean_char.lower() == letter_key.lower():
#                                 result.append(letter_map[letter_key]["url"])
#                                 break

#     return result

# def handle_arabic_special_chars(char):
#     """معالجة خاصة للحروف العربية مثل الهاء والتاء المربوطة"""
#     if char == 'ة':
#         return 'ه'  # يمكنك تغيير هذا إذا كنت تريد التعامل مع التاء المربوطة بشكل منفصل
#     return char

def get_animation_links(words, lang):
    result = []
    word_map = mappings[f"{lang}_words"]
    number_map = mappings[f"{lang}_numbers"]
    letter_map = mappings[f"{lang}_letters"]

    # تحويل قائمة الكلمات إلى نص كامل للبحث عن الجمل
    full_text = ' '.join(words)
    remaining_text = full_text
    
    # البحث عن أطول جملة مطابقة في JSON
    while remaining_text:
        found_phrase = None
        max_length = 0
        
        # البحث عن أطول جملة مطابقة في البداية
        for phrase in word_map:
            if remaining_text.lower().startswith(phrase.lower()):
                if len(phrase) > max_length:
                    max_length = len(phrase)
                    found_phrase = phrase
        
        if found_phrase:
            # إضافة الرابط الخاص بالجملة المطابقة
            result.append(word_map[found_phrase]["url"])
            # إزالة الجملة المطابقة من النص المتبقي
            remaining_text = remaining_text[len(found_phrase):].strip()
        else:
            # إذا لم نجد جملة مطابقة، نأخذ أول كلمة ونبحث عنها
            next_word = remaining_text.split(' ')[0]
            normalized_word = normalize_numerals(next_word) if lang == "ar" else next_word.lower()
            word_found = False
            
            # البحث في الكلمات المفردة
            for key in word_map:
                if normalized_word == key.lower():
                    result.append(word_map[key]["url"])
                    word_found = True
                    break
            
            # إذا لم توجد الكلمة، البحث في الأرقام
            if not word_found and normalized_word in number_map:
                result.append(number_map[normalized_word]["url"])
                word_found = True
            
            # إذا لم توجد كلمة أو رقم، تقسيم الكلمة إلى حروف
            if not word_found:
                for char in next_word:
                    char_normalized = normalize_numerals(char) if lang == "ar" else char.lower()
                    char_found = False
                    
                    # معالجة خاصة للتاء المربوطة والهاء
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
            
            # إزالة الكلمة التي تم معالجتها
            remaining_text = remaining_text[len(next_word):].strip()

    return result

def handle_arabic_special_chars(char):
    """معالجة خاصة للحروف العربية مثل الهاء والتاء المربوطة"""
    if char == 'ة':
        return 'ه'  # يمكنك تغيير هذا إذا كنت تريد التعامل مع التاء المربوطة بشكل منفصل
    return char