# pady/x Отступ по Х или У сверху/ сбоку
# radiobutton- класс позволяющий выбрать только одно значение
#chekbutton - Класс для создания кнопок-флагов
#BooleanVar - класс координирующий значения флагов
#onvalue, offvalue - включение кнопок


# Импорт модулей
from tkinter import *

root = Tk()

def collect_data():
    """Собирает, обрабатывает и сохраняет дату в базу данных"""
    data = {}
    
    print(data)
    
    
    
    
# Функция для текста
def open_text():
    text_frame.pack(side=TOP, anchor=W, pady=10)

    lbl_name.grid(row=0, column=0, sticky=E)
    ent_name.grid(row=0, column=1, sticky=W, padx=10)

    lbl_bdate.grid(row=1, column=0, sticky=E)
    ent_bdate.grid(row=1, column=1, sticky=W, padx=10)


def open_radio():
    radio_frame.pack(side=TOP, anchor=W, padx=10)

    lbl_sex.pack(side=TOP, anchor=W)
    male.pack(side=LEFT, anchor=W)
    female.pack(side=LEFT, anchor=W)

def create_flag(name):
    """Проектирует флаги"""
    boolean = BooleanVar()
    boolean.set(0)
    flag = Checkbutton(master=interest_frame, text=name, variable=boolean,
                       onvalue=1, offvalue=0)
    return flag, boolean

def open_flags():
    interest_frame.pack(side=TOP, anchor=W,pady=10)

    interest_lbl.pack(side=TOP,anchor=W)


    i=0
    while i < len(flags):
        flags[i].pack(side=TOP, anchor=W)
        i += 1

def open_buttons():
    but_frame.pack(side=TOP, pady=10)

    but_data.pack(side=RIGHT,padx=10)
    but_close.pack(side=RIGHT, padx=10, pady=10)


radio_frame = Frame(master=root)

lbl_sex = Label(master=radio_frame, text="Выберите пол:")

var = IntVar()
var.set(0)
male = Radiobutton(master=radio_frame, text="Мужской", variable=var, value=0)
female = Radiobutton(master=radio_frame, text="Женский", variable=var, value=1)

# Установка основного окна
root.title("Регистрация пользователя")

# Окно с текстом
text_frame = Frame(master=root)

lbl_name = Label(master=text_frame, text="Введите ФИО:")
ent_name = Entry(master=text_frame)

lbl_bdate = Label(master=text_frame, text="Введите дату рождения:")
ent_bdate = Entry(master=text_frame)


#Окно выборов интересов - флаги
interest_frame = Frame(master=root)

interest_lbl = Label(master=interest_frame, text='Выберите интересы:')
interest_names = "Наука","Техника","Искусство", "Спорт", "Путешествие","Другое"

#Создание лагов
flag_sc, bool_sc = create_flag(name=interest_names[0])
flag_tech, bool_tech = create_flag(name=interest_names[1])
flag_art, bool_art = create_flag(name=interest_names[2])
flag_tr, bool_tr = create_flag(name=interest_names[3])
flag_sp, bool_sp = create_flag(name=interest_names[4])
flag_an, bool_an = create_flag(name=interest_names[5])
#писок флагов и их булево значение
flags = flag_sc, flag_tech, flag_art, flag_tr, flag_sp, flag_an
booleans_interest = bool_sc, bool_tech, bool_art, bool_tr, bool_sp, bool_an

#Создание кнопок
but_frame = Frame(master=root)

#Кнопки действий
but_data = Button(master=but_frame, text='ЖМЯК', width=10, command=collect_data)
but_close = Button(master=but_frame, text='Закрой меня', width = 10, command=root.destroy)

# Активируем функцию
open_text()
open_radio()
open_flags()
open_buttons()
# Функции развертывания
root.mainloop()