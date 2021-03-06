### below is the full project, where the functions and data are all in one place

import pygame
pygame.init()
import time
from datetime import datetime

black     = (  0,   0,   0)
white     = (255, 255, 255)
darkgray  = ( 64,  64,  64)
gray      = (128, 128, 128)
lightgray = (212, 208, 200)
green = (0,255,0)
lightgreen = (0,250,154)
red = (255,0,0)
blue = (30,144,255)
lightblue = (0,191,250)
yellow = (150,150,0)
display_width = 1000
display_height = 600

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont('calibri',25)
mediumfont = pygame.font.SysFont('calibri',50)
largefont = pygame.font.SysFont('calibri',80)

appDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('NTUeat')

foodtype = pygame.image.load('Final_food.PNG')
canteenlist = pygame.image.load('canteen_list.PNG')

def mouseclick():
    finish = False
    while finish == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    print(mouseX,mouseY)
                    finish = True
    return (mouseX,mouseY)

def text_objects(text,color,size):
    if size == 'small':
        textsurface = smallfont.render(text,True,color)
    elif size == 'medium':
        textsurface = mediumfont.render(text,True,color)
    elif size == 'large':
        textsurface = largefont.render(text,True,color)
    return textsurface, textsurface.get_rect()

def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size):
    textsurf, textrect = text_objects(msg,color,size)
    textrect.center = ((buttonx +(buttonwidth/2)), buttony+(buttonheight/2))
    appDisplay.blit(textsurf,textrect)
    

def message_to_screen(msg,color,y_displace,size):
    textsurf, textrect = text_objects(msg,color,size)
    textrect.center = (display_width/2),(display_height/2)+ y_displace
    appDisplay.blit(textsurf,textrect)

def button(text,x,y,width,height,inactive_color,active_color):
    a = 0
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cur[0] > x and y+height > cur[1] > y:
        pygame.draw.rect(appDisplay,active_color,(x,y,width,height))
        if click[0] == 1:
            a= 1
            
    else:
        pygame.draw.rect(appDisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height,'small')
    return a

def trans_button(text,x,y,width,height,inactive_color,active_color):
    a = 0
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cur[0] > x and y+height > cur[1] > y:
        s = pygame.Surface((width,height))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill(active_color)           # this fills the entire surface
        appDisplay.blit(s, (x,y))    # (0,0) are the top-left coordinates
        
        if click[0] == 1:
            a= 1
            
    else:
        s = pygame.Surface((width,height))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill(inactive_color)           # this fills the entire surface
        appDisplay.blit(s, (x,y))    # (0,0) are the top-left coordinates
    text_to_button(text,black,x,y,width,height,'small')
    return a

def trans_button_special(color,text,x,y,width,height,inactive_color,active_color): #for opening time
    a = 0
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cur[0] > x and y+height > cur[1] > y:
        s = pygame.Surface((width,height))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill(active_color)           # this fills the entire surface
        appDisplay.blit(s, (x,y))    # (0,0) are the top-left coordinates
        
        if click[0] == 1:
            a= 1
            
    else:
        s = pygame.Surface((width,height))  # the size of your rect
        s.set_alpha(128)                # alpha level
        s.fill(inactive_color)           # this fills the entire surface
        appDisplay.blit(s, (x,y))    # (0,0) are the top-left coordinates
    text_to_button(text,color,x,y,width,height,'small')
    return a

def app_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        appDisplay.fill(white)
        message_to_screen('Welcome to NTUeat',blue,0,'large')
        pygame.display.update()
        intro = False
        



def choosehalal(): #choose if halal
    keeploop = True
    halal = False
    while keeploop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        appDisplay.fill(white)
        message_to_screen('Choose halal preference?',darkgray,-200,'medium')


        a = button('Halal',250,300,200,100,green,lightgreen)
        b = button('Non-halal',550,300,200,100,blue,lightblue)
        
        pygame.display.update()
        clock.tick(15)
        if a == 1 or b == 1:
            if a == 1:
                halal = True            
            keeploop = False
    return halal

def check_halal(foodlist_canteens):   #change foodlist canteen to all halal
    halal_foodlist_canteens = {}
    for i in foodlist_canteens.keys():
        halal_foodlist_canteens[i] = [{}, foodlist_canteens[i][1],foodlist_canteens[i][2]]
        for y,z in foodlist_canteens[i][0].items():
            if z[0] == 1:
                halal_foodlist_canteens[i][0][y] = z
    
    return halal_foodlist_canteens

def nothalalbuttons(): #food menu for non halal
    a = None
    korean = trans_button('',0,0,198,140,white,lightgreen)
    drinks = trans_button('',200,0,198,140,white,lightgreen)
    thai = trans_button('',400,0,198,140,white,lightgreen)
    japanese = trans_button('',600,0,198,140,white,lightgreen)
    indian = trans_button('',800,0,198,140,white,lightgreen)
    chinese = trans_button('',0,143,198,140,white,lightgreen)
    pasta = trans_button('',200,143,198,140,white,lightgreen)
    mixedrice = trans_button('',400,143,198,140,white,lightgreen)
    burger = trans_button('',600,143,198,140,white,lightgreen)
    chickenrice = trans_button('',800,143,198,140,white,lightgreen)
    western = trans_button('',0,283,198,140,white,lightgreen)
    pizza = trans_button('',200,283,198,140,white,lightgreen)
    muslim = trans_button('',400,283,198,140,white,lightgreen)
    indonesian = trans_button('',600,283,198,140,white,lightgreen)
    sandwiches = trans_button('',800,283,198,140,white,lightgreen)
    yongtaufoo = trans_button('',0,426,198,140,white,lightgreen)
    vietnamese = trans_button('',200,426,198,140,white,lightgreen)
    mala = trans_button('',400,426,198,140,white,lightgreen)
    bakery = trans_button('',600,426,198,140,white,lightgreen)
    nil = button('nil',800,426,198,140,white,lightgreen)
    pygame.display.update()
    clock.tick(15)
    if nil == 1 or korean == 1 or drinks == 1 or thai == 1 or japanese == 1 or indian == 1 or chinese == 1 or pasta == 1 or mixedrice == 1 or burger == 1 or chickenrice == 1 or western == 1 or pizza == 1 or muslim == 1 or indonesian == 1 or sandwiches == 1 or yongtaufoo == 1 or vietnamese == 1 or mala == 1 or bakery == 1:
        if korean == 1:
            a = 'korean'
        elif drinks == 1:
            a = 'drinks'
        elif thai == 1:
            a = 'thai'
        elif japanese == 1:
            a = 'japanese'
        elif indian == 1:
            a = 'indian'
        elif chinese == 1:
            a = 'chinese'
        elif pasta == 1:
            a = 'pasta'
        elif mixedrice == 1:
            a = 'mixed rice'
        elif burger == 1:
            a = 'burgers'
        elif chickenrice == 1:
            a = 'chicken rice'
        elif western == 1:
            a = 'western'
        elif pizza == 1:
            a = 'pizza'
        elif muslim == 1:
            a = 'muslim'
        elif indonesian == 1:
            a = 'indonesian'
        elif sandwiches == 1:
            a = 'sandwich'
        elif yongtaufoo == 1:
            a = 'yong tau foo'
        elif vietnamese == 1:
            a = 'vietnamese'
        elif mala == 1:
            a = 'mala'
        elif bakery == 1:
            a = 'bakery'
        elif nil == 1:
            a = 'nil'
    return a

def halalbuttons(): #food menu for halal
    a = None
    drinks = trans_button('',200,0,198,140,white,lightgreen)
    japanese = trans_button('',600,0,198,140,white,lightgreen)
    indian = trans_button('',800,0,198,140,white,lightgreen)
    mixedrice = trans_button('',400,143,198,140,white,lightgreen)
    burger = trans_button('',600,143,198,140,white,lightgreen)
    chickenrice = trans_button('',800,143,198,140,white,lightgreen)
    western = trans_button('',0,283,198,140,white,lightgreen)
    pizza = trans_button('',200,283,198,140,white,lightgreen)
    muslim = trans_button('',400,283,198,140,white,lightgreen)
    indonesian = trans_button('',600,283,198,140,white,lightgreen)
    sandwiches = trans_button('',800,283,198,140,white,lightgreen)
    yongtaufoo = trans_button('',0,426,198,140,white,lightgreen)
    bakery = trans_button('',600,426,198,140,white,lightgreen)
    nil = button('nil',800,426,198,140,white,lightgreen)
    pygame.display.update()
    clock.tick(15)
    if nil == 1 or drinks == 1 or japanese == 1 or indian == 1 or mixedrice == 1 or burger == 1 or chickenrice == 1 or western == 1 or pizza == 1 or muslim == 1 or indonesian == 1 or sandwiches == 1 or yongtaufoo == 1 or bakery == 1:
        if drinks == 1:
            a = 'drinks'
        elif japanese == 1:
            a = 'japanese'
        elif indian == 1:
            a = 'indian'
        elif mixedrice == 1:
            a = 'mixed rice'
        elif burger == 1:
            a = 'burgers'
        elif chickenrice == 1:
            a = 'chicken rice'
        elif western == 1:
            a = 'western'
        elif pizza == 1:
            a = 'pizza'
        elif muslim == 1:
            a = 'muslim'
        elif indonesian == 1:
            a = 'indonesian'
        elif sandwiches == 1:
            a = 'sandwich'
        elif yongtaufoo == 1:
            a = 'yong tau foo'
        elif bakery == 1:
            a = 'bakery'
        elif nil == 1:
            a = 'nil'
    return a


def chooseprice(): #choose the price of the food
    keeploop = True
    price = 0
    while keeploop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        appDisplay.fill(white)
        message_to_screen('Choose the price range of the food',darkgray,-200,'medium')
        message_to_screen('$ is $0 to $5',darkgray,-150,'small')
        message_to_screen('$$ is $5 to $10',darkgray,-120,'small')
        message_to_screen('$$$ is $10 to $20',darkgray,-90,'small')
        message_to_screen('$$$$ is $20 to $30',darkgray,-60,'small')


        one = button('$',75,350,120,100,green,lightgreen)
        two = button('$$',325,350,120,100,green,lightgreen)
        three = button('$$$',575,350,120,100,green,lightgreen)
        four = button('$$$$',825,350,120,100,green,lightgreen)

        
        pygame.display.update()
        clock.tick(15)
        if one == 1 or two == 1 or three == 1 or four == 1:
            if one == 1:
                price = 1
            elif two == 1:
                price = 2
            elif three == 1:
                price = 3
            elif four == 1:
                price = 4
            keeploop = False
    return price

def search_by_food(foodname,foodlist_canteens):
    correct_canteens_food = []
    for x in foodlist_canteens.keys():
        if foodname in foodlist_canteens[x][0].keys():
            correct_canteens_food.append(x)
    return correct_canteens_food


def search_food_and_price(foodname,price,foodlist_canteens):
    correct_canteens_food = search_by_food(foodname,foodlist_canteens)
    temp_dict = {}
    for i in correct_canteens_food:
        temp_dict[i]= foodlist_canteens[i] #dictionaries of canteens with the input foodtype
    correct_canteens_food_and_price = []
    for x in temp_dict.keys():
        for y,z in temp_dict[x][0].items():
            if y == foodname:
                if price == z[1]:
                    correct_canteens_food_and_price.append(x)
    if len(correct_canteens_food_and_price) == 0: #if no price that matches foodtype, return all the canteens with the food type
        for x in temp_dict.keys():
            for y,z in temp_dict[x][0].items():
                if y == foodname:
                    correct_canteens_food_and_price.append(x)
    return correct_canteens_food_and_price

def choosefood(if_halal): #choose the menu of the food
    keeploop = True
    foodname = None
    while keeploop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        appDisplay.blit(foodtype,(0,0))
        pygame.display.update()
        clock.tick(60)
        if if_halal == True:
            foodname = halalbuttons()
        else:
            foodname = nothalalbuttons()
        if foodname != 0 and foodname != None:
            keeploop = False

    return foodname

    

def search_by_price(price,foodlist_canteens):
    correct_canteens_price = []
    for x in foodlist_canteens.keys():
        for y,z in foodlist_canteens[x][0].items():
            if price == z[1]:
                if x not in correct_canteens_price:
                    correct_canteens_price.append(x)
    return correct_canteens_price

def foodpriceselect(foodlist_canteens): #choosing  from halal until price
    keeploop = True
    while keeploop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if_halal = choosehalal()
        if if_halal == True:
            foodlist_canteens = check_halal(foodlist_canteens)

        time.sleep(1)
        foodname = choosefood(if_halal) #choose the foodtype
        time.sleep(1)
                
        price = chooseprice() #choose the price

        if foodname != 'nil':
            canteen_list = search_food_and_price(foodname,price,foodlist_canteens) #filter the canteens
        else:
            canteen_list = search_by_price(price,foodlist_canteens)
        keeploop = False
    return canteen_list,foodname


def choosesatisfaction(): #if the food is good or not
    keeploop = True
    satisfaction = 0
    while keeploop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        appDisplay.fill(white)
        message_to_screen('Is the food awesome?',green,-200,'medium')
        awesome = button(':)',230,350,120,100,green,lightblue)
        notawesome = button(':(',650,350,120,100,green,lightblue)
        
        pygame.display.update()
        clock.tick(15)
        if awesome == 1 or notawesome == 1:
            if awesome == 1:
                satisfaction = 1
            keeploop = False
    return satisfaction
        
def update_information(database,canteen,food,halal,price,satisfaction): #update foodlist canteens
    value = []
    value.append(halal)
    value.append(price)
    if satisfaction == 1:
        value.append(':)')
    database[canteen][0][food] = value
    return database
    
def inputcanteen(): #enter name of canteen
    font = pygame.font.Font(None, 43)
    input_box = pygame.Rect(300,300, 400, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:

                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        appDisplay.fill(white)
        appDisplay.blit(canteenlist,(0,0))
        message_to_screen('enter the name of the canteen',blue,-200,'medium')
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        appDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(appDisplay, color, input_box, 2)

        pygame.display.update()
        clock.tick(30)
    return text

def enterinfo(foodlist_canteens): #update info only
    canteen = inputcanteen()
    print(canteen)
    time.sleep(1)
    if_halal = choosehalal()
    if if_halal == True:
        foodlist_canteens = check_halal(foodlist_canteens)
        halal = 1
    elif if_halal == False:
        halal = 0
    time.sleep(1)
    food = choosefood(if_halal)
    time.sleep(1)
    price = chooseprice()
    time.sleep(1)
    satisfaction = choosesatisfaction()
    time.sleep(1)
    return update_information(foodlist_canteens,canteen,food,halal,price,satisfaction)

def full_enterinfo(foodlist_canteens): #to update info, taking into consideration of invalid input
    try:
        foodlist_canteens = enterinfo(foodlist_canteens)     
        appDisplay.fill(white)
        message_to_screen('Information updated!',lightgray,-200,'large')
        pygame.display.update()
        

    except :
        appDisplay.fill(white)
        message_to_screen('Please enter a valid canteen',lightgray,-200,'large')
        message_to_screen('take note of the case of text',lightgray,0,'medium')
        pygame.display.update()
    
    return foodlist_canteens
############################################################################

from math import sqrt
        
def distance_ab(user_location, dest_location):

  dis = int(sqrt((user_location[0]-dest_location[0])**2 \
  + (user_location[1]-dest_location[1])**2))
  return dis


def transport(user_location, dest_location,foodlist_canteens):
    R = 9999
    for x in red_loop.keys():
        first = red_loop[x][0] * 0.625
        second = red_loop[x][1] * 0.6
        last = [first,second]
        r = distance_ab(user_location, last)
        if r < R:
            R = r
            bus_stop_red = x
    
    B = 9999
    for y in blue_loop.keys():
        first = blue_loop[y][0] * 0.625
        second = blue_loop[y][1] * 0.6
        last = [first,second]
        b = distance_ab(user_location, last)
        if b < B:
            B = b
            bus_stop_blue = y
           
    tagged_stops = canteen_bus_stops[dest_location]
    
    #getting no. of stops for red route
    i_red_stop = red_list.index(bus_stop_red)
    f_red_stop = red_list.index(tagged_stops[0])
    red_stops = f_red_stop - i_red_stop
    if red_stops < 0:
        red_stops = red_stops + len(red_list)
        
    #getting no. of stops for blue route
    i_blue_stop = blue_list.index(bus_stop_blue)
    f_blue_stop = blue_list.index(tagged_stops[1])
    blue_stops = f_blue_stop - i_blue_stop
    if blue_stops < 0:
        blue_stops = blue_stops + len(blue_list) 
        
    #2nd argument should be canteen_list[dest_location], call coordinates of canteen from dictionary
    x = (foodlist_canteens[dest_location][2][0])*0.625
    y = (foodlist_canteens[dest_location][2][0])*0.6
    coordinate = [x,y]
    canteen_dist = distance_ab(user_location,coordinate) 
    if canteen_dist < 100:
        return "Walking is faster"
    else:
        pass
    
    a = "Board Red bus at stop {} and alight at stop {} \n {} stop(s)\
    \n Board Blue bus at stop {} and alight at stop {}\n {} stop(s)"\
    .format(bus_stop_red, tagged_stops[0], red_stops, bus_stop_blue, tagged_stops[1],blue_stops)
    return a
    
    

#red bus stops and list
red_loop = {
"Lee Wee Nam Library": (629,377),
"School of Biological Sciences": (336,486),
"WKW School of Communications": (214,636),
"Hall 7":(244,870),
"Innovation Centre": (490,860),
"Hall 4": (718,904),
"Hall 1": (924,916),
"Canteen 2": (973,619),
"Hall 8 and 9": (1136,485),
"Hall 11": (1388,391),
"Graduate Hall 1 and Hall 11": (1437,276),
"Hall 23": (1281,227),
"Hall 12 and 13": (865,183)
}

#lists of red and blue 
red_list = [
  "Lee Wee Nam Library",
  "School of Biological Sciences",
  "WKW School of Communications",
  "Hall 7",
  "Innovation Centre",
  "Hall 4",
  "Hall 1",
  "Canteen 2",
  "Hall 8 and 9",
  "Hall 11",
  "Graduate Hall 1 and Hall 11",
  "Hall 23",
  "Hall 12 and 13"]

#blue bus stop and list
blue_loop = {
  "NIE": (629,378),
  "Opp Hall 3 and 16": (779,250),
  "Opp Hall 14 and 15": (1029,172),
  "Opp Hall 23": (1281,213),
  "Opp Hall 10 and 11": (1396,402),
  "Opp Hall 8 and 9": (1160,478),
  "Hall 6": (994,720),
  "Opp Hall 4 and 5": (752,956),
  "Opp Innovation Centre": (496,864),
  "SPMS": (316,738),
  "Opp WKW School of Communications": (203,630),
  "Opp CEE": (410,365)
  }

blue_list = [
  "NIE",
  "Opp Hall 3 and 16",
  "Opp Hall 14 and 15",
  "Opp Hall 23",
  "Opp Hall 10 and 11",
  "Opp Hall 8 and 9",
  "Hall 6",
  "Opp Hall 4 and 5",
  "Opp Innovation Centre",
  "SPMS",
  "Opp WKW School of Communications",
  "Opp CEE"
  ]

canteen_bus_stops = {
  "Ananda Kitchen": ["Hall 11","Opp Hall 10 and 11"],
  "Bakery Cuisine": ["Lee Wee Nam Library","NIE"],
  "Each-A-Cup": ["Lee Wee Nam Library","NIE"],
  "Food Court 1": ["Hall 1", "Hall 6"],
  "Food Court 2": ["Canteen 2", "Hall 6" ],
  "Food Court 9": ["Hall 8 and 9", "Opp Hall 8 and 9"],
  "Food Court 11": ["Hall 11", "Opp Hall 10 and 11"],
  "Food Court 13": ["Hall 1", "Opp Hall 3 and 16"],
  "Food Court 14": ["Hall 12 and 13","Opp Hall 14 and 15"],
  "Food Court 16": ["Hall 12 and 13","Opp Hall 3 and 16"],
  "Foodgle Food Court": ["Nanyang Crescent Hall","NIE"],
  "KFC": ["Lee Wee Nam Library","NIE"],
  "Koufu": ["Innovation Centre","Opp Innovation Centre"],
  "Long John Silver's": ["Lee Wee Nam Library","NIE"],
  "McDonald's": ["Lee Wee Nam Library","NIE"],
  "Mr Bean": ["Lee Wee Nam Library","NIE"],
  "North Hill Food Court": ["Hall 11","Opp Hall 10 and 11"],
  "North Spine Food Court": ["Lee Wee Nam Library","NIE"],
  "Paik's Bibim": ["Lee Wee Nam Library","NIE"],
  "Peach Garden Chinese Restaurant": ["Lee Wee Nam Library","NIE"],
  "Pizza Hut Express": ["Lee Wee Nam Library","NIE"],
  "Pioneer Food Court": ["Hall 1","Opp Hall 4 and 5"],
  "Subway": ["Lee Wee Nam Library","NIE"],
  "Starbucks Coffee": ["Lee Wee Nam Library","NIE"],
  "The Sandwich Guys": ["Lee Wee Nam Library","NIE"],
  "The Soup Spoon Union": ["Lee Wee Nam Library","NIE"]
  }
list_of_canteens =[ keys for keys in canteen_bus_stops.keys()]
list_of_canteens = ['Ananda Kitchen', 'Bakery Cuisine', 'Each-A-Cup',
                    'Food Court 1', 'Food Court 2', 'Food Court 9',
                    'Food Court 11', 'Food Court 13', 'Food Court 14',
                    'Food Court 16', 'Foodgle Food oCurt', 'KFC', 'Koufu',
                    "Long John Silver's", "McDonald's", 'Mr Bean',
                    'North Hill Food Court', 'North Spine Food Court',
                    "Paik's Bibim", 'Peach Garden Cuisine',
                    'Pizza Hut Express', 'Pioneer Food Court',
                    'Subway', 'Starbucks Coffee', 'The Sandwich Guys',
                    'The Soup Spoon Union']


#functions

def sort_distance(userlocation,foodlist_canteens):
    dist_dict= {}
    for key, value in foodlist_canteens.items():
        canteen = key
        dest_location = (0.625*value[2][0],0.6*value[2][1])
        canteen_dist = distance_ab(userlocation,dest_location)
        dist_dict[canteen] = canteen_dist
    sorted_by_dist = sorted(dist_dict.items(), key= lambda x: x[1])
    list_dist_canteens = [x[0] for x in sorted_by_dist]
    print(list_dist_canteens)
    return list_dist_canteens

def sort_by_rank(userlocation,canteen_list,foodlist_canteens): 
    can_list = canteen_list
    dist_list = sort_distance(userlocation,foodlist_canteens)
    sorted_list = []
    for x in dist_list:
        if x in canteen_list:
            sorted_list.append(x)     
    print(sorted_list)
    return sorted_list[0:3]

#one function for each top3 list length
        
def depend_on_length(top3,foodlist_canteens,foodname):
    if len(top3)==1:
        key = top3[0]
        timeStart = foodlist_canteens[key][1][0]
        timeEnd = foodlist_canteens[key][1][1]
        print(timeStart,timeEnd)
        ifopen = checkopen(timeStart,timeEnd)
        print(ifopen)
        color = opencolor(ifopen)
        print(color)
        final_dest = sel_final_1(color,top3,foodname,foodlist_canteens)
        return final_dest
    elif len(top3)==2:
        key1 = top3[0]
        timeStart1 = foodlist_canteens[key1][1][0]
        timeEnd1 = foodlist_canteens[key1][1][1]
        ifopen1 = checkopen(timeStart1,timeEnd1)
        color1 = opencolor(ifopen1)
        key2 = top3[1]
        timeStart2 = foodlist_canteens[key2][1][0]
        timeEnd2 = foodlist_canteens[key2][1][1]
        ifopen2 = checkopen(timeStart2,timeEnd2)
        color2 = opencolor(ifopen2)
        final_dest = sel_final_2(color1,color2,top3,foodname,foodlist_canteens)
        return final_dest
    else:
        key1 = top3[0]
        timeStart1 = foodlist_canteens[key1][1][0]
        timeEnd1 = foodlist_canteens[key1][1][1]
        ifopen1 = checkopen(timeStart1,timeEnd1)
        color1 = opencolor(ifopen1)
        key2 = top3[1]
        timeStart2 = foodlist_canteens[key2][1][0]
        timeEnd2 = foodlist_canteens[key2][1][1]
        ifopen2 = checkopen(timeStart2,timeEnd2)
        color2 = opencolor(ifopen2)
        key3 = top3[2]
        timeStart3 = foodlist_canteens[key3][1][0]
        timeEnd3 = foodlist_canteens[key3][1][1]
        ifopen3 = checkopen(timeStart3,timeEnd3)
        color3 = opencolor(ifopen3)
        final_dest = sel_final_dest(color1,color2,color3,top3,foodname,foodlist_canteens)
        return final_dest
    return 0

def sel_final_dest(color1,color2,color3,top3,foodname,foodlist_canteens):
    loop = True
    while loop:
        appDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif button_click(0,0,333,600):
                return top3[0]
            elif button_click(333,0,333,600):
                return top3[1]
            elif button_click(666,0,333,600):
                return top3[2]
                
        pygame.display.set_caption('Choice of canteen')
        #display 3 choices - means 3 buttons
        trans_button_special(color1,top3[0],0,0,333,600,white,lightgreen)
        trans_button_special(color2,top3[1],333,0,333,600,white,lightgreen)
        trans_button_special(color3,top3[2],666,0,333,600,white,lightgreen)
        recmd(top3,foodname,foodlist_canteens)

        pygame.display.update()

def sel_final_1(color,top3,foodname,foodlist_canteens):
    loop = True
    while loop:
        appDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif button_click(0,0,333,600):
                return top3[0]
                
        pygame.display.set_caption('Choice of canteen')
        #display 3 choices - means 3 buttons
        trans_button_special(color,top3[0],0,0,333,600,white,lightgreen)
        trans_button('',333,0,333,600,white,lightgreen)
        trans_button('',666,0,333,600,white,lightgreen)
        recmd(top3,foodname,foodlist_canteens)
        pygame.display.update()


def sel_final_2(color1,color2,top3,foodname,foodlist_canteens):
    loop = True
    while loop:
        appDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif button_click(0,0,333,600):
                return top3[0]
            elif button_click(333,0,333,600):
                return top3[1]
                
        pygame.display.set_caption('Choice of canteen')
        #display 3 choices - means 3 buttons
        trans_button_special(color1,top3[0],0,0,333,600,white,lightgreen)
        trans_button_special(color2,top3[1],333,0,333,600,white,lightgreen)
        trans_button('',666,0,333,600,white,lightgreen)
        recmd(top3,foodname,foodlist_canteens)
        pygame.display.update()
    
        
        #display 3 choices - means 3 buttons
   
def button_click(x,y,width,height):
    mouse_position = pygame.mouse.get_pos() #get x y coordinate of mouse
    mouse_click = pygame.mouse.get_pressed() #register press down mouse
    if x+width > mouse_position[0] > x and y+height > mouse_position[1] > y:
        if mouse_click[0] == 1:
            print(mouse_click)
            return True
    
def transport_page(userlocation,final_dest,foodlist_canteens):
    loop = True
    while loop:
        appDisplay.fill(white)
        pygame.display.set_caption('Getting there')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif button_click(0,500,200,100):
                return 0 #go back
            elif button_click(800,500,200,100):
                return 1 #restart

        route = transport(userlocation,final_dest,foodlist_canteens)
        if 'Walking' in route:
            text_to_button(route,black,0,0,
                       1000,600,'small')
        else:
            split_route = route.splitlines()
            text_to_button(split_route[0],black,333,250,
                           333,50,'small')
            text_to_button(split_route[1],black,333,290,
                           333,50,'small')
            text_to_button(split_route[2],black,333,330,
                           333,50,'small')
            text_to_button(split_route[3],black,333,370,
                           333,50,'small')
        trans_button('Go Back',0,500,200,100,white,lightgreen)
        trans_button('Restart',800,500,200,100,white,lightgreen)

               
        pygame.display.update()

    


def re_run(userlocation,foodlist_canteens):
    loop = True
    while loop:
        appDisplay.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #if upate or recommend or quit
        canteen_list,foodname = foodpriceselect(foodlist_canteens)

        #Hector part
        top3 = sort_by_rank(userlocation,canteen_list,foodlist_canteens)
        print(top3)  #2nd output

        final_dest = depend_on_length(top3,foodlist_canteens,foodname) 
        time.sleep(1)
        return_val = transport_page(userlocation,final_dest,foodlist_canteens)
        
        if return_val == 0:
            back_loop = True 
            while back_loop:
                final_dest = depend_on_length(top3,foodlist_canteens,foodname)
                print(final_dest) #3rd output
                time.sleep(1)
                return_val = transport_page(userlocation,final_dest,foodlist_canteens)
                if return_val == 1:
                    back_loop = False
        loop = False
    
            
def checkopen(timeStart,timeEnd): #check if the store is open
    x = str(datetime.now())
    hour = int(x[11:13])

    if hour<12:
        if hour != 0:
            str_hour = str(hour)
        else:
            str_hour = str(12)
        z = 'AM'
    elif hour>12:
        hour -= 12
        str_hour = str(hour)
        z = 'PM'

    y = str_hour +':'+ x[14:16] + z #current time
    timeNow = y
    timeEnd = datetime.strptime(timeEnd, "%I:%M%p")
    timeStart = datetime.strptime(timeStart, "%I:%M%p")
    timeNow = datetime.strptime(timeNow, "%I:%M%p")

    def check_if_open(timeStart, timeEnd, timeNow):
        if timeStart < timeEnd:
            return timeNow >= timeStart and timeNow <= timeEnd
        else: #Over midnight
            return timeNow >= timeStart or timeNow <= timeEnd
    return check_if_open(timeStart, timeEnd, timeNow)

def opencolor(checkopen): #if open = blue, else red
    if checkopen == True:
        return blue
    elif checkopen == False:
        return red

def home():
    home = True
    foodlist_canteens = {'Food Court 1':[{'chinese':[0,2],'mala':[0,2],'japanese':[0,1],'mixed rice':[0,1,':)']},['07:00AM','09:00PM'],[878, 751]],
                        'Food Court 2':[{'chinese':[0,2,':)'],'korean':[0,2],'indonesian':[1,1,':)'],'western':[0,2], 'mixed rice':[0,1], 'bakery':[0,1,':)']},['07:00AM','09:00PM'],[952, 625]],
                        'Food Court 9':[{'mala':[0,2],'chinese':[0,2],'chicken rice':[0,1,':)'],'pasta':[0,2], 'mixed rice':[1,1]},['07:00AM','09:00PM'],[1184, 409]],
                        'Food Court 11':[{'chicken rice':[1,1,':)'],'mixed rice':[0,1], 'vietnamese':[0,2],'japanese':[1,2,':)']},['07:00AM','09:00PM'],[1384, 329]],
                        'Food Court 13':[{'western':[1,2,':)'],'chinese':[0,2],'mixed rice':[0,1],'japanese':[0,2,':)']},['07:00AM','09:00pm'],[883, 208]],
                        'Food Court 14':[{'muslim':[1,1],'indian':[1,1,':)'],'bakery':[0,1],'korean':[0,2]},['07:00AM','09:00PM'],[1022, 217]],
                        'Food Court 16':[{'mala':[0,2],'japanese':[0,2],'indian':[1,1],'mixed rice':[0,1], 'chinese':[0,1]},['07:00AM','09:00PM'],[805, 290]],
                        'Ananda Kitchen':[{'indian':[1,1], 'muslim':[1,1]},['12:00PM','10:30PM'],[1419, 461]], 
                        'Foodgle Food Court':[{'mala':[0,2,':)'],'korean':[0,2,':)'],'western':[0,2],'mixed rice':[0,1],'chinese':[0,1]},['07:00AM','09:00PM'],[1282, 245]],
                        'North Hill Food Court':[{'western':[1,2],'mixed rice':[0,1],'chinese':[0,2],'mala':[0,2]},['07:00AM','09:00PM'],[1437, 445]],
                        'Pioneer Food Court':[{'japanese':[0,1],'yong tau foo':[0,1,':)'], 'thai':[0,2,':)'], 'mixed rice':[0,1]},['07:00AM','09:00PM'],[995, 903]],
                        'Bakery Cuisine':[{'bakery':[0,1]},['07:00AM','09:00PM'],[605, 455]],
                        'Each-A-Cup':[{'drinks':[1,1,':)']},['09:00AM','09:00PM'],[605, 455]],
                        'KFC':[{'western':[1,2,':)']},['07:30AM','10:00PM'],[605, 455]],
                        "Long John Silver's":[{'western':[0,2],'burgers':[0,2]},['07:30AM','10:00PM'],[605, 455]],
                        "McDonald's":[{'western':[1,2],'burgers':[1,2,':)']},['07:00AM','12:00AM'],[605, 455]],
                        'Mr Bean':[{'bakery':[0,1],'drinks':[0,1]},['07:30AM','08:30PM'],[605, 455]],
                        'North Spine Food Court':[{'western':[1,2],'mala':[0,2],'chicken rice':[0,1], 'mixed rice':[0,1], 'japanese':[0,2],'chinese':[0,1],'vietnamese':[0,1,':)']},['07:00AM','09:00PM'],[605, 455]],
                        "Paik's Bibim":[{'korean':[0,3,':)']},['10:00AM','09:00PM'],[605, 455]],
                        'Peach Garden Chinese Restaurant':[{'chinese':[0,4,':)']},['11:00AM','10:00PM'],[605, 455]],
                        'The Soup Spoon Union':[{'western':[0,2,':)']},['11:00AM','09:00PM'],[605, 455]],
                        'Koufu':[{'pasta':[0,2,':)'],'mixed rice':[0,1],'yong tau foo':[1,1],'drinks':[1,1],'japanese':[0,1],'indian':[1,1]},['07:00AM','01:00PM'],[446, 745]],
                        'The Sandwich Guys':[{'sandwich':[0,2,':)']},['10:00AM','07:00PM'],[605, 455]],
                        'Subway':[{'sandwich':[1,2]},['08:00AM','10:00PM'],[605, 455]],
                        'Pizza Hut Express':[{'pizza':[1,2,':)']},['11:00AM','10:00PM'],[605, 455]],
                        'Starbucks Coffee':[{'bakery':[1,2,':)'],'drinks':[1,2,':)']},['07:00AM','10:00PM'],[605, 455]]}

    app_intro()
    time.sleep(2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            appDisplay.fill(white)
            message_to_screen("Welcome to NTUEats", black, -80,'large')
            recommend = button("recommend",100,300,200,100,green,lightgreen)
            update = button("update",425,300,200,100,green,lightgreen)
            quitapp = button("quit",750,300,200,100,green,lightgreen)
            
            pygame.display.update()
            
            if recommend == 1:
                print("recommend food")
                userlocation= showmap()
                re_run(userlocation,foodlist_canteens)
            
            elif update == 1:
                print("update food")
                foodlist_canteens = full_enterinfo(foodlist_canteens)
                print(foodlist_canteens)
                time.sleep(2)
            
            elif quitapp == 1:
                print("leave")
                pygame.quit()
                quit()
            
                        
                        
    pygame.display.update()

def showmap():
    X = 0
    loop = True
    while loop:
    
        W = display_width

        H = display_height
        font = pygame.font.SysFont("monospace", 20)
        text1 = font.render("where are you!", True, (0, 0, 0))
        screen = pygame.display.set_mode((W, H))
        screenIm = pygame.image.load("NTUMap.png")
        screenIm = pygame.transform.scale(screenIm, (W , H))
        screen.blit(screenIm,(0, 0))

        screen.blit(text1 , (100,200))

        pygame.display.update()

        X,Y = mouseclick()
        if X != 0:
            loop = False
    return(X,Y)

def recmd(top3,foodname,foodlist_canteens):
    if len(top3) == 1:
        x = check_len(top3[0],foodname,foodlist_canteens)
        if x == True:
            text_to_button('*Recommended',black,0,200,333,400,'small')

    elif len(top3) == 2:
        x = check_len(top3[0],foodname,foodlist_canteens)
        if x == True:
            text_to_button('*Recommended',black,0,200,333,400,'small')
        y = check_len(top3[1],foodname,foodlist_canteens)
        if y == True:
            text_to_button('*Recommended',black,333,200,333,400,'small')
                        
    elif len(top3) == 3:
        x = check_len(top3[0],foodname,foodlist_canteens)
        if x == True:
            text_to_button('*Recommended',black,0,200,333,400,'small')
        y = check_len(top3[1],foodname,foodlist_canteens)
        if y == True:
            text_to_button('*Recommended',black,333,200,333,400,'small')
        z = check_len(top3[2],foodname,foodlist_canteens)
        if z == True:
            text_to_button('*Recommended',black,666,200,333,400,'small')


    
def check_len(canteen,foodname,foodlist_canteens):
    long_list = foodlist_canteens[canteen] #retrieve list of key value pairs
    short_list = long_list[0]
    foodname_value = short_list[foodname]
    if len(foodname_value) ==3:
        return True
    else:
        return False
#################################################################################





home()

pygame.display.update()
pygame.quit()
quit()
    



