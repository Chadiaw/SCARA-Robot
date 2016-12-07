from robot import *

bras = Robot(6.5, 4.0, True)

A = Point(3.0, 9.0, 3.7)
B = Point(-3.0, 9.0, 3.7)
C = Point(-3.0, 8.0, 3.7)

# Se placer pour dessiner (hauteurMax)
bras.go_to_coordinates(A.x, A.y, bras.MAX_HEIGHT)
time.sleep(1)

print(" Debut dessin")
bras.go_to_point(B)
time.sleep(3)  # temps de descente

bras.draw_line(A, B)
print(" Point B atteint")
time.sleep(0.5)
bras.draw_line(B, C)

print(" Point C atteint")
time.sleep(0.5)
bras.draw_line(C, A)

print(" Dessin termine.")
# rangerCrayon()
