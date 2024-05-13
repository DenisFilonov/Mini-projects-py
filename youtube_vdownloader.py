from pytube import YouTube
import tkinter as tk
from tkinter import filedialog as fd


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        streams.get_highest_resolution().download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = fd.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter YouTube url: ")
    # url = r"https://www.youtube.com/watch?v=2AEqzsr8Pes"
    save_dir = open_file_dialog()

    if save_dir:
        print("Downloading video...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
