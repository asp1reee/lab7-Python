import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO


def fetch_nasa_apod(api_key):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()


def display_apod(apod_data):
    if apod_data and apod_data['media_type'] == 'image':
        root = tk.Tk()
        root.title(apod_data['title'])

        response = requests.get(apod_data['url'])
        image = Image.open(BytesIO(response.content))
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()

        title_label = tk.Label(
            root, text=apod_data['title'], font=("Arial", 14, "bold")
        )
        title_label.pack()

        desc_label = tk.Label(
            root, text=apod_data['explanation'],
            wraplength=600, justify="left"
        )
        desc_label.pack()

        root.mainloop()
    else:
        print("Нет данных для отображения.")


if __name__ == "__main__":
    api_key = "93HSAIE4PTZ3cg5jhkKm20Nm06c10JN9qblzr2y6"
    apod_data = fetch_nasa_apod(api_key)
    display_apod(apod_data)


