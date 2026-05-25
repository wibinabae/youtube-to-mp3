# YouTube to MP3 Downloader (Python GUI)

Convert video dari youtube menjadi mp3.
---

## Fitur

- Mengunduh audio dari URL YouTube
- Mengonversi video menjadi MP3 secara otomatis
- Menampilkan progress bar saat download
- Menyimpan file hasil ke folder `downloads`
- GUI sederhana

---

## Teknologi yang digunakan

- Python
- tkinter (library GUI bawaan Python)
- yt-dlp (tool downloader YouTube)
- FFmpeg (tool konversi audio/video)

---

# PANDUAN INSTALASI (STEP BY STEP)

## 1. Install Python

Download Python di:
https://www.python.org/downloads/

Saat instalasi, pastikan mencentang:
Add Python to PATH

Cek instalasi dengan perintah:

```bash
python --version
```

Cek Tkinter
```bash
python -m tkinter
```

## Install yt-dlp
pip install yt-dlp

Cek yt-dlp
```bash
yt-dlp --version
```

## Instal ffmpeg
https://www.gyan.dev/ffmpeg/builds/

## Extract file

Contoh lokasi:

C:\ffmpeg\

Pastikan di dalamnya ada:

C:\ffmpeg\bin\ffmpeg.exe
C:\ffmpeg\bin\ffprobe.exe

Menambahkan FFmpeg ke PATH (Windows)
Tekan Windows + S
Cari Environment Variables
Klik Edit the system environment variables
Klik Environment Variables
Pada System variables, cari Path
Klik Edit
Klik New
Masukkan:

C:\ffmpeg\bin

Klik OK sampai semua tertutup

Cek ffmpeg
```bash
ffmpeg -version
```
