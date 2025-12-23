Yapılacaklar Listesi Uygulaması---Flask

Bu proje, Flask kullanılarak geliştirilmiş basit ama modern bir Yapılacaklar Listesi (To-Do App) uygulamasıdır.
Kullanıcılar görev ekleyebilir, tamamlanma durumunu değiştirebilir ve görev silebilir. Görevler ayrıca istenirse tarih ile birlikte kaydedilir.

Özellikler:
1-Yeni görev ekleme
2-Görev silme
3-Görevi tamamlandı / geri al yapma
4-Son tarih ekleme
5-Geçmiş tarihe izin vermeme kontrolü
6-Flash mesajlarla bildirim
7-Bootstrap ile modern ve responsive tasarım
8-Temiz HTML + CSS yapısı

Proje Dizini:
proje/
│ app.py
│
├── static/
│      style.css
│
└── templates/
       index.html

Kullanılan Teknolojiler:
-Python 3
-Flask
-HTML / Jinja2
-CSS
-Bootstrap 5

Kurulum ve Çalıştırma:

Flask'ı yükle: pip install flask
Projeyi çalışır: python app.py
Tarayıcıdan aç: http://127.0.0.1:5000

Nasıl Çalışırlar?
app.py:
/ rotasında görev ekleme yapılır.
Görev adı boşsa uyarı verilir.
Girilen tarih geçmiş bir tarih olamaz.
Görevler Python listesinde saklanır.
/toggle/<id> → görevin tamamlanma durumunu değiştirir.
/sil/<id> → görevi listeden siler.

index.html:
Bootstrap ile modern arayüz oluşturur.
Flash mesajlar gösterilir.
Görevler liste olarak ekranda görüntülenir.
Tamamlanan görevlerin üstü çizilir.

style.css:
Görev kartlarında hover animasyonu
Sade ve modern UI
Input ve buton tasarımları
Gölgelendirme ve yuvarlak köşeler