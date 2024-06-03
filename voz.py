from deep_translator import GoogleTranslator
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es-ES')
            rec = rec.lower()
            return rec
    except:
        return ""

def translate_text(text, dest_lang):
    try:
        translated_text = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        return translated_text
    except Exception as e:
        return f"Error en la traducción: {e}"

def empezar():
    talk("¿Qué quieres traducir del español?")
    talk("Puedo traducir al inglés, japonés, italiano y francés")
    print("¿Quieres traducir del español al inglés, japonés, italiano o francés?")

    rec = listen()

    if "español al inglés" in rec:
        dest_lang = 'en'
    elif "español al japonés" in rec:
        dest_lang = 'ja'
    elif "español al francés" in rec:
        dest_lang = 'fr'
    elif "español al italiano" in rec:
        dest_lang = 'it'
    else:
        talk("No entendí la opción. Inténtalo de nuevo.")
        return

    talk("¿Qué quieres decir?")
    text_to_translate = listen()

    if text_to_translate:
        translated_text = translate_text(text_to_translate, dest_lang)
        talk(translated_text)
        print(translated_text)
    else:
        talk("No se escuchó nada. Inténtalo de nuevo.")

empezar()
