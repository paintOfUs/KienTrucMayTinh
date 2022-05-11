import RPi.GPIO as GPIO
import time
import Adafruit_Nokia_LCD as LCD
from PIL import Image, ImageDraw, ImageFont

def main():
    d = 40/2
    # GPIO pins
    BT1 = 14
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    # init LCD
    global disp
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
    disp.begin(contrast=60) #do sang
    disp.clear()
    disp.display()
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT)) # create new image with 1 bit
    draw = ImageDraw.Draw(image) #chon doi tuong de ve
    #draw.ellipse((20,8,62,41), outline=255, fill=255)
    draw.polygon(([(50, 40),(10, 10),(50, 10)]), outline=255, fill=255)
    disp.image(image)
    disp.display()

try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()

