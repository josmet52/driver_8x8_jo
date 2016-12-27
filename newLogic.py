#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os.path
# print abspath('/home')

from initdeclare import cls
from initdeclare import gpio_init
from initdeclare import ds18b20_init
from initdeclare import display_init

cls()
gpio_init()
ds18b20_init()
display_init()

print in_btn_red, in_btn_blue
while True:
   
   print ''
   print('Infinite loop. CTRL-C for break')
#   print ''
   
   i = 0
   ds18b20_count = 1 #sensorArray.device_count()

   while i < ds18b20_count:
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
   

