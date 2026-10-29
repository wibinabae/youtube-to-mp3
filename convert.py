import os
import threading
import tkinter as tk
from tkinter import messagebox, ttk
from yt_dlp import YoutubeDL

DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "0%").strip()
        speed = d.get("_speed_str", "N/A").strip()
        eta = d.get("_eta_str", "N/A").strip()

        downloaded = d.get("downloaded_bytes", 0)
        total = d.get("total_bytes") or d.get("total_bytes_estimate")

        downloaded_mb = downloaded / (1024 * 1024)
        total_text = (
            f"{total / (1024 * 1024):.2f} MB"
            if total else "Menghitung..."
        )

        try:
            value = float(percent.replace("%", "").strip())
        except ValueError:
            value = 0

        detail = (
            f"{percent} | {downloaded_mb:.2f} MB / {total_text}\n"
            f"Kecepatan: {speed} | Sisa waktu: {eta}"
        )

        root.after(0, lambda v=value: progress_bar.configure(value=v))
        root.after(0, lambda t=detail: detail_var.set(t))

    elif d["status"] == "finished":
        root.after(0, lambda: progress_bar.configure(value=100))
        root.after(0, lambda: detail_var.set(
            "Download selesai, sedang memproses file..."
        ))


def start_download():
    url = url_var.get().strip()
    mode = format_var.get()

    if not url:
        messagebox.showerror("Error", "Masukkan link YouTube dulu!")
        return

    download_button.config(state="disabled")
    progress_bar["value"] = 0
    status_var.set("Memulai download...")
    detail_var.set("Menghubungkan ke YouTube...")

    def run():
        try:
            options = {
                "noplaylist": True,
                "outtmpl": os.path.join(
                    DOWNLOAD_FOLDER, "%(title)s.%(ext)s"
                ),
                "progress_hooks": [progress_hook],
            }

            if mode == "MP3":
                options.update({
                    "format": "bestaudio/best",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                })
            else:
                options.update({
                    "format": (
                        "bestvideo[ext=mp4]+bestaudio[ext=m4a]"
                        "/best[ext=mp4]/best"
                    ),
                    "merge_output_format": "mp4",
                })

            with YoutubeDL(options) as ydl:
                ydl.download([url])

            root.after(0, download_success)

        except Exception as e:
            error = str(e)
            root.after(0, lambda: download_error(error))

    threading.Thread(target=run, daemon=True).start()


def download_success():
    progress_bar["value"] = 100
    status_var.set("Anjaaaaaay berhasil!")
    detail_var.set("File sudah tersimpan di folder downloads.")

    download_button.config(state="normal")
    url_var.set("")
    url_entry.focus_set()

    messagebox.showinfo(
        "Sukses",
        f"Download selesai!\n\nLokasi:\n{DOWNLOAD_FOLDER}"
    )


def download_error(error):
    status_var.set("Aduuuh Download gagal.")
    detail_var.set("Link nya salah keknya.....")
    download_button.config(state="normal")
    messagebox.showerror("Error", error)


# GUI
root = tk.Tk()
root.title("Syarif Tampan Xixixixixi")
root.geometry("550x370")
root.resizable(False, False)

tk.Label(
    root,
    text="YouTube Downloader",
    font=("Arial", 16, "bold")
).pack(pady=(15, 10))

tk.Label(root, text="Masukin Link Youtube:").pack()

url_var = tk.StringVar()
url_entry = tk.Entry(root, textvariable=url_var, width=68)
url_entry.pack(pady=8)

tk.Label(root, text="Pilih format download:").pack(pady=(5, 2))

format_var = tk.StringVar(value="MP4")

format_frame = tk.Frame(root)
format_frame.pack()

tk.Radiobutton(
    format_frame, text="MP4 (Video)",
    variable=format_var, value="MP4"
).pack(side="left", padx=10)

tk.Radiobutton(
    format_frame, text="MP3 (Audio)",
    variable=format_var, value="MP3"
).pack(side="left", padx=10)

download_button = tk.Button(
    root,
    text="Download",
    command=start_download,
    bg="#16a34a",
    fg="white",
    font=("Arial", 10, "bold"),
    width=22
)
download_button.pack(pady=12)

progress_bar = ttk.Progressbar(
    root, length=460, mode="determinate", maximum=100
)
progress_bar.pack(pady=5)

status_var = tk.StringVar(value="Siap download.")
tk.Label(root, textvariable=status_var, font=("Arial", 10, "bold")).pack(
    pady=5
)

detail_var = tk.StringVar(value="Tunggu eaaaaaa.")
tk.Label(
    root, textvariable=detail_var,
    justify="center", wraplength=510
).pack(pady=3)

tk.Label(
    root, text="Folder penyimpanan: downloads", fg="gray"
).pack(pady=5)

root.mainloop()
