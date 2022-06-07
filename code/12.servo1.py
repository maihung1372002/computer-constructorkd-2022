import RPi.GPIO as GPIO
import time


def main():
    GPIO.setmode(GPIO.BCM)
    global s
    s = sg90()

    anglepulse = 5
    print("Tat ca da san sang")
    while True:
        anglepulse = controlservo(s, anglepulse)

def controlservo(s, anglepulseBT):
    current = s.currentdirection()
    if current >= 180 or current <= 0:
        anglepulseBT = -anglepulseBT
    rotato = anglepulseBT + current
    rotato = 180 if rotato >= 180 else 0 if rotato <= 0 else rotato
    s.setdirection(rotato, 40)
    led(rotato)
    time.sleep(0.5)
    return anglepulseBT


class sg90:
    def __init__(self):
        self.pin = 19
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 100)
        self.servo = GPIO.PWM(13, 100)
        self.servo.start(0.0)
        self.direction = 90

    def cleanup(self):
        self.servo.ChangeDutyCycle(self._henkan(0))
        time.sleep(0.3)
        self.servo.stop()
        GPIO.cleanup()

    def currentdirection(self):
        return self.direction

    def _henkan(self, value):
        return round(0.056 * value + 2.0)

    def setdirection(self, direction, speed):
        for d in range(self.direction, direction, int(speed)):
            self.servo.ChangeDutyCycle(self._henkan(d))
            self.direction = d
            time.sleep(0.1)
        self.servo.ChangeDutyCycle(self._henkan(direction))
        self.direction = direction


def led(distance):
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp  # khoi tao bien global
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)  # Khoi tao LCD
    disp.begin(contrast=60)  # cai dat do sang
    disp.clear()
    disp.display()
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, LCD.LCDWIDTH - 1, LCD.LCDHEIGHT - 1), outline=0, fill=255)
    font = ImageFont.load_default()
    draw.text((30, 15), str(distance) + "deg", font=font, fill=100)  # chen chu disp.image(image)
    disp.display()


try:
    main()
except KeyboardInterrupt:
    s.cleanup()
