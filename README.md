# Drone Filo Optimizasyonu

Bu proje, Kocaeli Üniversitesi Bilişim Sistemleri Mühendisliği öğrencileri için Yazılım Geliştirme Laboratuvarı II dersi kapsamında geliştirilmiştir. Amaç, birden fazla drone'un uçuş yasağı bölgeleri ve enerji limitleri gibi kısıtlar altında en uygun teslimat rotasını bulmasını sağlamaktır.

## 🚀 Projenin Amacı

Drone'lar:

- Maksimum taşıma kapasitesi, batarya limiti ve hız gibi özelliklere sahiptir.
- Teslimat noktaları: koordinat, ağırlık, öncelik, zaman aralığı içerir.
- Uçuşa yasak bölgeler: poligon şeklinde belirtilmiş, zaman bazlı aktiftir.

Amaç, bu şartlar altında en kısa sürede en fazla teslimatı gerçekleştirmektir.

---

## 🧠 Kullanılan Algoritmalar

### ✅ A\* Algoritması

- Drone'un tek bir teslimat noktasına en kısa ve en güvenli rotayı bulması için kullanılır.

### ✅ Genetik Algoritma (GA)

- Drone'ların birden fazla teslimat noktasına en verimli rotayla ulaşmasını sağlar.
- Başlangıç popülasyonu → çaprazlama → mutasyon → en iyi rota seçimi

### ✅ CSP (Constraint Satisfaction Problem)

- Zaman, ağırlık ve uçuş yasağı gibi kısıtları kontrol eder.

---

## 📁 Klasör Yapısı

```
DroneFiloOptimizasyonu/
├── data/
│   └── veri_seti.txt
├── src/
│   ├── models.py
│   ├── utils.py
│   ├── graph.py
│   ├── astar.py
│   ├── ga.py
│   ├── csp.py
│   └── __init__.py
├── tests/
│   └── test_cases.py
├── visualization/
│   └── plot_routes.py
├── main.py
├── rapor.pdf
└── README.md
```

---

## 🖥️ Çalıştırmak İçin

### 1. Sanal ortamı oluştur:

```bash
python -m venv venv
```

### 2. Sanal ortamı aktif et:

- Windows:

```bash
venv\Scripts\activate
```

### 3. Gereksinimleri yükle:

```bash
pip install matplotlib
```

### 4. Programı çalıştır:

```bash
python main.py
```

---

## 📊 Görselleştirme

`visualization/plot_routes.py` dosyası ile her bir drone’un rotası çizilir.  
Uçuş yasağı bölgeleri kırmızı alanlarla gösterilir.

---

## 📌 Rapor

IEEE formatında hazırlanmış `rapor.pdf` dosyası proje kök dizinindedir.

---

## 👨‍💻 Geliştirenler

- Bilişim Sistemleri Mühendisliği – Kocaeli Üniversitesi
- Yazılım Geliştirme Laboratuvarı II – 2024–2025 Bahar

---
