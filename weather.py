from tkinter import *

import requests 

root = Tk()

#pip install requests для работы с url  https://api. .org/data/2.5/weather?q={city name}&appid={API key}
#https://api.openweathermap.org/data/2.5/weather?q=London&appid={API key}
#f'Данные: {str(login)}, {str(password)}'
#f5184fc7d16d04d53af8d1ceebfcb7a0     my
#82b797b6ebc625032318e16f1b42c016     not my
def get_weather():
    city = cityField.get()

    key = 'f5184fc7d16d04d53af8d1ceebfcb7a0'
    url = 'http://openweathermap.org/data/2.5/weather'   #f   ?q={str(city)}&appid={str(key)}
    params1 = {'APPID': key, 'q': city, 'units': 'metric'}    #словарь 
    result = requests.get(url, params=params1)
    ###result = requests.get(url) 
    weather = result.json()

    print(weather)       

root['bg']='#fafafa'
root.title('Погодное приложение')
root.geometry('300x250')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

root.mainloop()  
