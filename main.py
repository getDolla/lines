from display import *
from draw import *

screen = new_screen()

color = [ 255, 255, 255 ]

#top of the head
draw_line( XRES/2 - 30, YRES-60, XRES/2 + 30, YRES-60, screen, color )

draw_line( XRES/2 - 50, YRES-80, XRES/2 - 30, YRES-60, screen, color )

draw_line( XRES/2 + 30, YRES-60, XRES/2 + 50, YRES-80, screen, color )

#sides of the head
draw_line( XRES/2 - 50, YRES-80, XRES/2 - 50, YRES-140, screen, color )

draw_line( XRES/2 + 50, YRES-80, XRES/2 + 50, YRES-140, screen, color )

#bottom of the head
draw_line( XRES/2 - 50, YRES-140, XRES/2 - 30, YRES-160, screen, color )

draw_line( XRES/2 - 30, YRES-160, XRES/2 + 30, YRES-160, screen, color )

draw_line( XRES/2 + 30, YRES-160, XRES/2 + 50, YRES-140, screen, color )

#main body


display(screen)
save_extension(screen, 'img.png')
