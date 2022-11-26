def f(n,i):
    print(n,i)
    from PIL import Image, ImageDraw, ImageFont

    im = Image.new('RGB', (1000,1000), color=('#9ACD32'))
    font = ImageFont.truetype('C:/Users/student/Documents/142/Шредер/bahnschrift.ttf', size=50)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
    (100, 100),
    n,
    font=font,
    fill='#1C0606')
    #im.show()
    im.save(f'C:/Users/student/Documents/142/Шредер{i}.jpg')
    print(f'C:/Users/student/Documents/142/Шредер{i}.jpg')

i = ['Я уважаю только двух людей',
    'Гагарина и Ньютона',
    'Один попытался улететь с этой планеты',
    'а второй доказал, что у первого ничего не выйдет.']
for n in range (4):
    f(i[n],n)
