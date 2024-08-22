# mandrill.py
#
# Image Processing With the Python Pillow Library
#
# 2022-04-26
# 실습 07 컴퓨터의 개념 및 실습 수업용 파일
# 언어학과 박유나 2021-1659에 의해 작성

from PIL import Image

# 이미지 파일을 읽어서 화면에 띄워 봅시다.
image = Image.open("mandrill.png")
image.show()

# 이미지를 변환해 볼 거예요.
# 변환된 결과를 보관하기 위해서 같은 크기의 빈 이미지를 만들어요.
width, height = image.size
newimg = Image.new("RGB", (width, height), (255, 255, 255))

# 확인해 보세요. 빈 이미지입니다.
newimg.show()

# 이미를 조작하려면 픽셀 정보에 접근할 수 있게 만들어야 합니다.
pixels = image.load() #load 함수가 이미지와 픽셀을 연동해줌
newpxl = newimg.load()

# 이제 컬러 이미지를 회색조(grayscale)로 바꾸어 봅시다.
# 그냥 RGB 값의 평균을 이용해 보지요. 
for h in range(height):
    for w in range(width):
        col = int(sum(pixels[w, h])/3)
        newpxl[w, h] = col, col, col   # 원본파일에 그대로 두지 않고 새로운 파일을 만들어 바꿈

newimg.show()

# 이번에는 회색조 변환 알고리즘을 이용할 거예요.
# 핵심!!
for h in range(height):
    for w in range(width):
        r, g, b = pixels[w, h]
        gr = int(0.3*r + 0.59*g + 0.11*b)
        newpxl[w, h] = gr, gr, gr

# 회색조로 변환된 이미지를 확인해 보세요.
newimg.show()

# 흑백로로도 바꾸어 볼까요? 회색조는 흰색부터 검은색 사이에 회색을
# 배치하여 256단계로 만든 것인데요. 흑백은 흰색과 검은색만 있는 것이에요.
# 어디를 흰색과 검은색의 경계로 할지 마음대로 정해 보세요.
threshold = 128
for h in range(height):
    for w in range(width):
        r, g, b = pixels[w, h]
        gr = int(0.3*r + 0.59*g + 0.11*b)
        if gr < threshold :
            newpxl[w, h] = 0, 0, 0
        else :
            newpxl[w, h] = 255, 255, 255

# 흑백으로 변환된 이미지를 확인해 보세요. 
# 어떤가요? 마음에 드시나요? 
# 혹시 threshold 값에 대해 이견이 있으신가요?
newimg.show()

# 세피아 톤으로 바꾸어 보세요.
# 다음에 있는 sepia() 함수를 만들어서 실행해 보세요.
def sepia(red, green, blue):
    r_sep = 0.393*r + 0.769*g + 0.189*b
    g_sep = 0.349*r + 0.686*g + 0.168*b
    b_sep = 0.272*r + 0.534*g + 0.131*b

    r_sep = min(int(r_sep), 255)
    g_sep = min(int(g_sep), 255)
    b_sep = min(int(b_sep), 255)


    return r_sep, g_sep, b_sep

for h in range(height):
    for w in range(width):
        r, g, b = pixels[w, h]
        newpxl[w, h] = sepia(r, g, b)

newimg.show()


# 이번에 좀 어려운 것입니다.
# 모자이크를 만들어 볼 거예요.
# 일종의 구조를 가진 자료를 다루는 연습이라고 해 둘까요?
tile_height = 10
tile_width = 10

for h in range(int(height / tile_height)):
    for w in range(int(width / tile_width)):
        tile = []
        total = [0, 0, 0]
        for th in range(tile_height):
            for tw in range(tile_width):
                r, g, b = pixels[w*tile_width + tw, h*tile_height + th]
                total[0] += r
                total[1] += g
                total[2] += b
        n = (tile_height*tile_width)
        r = int(total[0] / n)
        g = int(total[1] / n)
        b = int(total[2] / n)
        for th in range(tile_height):
            for tw in range(tile_width):
                newpxl[w*tile_width + tw, h*tile_height + th] = r, g, b


# 확인해 보세요.
newimg.show()

# 파일로 저장할 수도 있습니다.
newimg.save("mandrill_mosaic.png", "PNG")



# 세피아 톤 변환 알고리즘이에요.
# 이걸 보지 말고 직접 만들어 보시면 좋겠죠.
def sepia(r, g, b):
        tr = 0.393*r + 0.769*g + 0.189*b
        tg = 0.349*r + 0.686*g + 0.168*b
        tb = 0.272*r + 0.534*g + 0.131*b

        tr = min(int(tr), 255)
        tg = min(int(tg), 255)
        tb = min(int(tb), 255)

        return (tr, tg, tb)
