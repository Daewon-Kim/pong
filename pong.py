import turtle as t

writer = t.Turtle()


class Object2D:
    def __init__(self, pos=[0,0], shape="square", width=2, height=2, dx=0, dy=0, color="white"):
        self.pos, self.shape, self.width, self.height = pos, shape, width, height
        self.dx, self.dy = dx, dy
        self.color = color


class Pong:
    def __init__(self):
        self.board_size = [800, 600]
        self.playerL = Object2D(pos=[-350, 0], shape="square", color = "white", dx=0.2, dy=0.2,width=4, height=1)
        self.playerR = Object2D(pos=[350, 0], shape="square" , color = "black" ,dx=0.2, dy=0.2, width=4, height=1)
        self.ball = Object2D(pos=[0,0], shape="circle", color="orange", dx=0.2, dy=0.2)

    # MEMBER-3/4
    # player move functions
    def playerL_up(self):
        self.playerL.pos[1] +=10
        writer.clear(); writer.write("playerL_up"+str(self.playerL.pos))

    def playerR_up(self):
        self.playerR.pos[1] += 10
        writer.clear(); writer.write("playerR_up"+str(self.playerR.pos))

    def playerL_down(self):
        self.playerL.pos[1] -= 10
        writer.clear(); writer.write("playerL_down"+str(self.playerL.pos))

    def playerR_down(self):
        self.playerR.pos[1] -= 10
        writer.clear(); writer.write("playerR_down"+str(self.playerR.pos))


class Simulate: #시각화
    def __init__(self, pong):
        self.pong = pong
        self.window = window = t.Screen()
        window.title("The Pong Game")
        window.bgcolor("green")
        window.setup(width=self.pong.board_size[0], height=self.pong.board_size[1])
        window.tracer(0)
        
        #self.ball = self.draw_obj(self.pong.ball)
        
        # MEMBER-2
        # Use the draw_obj() below to draw the ball and players/paddles.
        # e.g., self.ball = self.draw_obj(...)
        self.ball = self.draw_obj(self.pong.ball)
        self.playerL = self.draw_obj(self.pong.playerL)
        self.playerR = self.draw_obj(self.pong.playerR)
        self.window.update()
        self.bind_keys()

    def bind_keys(self): # 다 그려지면 windowonkey 함수 쓰면 됨 w = l down
        self.window.listen()
        # MEMBER-1
        # add four key-events: w,s keys: playerL_up:down, Up,Down arrows: PlayerR_up:down

        # e.g. self.window.onkey(<func_to_run>, <key:string>)
        self.window.onkey(self.pong.playerL, "w")
        self.window.onkey(self.pong.playerL, "s")
        self.window.onkey(self.pong.playerR, "Up")
        self.window.onkey(self.pong.playerR, "Down")

        # e.g. self.window.onkey(<func_to_run>, <key:string>) -> pointer


    def draw_obj(self, obj): #player;, plyerR ball 을 self 인수 받아서? #그려서 저장리턴
        ob = t.Turtle()
        ob.speed(0)
        ob.shape(obj.shape)
        ob.color(obj.color)
        ob.shapesize(obj.width, obj.height, 0)
        ob.penup()
        ob.goto(obj.pos[0], obj.pos[1])
        return ob


pong = Pong()
sim = Simulate(pong)
pong.playerL_up
t.done()

