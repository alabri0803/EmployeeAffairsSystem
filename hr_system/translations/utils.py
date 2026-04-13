from googletrans import Translator

translator = Translator()

SPECIAL_TRANSLATIONS = {
    "Said": "سعيد",
    "Al-Abri": "العبري"
}

def translate_text(text, target='en'):
    # Check if text exists in special translations
    if text in SPECIAL_TRANSLATIONS:
        return SPECIAL_TRANSLATIONS[text]

    return translator.translate(text, dest=target).text
