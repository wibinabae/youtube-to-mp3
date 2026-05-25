import os
import threading
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from tkinter import ttk
from yt_dlp import YoutubeDL

DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%').strip().replace('%', '')
        try:
            p = float(percent)
            progress_bar['value'] = p
            root.update_idletasks()
        except:
            pass

    elif d['status'] == 'finished':
        progress_bar['value'] = 100
        root.update_idletasks()


def start_download():
    url = url_var.get()

    if not url:
        messagebox.showerror("Error", "URL masih kosong!")
        return

    def run():
        try:
            options = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_hook],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with YoutubeDL(options) as ydl:
                ydl.download([url])

            messagebox.showinfo("Sukses", "Download selesai!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # biar GUI ga freeze
    threading.Thread(target=run).start()


# GUI
root = Tk()
root.title("YouTube to MP3 Downloader")
root.geometry("500x250")

Label(root, text="Masukkan URL YouTube:").pack(pady=10)

url_var = StringVar()
Entry(root, textvariable=url_var, width=60).pack()

Button(root, text="Download MP3", command=start_download, bg="green", fg="white").pack(pady=10)

progress_bar = ttk.Progressbar(root, length=400, mode='determinate')
progress_bar.pack(pady=20)

root.mainloop()
