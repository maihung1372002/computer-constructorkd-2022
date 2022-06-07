import time
import Adafruit_Nokia_LCD as LCD

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def main():
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
    disp.begin(contrast=60)
    disp.clear()
    disp.display()
    message = '*hello world'
    n = len(message)
    
    while True:
        for i in range(n):
            image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
            draw = ImageDraw.Draw(image)
            draw.rectangle((0,0,LCD.LCDWIDTH-1,LCD.LCDHEIGHT-1), outline=0, fill=255)
            font = ImageFont.load_default()
            draw.text((8,30), message[n-i:n], font=font)
            print(message[n-i:n])
            disp.image(image)
            disp.display()
            time.sleep(0.5)

try:
    main()
except KeyboardInterrupt:
    disp.clear()
    disp.display()
