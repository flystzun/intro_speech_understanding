import speech_recognition

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    r = sr.Recognizer()
    with sr.Audiofile(filename, language=language) as source
        audio = r.record(source)
        text + recognizer_google(audio)
    return text
