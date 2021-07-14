import tm1637
import datetime
import sched, time
import argparse

pars = argparse.ArgumentParser(description='Hello!')
pars.add_argument('intz', metavar='1 or 0', type=int, #nargs='+',
help='1 to start watches, 0 to turn display off')
args = pars.parse_args()
print(f"ARGUMENT: {args.intz}")
print(("turning display off...", "start watches... OK")[args.intz])
displ = tm1637.TM1637(clk=3, dio=2)

s = sched.scheduler(time.time, time.sleep)

def show_time():
        tm = datetime.datetime.now().time()
        tm_s = str(tm)[:5].split(":")
        displ.numbers(int(tm_s[0]), int(tm_s[1]))
        s.enter(60, 1, show_time)

displ = tm1637.TM1637(clk=3, dio=2)
s = sched.scheduler(time.time, time.sleep)

displ.brightness(2)
func_list = [lambda : displ.write([0,0,0,0]), show_time]

func_list[args.intz]()
s.run()

