# Clovermatch
A PCB designed to play a game in order to test your reaction time and hand-eye coordination using colours!

You know that one reaction time game that gives you an amount of seconds when you "click when the screen turns green"? Or the Simon Says game where it gives you a specific pattern and you have to memorize it? Well I thought I would combine them into one game, where it'll test you on both your reaction time and hand-eye coordination! It's meant to be as easy as possible to play, not only for me to make but also for people that just want something with their friends to be competitive about. It's not just a game for yourself, more of something you can talk about with your friends and spend time trying to get better! Though it's relatively simple, it's also my first ever almost entirely custom PCB, so I'm super proud of it! :)

In the game, Clovermatch chooses a colour. Then, the player must press the button corresponding to that colour, and then Clovermatch will display the reaction time if the player was correct. If the player was wrong, the game will restart. Additionally, the LEDs and buttons change each round, so the right button is not always red every round, for example. In this way, the LEDs actually have some function in the game! <br>

<img width="477" height="402" alt="clovercover" src="https://github.com/user-attachments/assets/2d028494-aa9c-4486-b2e2-4b917be273ed" />

## Summary
### Files
The PCB was designed using **KiCad** and the code was made with **CircuitPython** in **VS Code**. Please see the files below for what you need to import/download:
|File|What's inside?|
|---|---|
|clovermatch.kicad_pcb|contains the PCB layout, including the footprints, footprints, and edge cuts|
|clovermatch.kicad_pro|contains the project settings and configuration|
|clovermatch.kicad_sch|contains the schematic and connections|
|clovermatch_gerbers.zip|contains several gerber files|
|code.py|contains the firmware used to run the microcontroller|
|BOM.csv|Bill of Materials [Half Life]|

### External Libraries
There was also the use of several external libraries, which can be seen here:
|File/Folder|What does it do?|Link|
|---|---|---|
|adafruit_displayio_ssd1306.mpy|contains info for CircuitPython on how to initialize the OLED and draw pixels|https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases (Extract from the lib folder in the bundle)|
|adafruit_display_text|allows the OLED to display texts and fonts|https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases (Extract from the lib folder in the bundle)|
|neopixel.mpy|contains colour data formatting, array management, voltage, etc. for the NeoPixels|https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases (Extract from the lib folder in the bundle)|
|Hackclub Footprints.pretty|contains footprints, specifically for the Kailh Low Choc Switches|https://github.com/KaiPereira/Hackclub-KiCad-Libraries|
|Seeed Studio Xiao Series|contains footprints, specifically for the XIAO ESP32-C3|https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/|

### Extra Resources
Here is also a list of useful links that I used (mostly just for the firmware, all in CircuitPython):
|Use|Link|
|---|---|
|bassics of the SSD1306 OLED screen|https://www.youtube.com/watch?v=nHECoycpmEY|
|displays on the OLED Screen|https://www.youtube.com/watch?v=-lrJ0fy0xm0|
|basics of NeoPixels|https://www.youtube.com/watch?v=qRyp4pKvi3g&t=300s|
|timer and use of time|https://www.youtube.com/watch?v=ZIKjZEkB48w|
|time.monotonic() and related functions|https://docs.circuitpython.org/en/latest/shared-bindings/time/|
|basics of push buttons|https://www.youtube.com/watch?v=UGaDaY-JTYU|
|how to use dictionaries|https://www.w3schools.com/python/python_dictionaries.asp|

## Schematic
The schematic is located in the clovermatch.kicad_sch file, and you'll see some points of interest. This was also mostly made by me based on information from the guide! The custom items I added are the 4 pin connector for the OLED, the switches, and back key lighting.
* [U1] XIAO Seeed Studio ESP32-C3 (microcontroller)
* [U2] 74AHCT1G125 (level shifter)
* [SW1, SW2, SW3, SW4] SW_Push (tactile push switches)
* [J2] Conn_o1x04_Pin (connecting pins for the OLED)
* [D1-D16] WS2812B (5mm * 5mm NeoPixels)
* [D17, D18, D19, D20] SK6812MINI-E (Back Key RGB LEDs)
* [C1-C21] 100nF Capacitor
* [C22] 22µF Bulk Capacitor

<img width="536" height="355" alt="image" src="https://github.com/user-attachments/assets/30dac385-13bc-447c-945c-b06d3e903487" />
<br><br>
Use these pins as reference for the firmware!
<br><br>

|Pin|Part|
|---|---|
|D0|Switch 1|
|D1|Switch 2|
|D2|Switch 3|
|D4|OLED I2C SCL|
|D5|OLED I2C SDA|
|D6|LED Data Line|
|D7|Switch 4|

I also added in the footprints according to the guide, and I used the same footprints I did for my MIDI for the OLED and switches. I'm also using 5mm * 5mm NeoPixels since they'll probably be easier to solder. <br><br>
<img width="512" height="424" alt="image" src="https://github.com/user-attachments/assets/10720042-4a7e-4a56-b09a-9709918f3e6e" />

## Routing & Customization
After looking at the schematic you can take a look at the routing and customization in the PCB editor (clovermatch.kicad_pcb). I'm a beginner to PCB making so the routing is definitely messy and non-symmetrical, but I tried my best to make it work. I also added the GND pour on the back since you can then just use vias to route close to GND traces in the front, so you don't need a GND pour on both sides (the back is cleaner, so it makes more sense to have it on the back). The graphics/text were added using KiCad's built in image converter to change it to a bitmap, and then added to a custom library before being added onto F.Silkscreen as a footprint. Also, make sure to notice the image resizer that is also built into image converter!! I had lots of trouble with trying to resize my footprints since there's no way to do so in KiCad's footprint editor, so you have to use an external website (such as https://kicad-footprint-resizer.streamlit.app/). However, because this footprint's only going to be used as a graphic, you can just resize it in the image converter! Another thing to note is that it's a lot more of a hassle to make an image as a footprint than it is to make text. So I'd recommend planning out what you want on your PCB instead of just trying different things and seeing what works, since that takes a lot more time than necessary. Take advantage of the fact that you can manipulate text to appear as a graphic; for example, I used + signs stretched out to use as sparkles!
<br><br>
<img width="441" height="422" alt="image" src="https://github.com/user-attachments/assets/0faa8e78-3e4e-4b9c-a4a2-485dfa912df6" />

## Firmware
For the firmware, I coded it in VS Code using Python (though I'll test it as CircuitPython once I get the actual PCB). You can just open up the code.py in VS Code (or any other applicable software). For this, I mostly used the extra resources I outlined in the beginning, and asked a few of my real-life friends that know Python better than I do for some help with the logic errors and cleaning up the code. It may have some extra logic errors that I'll fix when I can test out the board, but here's an explanation of each part of the only 147-line piece of code.

### Libraries
```python
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
```
This section imports the specific libraries that I'll be using in the code! A great thing about CircuitPython is that you don't have to code it all from scratch, you can just assemble different parts from libraries. So, for example, it would be very difficult to try and code a NeoPixel, but, with the neopixel library, you can just use pixels[i] (pixels/your applicable onboarding)! It's super easy for beginners and I already know a little bit of Python, so I'd recommend it even for people that know nothing about code.

### Setup
```python
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
```
This setup contains everything I need to run the OLED, display text on the OLED, onboard the Neopixels, set up the switches, and set some constants for the colours. To set up the OLED, you just need to set an address to it (and make sure to clear the entire OLED before starting). The text is a little more difficult, since you have to make a group and a label inside that group that will allow you display text; I'd recommend the "displays on the OLED screen" video I put in the summary. The NeoPixels are set up with just one line of code, which is to set its pin, how many there are, brightness, and auto_write. Since I connected all my NeoPixels to each other, I don't have to worry about needing multiple onboardings. The switches are also pretty simple, the only thing you really need to add is what pin they are. The direction just states that it's an input and the pull just states that you need to pull up to not use it (i.e., you need to press down to use it). Finally, I set some constants to RGB values, as NeoPixels only read RGB values and this just makes it so I don't have to write out the whole thing each time.

### Game Loop Setup
```python
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
```
This area of the code is for the actual game loop. In the first section, it waits until one of the buttons is pressed to start the game. Since the button only detects when it is pulled up, you need to use a not in front of its value to detect when it is pushed down. When any of the four are pressed, the game_start is set to True. After that, I made some dictionaries to correspond strings with RGB values. When I first made my code, I made each button store a string when pressed, and I don't know why I didn't just make it store the RGB value but I never fixed this so I just decided to make a dictionary instead. It would probably be faster for me to just replace each string, but this helps me practice a bit more, I guess? 

Once the game starts, a random target colour is selected. Then, it'll randomly shuffle the button colour set, before making each back key LED (16-19) light up to the button colour it corresponds to. It also starts the reaction timer using time.monotonic() (see the extra resources in the summary!)

### Iterations
```python
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
```
Clovermatch is meant to run on rounds, not just one game. This is so you don't have to restart each game just to continue playing, since each round only takes ~2 seconds. To do this, I added another while loop inside of the original game loop for each iteration. It starts by making the OLED display "Quick, press {target_colour}!". Then based on which button you press (and its corresponding button colour), it'll store that value inside of selected_colour. I also wanted to make the LEDs change in some way and not just stay static throughout the entire round, so I made it change to a lighter version of that colour when you press the button. It'll make it not only aesthetically pleasing but also allow you to see what colour you chose in case you forget and rage quit if you think the game is wrong. 

### Reaction Time Check
```python
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
```
The final part of the code is to tell you what your reaction time was and then restart the round or game. The reaction time is simply calculated using the difference between the current time and the start time, which gives the time elapsed. It detects once you have chosen a colour by detecting whether or not your selected colour is empty. If you get the colour correct, it'll display your reaction time and a cute little message based on how fast you were! Those times are solely based on average reaction times, however, so I'll probably need to change the values and do some of my own testing to account for having to think about which colour to press and your hand-eye coordination. If you get the colour wrong, it'll just display "Wrong colour!" before restarting the game. 

## Bill of Materials
Please note that this BOM is for general users! For Half Life, please view the BOM submitted on the Half Life website. Also note that these prices are given without any special discounts, but AliExpress often gives discounts anyways, so prices are probably cheaper than shown. Shipping is based off my own address and the tax is calculated with the Ontario rate of 13%.

|Part|Price (USD)|Quantity|Vendor|Link|
|---|---|---|---|---|
|XIAO Seeed Studio ESP32-C3|$4.47|1|AliExpress|https://www.aliexpress.com/item/1005008791937363.html?spm=a2g0o.cart.0.0.284238daZvshSH&mp=1&pdp_npi=6%40dis%21CAD%21CAD+13.16%21CAD+11.00%21%21CAD+11.00%21%21%21%40210327ef17935643738446320e103a%2112000052930246742%21ct%21CA%218338085966%21%211%210%21|
|SK6812 RGB LEDs|$2.61|1|AliExpress|https://www.aliexpress.com/item/1005007863635868.html?spm=a2g0o.productlist.main.1.467e66echpig2D&algo_pvid=17f43b4a-c6ec-4e01-9861-3f38f1696518&algo_exp_id=17f43b4a-c6ec-4e01-9861-3f38f1696518-0&pdp_ext_f=%7B%22order%22%3A%22641%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21CAD%216.71%211.42%21%21%214.68%210.99%21%402101c69517929046052793291e0d52%2112000042594617264%21sea%21CA%218338085966%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac42caa26%3Bm03_new_user%3A-29895%3BpisId%3A5000000218625932&curPageLogUid=AQFVQ5jQSkKF&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007863635868%7C_p_origin_prod%3A|
|330Ω Resistor|$2.11|1|Sayal Electronics|https://secure.sayal.com/STORE4/prodetails.php?SKU=198449|
|Kailh Low Choc Key Switches|$7.99|1|AliExpress|https://www.aliexpress.com/item/1005008883418065.html?spm=a2g0o.productlist.main.1.1c9e5913F8kBSt&algo_pvid=278c7c25-9ab1-4a2a-9760-88be0dc0cf20&algo_exp_id=278c7c25-9ab1-4a2a-9760-88be0dc0cf20-0&pdp_ext_f=%7B%22order%22%3A%221409%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21CAD%2111.19%212.96%21%21%217.81%212.07%21%402101c69517929071229613399e0f00%2112000047082945007%21sea%21CA%218338085966%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac42caa26%3Bm03_new_user%3A-29895%3BpisId%3A5000000218625932&curPageLogUid=Vd6zfVEWhxYp&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005008883418065%7C_p_origin_prod%3A|
|Low Choc Kailh Key Caps|$4.01|AliExpress|1|https://www.aliexpress.com/item/1005006734545486.html?spm=a2g0o.cart.0.0.e95238dafhFbxx&mp=1&pdp_npi=6%40dis%21CAD%21CAD+6.09%21CAD+1.70%21%21CAD+1.70%21%21%21%402101d33417935618930793539e0e8c%2112000044697706461%21ct%21CA%218338085966%21%211%210%21&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D|
|128 x 64 0.96" OLED|$2.51|AliExpress|1|https://www.aliexpress.com/item/1005005462085489.html?spm=a2g0o.productlist.main.1.38bc2365vp9GcI&algo_pvid=6d367ac4-7b02-4b22-ba6b-ba9d2b3a06f9&algo_exp_id=6d367ac4-7b02-4b22-ba6b-ba9d2b3a06f9-0&pdp_ext_f=%7B%22order%22%3A%22462%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21CAD%214.34%211.71%21%21%213.03%211.19%21%40210303cd17929073709107426e0c72%2112000049496537372%21sea%21CA%218338085966%21ABX%211%210%21n_tag%3A-29910%3Bd%3Ac42caa26%3Bm03_new_user%3A-29895%3BpisId%3A5000000218656158&curPageLogUid=9Jwm7mz2IcVf&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005005462085489%7C_p_origin_prod%3A|
|74AHCT125N Level Shifter|$2.26|1|AliExpress|https://www.aliexpress.com/item/1005007655828920.html?spm=a2g0o.productlist.main.2.26b7551ew076eH&algo_pvid=78c66c40-76f2-432e-87b2-bd3bfed3491f&algo_exp_id=78c66c40-76f2-432e-87b2-bd3bfed3491f-1&pdp_ext_f=%7B%22order%22%3A%222562%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21CAD%213.50%211.41%21%21%212.45%210.99%21%402103081117935628901173779e0e93%2112000041675151148%21sea%21CA%218338085966%21ABX%211%210%21n_tag%3A-29910%3Bd%3A251db7%3Bm03_new_user%3A-29895%3BpisId%3A5000000218625936&curPageLogUid=agilp282nRvO&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007655828920%7C_p_origin_prod%3A|
|22uF Bulk Capacitor|$2.96|1|AliExpress|https://www.aliexpress.com/item/1005007464553853.html?spm=a2g0o.cart.0.0.36d438dalcLke0&mp=1&pdp_npi=6%40dis%21CAD%21CAD+9.00%21CAD+1.70%21%21CAD+1.70%21%21%21%40210327ef17935644201098839e103a%2112000040865339146%21ct%21CA%218338085966%21%211%210%21|
|100nF Capacitor|$3.32|1|AliExpress|https://www.aliexpress.com/item/1005003512666695.html?spm=a2g0o.productlist.main.3.83c45afbDEEDUU&algo_pvid=ef56e91d-e1a5-43da-841c-f11ec07990dc&algo_exp_id=ef56e91d-e1a5-43da-841c-f11ec07990dc-2&pdp_ext_f=%7B%22order%22%3A%22202%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21CAD%213.77%213.31%21%21%212.64%212.32%21%40210327ef17935650993205568e109d%2112000026121796491%21sea%21CA%218338085966%21ABX%211%210%21n_tag%3A-29910%3Bd%3A251db7%3Bm03_new_user%3A-29895%3BpisId%3A5000000220770329&curPageLogUid=wUzDEXA1trVM&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005003512666695%7C_p_origin_prod%3A|
|PCB|$4.00|1|JLCPCB|https://jlcpcb.com/|
|Shipping & Taxes|-||$1.77|-|
|Total|-|-|$36.24|-|

## Extra Notes 
Note that, for the cart screenshots submitted on the Half Life website, all prices are in CAD. However, all prices have been converted for each individual item into USD for the BOM, thus there may be a small rounding error (will most likely be negligible; I can pay the difference out of pocket). There is 1 cart screenshot labeled [ALREADY OWNED] that displays the cart of the items I already own, so the prices for every item in there are not counted. Furthermore, there are special discounts (specifically for AliExpress) located in the BOM.csv from Half Life, which is why I am able to afford it under the $30 budget. Additionally, a lot of the parts in the BOM.csv are priced at $0.01 because I already own them. This is because the parts are the exact parts I will be using in my Week 3 project, so I can just reuse the excess in this project and save on having to buy completely new parts. 

Please pay attention to the descriptions of each item! Those that are labeled with [OUT OF POCKET] and [ALREADY OWNED] are not purchased with the grant and thus cost $0.01. Additionally, the vendors labeled (Local) are local to me, so I do not have to pay for shipping as I can go to them in person. All shipping prices are based on my own address and ability to go in-person for certain vendors.

This was my first ever basically-entirely-custom PCB! I'm super excited to actually get to use it :)
