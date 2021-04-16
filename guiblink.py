from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

# Hardware
led_blue = LED(14)
led_green = LED(27)
led_red = LED(22)

# GUI Definitions
win = Tk()
win.title("LED Control Panel")
my_font = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")

# Event Functions
def led_blue_toggle():
    if led_blue.is_lit:
        led_blue.off()
        led_blue_button["text"] = "Turn Blue LED On"
    else:
        led_blue.on()
        led_blue_button["text"] = "Turn Blue LED Off"
        
def led_green_toggle():
    if led_green.is_lit:
        led_green.off()
        led_green_button["text"] = "Turn Green LED On"
    else:
        led_green.on()
        led_green_button["text"] = "Turn Green LED Off"
        
def led_red_toggle():
    if led_red.is_lit:
        led_red.off()
        led_red_button["text"] = "Turn Red LED On"
    else:
        led_red.on()
        led_red_button["text"] = "Turn Red LED Off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
# Widgets
led_blue_button = Button(win, text = 'Turn Blue LED On', font = my_font, command = led_blue_toggle, bg = 'bisque2', height = 1, width = 24)
led_blue_button.grid(row = 0, column = 1)

led_green_button = Button(win, text = 'Turn Green LED On', font = my_font, command = led_green_toggle, bg = 'bisque2', height = 1, width = 24)
led_green_button.grid(row = 1, column = 1)

led_red_button = Button(win, text = 'Turn Red LED On', font = my_font, command = led_red_toggle, bg = 'bisque2', height = 1, width = 24)
led_red_button.grid(row = 2, column = 1)

exit_button = Button(win, text = 'Exit', font = my_font, command = close, bg = 'red', height = 1, width = 6)
exit_button.grid(row = 3, column = 1)

# Will exit clean
win.protocol("WM_DELETE_WINDOW", close)

# Loop
win.mainloop() 
