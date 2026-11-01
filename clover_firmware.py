import board
import digitalio
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
import terminalio
import adafruit_displayio_ssd1306
import displayio
from adafruit_display_text import label
import random

# sets up display
displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d)
WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

group = displayio.Group()
text_area = label.Label(terminalio.FONT, text = "", x=10, y=25)
group.append(text_area)
display.root_group = group

# sets up the NeoPixels
onboard_pixel = neopixel.NeoPixel(board.D6, 20, brightness=0.3, auto_write=True)

# sets up the switches
button1 = DigitalInOut(board.D0)
button1.direction = Direction.INPUT
button1.pull = Pull.UP

button2 = DigitalInOut(board.D1)
button2.direction = Direction.INPUT
button2.pull = Pull.UP

button3 = DigitalInOut(board.D2)
button3.direction = Direction.INPUT
button3.pull = Pull.UP

button4 = DigitalInOut(board.D7)
button4.direction = Direction.INPUT
button4.pull = Pull.UP

# colours
RED = (219, 95, 81)
LIGHT_RED = (247, 155, 145)
BLUE = (105, 162, 214)
LIGHT_BLUE = (166, 210, 252)
GREEN = (106, 214, 114)
LIGHT_GREEN = (158, 242, 163)
YELLOW = (242, 208, 121)
LIGHT_YELLOW = (250, 224, 175)
OFF = (0, 0, 0)

game_start = False
while game_start == False:
    if not button1.value or not button2.value or not button3.value or not button4.value:
        game_start = True
        time.sleep(0.2)
button_colour = ["red", "blue", "green", "yellow"]
colours = {
    "red": RED,
    "blue": BLUE,
    "green": GREEN,
    "yellow": YELLOW
}

light_colours = {
    "red": LIGHT_RED,
    "blue": LIGHT_BLUE,
    "green": LIGHT_GREEN,
    "yellow": LIGHT_YELLOW
}

# loop
while game_start:
    target_colour = random.choice(["red", "blue", "green", "yellow"])
    random.shuffle(button_colour)
    start_time = time.monotonic()
    iteration = True
    onboard_pixel[16] = colours[button_colour[0]]
    onboard_pixel[17] = colours[button_colour[1]]
    onboard_pixel[18] = colours[button_colour[2]]
    onboard_pixel[19] = colours[button_colour[3]]
    while iteration:
        text_area.text = (f"Quick, press {target_colour}!")
        selected_colour = ""
        if not button1.value:
            for i in range(4):
                onboard_pixel[i] = light_colours[button_colour[0]]
            selected_colour = button_colour[0]
        elif not button2.value:
            for i in range(4, 8):
                onboard_pixel[i] = light_colours[button_colour[1]]
            selected_colour = button_colour[1]
        elif not button3.value:
            for i in range(8, 12):
                onboard_pixel[i] = light_colours[button_colour[2]]
            selected_colour = button_colour[2]
                
        elif not button4.value:
            for i in range(12, 16):
                onboard_pixel[i] = light_colours[button_colour[3]]
            selected_colour = button_colour[3]
        else:
            for i in range(4):
                onboard_pixel[i] = colours[button_colour[0]]
            for i in range(4, 8):
                onboard_pixel[i] = colours[button_colour[1]]
            for i in range(8, 12):
                onboard_pixel[i] = colours[button_colour[2]]
            for i in range(12, 16):
                onboard_pixel[i] = colours[button_colour[3]]

        if selected_colour != "":
            reaction_time = time.monotonic() - start_time
            if selected_colour == target_colour:
                text_area.text = f"Time: {reaction_time}\n"
                if reaction_time > 0.600:
                    text_area.text = "If you didn't know, you're supposed to be quick!"
                elif 0.400 < reaction_time <= 0.600:
                    text_area.text = "Try a little faster?"
                elif 0.300 < reaction_time <= 0.400:
                    text_area.text = "A little slower than average."
                elif 0.273 < reaction_time <= 0.300:
                    text_area.text = "Perfectly average!"
                elif 0.250 < reaction_time <= 0.273:
                    text_area.text = "A little faster than average."
                elif 0.200 < reaction_time <= 0.250:
                    text_area.text = "Nice and quick!"
                elif 0.180 < reaction_time <= 0.200:
                    text_area.text = "Faster than a cheetah!"
                elif 0.150 < reaction_time <= 0.180:
                    text_area.text = "Are you trained for this?"
                elif reaction_time <= 0.150:
                    text_area.text = "Are you sure you aren't cheating?"
                time.sleep(1)
            else:
                game_start = False
                text_area.text = "Wrong colour!"
                time.sleep(1)
            iteration = False

    time.sleep(0.02)
