import pygame
import os
import time
pygame.font.init()

Health_font = pygame.font.SysFont('poppins',35)
winner_font = pygame.font.SysFont('poppins',70)

width,height = 900,500 # game window width and height

#to set the display
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("My first game")

#global variables
win_color = (255,255,255)
FPS = 60
vel = 5 #ship moving speed
Bullet_speed = 8
MAX_BULLET = 4

shp_wid, shp_hgt = 50,50 #ship width and height

space = pygame.image.load(os.path.join('images','space.png'))

yel_spship = pygame.image.load(os.path.join('images','spaceship_yellow.png'))
yel_spship = pygame.transform.rotate(pygame.transform.scale(yel_spship,(shp_wid,shp_wid)),270)

red_spship = pygame.image.load(os.path.join('images','spaceship_red.png'))
red_spship = pygame.transform.rotate(pygame.transform.scale(red_spship,(shp_wid,shp_wid)),90)

#Middle Border or partition
border = pygame.Rect(width/2 - 5,0, 5,500)
pygame.display.update()

#userevents
red_hit = pygame.USEREVENT + 1
yellow_hit = pygame.USEREVENT + 2

#to generate the game window
def draw_game_window(yellow,red,red_bullets,yellow_bullets,red_health,yellow_health):

	window.blit(space,(0,0))
	#drawing the partition of 2 sides
	pygame.draw.rect(window,(0,0,0),border)

	red_health_text = Health_font.render("Health: "+str(red_health),1,(255,255,255))
	yellow_health_text = Health_font.render("Health: "+str(yellow_health),1,(255,255,255))
	window.blit(red_health_text,(width-red_health_text.get_width()-10,10))
	window.blit(yellow_health_text,(10,10))

	window.blit(yel_spship,(yellow.x,yellow.y))#yellow spaceship
	window.blit(red_spship,(red.x,red.y))#red spaceship

	for bullets in red_bullets:
		pygame.draw.rect(window,(255,0,0),bullets)

	for bullets in yellow_bullets:
		pygame.draw.rect(window,(255,255,0),bullets)

	pygame.display.update()

def position():
	yellow = pygame.Rect(700,300,shp_wid,shp_hgt)
	red = pygame.Rect(100,300,shp_wid,shp_hgt)

	return yellow,red

def redShip_movements(key_hit,red):
	if key_hit[pygame.K_a] and red.x - vel > 0 :
		red.x -= vel
	if key_hit[pygame.K_d] and red.x + vel + shp_wid< border.x - vel:
		red.x += vel
	if key_hit[pygame.K_w] and red.y - vel > 0:
		red.y -= vel
	if key_hit[pygame.K_s] and red.y + vel + shp_hgt < height:
		red.y += vel

def yellowShip_movements(key_hit,yellow):
	if key_hit[pygame.K_LEFT] and yellow.x - vel > border.x + border.width  :
		yellow.x -= vel
	if key_hit[pygame.K_RIGHT] and yellow.x + shp_wid < width:
		yellow.x += vel
	if key_hit[pygame.K_UP] and yellow.y - vel > 0:
		yellow.y -= vel
	if key_hit[pygame.K_DOWN] and yellow.y + vel + shp_hgt < height:
		yellow.y += vel

def bullet_handle(red_bullet,yellow_bullet,red,yellow):
	for bullet in red_bullet:
		bullet.x += Bullet_speed
		if yellow.colliderect(bullet):
			pygame.event.post(pygame.event.Event(yellow_hit))
			red_bullet.remove(bullet)
		elif bullet.x > width:
			red_bullet.remove(bullet)

	for bullet in yellow_bullet:
		bullet.x -= Bullet_speed
		if red.colliderect(bullet):
			pygame.event.post(pygame.event.Event(red_hit))
			yellow_bullet.remove(bullet)
		elif bullet.x < 0:
			yellow_bullet.remove(bullet)

def main():
	clock = pygame.time.Clock()
	run = True
	yellow,red = position()

	yellow_bullets = []
	red_bullets = []

	red_health = 15
	yellow_health = 15
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			#print(event.type,"This is the evnt"
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LSHIFT and len(red_bullets) < MAX_BULLET:
					bullets = pygame.Rect(red.x + red.width, red.y + red.height//2, 10,5)
					red_bullets.append(bullets)

				if event.key == pygame.K_RSHIFT and len(yellow_bullets) < MAX_BULLET:
					bullets = pygame.Rect(yellow.x, yellow.y+yellow.height//2,10,5)
					yellow_bullets.append(bullets)

			if event.type == yellow_hit:
				yellow_health -= 1
			if event.type == red_hit:
				red_health -= 1

		result = ""
		if red_health == 0:
			result = "Yellow Wins!!"
		elif yellow_health == 0:
			result = "Red Wins!!"

		if result != "":
			draw_result = winner_font.render(result,1,(255,255,255))
			window.blit(draw_result,(width/2 - draw_result.get_width()/2,height/2-draw_result.get_height()/2))
			pygame.display.update()
			pygame.time.delay(5000)
			break
			
		#to fill create the game window
		key_hit = pygame.key.get_pressed()
		redShip_movements(key_hit,red)
		yellowShip_movements(key_hit,yellow)

		bullet_handle(red_bullets,yellow_bullets,red,yellow)

		draw_game_window(yellow,red,red_bullets,yellow_bullets,red_health,yellow_health)

	pygame.quit()

	

if __name__ == "__main__":
	main()