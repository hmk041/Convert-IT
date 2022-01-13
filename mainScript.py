import recognition
import YTdownloader


# Video linkini input alma
url = input('Link: ')

'''
    Video indirme ve ses formatına çevirme işlemi için url 
    YTdownloader py scriptine gönderilir.
    downloadYoutbe() fun ise kaydedilen ses dosyasının header bilgisi
    return olarak verilir.
    
    Header bilgisi sayesinde dosya ismiyle belirlenen dosya yoluna 
    erişilir ve ses dosyası speech(Metinlestir) işlemine
    taabi tutulur.
    
    Metinleştirme işlemi için ses dosyası yoluna ve header
    (title) bilgisine ihityaç duyulur.

'''

filePath = YTdownloader.downloadYouTube(url)
recognition.metinlestir(filePath,YTdownloader.video_title)

