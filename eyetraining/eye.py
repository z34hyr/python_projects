from tkinter import *
import random
import math

window = Tk()
wid = window.winfo_screenwidth()
hei = window.winfo_screenheight()
window.title("Eye trainer")
window.iconphoto(False, PhotoImage(file='./eye.png'))
ball_width = 40.0
speed = [1000, 5000, 200, 100] # [0] - current speed, [1] - max speed, [2] - min speed, [3] - step

x_center = wid/2
y_center = hei/2
r = 100.0
r_sign = 1
x_curr = 0.0
y_curr = r
way_global = 1

x_sign = 1
y_sign = 1
step = 0.2
coord_x = 0
coord_y = 0

angle = 0
rotation = 1

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
	mode[current_mode](rotation)
	c.coords(circle, coord_x, int(coord_y), coord_x + ball_width, int(coord_y + ball_width))
	window.after(current_speed, loop)

def lclick(event):
	print("leftclick")

def change_speed(sign):
	after_change = speed[0] + speed[3] * sign
	#speed[0] = speed[0] + speed[3] * sign if speed[1] >= (speed[0] + speed[3] * sign) >= speed[2] else speed[0] # another way
	speed[0] = (speed[0], after_change)[speed[1] >= after_change >= speed[2]] # ternary operator
	check_mode()
	print(f"speed: {speed[0]} milliseconds")

def check_mode():
	global current_speed
	if (current_mode == 0): # random mode, must execute slower
		current_speed = speed[0]
	else:
		current_speed = speed[0] // 100
		c.itemconfig(letter, text="")


# use key 1..9 on keyboard to change mode
def some_key(event):
	global current_mode
	global rotation
	if event.char:
		key = ord(event.char)
		if key == 27: # esc
			window.destroy()
		if key == 43: # +
			change_speed(-1)
		if key == 45: # -
			change_speed(1)
		if 49 + len(mode) > key >= 49: # 1..9
			current_mode = key - 49
			check_mode()
		if key == 114: # r - change direction of rotation
			rotation *= -1

def random_mode(way = 1):
	global x_curr
	global y_curr
	global i_letter
	global i_phrase
	global coord_x
	global coord_y
	x_curr = random.randint(0, int(wid - ball_width * 2))
	y_curr = random.randint(0, int(hei - ball_width * 2))
	coord_x = x_curr
	coord_y = y_curr
	c.coords(letter, coord_x + ball_width/2, coord_y + ball_width/2)
	c.itemconfig(letter, text=phrase[i_phrase][0][i_letter])
	i_letter += 1
	if i_letter == phrase[i_phrase][1]:
		i_letter = 0
		i_phrase = random.randint(0, len(phrase) - 1)

def move_by_full_circle(way = 1):
	global x_curr
	global y_curr
	global x_sign
	global y_sign
	global coord_x
	global coord_y
	global angle
	global current_speed

	rad_angle = math.radians(angle)
	x_curr = way_global * math.cos(rad_angle) * r
	y_curr = math.sin(rad_angle) * r
	angle += 1 * way
	coord_x = x_curr + x_center
	coord_y = y_curr + y_center

def move_by_lhalf_circle(way = 1):
	global x_curr
	global y_curr
	global x_sign
	global y_sign
	global coord_x
	global coord_y
	global angle

	rad_angle = math.radians(angle)
	x_curr = math.cos(rad_angle) * r
	y_curr = abs(math.sin(rad_angle) * r)
	angle += 1 * way
	coord_x = x_curr + x_center
	coord_y = y_curr + y_center

def move_by_uhalf_circle(way = 1):
	global x_curr
	global y_curr
	global x_sign
	global y_sign
	global coord_x
	global coord_y
	global angle

	rad_angle = math.radians(angle)
	x_curr = math.cos(rad_angle) * r
	y_curr = - abs(math.sin(rad_angle) * r)
	angle += 1 * way
	coord_x = x_curr + x_center
	coord_y = y_curr + y_center

def move_by_spiral(way = 1):
	global x_curr
	global y_curr
	global x_sign
	global y_sign
	global coord_x
	global coord_y
	global angle
	global r
	global r_sign

	rad_angle = math.radians(angle)
	x_curr = way_global * math.cos(rad_angle) * r
	y_curr = math.sin(rad_angle) * r
	angle += 1 * way
	r += r_sign * step
	if (r <= 0 or r > 300):
		r_sign *= -1
		r += r_sign * step
	coord_x = x_curr + x_center
	coord_y = y_curr + y_center
	return r

def move_by_inf_symbol(way = 1):
	global angle
	global x_center
	global way_global
	global x_curr
	global x_sign
	move_by_full_circle(way)
	if (angle % 360 == 0):
		way_global *= -1
		x_center += (2*r, -2*r)[way_global == 1]

def mouse_pos(event):
	print("x:%s y:%s" % (event.x, event.y))

c = Canvas(window, width=wid, height=hei, bg='green')
c.pack()
circle = c.create_oval(wid/2, hei/2, ball_width, ball_width,
				fill='yellow',
				width=1)

current_mode = 1
# functions list
mode = [random_mode, move_by_full_circle, move_by_lhalf_circle, move_by_uhalf_circle, move_by_spiral, move_by_inf_symbol]
letter = c.create_text(wid/2 + ball_width/2, wid/2 + ball_width, text = phrase[i_phrase][0][i_letter], tags = "text")
check_mode()
window.configure(width=wid, height=hei, bg="black", )
window.bind('<Button-1>', lclick)
window.bind('<KeyPress>', some_key)
window.after(0, loop)
window.mainloop()
