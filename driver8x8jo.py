import time
from Adafruit_LED_Backpack import BicolorMatrix8x8
    
# Digit value to bitmask mapping:
DIGIT_VALUES = {
    ' -000000',
    '%-025004019000',
    '+-004012004000',
    '--004004004000',
    '.-016000',
    '!-023000',
    '/-024004024000',
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
    

def display_scroll(vTxt, txtColor, baseLineColor, letLastDataOnScreen):

    vTxt = vTxt.upper() # les minuscules sont converties en majuscules
    
    # Create display instance on default I2C address (0x70) and bus number.
    display = BicolorMatrix8x8.BicolorMatrix8x8()
    display.begin()

    vCol = 7 # on part depuis la colonne 7
    nCol = 1000 # aux max 1000 colonnes soir environ 250 caracteres
    nRow = 8 # matrice de 8x8 leds
    vDisp = [[0]*nRow for k in range(nCol)] # declaration d'un array 1000 col de 8 leds
    
    for c in vTxt: # pour tous les caractres de vTxt
        for d in DIGIT_VALUES: # on recherche la correspondance
            if d[0] == c:
                vStart = 2
                vStop = vStart + 3
                while vStop < len(d):
                    i=int(d[vStart:vStop])
                    if i&1 <> 0:
                        vDisp[vCol][0]=txtColor
                    if i&2 <> 0:
                        vDisp[vCol][1]=txtColor
                    if i&4 <> 0:
                        vDisp[vCol][2]=txtColor
                    if i&8 <> 0:
                        vDisp[vCol][3]=txtColor
                    if i&16 <> 0:
                        vDisp[vCol][4]=txtColor
                    if i&32 <> 0:
                        vDisp[vCol][5]=txtColor
                    if baseLineColor <> 0:
                        vDisp[vCol][6]=baseLineColor
                    if baseLineColor <> 0:
                        vDisp[vCol][7]=baseLineColor
                    
                    vStart=vStop
                    vStop = vStart + 3
                    vCol+=1

        if baseLineColor <> 0:
            vDisp[vCol][6]=baseLineColor
        if baseLineColor <> 0:
            vDisp[vCol][7]=baseLineColor
        vCol+=1
        
    display.clear()
    
    if letLastDataOnScreen:
        vRange = vCol-7
    else:
        vRange = vCol + 1
        
    for c in range(vRange):
        for d in range(c,c+8):
            for l in range(nRow):
                # display a activer
                display.set_pixel(7-l,d-c,vDisp[d][l])
            display.write_display()
        time.sleep(0.15)
                
            
        
    
                        
