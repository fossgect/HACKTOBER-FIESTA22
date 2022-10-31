import pygame
import time
import random

pygame.init()
pygame.mixer.init()
DIM=(600,360)
screen=pygame.display.set_mode(DIM)
pygame.display.set_caption("FLAPPY BIRD")
PATH=r"gameit\Flappy"

bg1=pygame.image.load("gameit/static/AnjanaPR/background.png")
bg2=pygame.image.load("gameit/static/AnjanaPR/background.png")
bg1_x,bg1_y=0,0
bg2_x,bg2_y=0,0
bg1c=True
bg2c=False
bg_vel=2

bird_sprite=[pygame.image.load(PATH+r"\upstroke.png"),pygame.image.load(PATH+r"\upstroke.png"),pygame.image.load(PATH+r"\upstroke.png"),pygame.image.load(PATH+r"\midstroke.png"),pygame.image.load(PATH+r"\midstroke.png"),pygame.image.load(PATH+r"\midstroke.png"),pygame.image.load(PATH+r"\downstroke.png"),pygame.image.load(PATH+r"\downstroke.png"),pygame.image.load(PATH+r"\downstroke.png"),pygame.image.load(PATH+r"\bottomstroke.png"),pygame.image.load(PATH+r"\bottomstroke.png"),pygame.image.load(PATH+r"\bottomstroke.png")]
pipe=[pygame.image.load(PATH+r"\pipe_down.png"),pygame.image.load(PATH+r"\pipe_up.png"),pygame.image.load(PATH+r"\pipe.png")]
jumpSound=pygame.mixer.Sound(PATH+r"\moosic\sfx_wing.wav")
pointSound=pygame.mixer.Sound(PATH+r"\moosic\sfx_point.wav")
dieSound=pygame.mixer.Sound(PATH+r"\moosic\sfx_die.wav")
hitSound=pygame.mixer.Sound(PATH+r"\moosic\sfx_hit.wav")
threshold=0.05
now=time.time()
l={"space":now}
clock=pygame.time.Clock()
FPS=80
points=0
MAIN=True
RUN=False
n=0
oldpoints=0
def flappy():
	global MAIN,RUN, points
	class Bird():
		def __init__(self):
			self.X=DIM[0]//4
			self.y=DIM[1]//2
			self.Y=0
			self.down_vel=10
			self.up_vel=3
			self.stroke_stage=0
			self.Fly=False
			self.x=15
			self.x1=1
			self.width=bird_sprite[0].get_width()
			self.height=bird_sprite[0].get_height()

		def draw(self):
			stage=bird_sprite[self.stroke_stage]
			screen.blit(stage,(self.X,self.y))
			self.stroke_stage+=1
			if self.stroke_stage>=11:
				self.stroke_stage=0
		def move(self):
			if not (self.Fly):
				self.y+=(self.x1**2)*0.005
				self.x1+=1

		def fly(self):
			if self.Fly:
				if self.x==15:
					jumpSound.play()
				neg=1
				if self.x<0:
					neg=-1
				self.y-=(self.x**2)*0.05*neg
				self.x-=1
				if self.y>=self.Y:
					allowed=True
					self.Fly=False
					self.x=15
					self.x1=self.x
					neg=1
					self.y=self.Y


	class Pipe():
		def __init__(self,x):
			self.x=x
			self.headlength=pipe[0].get_height()
			self.bodylength=pipe[2].get_height()
			self.width=pipe[0].get_width()
			self.GAP=10
			self.dblocks,self.upblocks,self.y1,self.y2=self.noOfBlocks()
			self.ext=14
			self.vel=2

		def noOfBlocks(self):
			ndown=random.randint(1,12)
			y1=self.bodylength*ndown
			rem_height=DIM[1]-(y1+self.headlength+self.GAP+self.headlength)
			nup=rem_height//self.bodylength
			y2=DIM[1]-self.bodylength*nup+self.headlength
			return ndown,nup,y1,y2


		def draw(self):
			screen.blit(pipe[0],(self.x,self.y1))
			screen.blit(pipe[1],(self.x,self.y2))
			r1=range(0,self.y1,self.bodylength)
			r2=range(self.y2+self.headlength,DIM[1],self.bodylength)
			for pipes_y1 in r1:
				screen.blit(pipe[2],(self.x,pipes_y1))
			for pipes_y2 in r2:
				screen.blit(pipe[2],(self.x,pipes_y2))
		def move(self):
			global points
			self.x-=self.vel+points//50

	def checkCollision():
		global n,points,oldpoints
		for pipes in pipe_array:
			if bird.X<=pipes.x+pipes.width-pipes.ext:

				if bird.X+bird.width>=pipes.x+pipes.ext and bird.X<=pipes.x+pipes.width-pipes.ext:
						if bird.y<=pipes.y1+pipes.headlength or bird.y+bird.height>=pipes.y2:
							hitSound.play()
							return True
				break			
			else:
				points=n+len(pipe_array[:pipe_array.index(pipes)+1])
				if points-oldpoints==1:
					pointSound.play()
					oldpoints=points
				continue




	def draw_bg():
		global bg1c,bg2c,bg1_x,bg2_x
		if bg1c:
			screen.blit(bg1,(bg1_x,bg1_y))
			bg1_x-=bg_vel

		if bg1_x+bg1.get_width()<DIM[0]:
			bg2c=True
			bg2_x=bg1_x+bg1.get_width()
		if bg1_x+bg1.get_width()<=0:
			bg1c=False
			bg1_x=bg2_x+bg2.get_width()
		if bg2c:
			screen.blit(bg2,(bg2_x,bg2_y))
			bg2_x-=bg_vel
		if bg2_x+bg2.get_width()<=0:
			bg2c=False
			bg2_x=bg1_x+bg1.get_width()

		if bg2_x+bg2.get_width()<DIM[0]:
			bg1c=True
			bg1_x=bg2_x+bg2.get_width()
		

	def checkpressed(key):
		global threshold,l,now
		if key[pygame.K_SPACE]:
			now=time.time()
		if l["space"]==None or now-l["space"]>threshold:
			l["space"]=now
			return True
		else:
			return False

	def displayPoints():
		global points
		#print(points,"there")
		font=pygame.font.Font("freesansbold.ttf",20)
		point=font.render(f"POINTS:{points}",True,(255,0,255))
		screen.blit(point,(DIM[0]//2,0))
	def drawgameScreen():
		global n
		draw_bg()
		bird.draw()
		displayPoints()

		for pipes in pipe_array:
			
			if pipes.x+pipes.width<0:

				pipe_array.remove(pipes)
				n+=1
				pipe_array.append(Pipe(pipe_array[len(pipe_array)-1].x+170))
			pipes.draw()
		displayPoints()
		pygame.display.update()

	def checkFall():
		if bird.y>=DIM[1]:
			dieSound.play()
			return True
		else:
			return False

	


	while MAIN:
		pipe_array=[Pipe(DIM[0]+i*170) for i in range(10)]
		
		bird=Bird()
		font=pygame.font.Font("freesansbold.ttf",20)
		point=font.render(f"PRESS SPACE TO START",True,(255,0,255))
		screen.blit(point,(DIM[0]//3,DIM[1]//2))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				MAIN=False
				pygame.quit()
		key=pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			RUN=True
			MAIN=False
		pygame.display.update()
		while RUN:

			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					RUN=False
					pygame.quit()
			key=pygame.key.get_pressed()
			bird.move()
			if checkpressed(key):
				bird.Fly=True
				bird.Y=bird.y
				allowed=False
			bird.fly()
			for pipes in pipe_array:
				pipes.move()

			drawgameScreen()
			if checkCollision() or checkFall():

				RUN=False
				MAIN=True
				points=0
				n=0
				pygame.time.delay(1000)
			clock.tick(FPS)
	
if __name__=="__main__":
	flappy()
	pygame.quit()
