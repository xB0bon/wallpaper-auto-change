import ctypes
import time

rano = r"C:\Users\Piotrek\OneDrive - Zespół Szkół Technicznych im. Tadeusza Kościuszki w Radomiu\Komputer domowy\Desktop\Wallpaper changer\walllpaper changer\rano.png"
dzien = r"C:\Users\Piotrek\OneDrive - Zespół Szkół Technicznych im. Tadeusza Kościuszki w Radomiu\Komputer domowy\Desktop\Wallpaper changer\walllpaper changer\dzien.png"
bardzowczesnanoc = r"C:\Users\Piotrek\OneDrive - Zespół Szkół Technicznych im. Tadeusza Kościuszki w Radomiu\Komputer domowy\Desktop\Wallpaper changer\walllpaper changer\bardzowczesnanoc.jpg"
wczesnanoc = r"C:\Users\Piotrek\OneDrive - Zespół Szkół Technicznych im. Tadeusza Kościuszki w Radomiu\Komputer domowy\Desktop\Wallpaper changer\walllpaper changer\wczesnanoc.jpg"
noc = r"C:\Users\Piotrek\OneDrive - Zespół Szkół Technicznych im. Tadeusza Kościuszki w Radomiu\Komputer domowy\Desktop\Wallpaper changer\walllpaper changer\noc.png"


def czas():
    global rano, dzien, bardzowczesnanoc, wczesnanoc, noc
    string_czasu = time.strftime("%H")
    string_czasu = int(string_czasu)
    try:
        if 5 <= string_czasu <= 8:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, rano, 3)
        elif 9 <= string_czasu <= 17:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, dzien, 3)
        elif 18 <= string_czasu <= 19:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, bardzowczesnanoc, 3)
        elif 20 <= string_czasu <= 22:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, wczesnanoc, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, noc, 3)
        time.sleep(60)
    except Exception as e:
        print(e)


while True:
    czas()
