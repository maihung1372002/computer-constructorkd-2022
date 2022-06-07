from dis import dis
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

    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    x_coor = LCD.LCDWIDTH // 2
    y_coor = LCD.LCDHEIGHT // 2
    draw.ellipse((x_coor - 15, y_coor - 15, x_coor +
                 15, y_coor + 15), outline=0, fill=1)

    disp.image(image)
    disp.display()
    while True:
        time.sleep(2)


try:
    main()
except KeyboardInterrupt:
    disp.clear()
