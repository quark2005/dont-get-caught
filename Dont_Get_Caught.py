import time, pygame, math
pygame.display.set_caption("Dont Get Caught")

###############
## VARIABLES ##
###############

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (155, 0, 155)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

game_over = False
g_score = 0
count = g_score
high_score = 0

player_left_y = 10
player_left_x = 10
player_height = 30
player_width = 30
player_speed = 10


opponent_left_y = 500
opponent_left_x = 500
opponent_height = 30
opponent_width = 30
opponent_speed = 6

added_size = 0

obstacle_center_y =  100
obstacle_center_x = 500 
obstacle_radius = 25 
obstacle_speed = 6



###############
##   DRAW    ##
###############

def draw_player():
    global player_left_y, player_left_x
    global player

    player = Rect((player_left_x, player_left_y), (30,30))
    screen.draw.filled_rect(player, GREEN)

def draw_opponent():
    global opponent_left_y, opponent_left_x, opponent_width, opponent_height, opponent_speed
    global opponent
    global added_size
    global count
    
    if count == 5:
        opponent_width += 2
        opponent_height += 2
        added_size += 2
        count = 0
            
    opponent = Rect((opponent_left_x, opponent_left_y), (opponent_width, opponent_height))
    screen.draw.filled_rect(opponent, RED)

def draw_obstacle():
    global obstacle_center_y, obstacle_center_x, obstacle_radius
    global count

    if count == 5:
        radius += 2
        count = 0

    obstacle = ((obstacle_center_x, obstacle_center_y), obstacle_radius)
    screen.draw.filled_circle(obstacle, PURPLE)
    
    

###############
##   MOVE    ##
###############
def move_player():
    global player_left_y, player_left_x, player_speed

    if keyboard.down:
        pygame.display.flip()
        player_left_y += player_speed
        if player_left_y > 570:
            player_left_y = 570

    elif keyboard.up:
        pygame.display.flip()
        player_left_y -= player_speed
        if player_left_y < 0:
            player_left_y = 0

    elif keyboard.right:
        pygame.display.flip()
        player_left_x += player_speed
        if player_left_x > 770:
            player_left_x = 770

    elif keyboard.left:
        pygame.display.flip()
        player_left_x -= player_speed
        if player_left_x < 0:
            player_left_x = 0

def move_opponent():
    global opponent_left_y, opponent_left_x, opponent_speed
    global added_size
    global player_left_y, player_left_x

    make_center = (2 + added_size) / 2

    if opponent_left_y - make_center  > player_left_y:
        pygame.display.flip()
        opponent_left_y -= opponent_speed

    if opponent_left_y - make_center < player_left_y:
        pygame.display.flip()
        opponent_left_y += opponent_speed

    if opponent_left_x - make_center > player_left_x:
        pygame.display.flip()
        opponent_left_x -= opponent_speed

    if opponent_left_x - make_center < player_left_x:
        pygame.display.flip()
        opponent_left_x += opponent_speed


def score():
    global game_over
    global g_score, high_score, count
    
    if game_over == False:
        g_score += 1
        count += 1

def show_score():
    global g_score, high_score

    if game_over == False:
        show_text("Score = " + str(g_score) +"   ||||   High score = " + str(high_score), 0)

        
def caught():
    global opponent_left_y, opponent_left_x, opponent_height, opponent_width
    global player_left_y, player_left_x, player_height, player_width
    global game_over
    global g_score, high_score
    global player
    global opponent
    
    pygame.display.flip
    if pygame.Rect.colliderect(player, opponent):
        show_text("GAME_OVER! ------- Score = " + str(g_score)+"   ||||   High score = " + str(high_score), 0)
        game_over = True
    
    

    
def reset():
    global opponent_left_y, opponent_left_x, opponent_height, opponent_width, opponent_speed
    global player_left_y, player_left_x
    global g_score, high_score
    global game_over

    if keyboard.r:
        player_left_y = 10
        player_left_x = 10
        opponent_left_y = 500
        opponent_left_x = 500
        opponent_height = 30
        opponent_width = 30
        if g_score > high_score:
            high_score = g_score
        g_score = 0         

def show_text(text_to_show, line_number):
    text_lines = [15, 50]
    screen.draw.text(text_to_show,
                      (20, text_lines[line_number]), color=BLACK)

def game_loop():
    global opponent_left_y, opponent_left_x
    global player_left_y, player_left_x
    global game_over

    if opponent_left_x == player_left_x and opponent_left_y == player_left_y:
        game_over = True
    else:
        game_over = False

    screen.fill(WHITE)

    draw_player()
    draw_opponent()
    draw_obstacle()
    caught()
    show_score()
    if game_over == False:
        move_player()
        move_opponent()
    reset()
    
    if keyboard.q:
        pygame.quit()
        
clock.schedule_interval(game_loop, 0.03)
clock.schedule_interval(score, 1)




