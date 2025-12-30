# Canlı Kamera ROI ve Grayscale Filtre Projesi

Bu proje, Python ve OpenCV kullanarak bilgisayar kamerasından canlı görüntü alır, görüntünün boyutlarını otomatik algılar ve merkezin 200x200 piksel çevresindeki alanı  **siyah-beyaz (grayscale)** filtre ile işler.

##  Özellikler

* **Otomatik Çözünürlük Tespiti:** Kamera boyutu (480p, 720p, 1080p) ne olursa olsun kod bozulmaz.
* **ROI (Region of Interest):** Görüntünün merkezinden 200x200 piksellik alan kesilir (Cropping).
* **Real-time Processing:** Kesilen alan anlık olarak gri tona çevrilip orijinal yerine geri yapıştırılır. Birden fazla kamera sekmesi açılmaz.
* **Görselleştirme:** İşlem yapılan alan kırmızı bir çerçeve ile belirtilir.
* **Uyarı:** Görüntü gelmemesi halinde selected_camera değerini değiştirmeyi deneyiniz.