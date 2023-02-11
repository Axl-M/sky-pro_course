# Перевод фразы на английский или русский с помощью Google-переводчика

import googletrans
#
# text_input = input("Введите фразу для перевода: ")
#
# while 1:
#     lang = int(input("1 - для перевода на русский, 2- на английский: "))
#     if lang == 1:
#         dest = 'ru'
#         break
#     elif lang == 2:
#         dest = 'en'
#         break
#     else:
#         print('Вы ввели что-то не то.')
#
# translated_text = googletrans.Translator().translate(text_input, dest=dest).text
# translated_text = googletrans.Translator().translate('cat', dest='ru')
# print(translated_text)
#
# translator = googletrans.Translator()
# translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
# print(translation.text)

# from googletrans import Translator
# translator = Translator(service_urls=['translate.googleapis.com'])
# translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
# 
# from google_trans_new import google_translator
# 
# translator = google_translator()
# translate_text = translator.translate('Hola mundo!', lang_src='es', lang_tgt='en')
# print(translate_text)

# from deep_translator import GoogleTranslator
# GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")
# 'weiter so, du bist toll'

# translation = googletrans.Translator.translate('이 문장은 한글로 쓰여졌습니다.', dest='en')
translation = googletrans.Translator.translate(text='кошка', dest='en')
print(translation.text)
# detected_lang = translator.detect('mein english me hindi likh raha hoon')
# print(detected_lang)
# detected_lang = translator.detect('이 문장은 한글로 쓰여졌습니다.')
# print(detected_lang)
