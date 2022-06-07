import RPi.GPIO as GPIO
import time

def main():
    # blue = 5, red = 22, green = 1/7
    RED = 22
    GREEN = 7
    BLUE = 5
    BT1 = 14

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(BLUE, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.output(RED, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)

    l = 0

    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            l = (l+1) % 2
            time.sleep(0.5)
        if l > 0:
            GPIO.output(RED, GPIO.HIGH)
        else:
            GPIO.output(RED, GPIO.LOW)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
