import RPi.GPIO as GPIO
import time


def main():
    # red = 22, green = 1/7
    RED = 22
    GREEN = 1
    BT1 = 14

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RED, GPIO.OUT)
    GPIO.setup(GREEN, GPIO.OUT)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)

    is_on = True

    while True:
        if is_on:
            GPIO.output(GREEN, GPIO.LOW)
            GPIO.output(RED, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(RED, GPIO.LOW)
            GPIO.output(GREEN, GPIO.HIGH)
            time.sleep(1)
        if GPIO.input(BT1) == GPIO.LOW:
            is_on = not is_on
            GPIO.output(GREEN, GPIO.LOW)
            GPIO.output(RED, GPIO.LOW)
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
