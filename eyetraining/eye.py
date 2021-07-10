from tkinter import *
import random

window = Tk()
wid = window.winfo_screenwidth()
hei = window.winfo_screenheight()
ball_width = 40
speed = [700, 2000, 200, 100] # [0] - current speed, [1] - max speed, [2] - min speed, [3] - step

phrase = [["ничтонеистинавсёдозволено", 0],
		["молчитдуракзаумногосойдет", 0],
		["пулядурааштыкмолодец", 0],
		["дареномуконювзубынесмотрят", 0],
		[""" Впрочем, нас интересует отнюдь не история алчности, 
а вполне конкретная фраза, неоднократно звучавшая в \"Кредо ассасина\". 
Ее авторство приписывается основателю движения низаритов Хасану ибн Саббаху. 
Вот только к анархии и беспринципности она не имеет никакого отношения. 
Первая ее часть, \"ничто не истинно\" указывает на зыбкость догматов социума,
проистекающих из позабытых традиций, суеверий, привычек, 
общественного мнения. Саббах считал, что лишь сам человек способен 
выстроить свое будущее, а это невозможно, если постоянно оглядываться 
на окружающих. \"Все дозволено\", в свою очередь, означает полное 
принятие ответственности за свои действия и собственную судьбу. 
Никто не способен ограничить человека в его поступках, 
кроме него самого: каждый из нас может стать тем, кем хочет. 
Главное - понять, где кончаются желания других и начинаются 
ваши собственные, ведь только они имеют значение.""", 0] ]
for i in range(0, len(phrase)):
	phrase[i][1] = len(phrase[i][0])
i_letter = 0
i_phrase = 4

def loop():
	global i_letter
	global i_phrase
	x0 = random.randint(0, int(wid - ball_width * 2))
	y0 = random.randint(0, int(hei - ball_width * 2))

	c.coords(circle, x0, y0, x0 + ball_width, y0 + ball_width)
	c.coords(letter, x0 + ball_width/2, y0 + ball_width/2)
	i_letter += 1
	if i_letter == phrase[i_phrase][1]:
		i_letter = 0
		i_phrase = random.randint(0, len(phrase) - 1)
	c.itemconfig(letter, text=phrase[i_phrase][0][i_letter])
	window.after(speed[0], loop)

def lclick(event):
	print("leftclick")

def change_speed(sign):
	after_change = speed[0] + speed[3] * sign
	#speed[0] = speed[0] + speed[3] * sign if speed[1] >= (speed[0] + speed[3] * sign) >= speed[2] else speed[0]
	speed[0] = (speed[0], after_change)[speed[1] >= after_change >= speed[2]] # ternary operator
	print(speed[0])

def some_key(event):
	if event.char:
		key = ord(event.char)
		if key == 27:
			window.destroy()
		if key == 43:
			change_speed(1)
		if key == 45:
			change_speed(-1)

#def print_esc(event):
#	print("ESC!")	

def mouse_pos(event):
	print("x:%s y:%s" % (event.x, event.y))

c = Canvas(window, width=wid, height=hei, bg='green')
c.pack()
circle = c.create_oval(wid/2, hei/2, ball_width, ball_width,
				fill='yellow',
				width=1)
letter = c.create_text(wid/2 + ball_width/2, wid/2 + ball_width, text = phrase[i_phrase][0][i_letter], tags = "text")
window.configure(width=wid, height=hei, bg="black", )
window.bind('<Button-1>', lclick)
window.bind('<KeyPress>', some_key)
window.after(0, loop)
window.mainloop()
