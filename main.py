from display import *
from draw import *

screen = new_screen()

color = [ 0, 255, 0 ]

#top
x = XRES/2 - 1
y = YRES - 1
i = y - 15
j = 0
while i > (YRES/2) - 1:
    draw_line( 0, i, x + j, y, screen, color )
    draw_line( x - j, y, XRES - 1, i, screen, color )
    i -= 15
    j += 6

#left
x = 0
y = YRES/2 - 1
i = x + 15
j = 0
while i < (XRES/2) - 1:
    draw_line( x, y - j, i, YRES - 1, screen, color )
    draw_line( x, y + j, i, 0, screen, color )
    i += 15
    j += 6

#right
x = XRES - 1
y = YRES/2 - 1
i = x - 15
j = 0
while i > (XRES/2) - 1:
    draw_line( i, YRES - 1, x, y - j, screen, color )
    draw_line( i, 0, x, y + j, screen, color )
    i -= 15
    j += 6

#top
x = XRES/2 - 1
y = 0
i = y + 15
j = 0
while i < (YRES/2) - 1:
    draw_line( 0, i, x + j, y, screen, color )
    draw_line( x - j, y, XRES - 1, i, screen, color )
    i += 15
    j += 6

#draws x and y axis and slopes of 1 and -1
draw_line( XRES/2, 0, XRES/2, YRES-1, screen, color )
draw_line( 0, YRES/2, XRES - 1, YRES/2, screen, color )
draw_line( 0, 0, XRES - 1, YRES - 1, screen, color )
draw_line( 0, YRES - 1, XRES - 1, 0, screen, color )
    
display(screen)
save_extension(screen, 'img.png')
