import pytube
import moviepy.editor as mp

''' 
    Metinlestir() fun'a gönderilmek üzere global 
    değişken olarak downloadYotube() fun'nun bloklarında
    video bilgisine göre atanır.
'''
video_title = ""

def downloadYouTube(url):
    global video_title
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(file_extension='mp4').first()
    video.download(f'static/Video Files/{video.title}')

    # print(video.title)
    # Metinlsitir() fun için dosya yolu belirlenir
    file_path = f'static/Video Files/{video.title}/{video.title}'
    video_title = video.title
    print("Video indirildi!")

    # MoviePy kütüphanesi sayesinde video ses formatına çevrilir
    clip = mp.VideoFileClip(file_path + '.mp4')
    clip.audio.write_audiofile(file_path + '.wav')
    print("Ses formatına çevrildi!")
    return file_path + '.wav'

    