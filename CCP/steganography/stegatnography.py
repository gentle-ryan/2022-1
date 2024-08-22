from base64 import encode, decode
from PIL import Image

image = Image.open("mandrill_stegano2.png")
image2 = Image.open("mandrill_stegano.png")
width, height = image.size

pixels = image.load() 

list = []
for h in range(0, height, 16):
    for w in range(0, width, 16):
        list.append(chr(pixels[w, h][1]))
''.join(list)
 
# look at the red channel 
# collect lsb
# convert binary to unicode 
# try chr(0b0000000001000001)

red = image.getchannel(0)
red.show()
width, height = red.size
newimg = Image.new("RGB", (width, height), (255, 255, 255))

pixel = red.load()
newpixel = newimg.load()

tile_height = 16
tile_width = 16

for h in range(int(height / tile_height)):
    for w in range(int(width / tile_width)):
        tile = []
        total = [0]
        for th in range(tile_height):
            for tw in range(tile_width):
                r = pixel[w*tile_width + tw, h*tile_height + th]
                total[0] += r
        n = (tile_height*tile_width)
        r = int(total[0] / n)
        for th in range(tile_height):
            for tw in range(tile_width):
                newpixel[w*tile_width + tw, h*tile_height + th] = r

newimg.show()

hoho = newimg.getchannel(0)
hoho.show()
hoho2 = hoho.load()


list_red = []
for h in range(height):
    for w in range(width):
        list_red.append(bin(pixel[w, h])[-1])
list_red
    
list_red2 = [list_red[i:i + 16] for i in range(0, len(list_red), 16)]
list_red2

for i in list_red2:
    s = ''.join(i)
    s = '0b' + s
    a = int(s, 2)
    #c = format(a, '#x')
    #c = int(s, 16)
    c = chr(a)
    u = c.encode('utf-8', 'ignore')
    u = u.decode('utf-8')
    u


    




    #a = int(s)
    #chr(a)
chr('0b1000000000000000')
c = unicode('a')
print(c)
type(chr('0b000000000000000'))   
type(bin(2))

type(0b001)