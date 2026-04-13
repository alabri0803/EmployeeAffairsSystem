from googletrans import Translator

def translate_text(text, target='en'):
    translator = Translator()
    result = translator.translate(text, dest=target)
    return result.text