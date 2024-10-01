# BIKESHARING DICODING

Proyek ini adalah bagian dari tugas akhir dalam kursus "Belajar Analisis Data dengan Python" di Dicoding. Di sini, saya menganalisis dataset penyewaaan sepeda dan membuat dashboard interaktif berbasis Streamlit. Tahapan yang saya lakukan meliputi pembersihan data, eksplorasi data untuk menemukan pola, serta visualisasi menggunakan grafik interaktif. Dashboard dapat diakses pada link berikut https://bikerentalset.streamlit.app/

# 1. File Struktur
```plaintext
.
├── Dashboard
│   ├── Dashboard.py
│   └── day_df_clean.csv
│   └── bikery-high-resolution-logo.png
├── data
│   ├── Readme.txt
│   ├── day.csv
│   └── hour.csv
├── screenshots
│   ├── Screenshots 1.png
│   ├── Screenshots 2.png
│   ├── Screenshots 3.png
│   ├── Screenshots 4.png
│   ├── Screenshots 5.png
│   ├── Screenshots 6.png
│   ├── Screenshots 7.png
│   └── Screenshots 8.png
├── README.md
├── notebook.ipynb
└── requirements.txt
```
# 2. Langkah-langkah mengerjakan project
## 1. Data Wrangling:
- Pengumpulan Data: Mengumpulkan data dari sumber yang tersedia, termasuk data harian dan jam.
- Penilaian Data: Memeriksa kualitas data dengan memperhatikan tipe data, nilai yang hilang, dan duplikat.
- Pembersihan Data: Menghapus atau memperbaiki nilai yang hilang, duplikat, serta kolom yang tidak relevan.

## 2. Exploratory Data Analysis (EDA) :
- Menentukan Pertanyaan Bisnis: Merumuskan pertanyaan bisnis yang ingin dijawab, seperti tren penggunaan berdasarkan hari kerja/hari libur dan tipe pengguna.
- Eksplorasi Data: Menganalisis data untuk menemukan pola, tren, atau informasi penting yang dapat membantu memahami data lebih baik.

## 3. Visualisasi Data:
- Membuat Visualisasi Data: Menampilkan grafik untuk melihat penggunaan berdasarkan hari, dampak musim terhadap penggunaan, serta perbandingan penggunaan antara pengguna kasual dan terdaftar.

## 4. Dashboard
- Mengatur DataFrame untuk Dashboard: Menyiapkan data dari DataFrame yang sudah dianalisis untuk diintegrasikan ke dalam dashboard.
- Membuat Komponen Filter: Menambahkan filter seperti bulan dan cuaca untuk memudahkan eksplorasi data.
- Melengkapi Dashboard dengan Visualisasi: Menambahkan grafik untuk menjawab pertanyaan bisnis.
- Tahapan 1 hingga 3 dilakukan dalam analisis data, sedangkan tahapan 4 dilakukan untuk membuat dashboard menggunakan Streamlit.

# 3. Langkah Menjalankan project
## notebook.ipynb
### 1. Download file projectnya
### 2. Kemudian buka google colaboratory di website/chroem
### 3. Buat notebook baru di Google Colab.
### 4. upload dan pilih file dengan format .ipynb yang telah didownload tadi
### 5. Hubungkan ke runtime yang sudah di-hosting dengan mengklik "Connect".
### 6. Jalankan kode di notebook dengan menekan tombol "Run" pada setiap cell kode.

## Dashboard/Dashboard.py
## Dashboard.py
### 1. Download file projectnya
### 2. install streamlit di terminal dengan mengetikkan "pip install streamlit"
- Buat file `requirements.txt` yang berisi library yang dibutuhkan seperti pandas, numpy, matplotlib, dan seaborn.
- Install library tersebut dengan mengetikkan `pip install -r requirements.txt` di terminal.
### 3. Pastikan file CSV (dataset) disimpan dalam folder yang sama dengan file dashboard.py atau main.py.
### 4. Buka Visual Studio Code (VSCode), aktifkan virtual environment dengan mengetikkan perintah berikut di terminal:
```
.\venv\Scripts\activate
```
- Jika sudah masuk ke virtual environment, jalankan Streamlit dengan perintah:
```
streamlit run Dashboard.py
```
# 4. Screenshots
![Screenshot 2024-10-01 031138](https://github.com/user-attachments/assets/29f4d975-1c74-4642-98e6-979a521a39ea)
![Screenshot 2024-10-01 031150](https://github.com/user-attachments/assets/bfd9a7ff-319b-422c-a1cc-2c7ded2a1a5c)
![Screenshot 2024-10-01 031202](https://github.com/user-attachments/assets/bc642d46-ff1b-4c5f-9372-b3b29ae2c6c2)
![Screenshot 2024-10-01 031214](https://github.com/user-attachments/assets/bcc27aa8-f726-412b-87a4-ba77d523e484)
![Screenshot 2024-10-01 031225](https://github.com/user-attachments/assets/c8ba9d7c-3aab-40d4-938b-fcd1ae36e205)
![Screenshot 2024-10-01 031252](https://github.com/user-attachments/assets/9d903e72-82a5-4996-850c-3e859b57dd02)
![Screenshot 2024-10-01 031308](https://github.com/user-attachments/assets/e0d72e23-ae23-4f52-a2d7-802e588c39b5)
![Screenshot 2024-10-01 031323](https://github.com/user-attachments/assets/14991e02-f0f1-44d8-ab71-53efb5015f58)








