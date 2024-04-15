from tkinter import*
import random
gw=500
gh=500
speed=70
space=50
parts=3
scolor='#41F30C'
fcolor='red'
bcolor='black'
class Snake:
    def __init__(self):
        self.bodysize=parts
        self.coordinates=[]
        self.squares=[]
        for i in range(0,parts):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square=cv.create_rectangle(x ,y , x+space,y+space,
                                       fill=scolor,tag='snake')
            self.squares.append(square)


class Food:
    def __init__(self):
        x=random.randint(0,(int(gw/space)-1))*space
        y=random.randint(0,(int(gh/space)-1))*space
        self.coordinates=(x,y)

        cv.create_oval(x,y,x+space,y+space,fill=fcolor,tag='food')
def next(snake,food):
    x,y= snake.coordinates[0]
    if direction=='up':
        y-=space
    elif direction=='down':
        y+=space
    elif direction=='right':
        x+=space
    elif direction=='left':
        x-=space
    snake.coordinates.insert(0,(x,y))
    square=cv.create_rectangle(x,y,x+space,y+space,fill=scolor)
    snake.squares.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text='Score:{}'.format(score))
        cv.delete('food')
        food=Food()
    else:
        del snake.coordinates[-1]
        cv.delete(snake.squares[-1])
        del snake.squares[-1]
    if collision(snake):
        over()
    else:
        ww.after(speed,next,snake,food)
def collision(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>gw:
        return True
    elif y<0 or y>gh:
        return True
    for parts in snake.coordinates[1:]:
        if x==parts[0] and y==parts[1]:
            return True
    return False
def change(new):
    global direction
    if new=='left':
        if direction!='right':
            direction=new
    if new=='right':
        if direction!='left':
            direction=new
    if new=='up':
        if direction!='down':
            direction=new
    if new=='down':
        if direction!='up':
            direction=new

def over():
    global maged
    maged=0
    cv.delete(ALL)
    cv.create_text(cv.winfo_width()/2,cv.winfo_height()/2,
                   font=('consolas',50),text='GAME OVER',fill='red',
                  tag='gameover' )

ww=Tk()
ww.title('Snake Game')
ww.resizable(False,False)
score=0
direction='down'
label=Label(ww,text='Score:{}'.format(score),font=('consolas',40))
label.pack()
cv=Canvas(ww,bg=bcolor,height=gh,width=gw)
cv.pack()
ww.update()
www=ww.winfo_width()
wwh=ww.winfo_height()
scrnw=ww.winfo_screenwidth()
scrnh=ww.winfo_screenheight()
x=int((scrnw/2)-(www/2))
y=int((scrnh/2)-(wwh/2))
ww.geometry(f"{www}x{wwh}+{x}+{y}")
ww.bind('<Left>',lambda event:change('left'))
ww.bind('<Right>',lambda event:change('right'))
ww.bind('<Up>',lambda event:change('up'))
ww.bind('<Down>',lambda event:change('down'))
snake=Snake()
food=Food()
next(snake,food)
ww.mainloop()

