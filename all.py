# -*- coding: utf-8 -*-

import os
import time
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO

from ds18b20 import DS18B20
from driver8x8jo import display_scroll
from PIL import Image
from PIL import ImageDraw
from Adafruit_LED_Backpack import BicolorMatrix8x8

def cls(): print "\n" * 100

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

# initialise temperature sensors
sensorArray = DS18B20()
count=sensorArray.device_count()

# Create display instance on default I2C address (0x70) and bus number.
display = BicolorMatrix8x8.BicolorMatrix8x8()
display.begin()

# Clear the display buffer.
display.clear()
tSleep = 1
tSleep_main = 5
print 'CTRL-C to stop'

# Sourire
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

while True:
   
   print ''
   print('Infinite loop. CTRL-C for break')
#   print ''
   
   i = 0
   while i < count:
      temperature,sensorId,mesureStatus = sensorArray.tempC(i)
      print('Sensor '+sensorId+' mesure '+str(temperature)+'°C')
      vTxt = 'DS18B20 temp: '+str(temperature)+'°C'
      if temperature < 19 : vColor = 3
      elif temperature > 24 : vColor =2
      else : vColor = 1
      display_scroll(vTxt,vColor,0,False, False)
      i += 1

   # test_dht11
#   humidity, temperature = Adafruit_DHT.read_retry(11, in_DH11)
#   print 'DH11 -> Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

   # test_am2302 (dht22 avec boitier et cables)
   humidity, temperature = Adafruit_DHT.read_retry(22, in_DH22)
   print 'DHT22 temp: {0:0.1f}°C  Humidity: {1:0.1f} %'.format(temperature, humidity)
   vTxt = 'DHT22 temp: {0:0.1f}°C  Hrel: {1:0.1f} %'.format(temperature, humidity)
   if temperature < 19 : vColor = 3
   elif temperature > 24 : vColor =2
   else : vColor = 1
   display_scroll(vTxt,vColor,0,False, False)

   # light and infrared sensors
   vLight = not GPIO.input(in_LCD)
   vPir = GPIO.input(in_PIR)

   # LCD
   if vLight :
      print 'light ON' ,
      display_scroll('light ON',1,0,False, False)
   else :
      print 'light OFF' ,
      display_scroll('light OFF',1,0,False, False)

   # PIR
   if vPir :
      print 'pir ON'
      display_scroll('PIR ON',1,0,False, False)
      lcdState = True
   else :
      print 'pir OFF'
      display_scroll('PIR OFF',1,0,False, False)
      lcdState = False
      display.set_image(image_black)
      display.write_display()

   if vLight and vPir :
      print 'Fini de rever. Au boulot'
      display.set_image(image_smile)
   elif vLight and not vPir :
      print 'Il fait jour, la vie est belle'
      display.set_image(image_smile)
   elif not vLight and vPir :
      print 'Alarme, des cambrioleurs'
      display.set_image(image_grr)
   elif not vLight and not vPir :
      print 'Tout est calme, dormez braves gens'
      display.set_image(image_bof)
   else :
      print 'OUUUPS quelque chose de bizare s'' est passe'
      display.set_image(image_froid)

   display.write_display()
   time.sleep(tSleep_main)

# read the state of the buttons
   vbtn_red = GPIO.input(in_btn_red)
   vbtn_green = GPIO.input(in_btn_green)
   vbtn_blue = GPIO.input(in_btn_blue)
   vbtn_left = GPIO.input(in_btn_left)
   vbtn_right = GPIO.input(in_btn_right)
   vbtn_up = GPIO.input(in_btn_up)
   vbtn_down = GPIO.input(in_btn_down)

   vRepeat = vbtn_red or vbtn_green or vbtn_blue or vbtn_left or vbtn_right or vbtn_up or vbtn_down
   while vRepeat:
      if vbtn_red :
         print 'RED button pressed'
         vTxt = 'The quick brown fox jumps over the lazy dog 1234567890'
         display_scroll(vTxt,2,0,False, False)
      if vbtn_green :
         print 'GREEN button pressed'
         vTxt = 'The quick brown fox jumps over the lazy dog 1234567890'
         display_scroll(vTxt,1,0,False, False)
      if vbtn_blue :
         print 'BLUE button pressed'
         vTxt = 'The quick brown fox jumps over the lazy dog 1234567890'
         display_scroll(vTxt,3,0,False, False)
      if vbtn_left :
         print '<  button pressed'
         vTxt = '<<<<<<<<'
         display_scroll(vTxt,3,0,False, False)
      if vbtn_right :
         print '>  button pressed'
         vTxt = '>>>>>>>>'
         display_scroll(vTxt,3,0,False, False)
      if vbtn_up :
         print '^  button pressed'
         vTxt = '^^^^^^^^^^'
         display_scroll(vTxt,3,0,False, False)
      if vbtn_down :
         print 'v  button pressed'
         vTxt = ',,,,,,,,,'
         display_scroll(vTxt,3,0,False, False)

      vbtn_red = GPIO.input(in_btn_red)
      vbtn_green = GPIO.input(in_btn_green)
      vbtn_blue = GPIO.input(in_btn_blue)
      vbtn_left = GPIO.input(in_btn_left)
      vbtn_right = GPIO.input(in_btn_right)
      vbtn_up = GPIO.input(in_btn_up)
      vbtn_down = GPIO.input(in_btn_down)
      vRepeat = vbtn_red or vbtn_green or vbtn_blue or vbtn_left or vbtn_right or vbtn_up or vbtn_down
   

