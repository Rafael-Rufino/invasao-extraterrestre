import pygame, sys

pygame.init()
#pygame.joystick.init()

  	

#imagens
fundo = pygame.image.load("imagens/plano.png")
nave = pygame.image.load("imagens/1.png")
mostro = pygame.image.load("imagens/et.png")
bala = pygame.image.load("imagens/bala.png")
bala2= pygame.image.load("imagens/bala2.png")
bl= pygame.image.load("imagens/bl.png")
explosão = pygame.image.load("imagens/exp.png")
lifecheio= pygame.image.load("imagens/lifecheio.png")
lifemeio= pygame.image.load("imagens/lifemeio.png")
lifevazio= pygame.image.load("imagens/lifevazio.png")
explo= pygame.image.load("imagens/3.png")
explo2= pygame.image.load("imagens/4.png")
tela_menu= pygame.image.load("imagens/menu2.png")

fim = pygame.image.load("imagens/menu4.png")


inter = bala2
preto=(0,0,0)
audio = pygame . mixer . Sound ( 'imagens/alienv.wav' )
cor = (255,255, 255)
titulo_font = pygame.font.SysFont("Arial Rounded MT", 45)
menu_titulo = titulo_font.render("Jogar", True, (0,255,255))

nave.set_colorkey((-0,-0,-0))
mostro.set_colorkey((0,0,0))
bala.set_colorkey((0,0,0))
bala2.set_colorkey((0,0,0))
lifecheio.set_colorkey((0,0,0))
lifemeio.set_colorkey((0,0,0))
lifevazio.set_colorkey((0,0,0))
explo.set_colorkey((0,0,0))
explo2.set_colorkey((0,0,0))
placar = 0
life =lifecheio
contador =0
branco = (255,255,0)

#LARGURA E ALTURA
life_x = 10
life_y =0

nave_x = 664
nave_y = 460




bala_x = 250
bala_y = 490

bala2_x = 0
bala2_y = 0


explosão_x = 0
explosão_y = 0

mostroo = [mostro]
mostro_x = [664]
mostro_y = [30]

#velocidade 
vel_x = 4
vel_y =5

velocidade_x = 5.70
velocidade_y = 10




velocidadeBala_x = 0
velocidadeBala_y = 12



size = largura, altura = 1324, 550
display = pygame.display.set_mode(size)
pygame.display.set_caption("invasão extraterrestre")
disparo = pygame.mixer.Sound("imagens/Bala.wav")

menu = True

pygame.init()
while True:

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


            elif event.type == pygame.MOUSEBUTTONDOWN:
               if event.button == 1:
                    menu = False

        pygame.display.update()
        display.blit(tela_menu, (0, 0))
        display.blit(menu_titulo, (628, 430))












    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if contador > 0:
        contador += 1

    def texto(msg, cor, tam, x, y):
        font = pygame.font.SysFont("Arial Black", tam)
        texto1 = font.render(msg, True, cor)
        fundo.blit(texto1, [x, y])



#comando usado para MOVER o objeto pelo teclado
    keys = pygame.key.get_pressed()
    #joystick = pygame.joystick.Joystick(0)
    #joystick.init()
    if keys[pygame.K_LEFT]:# or joystick.get_button(4):
        nave_x -= velocidade_x
    if keys[pygame.K_RIGHT]:# or joystick.get_button(5):
        nave_x += velocidade_x
    if bala_y < 0:
        bala_y = 470
    if bala_y < 470:
        bala_y -= 20
    
#mover pelo controle ps2

 

#bala monstro
    if bala2_y > 520:
        bala2_y = 60
    if bala2_y > 520:
        bala2_y -= 20

    for i in range(0,len(mostro_x)):
      if mostro_x[i] + nave_x > 100:


# disparo.play()
        bala2_y += velocidadeBala_y
        velocidadeBala_x = 0
        if bala2_y >524:
            bala2 = bl
            bala2_x = mostro_x[i]+10

        else:
            bala2 = inter
 









#placar
    pygame.draw.rect(fundo, (0,0,255), [172, altura - 544, 161, 18])
    texto("score: " + str(placar),(cor),16,220,altura - 547)

#bala

    if keys[pygame.K_SPACE] and life!=lifevazio:# or joystick.get_button(2):
        disparo.play()
        bala_y -= velocidade_y
        bala_x = nave_x + 42
        display.blit(bala, (bala_x, bala_y))
        
    titulo_font = pygame.font.SysFont("Arial Rounded MT", 30)
    fimjogo = titulo_font.render("                   Parabéns, seu  score é: " + str(placar)+" Pontos", True, ( 0,255,255))
    fimjogo2 = titulo_font.render("Que pena, você não salvou a terra, se esforce e tente novamente!  " + str(placar) + " Pontos", True, (0, 255, 255))
    if placar>0:   
        fim2 = fimjogo
    else:
        fim2 = fimjogo2

#colisão
    for i in range(len(mostro_x)-1,-1,-1):
       if abs(bala_y - mostro_y[i]) < 30 and abs(mostro_x[i] - bala_x) < 30 and mostroo[i] == mostro:
          mostroo[i] = explosão     
          mostro_x.append(664)
          mostro_y.append(30)
          mostroo.append(mostro)
          contador = 1
          placar +=10

       if (mostroo[i] != mostro and contador == 0):
           contador=1

       #print(mostroo, mostro_x, mostro_y)         
       if contador > 15 and mostroo[i] != mostro:
          contador=0
          del mostroo[i]
          del mostro_x[i]
          del mostro_y[i]





     
         
          




    if abs(bala2_y - nave_y) < 10 and abs(nave_x - bala2_x+50) < 50:
        bala2_y = 60
        nave = explo
        if life == lifemeio:
           life = lifevazio


        elif life == lifecheio:
           life =lifemeio

        
    
        

#ATIRAR


    #nave limit
    if nave_x >= 1235:
        nave_x = 1235
    if nave_x <= 5:
        nave_x = 5





    if life!=lifevazio:
        display.blit(fundo, (0, 0))
        display.blit(nave, (nave_x, nave_y))
        display.blit(life, (life_x, life_y))
        display.blit(bala2, (bala2_x, bala2_y))
        display.blit(mostroo[i], (mostro_x[i], mostro_y[i]))

    else:
        display.blit(fim, (0, 0))
        velocidadeBala_y = velocidade_x = vel_x = 0
        bala2_y = 600
        display.blit(fim2, (375, 400))
        




    if bala_y < 470:

       display.blit(bala, (bala_x, bala_y))

    if bala2_y > 10:

       display.blit(bala2, (bala2_x, bala2_y))


    for i in range(0,len(mostro_x)):

        pygame.display.flip()
        #audio.play()

#mover o objeto movimentar
    for i in range(0,len(mostro_x)):
      if mostroo[i] != explosão:
          mostro_x[i] += vel_x
      if mostro_x[i]>= largura-50 or mostro_x[i]<= 0:
          vel_x = -vel_x














