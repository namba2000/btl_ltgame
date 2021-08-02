import pygame

# khởi tạo game
pygame.init()

# thiết lập màn hình
screen = pygame.display.set_mode((600,415))
# tiêu đề
pygame.display.set_caption('Mario_run_run')

# thiết lập màu
W = (255, 255, 255)
B = (255, 0, 0)

# thiết lập tọa độ và chèn ảnh nhân vật, hình nền

# hình nền
bg_x = 0
bg_y = 30
bg = pygame.image.load('backg.png')

# mario
mario_x = 30
mario_y = 305
mario = pygame.image.load('mario.png')

# cây - trướng ngại vật
flower_x = 550
flower_y = 285
flower = pygame.image.load('flower.png')

# thiết lập âm thanh
sound_jump = pygame.mixer.Sound('tick.wav')
sound_accident = pygame.mixer.Sound('te.wav')

running = True
jump = False
pausing = False

# tốc độ của tọa độ
x_velocity = 5
y_velocity = 7

clock = pygame.time.Clock()

score = 0
font = pygame.font.SysFont('san' ,40)

while running:
	# nháy 60 lần/s
	clock.tick(60)
	screen.fill(B)
	score_text = font.render("Score: " + str(score), True, W)
	screen.blit(score_text, (255,5))
# Đưa hình vào app
	# màn hình cho background
	bg_rect_1 = screen.blit(bg, (bg_x,bg_y))
	bg_rect_2 = screen.blit(bg, (bg_x + 600,bg_y)) # background 2 nối tiếp background 1
	if bg_x + 600 <= 0:
		bg_x = 0
	## chuyển cảnh background
	bg_x = bg_x - x_velocity

	# màn hình cho cây
	flower_rect = screen.blit(flower, (flower_x,flower_y))
	if flower_x <= -20:
		flower_x = 550
		score += 1
	## chuyển cảnh cho cây
	flower_x = flower_x - x_velocity

	# màn hình cho mario
	mario_rect = screen.blit(mario, (mario_x,mario_y))
	## nhảy
	if 305 >= mario_y >= 140:
		if jump == True:
			mario_y = mario_y - y_velocity
	else:
		jump = False
	## xuống
	if mario_y < 305:
		if jump == False:
			mario_y = mario_y + y_velocity

	## mario chạm cây
	if mario_rect.colliderect(flower_rect):
		pausing = True
		gameover_text = font.render("GAME OVER", True, W)
		screen.blit(gameover_text, (200,200))
		x_velocity = 0
		y_velocity = 0
		#pygame.mixer.Sound.play(sound_accident)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if mario_y == 305:
					#pygame.mixer.Sound.play(sound_jump)
					jump = True
				if pausing:
					bg_x = 0
					bg_y = 30
					mario_x = 30
					mario_y = 305
					flower_x = 550
					flower_y = 285
					x_velocity = 5
					y_velocity = 7
					score = 0
					pausing = False
	pygame.display.flip()
pygame.quit()

