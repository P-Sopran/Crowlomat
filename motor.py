import RPi.GPIO as GPIO
from time import sleep
import schedule
from datetime import date

class motor:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def turn(self):
        GPIO.setmode(GPIO.BOARD)
        pins = [self.p1, self.p2, self.p3, self.p4]

        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin,0)

        sequence = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
            ]

        for i in range(512):
            for step in range(8):
                for pin in range(4):
                    GPIO.output(pins[pin], sequence[step][pin])
                sleep(0.0015)
        GPIO.cleanup()


    def turnOnDate(self, checkDate):
        datum = date.today().strftime("%d.%m.%Y")
        if datum == checkDate:
            self.turn()
        return schedule.CancelJob


