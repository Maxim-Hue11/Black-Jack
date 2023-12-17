import tkinter as tk
import random
from settings import *

def click():
    global score
    button.configure(text = 'Бери ещё карту!!!')
    while True:
        key = random.choice(list(cards.keys()))
        texts.append(key)
        score += (cards[key])
        break
    print(texts)
    lb_spis.configure(text = texts)
    lb_score.configure(text = score)
    
def deleted():
    global score
    texts.clear()
    lb_spis.configure(text = 'У тебя не существуют карты!')
    score = 0
    lb_score.configure(text = 0)

win = tk.Tk()
win.title('Опа карты')
win.geometry(f"{W}x{H}")


cards = {'тузик': 11,
               'Десятка': 10,
               'Королище': 4,
               'Мадмуазель': 3,
               'Волонтёр': 2,
               'Девятка': 9,
               'Восьмёрик': 8,
               'Семя': 7,
               'Шестёрик': 6,
               }

score = 0

texts = []

button = tk.Button(bg = COLOR_Lavender, fg = COLOR_Violet,font = ('Times New Roman',12), text = "Взять Карту/ Начать игру", command=lambda: click())
button.place(x = 70, y = 60, width = 230, height = 80)

button_2 = tk.Button(bg = COLOR_Lavender, fg = COLOR_Violet,font = ('Times New Roman',12),text = 'Руку брось!',command=lambda: deleted())
button_2.place(x = 70,y = 160, width = 230, height = 80)


lb = tk.Label(text='Список карт:', fg = COLOR_Lavender, font = ('Times New Roman',15))
lb.place(x = 80,y = 250)

lb_spis = tk.Label(text= texts, fg = COLOR_Lavender, font = ('Times New Roman',10))
lb_spis.place(x = 75,y = 275)

lb_score_sum = tk.Label(text='Очки:', fg = COLOR_Lavender, font = ('Times New Roman',15))
lb_score_sum.place(x = 80,y = 300)

lb_score = tk.Label(text= score, fg = COLOR_Lavender, font = ('Times New Roman',10))
lb_score.place(x = 75,y = 327)

win.mainloop()