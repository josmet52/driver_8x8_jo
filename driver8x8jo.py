# -*- coding: utf-8 -*-


# driver8x8jo.py
# --------------
# driver to display texts and numbers on the Adafruit 8x8 leds display with backpack
#
# dec 2016
# J. Metrailler / joseph.metrailler@bluewin.ch
#
# call example : display_scroll(vTxt, txtColor, baseLineColor, scrollNonStop, letLastDataOnScreen)
#
# with  vTxt                : the text to display. The lower case char are automatiquely converted in upper case
#       txtColor            : the color of the displayed text : 0=not displayed, 1=green, 2=red, 3=orange
#       baselineColor       : the color of the base line : 0=not displayed, 1=green, 2=red, 3=orange
#       scrollNonStop       : when True the texte restart when finished
#       letLastDataOnScreen : when True the last data stay on display
#

import time
from Adafruit_LED_Backpack import BicolorMatrix8x8
    
# Digit value to bitmask mapping:
#     '°-000000',
DIGIT_VALUES = {
    ' -000000',
    '%-025004019000',
    '+-004012004000',
    '--004004004000',
    '.-016000',
    '!-023000',
    ',-016008000',
    ':-010000',
    '/-024004024000',
    '>-017010004000',
    '<-004010017000',
    '^-004002004000',
    '0-014017014000',
    '1-002031000',
    '2-018025022000',
    '3-017021010000',
    '4-007004030000',
    '5-023021009000',
    '6-014021012000',
    '7-017013003000',
    '8-014021014000',
    '9-007005031000',
    '=-010010010000',
    'A-031005031000',
    'B-031021010000',
    'C-014017017000',
    'D-031017014000',
    'E-031021017000',
    'F-031005001000',
    'G-014021025000',
    'H-031004031000',
    'I-031000',
    'J-008016015000',
    'K-031012019000',
    'L-031016016000',
    'M-031002031000',
    'N-031001031000',
    'O-031017031000',
    'P-031005007000',
    'Q-015009031000',
    'R-031013023000',
    'S-023021029000',
    'T-001031001000',
    'U-031016031000',
    'V-007024007000',
    'W-031008031000',
    'X-027004027000',
    'Y-003028003000',
    'Z-025021019000',
}
    

def display_scroll(vTxt, txtColor, baseLineColor, scrollNonStop, letLastDataOnScreen):

    vTxt = vTxt.upper() # lower case char are converted in upper case 
    # because not possible lower case char on a 3x5 matrix
    
    # Create display instance on default I2C address (0x70) and bus number.
    display = BicolorMatrix8x8.BicolorMatrix8x8()
    display.begin()
    display.clear()
    
    vCol = 7 # start on the sevens column (the right of the display)
    nCol = 1000 # max 1000 column so about 250 char
    nRow = 8 # 8x8 leds matrix
    vDisp = [[0]*nRow for k in range(nCol)] # the array of 1000 columns and 8 rows filled with 0

    # Prepare the display matrix
    for c in vTxt: # for each char in vTxtx
        for d in DIGIT_VALUES: # search the char
            if d[0] == c: # char found
                vStart = 2 # coding start at thirst char
                vStop = vStart + 3 # every value coded on 3 char

                # find the bits for each coded value
                while vStop <= len(d):
                    i=int(d[vStart:vStop])

                    # codage du caractere
                    if i&1 <> 0: # bit0
                        vDisp[vCol][0]=txtColor
                    if i&2 <> 0: # bit1
                        vDisp[vCol][1]=txtColor
                    if i&4 <> 0: # bit2
                        vDisp[vCol][2]=txtColor
                    if i&8 <> 0: # bit 3
                        vDisp[vCol][3]=txtColor
                    if i&16 <> 0: # bit 4
                        vDisp[vCol][4]=txtColor
                    if i&32 <> 0: # bit 5
                        vDisp[vCol][5]=txtColor
##                    if i&64 <> 0: # bit 6
##                        vDisp[vCol][6]=txtColor
##                    if i&128 <> 0: # bit 7
##                        vDisp[vCol][7]=txtColor

                    # Codage de la ligne de base
                    vDisp[vCol][6]=baseLineColor
                    vDisp[vCol][7]=baseLineColor

                    # on prepare la valeur suivante
                    vStart=vStop
                    vStop = vStart + 3
                    vCol+=1

    if letLastDataOnScreen:
        vRange = vCol-7
    else: # clear the screen when the scroll finished
        vRange = vCol + 1

    if not scrollNonStop:
        for c in range(vRange):
            for d in range(c,c+8):
                for l in range(nRow):
                    # display a activer
                    display.set_pixel(7-l,d-c,vDisp[d][l])
                display.write_display()
            time.sleep(0.15)
    else:
        while True:
            for c in range(vRange):
                for d in range(c,c+8):
                    for l in range(nRow):
                        # display a activer
                        display.set_pixel(7-l,d-c,vDisp[d][l])
                    display.write_display()
                time.sleep(0.15)
                
            
        
    
                        
