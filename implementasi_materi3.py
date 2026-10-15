import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import time

print("==================================================================")
print(" STUDI KASUS BIG DATA SPASIAL: ANALISIS & KLUSTER ASET 100K TITIK")
print(" Nama File : implementasi_materi3.py")
print(" Berdasarkan Materi: Widi Primadepa (Asset Management GIS Analyst)")
print(" Topik: Career & Competition in Industrial Era with GIS")
print("==================================================================\n")

# ==================================================================
# 1. GENERATE DATASET SPASIAL SKALA MASIF (100.000 Titik Aset)
# ==================================================================
np.random.seed(42)
n_assets = 100000  # Skala data ditingkatkan drastis menjadi 100.000 titik aset

print("--- [Langkah 1] Memuat & Mensimulasikan 100.000 Data Spasial Aset Kota ---")
asset_categories = [
    'Taman Kota', 'Tiang Lampu Jalan', 'Pohon Perlindungan', 
    'Hidran Air', 'Halte Bus', 'Jembatan Penyeberangan', 'Drainase Utama'
]

start_gen = time.time()
df_city_assets = pd.DataFrame({
    'asset_id': [f"CC-MEGAST-{str(i).zfill(7)}" for i in range(1, n_assets + 1)],
    'category': np.random.choice(asset_categories, n_assets, p=[0.10, 0.30, 0.20, 0.10, 0.10, 0.05, 0.15]),
    'coord_longitude': np.random.uniform(101.9000, 102.6000, n_assets), # Cakupan wilayah metropolitan luas
    'coord_latitude': np.random.uniform(-4.1000, -3.5000, n_assets),   
    'installation_year': np.random.randint(2000, 2026, n_assets),
    'last_audit_score': np.random.uniform(25.0, 100.0, n_assets),      # Skor kesehatan fisik (0-100)
    'maintenance_cost_usd': np.random.uniform(80.0, 7500.0, n_assets)  # Biaya perawatan historis
})
end_gen = time.time()

print(f"Berhasil men-generate {len(df_city_assets):,} titik geospasial dalam {end_gen - start_gen:.4f} detik.")
print(df_city_assets.head(3), "\n")

# ==================================================================
# 2. SPATIAL METRICS & RISK SCORING MODEL (Analisis Risiko Lanjutan)
# ==================================================================
print("--- [Langkah 2] Analisis Penilaian Risiko Spasial Skala Masif ---")

current_year = 2026
df_city_assets['asset_age_years'] = current_year - df_city_assets['installation_year']

# Kriteria Risiko: Usia > 15 tahun DAN Skor Audit < 55.0
df_city_assets['risk_status'] = np.where(
    (df_city_assets['asset_age_years'] > 15) & (df_city_assets['last_audit_score'] < 55.0),
    'High Risk (Perlu Peremajaan)',
    'Stable (Aman)'
)

risk_summary = df_city_assets['risk_status'].value_counts()
print("Distribusi Status Risiko 100.000 Aset Kota:")
print(risk_summary, "\n")

# ==================================================================
# 3. MACHINE LEARNING SPATIAL CLUSTERING (Spatial K-Means untuk 8 Zona)
# ==================================================================
print("--- [Langkah 3] Machine Learning: K-Means Kluster untuk 8 Zona Pos Operasional ---")

spatial_features = df_city_assets[['coord_longitude', 'coord_latitude']]

start_ml = time.time()
# Membagi 100.000 titik ke dalam 8 kluster wilayah operasional pemeliharaan metropolitan
kmeans = KMeans(n_clusters=8, random_state=42, n_init=10)
df_city_assets['operational_cluster'] = kmeans.fit_predict(spatial_features)
end_ml = time.time()

print(f"Proses kluster K-Means untuk 100k data selesai dalam {end_ml - start_ml:.4f} detik.")
cluster_centers = kmeans.cluster_centers_
print("Koordinat Titik Pusat Pos Pemeliharaan Baru (Cluster Centroids):")
for idx, center in enumerate(cluster_centers):
    print(f"  - Pos Wilayah Zona {idx + 1} -> Longitude: {center[0]:.4f}, Latitude: {center[1]:.4f}")
print()

# ==================================================================
# 4. DATA AGGREGATION & EXECUTIVE REPORTING (Standar FME Engine)
# ==================================================================
print("--- [Langkah 4] Agregasi Data & Pembuatan Laporan Eksekutif Per Zona ---")

df_cluster_report = df_city_assets.groupby('operational_cluster').agg(
    total_aset=('asset_id', 'count'),
    rata_rata_kesehatan=('last_audit_score', lambda x: round(x.mean(), 2)),
    total_biaya_perawatan=('maintenance_cost_usd', lambda x: round(x.sum(), 2)),
    aset_berisiko_tinggi=('risk_status', lambda x: (x == 'High Risk (Perlu Peremajaan)').sum())
).reset_index()

print("Laporan Ringkasan Performa 8 Kluster Wilayah Metropolitan:")
print(df_cluster_report.to_string(index=False), "\n")

# ==================================================================
# 5. EKSPOR DATASET MASIF KE FORMAT CSV
# ==================================================================
output_file = "laporan_analisis_implementasi_materi3_megadata.csv"
print(f"--- [Langkah 5] Mengekspor {len(df_city_assets):,} baris data ke '{output_file}' ---")
df_city_assets.to_csv(output_file, index=False)
print(f"[Sukses] File laporan megadata spasial berhasil disimpan.\n")

# ==================================================================
# 6. KESIMPULAN PERSPEKTIF INDUSTRI (Integrator Mindset)
# ==================================================================
print("==================================================")
print(" KESIMPULAN PERSPEKTIF INDUSTRI GIS & IT (MEGA DATA):")
print("==================================================")
print("1. Kapasitas Big Data: Menangani 100.000+ titik aset membuktikan")
print("   bahwa integrasi ilmu Informatika dan GIS mampu menyelesaikan")
print("   permasalahan tata kota skala megapolitan secara otomatis.")
print("2. Pengambilan Keputusan Strategis: Kluster K-Means dan penilaian risiko")
print("   membantu pemerintah kota mengoptimalkan alokasi anggaran bernilai tinggi.")
print("3. Kesiapan Profesional: Kompetensi pemrosesan data masif ini menjadi")
print("   daya tawar utama bagi sarjana IT untuk bersaing di tingkat global.")
print("==================================================")