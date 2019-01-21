from pynput import mouse


def on_click(x, y, button, pressed):
    if pressed:
        print("[", x, ",", y, end='')
    else:
        print(",", x, ",", y, "],")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
