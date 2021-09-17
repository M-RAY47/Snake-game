from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

	def __init__(self):
		self.tails = []
		self.create_snake()
		self.head = self.tails[0]

	def create_snake(self):
		for position in STARTING_POSITIONS:
			new_tail = Turtle(shape="square")
			new_tail.color("white"), new_tail.penup()
			new_tail.goto(position)
			self.tails.append(new_tail)

	def move(self):
		for tail_num in range(len(self.tails)-1, 0, -1):
			new_x = self.tails[tail_num-1].xcor()
			new_y = self.tails[tail_num-1].ycor()
			self.tails[tail_num].goto(new_x, new_y)
		self.head.fd(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)
