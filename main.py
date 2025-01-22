from tkinter import *
from PIL import Image, ImageTk
import math
from itertools import count
from tkinter import messagebox


class ImageLabel(Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []
        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()
    def unload(self):
        self.config(image="")
        self.frames = None
    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

W = Tk()
W.geometry('600x540+200+100')
W.title('Cats adventure')

lbl = ImageLabel(W)
lbl.pack()
lbl.load('main.gif')

l1 = PhotoImage(file='l1.png')
l2 = PhotoImage(file='l2.png')
l3 = PhotoImage(file='l3.png')
l4 = PhotoImage(file='l4.png')

r1 = PhotoImage(file='r1.png')
r2 = PhotoImage(file='r2.png')
r3 = PhotoImage(file='r3.png')
r4 = PhotoImage(file='r4.png')

u1 = PhotoImage(file='u1.png')
u2 = PhotoImage(file='u2.png')
u2 = PhotoImage(file='u2.png')
u3 = PhotoImage(file='u3.png')
u4 = PhotoImage(file='u4.png')

d1 = PhotoImage(file='d1.png')
d2 = PhotoImage(file='d2.png')
d3 = PhotoImage(file='d3.png')
d4 = PhotoImage(file='d4.png')

d = [[l1,l2,l3,l4],[r1,r2,r3,r4],[d1,d2,d3,d4],[u1,u2,u3,u4]]

p_cat = l1
d_count = 1
speed = 5

p_c1 = PhotoImage(file='Gifts2.gif')
p_c2 = PhotoImage(file='Gifts3.png')
p_c3 = PhotoImage(file='Box1.png')
p_c4 = PhotoImage(file='Box2.png')
p_W4 = PhotoImage(file='W4.png')

p_present = p_c2
p_bad = PhotoImage(file='p_bad.png')
p_Pin = PhotoImage(file='Pin.png')

w_gift = 100
h_gift = 100

w_win = 600
h_win = 540

f1 = ('Times New Roman', '14')
f2 = ('Times New Roman', '10')

c1 = Label(W, image=p_c1, borderwidth=0)
c1.place(x=w_win//5-w_gift//2, y=h_win//5-h_gift//2, width=w_gift, height = h_gift)

c2 = Label(W, image=p_c2, borderwidth=0)
c2.place(x=w_win//5-w_gift//2, y=h_win//5*4-h_gift//2, width = w_gift, height = h_gift)

c3 = Label(W, image=p_c3, borderwidth=0)
c3.place(x=w_win//5*4-w_gift//2, y=h_win//5-h_gift//2, width = w_gift, height = h_gift)

c4 = Label(W, image=p_c4, borderwidth=0)
c4.place(x=w_win//5*4-w_gift//2, y=h_win//5*4-h_gift//2, width = w_gift, height = h_gift)

cat = Label(W, image=p_cat, borderwidth=0)
cat.place(x=w_win//5*3-w_gift//2, y=h_win//5*3-h_gift//2, width = 64, height = 64)

b_c1 = False
b_c2 = False
b_c3 = False
b_c4 = False

def on_close():
    if messagebox.askokcancel('Выход', 'С Наступившим Новым Годом!'):
        W.destroy()

def first_f():

    def f1():
        ans = E2.get()
        text = ''
        if ans.lower() == 'да':
            text = 'Это же тот, о котором ты мечтал!'
            present = p_present
            W2 = Toplevel(W)
            W2.geometry('690x384+1200+100')
            W2.title('Подарок')
            W2.resizable(False, False)
            lb = ImageLabel(W2)
            lb.pack()
            lb.load('p_present.gif')

        elif ans.lower() == 'нет':
            text = 'К сожалению, подарок бесполезный('
            present = p_bad

        L3 = Label(W1, image=present, borderwidth=0)
        L3.place(x=300, y=540, width=100, height=100)

        L4 = Label(W1, text=text, font=f1, fg='red')
        L4.place(x=0, y=165, width=400, height=30)

        L4 = Label(W1, text=f'С Новым Годом,{E1.get()}!', font=f1, fg='red')
        L4.place(x=0, y=200, width=400, height=30)

    W1 = Toplevel(W)
    W1.geometry('700x700+800+100')
    W1.title('Подарок')
    W1.resizable(False, False)

    lbl = ImageLabel(W1)
    lbl.pack()
    lbl.load('Pin.gif')

    Q1 = Label(W1, text='КАК ВАС ЗОВУТ? ', font=f1, bg='white', fg='red')
    Q1.place(x=10, y=10, width=250, height=40)

    E1 = Entry(W1, font=f1, fg='black')
    E1.place(x=270, y=10, width=100, height=40)

    Q2 = Label(W1, text='ВЫ ХОРОШО ВЕЛИ СЕБЯ В ЭТОМ ГОДУ? ', font=f2, fg='red')
    Q2.place(x=10, y=65, width=250, height=40)

    E2 = Entry(W1, font=f1, fg='black')
    E2.place(x=270, y=65, width=100, height=40)

    B1 = Button(W1, text='Проверить под ёлкой', fg='red', font=f2, command=f1)
    B1.place(x=10, y=130, width=150, height=30)

def second_f():

    def f2():
        answr = int(E1W2.get())
        if answr <= 100:
            L2W2 = Label(W2, text='вам хватит двух коробок игрушек', font=f1, bg='white')
            L2W2.place(x=5, y=170, width=290, height=40)
        elif answr >= 100 and answr <= 150:
            L3W2 = Label(W2, text='вам хватит трех коробок игрушек', font=f1, bg='white',
                         anchor='w')
            L3W2.place(x=5, y=170, width=290, height=40)
        elif answr >= 150 and answr <= 200:
            L3W2 = Label(W2, text='вам хватит четырех коробок игрушек', font=f1,
                         bg='white', anchor='w')
            L3W2.place(x=5, y=170, width=290, height=40)
        elif answr >= 200:
            L4W2 = Label(W2, text='Елка не влезет в дом!', font=f1, bg='white',
                         anchor='w')
            L4W2.place(x=5, y=170, width=290, height=40)

    W2 = Toplevel(W)
    W2.geometry('320x320+0+680')
    W2.title('Наряжаем елку')
    W2.resizable(False, False)

    L1W2 = Label(W2, image=p_Pin, borderwidth=0)
    L1W2.place(x=0, y=0, width=300, height=265)

    Q1W2 = Label(W2, text='КАКАЯ ВЫСОТА У ВАШЕЙ ЕЛКИ? ', font=f2, fg='red')
    Q1W2.place(x=0, y=10, width=300, height=40)

    E1W2 = Entry(W2, font=f1, fg='red')
    E1W2.place(x=10, y=65, width=80, height=40)

    Q2W2 = Label(W2, text='CМ', font=f1, fg='red')
    Q2W2.place(x=100, y=65, width=40, height=40)

    B1W2 = Button(W2,text='Расчёт игрушек', fg='red', font=f1, command=f2)
    B1W2.place(x=140, y=65, width=140, height=40)

def third_f():
    W3 = Toplevel(W)
    W3.geometry('300x265+330+680')
    W3.title('Ёлочка - гори')
    W3.resizable(False, False)

    L1 = Label(W3, image=p_W4, borderwidth=0)
    L1.place(x=0, y=0, width=320, height=320)

    Q1W3 = Label(W3, text='КАКОЙ ЦВЕТ?', font=f1, fg='red')
    Q1W3.place(x=10, y=10, width=140, height=40)

    E1W3 = Entry(W3, font=f1, fg='black')
    E1W3.place(x=160, y=10, width=130, height=40)

    def f3():
        col = E1W3.get().lower()
        if col == 'красный':
            L2W3 = Label(W3, text='следующим идет СИНИЙ', font=f1, bg='white',
                         anchor='w')
            L2W3.place(x=10, y=110, width=290, height=40)
        elif col == 'синий':
            L3W3 = Label(W3, text='следующим идет ГОЛУБОЙ', font=f1, bg='white')
            L3W3.place(x=10, y=110, width=290, height=40)
        elif col== 'голубой':
            L3W3 = Label(W3, text='следующим идет КРАСНЫЙ', font=f1, bg='white')
            L3W3.place(x=10, y=110, width=290, height=40)

    B1W3 = Button(W3, text='CЛЕДУЮЩИЙ', fg='red', font=f1, command=f3)
    B1W3.place(x=10, y=60, width=170, height=40)

def fourth_f():

    def f4():
        amt = int(E1W4.get())
        k = math.ceil((3 * amt + 3) / 4)
        count = k * 690
        L2W4 = Label(W4, text=f'Расходы на салаты: {count} руб.', font=f1, bg='white')
        L2W4.place(x=10, y=110, width=250, height=40)

    W4 = Toplevel(W)
    W4.geometry('320x320+660+680')
    W4.title('Чем гостей-то кормить?')
    W4.resizable(False, False)

    L1 = Label(W4, image=p_W4, borderwidth=0)
    L1.place(x=0, y=0, width=320, height=320)

    Q1W4 = Label(W4, text='СКОЛЬКО БУДЕТ ГОСТЕЙ?', font=f1, fg='red')
    Q1W4.place(x=10, y=10, width=250, height=40)

    E1W4 = Entry(W4, font=f1, fg='black')
    E1W4.place(x=270, y=10, width=40, height=40)

    B4 = Button(W4, text='Узнать стоимость', fg='red', font=f1, command=f4)
    B4.place(x=10, y=60, width=250, height=40)

def leftkey(e):
    animation(0,-1,0)
    check()

def rightkey(e):
    animation(1,1,0)
    check()

def downkey(e):
    animation(2, 0,1)
    check()

def upkey(e):
    animation(3,0, -1)
    check()

def check():
    global w_gift, h_gift, b_c1, b_c2, b_c3, b_c4
    x = cat.winfo_x()
    y = cat.winfo_y()

    if 32 + w_gift // 2 >= abs(x + 32 - c1.winfo_x() - w_gift // 2) and 32 + h_gift // 2 >= abs(y + 32 - c1.winfo_y() - h_gift // 2) and b_c1 == False:
        b_c1 = True
        first_f()
    elif 32 + w_gift // 2 >= abs(x + 32 - c2.winfo_x() - w_gift // 2) and 32 + h_gift // 2 >= abs(y + 32 - c2.winfo_y() - h_gift // 2) and b_c2 == False:
        b_c2 = True
        second_f()
    elif 32 + w_gift // 2 >= abs(x + 32 - c3.winfo_x() - w_gift // 2) and 32 + h_gift // 2 >= abs(y + 32 - c3.winfo_y() - h_gift // 2) and b_c3 == False:
        b_c3 = True
        third_f()
    elif 32 + w_gift // 2 >= abs(x + 32 - c4.winfo_x() - w_gift // 2) and 32 + h_gift // 2 >= abs(y + 32 - c4.winfo_y() - h_gift // 2) and b_c4 == False:
        b_c4 = True
        fourth_f()

def animation(n,dx,dy):
    global d_count, d, speed, h_win, w_win
    d_count += 1
    if d_count > 3:
        d_count = 1
    cat['image'] = d[n][d_count]

    x = cat.winfo_x()
    y = cat.winfo_y()

    if x > w_win:
        x=0-64
    elif y > h_win:
        y=0-64
    elif x < -64:
        x = w_win
    elif y < -64:
        y = h_win

    cat.place(x=x + dx*speed, y=y + dy*speed)

W.protocol('WM_DELETE_WINDOW', on_close)

W.bind('<Left>', leftkey)
W.bind('<Right>', rightkey)
W.bind('<Down>', downkey)
W.bind('<Up>', upkey)

W.mainloop()
