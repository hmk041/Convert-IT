import speech_recognition as sr


# Recognition Kütüphanesi ile ses dosyasını metne çevirme

'''
    Verilen ses dosya yolu ile ses dosyasına erişilir.
    Ardından ses dosyası kadar Recognition işlemi yapılır.
    Ses dinlenir ve tek tek metne çevrilir.
    (Metinleştirme işlem için Googe,IBM,BING gibi
    fırmaların sunduğu kütüphaneler ve fonksiyonlar kullanılabilir)
'''
def metinlestir(audio_path,title):
    recoder = sr.Recognizer()

    ses = sr.AudioFile(audio_path)

    with ses as source:
        audio_file = recoder.record(source)
        recoder.adjust_for_ambient_noise(source)
    result = recoder.recognize_google(audio_file)

    # Çıktıyı text olarak belirlenen dosya yoluna kaydetmek
    with open(f'static/Recognition Files/{title}.txt', mode='w') as file:
        file.write("Cevirilen metin:")
        file.write("\n")
        file.write(result)
        print("Speech dosyasi basarili bir sekilde olusturuldu!")



'''
import os
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence



def load_chunks(filename):
    long_audio = AudioSegment.from_mp3(filename)
    audio_chunks = split_on_silence(
        long_audio, min_silence_len=1800,
        silence_thresh=-17
    )
    return audio_chunks




def metinlestir(audio_path,title):
    recognizer = sr.Recognizer()
    for audio_chunk in load_chunks(audio_path):
        audio_chunk.export("temp", format="wav")
        with sr.AudioFile("temp") as source:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                print("Chunk : {}".format(text))
            except Exception as ex:
                print("Error occured")
                print(ex)

    print("++++++")
'''

