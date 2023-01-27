# в PyChame не работает, в Collab тоже (что-то не так)
from PIL import Image, ImageDraw  # для PIL нужно было установить pillow

# создать новое изображение
img = Image.new('RGB', (780, 340), 'white') # палитра, размер, чем заполнить
draw = ImageDraw.Draw(img)                  # объект (поле для рисования)

data = '1101110001101011000111111'      # как бы набор битов
for x in range(5):
    for y in range(5):
        if data[x + y * 5] == '1':
            draw.rectangle((x*10, y*10, x*10 + 9, y*10 + 9), fill='black')  # рисуем черным

# градиентная серая линия
for i in range(255):    # шкала серого
    draw.rectangle((i*3, 60, i*3+2, 70), fill=(i, i, i))    # red = green = blue --> grey

for x in range(255):    # цветные кубики с градиентом
    for y in range(255):
        draw.point((x      , y + 80), fill=(x, 0, y))
        draw.point((x + 260, y + 80), fill=(y, x, y))
        draw.point((x + 520, y + 80), fill=(y, y, x))

