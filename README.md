# readme-py-generator
Generate readme template with python 🐍

---

## 🚀 Portfolio Generator - Dulanova

Skrip Python ini (`build_portfolio.py`) digunakan untuk menghasilkan portofolio digital milik **Dulanova** secara otomatis. Skrip akan membuat folder kerja baru, menghasilkan aset portofolio, dan mengemasnya langsung ke dalam sebuah berkas `.zip`.

---

## 📂 Komponen yang Dihasilkan
Setelah dijalankan, skrip ini akan membuat folder `Dulanova_Portfolio` yang berisi:
1. 📄 **`README.md`**: Profil utama GitHub dengan tampilan visual menarik, grafik statistik, dan animasi kontribusi.
2. 🌐 **`index.html`**: Halaman portofolio mini interaktif berbasis web dengan tema futuristik (*cyberpunk/cyber-blue*).
3. 🖼️ **`preview.gif`**: Berkas gambar *placeholder*.
4. 🗜️ **`Dulanova_Portfolio.zip`**: Paket arsip instan dari semua komponen di atas.

---

## 🛠️ Prasyarat Sebelum Menjalankan

Sebelum menjalankan skrip, pastikan perangkat kamu sudah memiliki:
* **Python 3.x** terpasang di sistem. Kamu bisa mengunduhnya di [python.org](https://www.python.org/).

> 📝 **Catatan:** Skrip ini hanya menggunakan pustaka bawaan Python (`os` dan `zipfile`), jadi kamu **tidak perlu** menginstal pustaka tambahan menggunakan `pip`.

---

## ⚡ Cara Menjalankan Skrip

Ikuti langkah-langkah mudah berikut:

### 1. Buka Terminal atau Command Prompt
Buka terminal (Linux/macOS) atau Command Prompt/PowerShell (Windows) di direktori tempat kamu menyimpan berkas `build_portfolio.py`.

### 2. Jalankan Perintah Python
Ketik perintah berikut lalu tekan **Enter**:

```bash
python build_portfolio.py

```

*Jika di sistem kamu perintah `python` merujuk ke Python lama, gunakan:*

```bash
python3 build_portfolio.py

```

### 3. Selesai! 🎉

Jika berhasil, terminal akan menampilkan pesan sukses:

```text
✅ ZIP file 'Dulanova_Portfolio.zip' berhasil dibuat!

```

---

## 🔍 Cara Melihat Hasil Portofolio

* **Melihat Halaman Web:** Buka folder `Dulanova_Portfolio`, lalu klik dua kali berkas `index.html` untuk membukanya di browser favoritmu (Chrome, Edge, Firefox, dll).
* **Melihat Profil GitHub (`README.md`):** Kamu bisa menyalin isi berkas `README.md` yang ada di dalam folder tersebut langsung ke repositori profil GitHub pribadimu untuk mempercantik halaman depan profilmu!
