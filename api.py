import requests #library yang kita gunakan untuk mengakses API/json
import pandas as pd
import json
 
# Alamat URL API
api_url = "https://data.jabarprov.go.id/api-backend/bigdata/diskanlut/od_jumlah_kapal_penangkap_ikan_di_perairan_umum"
 
try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima
        data_ = response.json()
 
        with open("data.json", "w") as json_file:
            json.dump(data_, json_file)
 
        # Baca data JSON dari file
        with open('data.json', 'r') as json_file:
            data = json_file.read()
 
        # Ubah JSON menjadi DataFrame pandas
        df = pd.read_json(data)
 
        # Simpan DataFrame ke dalam file Excel
        excel_file = 'data.xlsx'
        df.to_excel(excel_file, index=False)
 
        print(f"Data telah disimpan dalam file Excel: {excel_file}")
 
        # Menampilkan hasil
        for user in data_:
            print(f"Nama: {user['name']}")
            print(f"Email: {user['email']}")
            print("-" * 30)
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
