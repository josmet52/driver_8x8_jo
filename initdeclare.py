
#!/usr/bin/env python


#import os
#import time
#import sys
#import Adafruit_DHT
import RPi.GPIO as GPIO

#from driver8x8jo import display_scroll
from ds18b20 import DS18B20
from PIL import Image
from PIL import ImageDraw
from Adafruit_LED_Backpack import BicolorMatrix8x8

def cls(): print "\n" * 100

def gpio_init():

    # initialise GPIO

    GPIO.setmode(GPIO.BCM)
    in_LCD = 27
    in_PIR = 22
    GPIO.setup(in_LCD, GPIO.IN, GPIO.PUD_UP) 
    GPIO.setup(in_PIR, GPIO.IN)

    # intialise temprature sensor DHxx
    in_DH11 = 21
    in_DH22 = 17

    # initialise free GPIO
    inout_Free_GPIO = 12 

    # initialise buttons
    GPIO.setwarnings(False)

    in_btn_red = 19
    in_btn_green = 5
    in_btn_blue = 6

    in_btn_left = 13
    in_btn_right = 20
    in_btn_up = 26
    in_btn_down = 16

    GPIO.setup(in_btn_red, GPIO.IN, GPIO.PUD_DOWN) 
    GPIO.setup(in_btn_green, GPIO.IN, GPIO.PUD_DOWN) 
    GPIO.setup(in_btn_blue, GPIO.IN, GPIO.PUD_DOWN) 
    GPIO.setup(in_btn_left, GPIO.IN, GPIO.PUD_DOWN) 
    GPIO.setup(in_btn_right, GPIO.IN, GPIO.PUD_DOWN) 
    GPIO.setup(in_btn_up, GPIO.IN, GPIO.PUD_DOWN) 
    GPIO.setup(in_btn_down, GPIO.IN, GPIO.PUD_DOWN)

def ds18b20_init():
    # initialise temperature sensors
    sensorArray = DS18B20()

def display_init():
    # Create display instance on default I2C address (0x70) and bus number.
    display = BicolorMatrix8x8.BicolorMatrix8x8()
    display.begin()
    display.clear()

    # Smile
    image_smile= Image.new('RGB',(8,8))
    draw_smile = ImageDraw.Draw(image_smile)
    draw_smile.line((0, 2, 0, 5), fill=(0, 255, 0))
    draw_smile.line((1, 1, 1, 1), fill=(0, 255, 0))
    draw_smile.line((1, 6, 1, 6), fill=(0, 255, 0))
    draw_smile.line((2, 0, 5, 0), fill=(0, 255, 0))
    draw_smile.line((2, 7, 5, 7), fill=(0, 255, 0))
    draw_smile.line((7, 2, 7, 5), fill=(0, 255, 0))
    draw_smile.line((2, 3, 2, 4), fill=(0, 255, 0))
    draw_smile.line((3, 2, 3, 2), fill=(0, 255, 0))
    draw_smile.line((3, 5, 3, 5), fill=(0, 255, 0))
    draw_smile.line((5, 2, 5, 2), fill=(255, 255, 0))
    draw_smile.line((5, 5, 5, 5), fill=(255, 255, 0))

    # pote
    image_pote= Image.new('RGB',(8,8))
    draw_pote = ImageDraw.Draw(image_pote)
    draw_pote.line((0, 2, 0, 5), fill=(0, 255, 0))
    draw_pote.line((1, 1, 1, 1), fill=(0, 255, 0))
    draw_pote.line((1, 6, 1, 6), fill=(0, 255, 0))
    draw_pote.line((2, 0, 5, 0), fill=(0, 255, 0))
    draw_pote.line((2, 7, 5, 7), fill=(0, 255, 0))
    draw_pote.line((7, 2, 7, 5), fill=(0, 255, 0))
    draw_pote.line((3, 3, 3, 4), fill=(0, 255, 0))
    draw_pote.line((2, 2, 2, 2), fill=(0, 255, 0))
    draw_pote.line((2, 5, 2, 5), fill=(0, 255, 0))
    draw_pote.line((5, 2, 5, 2), fill=(255, 255, 0))
    draw_pote.line((5, 5, 5, 5), fill=(255, 255, 0))

    # froid
    image_froid= Image.new('RGB',(8,8))
    draw_froid = ImageDraw.Draw(image_froid)
    draw_froid.line((0, 2, 0, 5), fill=(0, 255, 0))
    draw_froid.line((1, 1, 1, 1), fill=(0, 255, 0))
    draw_froid.line((1, 6, 1, 6), fill=(0, 255, 0))
    draw_froid.line((2, 0, 5, 0), fill=(0, 255, 0))
    draw_froid.line((2, 7, 5, 7), fill=(0, 255, 0))
    draw_froid.line((7, 2, 7, 5), fill=(0, 255, 0))
    draw_froid.line((2, 3, 2, 4), fill=(0, 255, 0))
    draw_froid.line((2, 2, 2, 2), fill=(0, 255, 0))
    draw_froid.line((2, 5, 2, 5), fill=(0, 255, 0))
    draw_froid.line((5, 2, 5, 2), fill=(255, 255, 0))
    draw_froid.line((5, 5, 5, 5), fill=(255, 255, 0))

    # bof
    image_bof= Image.new('RGB',(8,8))
    draw_bof = ImageDraw.Draw(image_bof)
    draw_bof.line((0, 2, 0, 5), fill=(0, 255, 0))
    draw_bof.line((1, 1, 1, 1), fill=(0, 255, 0))
    draw_bof.line((1, 6, 1, 6), fill=(0, 255, 0))
    draw_bof.line((2, 0, 6, 0), fill=(0, 255, 0))
    draw_bof.line((2, 7, 6, 7), fill=(0, 255, 0))
    draw_bof.line((7, 2, 7, 5), fill=(0, 255, 0))
    draw_bof.line((2, 3, 2, 4), fill=(0, 255, 0))
    draw_bof.line((3, 2, 3, 3), fill=(0, 255, 0))
    draw_bof.line((2, 5, 2, 5), fill=(0, 255, 0))
    draw_bof.line((5, 2, 5, 2), fill=(0, 255, 0))
    draw_bof.line((5, 5, 5, 5), fill=(0, 255, 0))

    # grrrr
    image_grr= Image.new('RGB',(8,8))
    draw_grr = ImageDraw.Draw(image_grr)
    draw_grr.line((0, 2, 0, 5), fill=(0, 255, 0))
    draw_grr.line((1, 1, 1, 1), fill=(0, 255, 0))
    draw_grr.line((1, 6, 1, 6), fill=(0, 255, 0))
    draw_grr.line((2, 0, 6, 0), fill=(0, 255, 0))
    draw_grr.line((2, 7, 6, 7), fill=(0, 255, 0))
    draw_grr.line((7, 2, 7, 5), fill=(0, 255, 0))
    draw_grr.line((2, 2, 2, 5), fill=(0, 255, 0))
    draw_grr.line((3, 2, 3, 5), fill=(0, 255, 0))
    draw_grr.line((5, 2, 5, 2), fill=(255, 0, 0))
    draw_grr.line((5, 5, 5, 5), fill=(255, 0, 0))

    # black
    image_black= Image.new('RGB',(8,8))
    draw_black = ImageDraw.Draw(image_black)

