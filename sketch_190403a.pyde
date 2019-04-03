add_library('pdf')
def setup():
    size(246, 316)
    global elementy
    global ok
    global im
    global jez
    global kap
    beginRecord(PDF,"eksportpdf.pdf")
    im = loadImage("dowodowe.JPG")
    imageMode(CENTER)
    image(im, width/2, height/2, width, height)
    ok = loadImage("okularki.png")
    imageMode(CENTER)
    jez = loadImage("jezyk.png")
    imageMode(CENTER)
    kap = loadImage("kapelusz.png")
    imageMode(CENTER)
    elementy = "okularki", "jezyk", "kapelusz"
    print "Wcisnij LEWY klawisz, by dodac element"
    print "Wcisnij PRAWY klawisz, usunac element"
def draw():
    global elementy
    global ok
    global im
    global jez
    global kap
    if mousePressed and (mouseButton == LEFT):
        losowanie = int(random(len(elementy)))
        wylosowany = elementy[losowanie]
        if wylosowany == "okularki":
            image(ok, 125, 159, 200, 100)
        elif wylosowany == "kapelusz": 
            image(kap, 120, 100, 375, 500)
        elif wylosowany == "jezyk": 
            image(jez, 125, 237, 75, 76)
        print "Wcisnij LEWY klawisz, by dodac element"
        print "Wcisnij PRAWY klawisz, usunac element"
        print(wylosowany)
    elif mousePressed and (mouseButton == RIGHT):
        image(im, width/2, height/2, width, height)
    endRecord()
    
    
        

#https://i.ebayimg.com/00/s/NTA4WDQwMA==/z/0pwAAOSwgmtaM7Tg/$_20.JPG
#https://www.pkt.pl/imgb/product/97/22/okulary-oakley-0oo9265-24-5c64d69c-1.png
#http://www.dbamyozeby.net.pl/wp-content/uploads/2018/04/czysty-jezyk.png
#http://stylistki.pl/kapelusz-damski-top-secret-i50252.png

#wczytać obrazek, zdjecie dowodowe
#jak wczytamy twarz dodać coś do niej (okulary, brodę itp)
#obrazek z zawartością dodatkową wyeksportować do pdf
#dodać coś od siebie
