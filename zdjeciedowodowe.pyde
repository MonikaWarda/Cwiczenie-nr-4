def setup():
    size(246, 316)
    im = loadImage("dowodowe.JPG")
    print(type(im))
    imageMode(CENTER)
    image(im, width/2, height/2, width, height)
def draw():
    if mousePressed():
        ok = loadImage("okularki.png")
        imageMode(CENTER)
        image(ok, 125, 159, 200, 100)
        
#https://i.ebayimg.com/00/s/NTA4WDQwMA==/z/0pwAAOSwgmtaM7Tg/$_20.JPG
#https://www.pkt.pl/imgb/product/97/22/okulary-oakley-0oo9265-24-5c64d69c-1.png
