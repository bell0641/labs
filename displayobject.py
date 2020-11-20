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

        
def diplayObject(obj,x,y) : 
    lcd.clear()
    xp=x
    for y1 in obj : 
        for x2 in y1 : 
            lenY = len(obj)
            lenX = len(y1)
            
            if x2 == 1 :
                pixel = 1 
            else : 
                pixel = 0
            
            lcd.set_pixel(xp,y,pixel)
            xp = xp+1
        y = y + 1
        lcd.set_pixel(xp,y,pixel)
        xp=x
    lcd.show()


f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

def MainMenu():
    print("select ... : ")
    print("1 - Display Object ")
    print("2 - Exit")
    option = input("Enter Your Choise : ")

    if option == "1":
        lcd.clear()
        lcd.show()
        print("choose : \n 1 - to draw a PAC MAN \n 2 - to draw fighter ")
        obj = int(input())
        if obj== 1 :
            obj = pm
        elif obj == 2 :
            obj= f1

        else : 
            print("invalid option ...")
            print("choose : \n 1 - to draw a PAC MAN \n -2 to draw fight")
            obj = int(input())


        for y1 in obj:
            for x1 in y1 : 
                lenthX = len(y1)
                lenthY = len(obj)


        xPoint = int(input("input the x cordinate -must be between 0 and 127 :"))
        yPoint = int(input("input the  y cordinate -must be between 0 and 63 : "))

        totalX = lenthX + xPoint
        totalY = lenthY + yPoint

        if totalX > 127 :
            print("X value is too big for the image please type a smaller X cordinate ")
            xPoint = int(input("input the x cordinate -must be between 0 and 127 : "))
            diplayObject(obj,xPoint,yPoint)
        
        elif totalY > 63 : 
            print("Y value is too big for the image please type a smaller X cordinate ")
            yPoint = int(input("input the  y cordinate -must be between 0 and 63 : "))
            diplayObject(obj,xPoint,yPoint)

        else : 
            diplayObject(obj,xPoint,yPoint)
    elif option == "2" :
        lcd.clear()
        lcd.show()
MainMenu()



