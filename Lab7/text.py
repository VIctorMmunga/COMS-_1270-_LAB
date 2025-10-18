#from turtle  import*
import colorsys
#bgcolor("black")
#speed(0)

#tracer(300)
#def draw():
#h=0
#for i in range(16):
   # for j in range(18):
     #  c= colorsys.hsv_to_rgb(h, 1, 1)
      # color(c)
       #h +=0.005
      # rt(90)
       #circle(150 - j* 6, 90)
       #lt(90)
       #circle(150 - j* 6, 90)
       #rt(180)
    #circle(40, 24)
#done()
#def self_drive(words:str)-> str:
    #result=" "
    #for i in range (0, len(words)-1):
      #  result+= result[i]
    #return result 

#def main():
# words=input("Enter your number: ")
#print("Your word:", self_drive(words
"""""
# import pygame
# import sys
# import math

# # --- setup ---
# pygame.init()
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Swimming Whale")

# clock = pygame.time.Clock()
# FPS = 60

# # load whale image (replace with your file path)
# # ensure you have a "whale.png" in the same folder
# try:
#     whale = pygame.image.load("C:/New folder/COMS 127/Lab7/whale.png").convert_alpha
# except pygame.error:
#     print("Error: whale.png not found. Make sure the file is in the same folder.")
#     pygame.quit()
#     sys.exit()

# whale = pygame.transform.scale(whale, (200, 120))  # resize if too big
# whale_rect = whale.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# # time counter for wave effect
# time_counter = 0

# # --- main loop ---
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False  # this will exit the loop immediately

#     # get mouse position
#     mouse_x, mouse_y = pygame.mouse.get_pos()

#     # smooth movement toward mouse
#     whale_rect.centerx += (mouse_x - whale_rect.centerx) * 0.05
#     whale_rect.centery += (mouse_y - whale_rect.centery) * 0.05

#     # add wave effect (bob up & down)
#     time_counter += 0.1
#     wave_offset = math.sin(time_counter) * 20
#     whale_rect.centery += wave_offset

#     # draw background and whale
#     screen.fill((0, 105, 148))  # ocean blue
#     screen.blit(whale, whale_rect)

#     pygame.display.flip()
#     clock.tick(FPS)

# # quit Pygame immediately when loop ends
# pygame.quit()
# sys.exit()
"""
# import pygame
# import sys
# import math

# # --- Setup ---
# pygame.init()
# WIDTH, HEIGHT = 1000, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Realistic Whale in Ocean")

# clock = pygame.time.Clock()
# FPS = 60

# # --- Load images ---
# try:
#     whale_img = pygame.image.load("whale.png").convert_alpha()
#     whale_img = pygame.transform.scale(whale_img, (300, 150))  # resize as needed
#     ocean_bg = pygame.image.load("ocean.jpg").convert()
#     ocean_bg = pygame.transform.scale(ocean_bg, (WIDTH, HEIGHT))
# except Exception as e:
#     print("Error loading images:", e)
#     pygame.quit()
#     sys.exit()

# # --- Whale position and movement ---
# base_x = WIDTH // 2
# base_y = HEIGHT // 2
# time_counter = 0
# running = True

# while running:
#     dt = clock.tick(FPS) / 1000
#     time_counter += dt * 5  # speed of wave animation

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # --- Mouse tracking ---
#     mouse_x, mouse_y = pygame.mouse.get_pos()
#     base_x += (mouse_x - base_x) * 0.05
#     base_y += (mouse_y - base_y) * 0.05

#     # Bobbing effect
#     wave_offset = math.sin(time_counter * 2) * 10
#     whale_y = base_y + wave_offset

#     # Tilt depending on horizontal movement
#     tilt = -(mouse_x - base_x) * 0.3

#     # --- Draw scene ---
#     screen.blit(ocean_bg, (0, 0))
#     whale_rotated = pygame.transform.rotate(whale_img, tilt)
#     rect = whale_rotated.get_rect(center=(base_x, whale_y))
#     screen.blit(whale_rotated, rect.topleft)

#     pygame.display.flip()

# pygame.quit()
# sys.exit()
# def taxiFare(distance):
#     total_fare=4
#     if distance > 0:
#        total_fare= total_fare+ (2*distance)
#        if  total_fare > 50:
#           total_fare= 50
#        return total_fare
# def main():
#      user= int(input("Enter you distance per kilo:"))
#      result= taxiFare(user)
#      print(result)
# if __name__=="__main__":
#      main()
# 
# def calculateScore( test_score, ):
#     if test_score <= 60:
#        return "fail"
#     elif 60 <= test_score <= 69:
#         return "pass"
#     elif 70 <= test_score <= 79:
#         return "Good"
#     elif 80 <= test_score <= 89:
#         return "Very Good"
#     else:
#         return "Excellent"
# def Bonus_point(num_assignments, score):
#     score += 2 * num_assignments
#     if score > 100:
#         score = 100
#     return score

# def maskID(student_id):
#     result=" "
#     for ch in student_id:
#         if ch in student_id:
#            result+="#"
#         else:
#             result+=ch
#     return result
# def AgeFactor(age, score):
#        if age % 2==0:
#            score*=1.05
#        else:
#          score*= 0.95
#        if score > 100:
#          score=100
#        return age
# def main():
#     name = input("What is your name? ")
#     age = int(input("What is your age? "))
#     test = int(input("What is your test score? "))
#     num_assignments = int(input("How many assignments completed? "))
#     student_id = input("Enter your ID: ")

#     # Process the score
#     score = Bonus_point(test, num_assignments)
#     score = AgeFactor(score, age)
#     grade_category = calculateScore(score)
#     masked_id = maskID(student_id)

#     # Print summary
#     print("\n--- Student Summary ---")
#     print("Name:", name)
#     print("Age:", age)
#     print("ID:", masked_id)
#     print("Final Score:", round(score, 2))
#     print("Grade Category:", grade_category)

# if __name__ == "__main__":
#     main()

# import numpy as np
# def create ():
#     board = np.zeros((6, 7))
#     return board
# board = create()
# game= False
# turn=0
# while not game:
#     if turn==0:
#         select=int( input("players(0-6):"))
#     else:
#         select= int(input('PLAYER (0-6)'))
#     turn +=1
#     turn= turn%2

