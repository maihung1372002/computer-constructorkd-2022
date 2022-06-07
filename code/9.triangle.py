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
    global disp  # Khoi tao bien global
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)  # khoi tao LCD
    disp.begin(contrast=60)  # Cai dat do sang

    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    # ve hinh chu nhat mau trang
    draw.rectangle((0, 0, LCD.LCDWIDTH - 1, LCD.LCDHEIGHT - 1),
                   outline=0, fill=255)
    # font = ImageFont.load_default()
    # draw.polygon([(32,32),(42,12),(52,32)],outline=0, fill=255)
    # ve hinh tam giac vuong trong hinh chu nhat
    A = (21, 12)
    B = (21, 36)
    C = (63, 36)
    draw.polygon([A, B, C], outline=0, fill=255)
    # hien thi hinh anh
    disp.image(image)
    disp.display()
    while True:
        time.sleep(2)


try:
    main()
except KeyboardInterrupt:
    disp.clear()
