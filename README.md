# Identitas Pembuat
* **Nama:** Anisa Julianti
* **NPM:** G1A023052
* **Program Studi:** Informatika, Universitas Bengkulu

---

# Studi Kasus: Analisis Spasial & Kluster Aset Megadata (*Big Data Spatial Analysis & K-Means Clustering*)

Proyek dan skrip implementasi ini dikembangkan berdasarkan materi **Informatics Practitioner Lecture Series** dengan narasumber **Widi Primadepa, S.Com.** (Asset Management GIS Analyst di City Care Property, Selandia Baru — alumni Informatika Universitas Bengkulu Angkatan 2008) dengan tema **"Career and Competition in Industrial Era with GIS"**.

---

## 1. Latar Belakang & Konteks Industri
* **Manajemen Aset Modern (*Smart Cities*):** Di kota-kota modern (seperti yang diterapkan di Selandia Baru), pengelolaan infrastruktur publik dan aset kota (seperti taman, halte, tiang lampu, hingga drainase) menuntut sistem integrasi data geospasial yang presisi dan transparan.
* **Peran Sarjana IT (*One Step Ahead*):** Lulusan Informatika memiliki keunggulan kompetitif di bidang GIS karena mampu membangun otomatisasi skrip (*scripting & automation*) untuk mengolah data geospasial dalam jumlah besar (*Big Data*), alih-alih bergantung sepenuhnya pada operasi manual perangkat lunak desktop.
* **Tujuan Proyek (`implementasi_materi3.py`):** Mensimulasikan pemrosesan data spasial skala masif (**100.000 titik aset kota**), melakukan penilaian risiko fisik aset (*Risk Scoring Model*), menerapkan *Machine Learning* (**Spatial K-Means Clustering**) untuk menentukan titik pos operasional baru, serta menghasilkan laporan eksekutif secara otomatis.

---

## 2. Alur Kerja Analisis Spasial (*GIS Processing Workflow*)
Skrip ini mensimulasikan alur kerja standar industri geospasial modern:
1. **Pembangkitan Data Masif (*Data Generation*):** Mensimulasikan 100.000 titik koordinat geospasial (Longitude & Latitude) di wilayah cakupan luas beserta atribut pendukungnya.
2. **Model Penilaian Risiko (*Risk Scoring*):** Menyaring aset berdasarkan usia operasional dan skor audit kesehatan fisik untuk mengidentifikasi aset berisiko tinggi yang memerlukan peremajaan.
3. **Kluster Spasial Berbasis AI (*K-Means Clustering*):** Mengelompokkan ratusan ribu titik aset ke dalam zona operasional (8 zona wilayah) guna menentukan titik pusat koordinat (*Centroids*) sebagai lokasi strategis pos pemeliharaan baru.
4. **Agregasi & Pelaporan Eksekutif:** Mengelompokkan data per zona untuk menghitung total biaya perawatan, rata-rata skor kesehatan, dan jumlah aset berisiko.
5. **Ekspor Data (*Cloud-Ready Output*):** Menyimpan hasil analisis megadata ke dalam format file `.csv` yang siap diintegrasikan ke platform *Web/Cloud GIS*.

---

## 3. Implementasi Kode (`implementasi_materi3.py`)

Skrip Python ini dibangun menggunakan pustaka analitik standar industri (*Pandas, NumPy, Scikit-Learn*):

```python
# 1. Pembangkitan 100.000 Data Spasial Aset Kota (Big Data Simulation)
# 2. Implementasi Model Penilaian Risiko Berdasarkan Usia & Skor Audit
# 3. Penerapan Machine Learning K-Means Clustering untuk 8 Zona Operasional
# 4. Agregasi Data Laporan Eksekutif & Ekspor ke File Megadata CSV
