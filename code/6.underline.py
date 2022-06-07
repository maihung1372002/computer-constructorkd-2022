from dis import dis
import time
import Adafruit_Nokia_LCD as LCD
import RPi.GPIO as GPIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    BT1 = 14
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global disp
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
    disp.begin(contrast=60)

    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LCD.LCDWIDTH - 1, LCD.LCDHEIGHT - 1),
                   outline=0, fill=255)

    # and another shape

    font = ImageFont.load_default()

    draw.text((8, 20), '*Hello world!', font=font, fill=0)
    draw.line((8, 30, LCD.LCDWIDTH - 1, 30), fill=0)

    disp.image(image)
    disp.display()
    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            # draw.text((8, 20), '*Hello world!', font=font, fill=255)
            image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, LCD.LCDWIDTH - 1, LCD.LCDHEIGHT - 1),
                           outline=0, fill=255)
            disp.image(image)
            disp.display()


try:
    main()
except KeyboardInterrupt:
    disp.clear()
