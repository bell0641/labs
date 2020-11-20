from gfxhat import lcd,  fonts , backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar



def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 


def etchSketch(x,y):
    while True : 
        key = getchar()
        lcd.set_pixel(x,y,1)
        lcd.show()
        if key == 's':
            lcd.clear()
            lcd.show()
        elif key == '\x1b[A' : 
            y = y-1
            if y == 0:
                y=63
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[B':
            y=y+1
            if y==63:
                y=0
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[D' :
            x = x - 1
            if x == 0:
                x=127
            lcd.set_pixel(x,y,1)
            lcd.show()

        elif key == '\x1b[C':
            x = x +1 
            if x== 127 : 
                x=0
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key =='q' : 
            lcd.clear()
            lcd.show()
            exit()

        else : 
            print("chose a valid option ")

def MainMenu():
    print("select ... : ")
    print("1 - Etch Sketch ")
    print("2 - Exit")
    option = input("Enter Your Choise : ")

    if option =="1":
        lcd.clear()
        lcd.show()
        bg = "Etch a Sketch"
        xPoint = int(input("input the x cordinate -must be between 0 and 127 : "))
        yPoint = int(input("input the  y cordinate -must be between 0 and 63 : "))
        displayText(bg,lcd,20,20)
        etchSketch(xPoint,yPoint)
        MainMenu()
        
    elif option == "2" :
        lcd.clear()
        lcd.show()

MainMenu()



