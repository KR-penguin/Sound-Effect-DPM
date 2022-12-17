import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Sound Effect DPM")

Background = pygame.image.load("./image/Background.png")

background_X_pos = 0
background_Y_pos = 0

ClickBox1 = pygame.image.load("./image/ClickBox.png")
ClickBox2 = pygame.image.load("./image/ClickBox.png")
ClickBox3 = pygame.image.load("./image/ClickBox.png")
ClickBox4 = pygame.image.load("./image/ClickBox.png")
ClickBox5 = pygame.image.load("./image/ClickBox.png")
ClickBox6 = pygame.image.load("./image/ClickBox.png")
ClickBox7 = pygame.image.load("./image/ClickBox.png")
PauseBox = pygame.image.load("./image/PauseBox.png")
OffBox = pygame.image.load("./image/OffBox.png")

MusicTitle1 = pygame.font.Font(None, 15)
MusicTitle2 = pygame.font.Font(None, 15)
MusicTitle3 = pygame.font.Font(None, 15)
MusicTitle4 = pygame.font.Font(None, 15)
MusicTitle5 = pygame.font.Font(None, 15)
MusicTitle6 = pygame.font.Font(None, 15)
MusicTitle7 = pygame.font.Font(None, 15)
Turnoff = pygame.font.Font(None, 15)
Pause = pygame.font.Font(None, 15)

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_1: 
                sound = pygame.mixer.Sound("./Sound Effect/Snow White Whistle While You Work Instrumental.mp3")
                for x in range(1):
                    sound.play(0)
            elif event.key == pygame.K_3: 
                sound = pygame.mixer.Sound("./Sound Effect/reload gun sound effects.mp3")
                for x in range(1):
                    sound.play(0)
            elif event.key == pygame.K_5: 
                sound = pygame.mixer.Sound("./Sound Effect/George Michael  Careless Whisper Official Video.mp3")
                for x in range(1):
                    sound.play(0)
            elif event.key == pygame.K_7: 
                sound = pygame.mixer.Sound("./Sound Effect/Gallop by SGAK Id-467749.wav")
                for x in range(1):
                    sound.play(0)
            elif event.key == pygame.K_a: 
                sound = pygame.mixer.Sound("./Sound Effect/코난브금.mp3")
                for x in range(1):
                    sound.play(0)
            elif event.key == pygame.K_d: 
                sound = pygame.mixer.Sound("./Sound Effect/명탐정코난 우우우 브금.mp3")
                for x in range(1):
                    sound.play(0)
            elif event.key == pygame.K_g: 
                sound = pygame.mixer.Sound("./Sound Effect/경찰서 가고 싶어.mp3")
                for x in range(1):
                    sound.play(0)

            
            if event.key == pygame.K_SPACE:
                sound.stop()
            elif event.key == pygame.K_x:
                running = False

    ClickBox1Title = MusicTitle1.render((str("White Princess [1]")), True, (255, 255, 255))
    ClickBox2Title = MusicTitle1.render((str("Reload Gun [3]")), True, (255, 255, 255))
    ClickBox3Title = MusicTitle1.render((str("Sexy BGM [5]")), True, (255, 255, 255))
    ClickBox4Title = MusicTitle1.render((str("Horse [7]")), True, (255, 255, 255))
    ClickBox5Title = MusicTitle1.render((str("Conan [a]")), True, (255, 255, 255))
    ClickBox6Title = MusicTitle1.render((str("UUU~ [d]")), True, (255, 255, 255))
    ClickBox7Title = MusicTitle1.render((str("Police [g]")), True, (255, 255, 255))
    PauseBoxTitle = MusicTitle1.render((str("Stop [space]")), True, (255, 255, 255))
    OffBoxTitle = MusicTitle1.render((str("Shutdown [x]")), True, (255, 255, 255))

    screen.blit(Background, (0, 0))
    
    screen.blit(ClickBox1, (0, 0))
    screen.blit(ClickBox2, (170, 0))
    screen.blit(ClickBox3, (340, 0))
    screen.blit(ClickBox4, (0, 150))
    screen.blit(ClickBox5, (170, 150))
    screen.blit(ClickBox6, (340, 150))
    screen.blit(ClickBox7, (0, 300))
    screen.blit(PauseBox, (170, 300))
    screen.blit(OffBox, (340, 300))

    screen.blit(ClickBox1Title, (80, 90))
    screen.blit(ClickBox2Title, (270, 90))
    screen.blit(ClickBox3Title, (430, 90))
    screen.blit(ClickBox4Title, (80, 250))
    screen.blit(ClickBox5Title, (270, 250))
    screen.blit(ClickBox6Title, (430, 250))
    screen.blit(ClickBox7Title, (80, 400))
    screen.blit(PauseBoxTitle, (270, 400))
    screen.blit(OffBoxTitle, (430, 400))

    pygame.display.update() 

pygame.quit()