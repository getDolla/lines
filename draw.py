from display import *

def draw_o1( x, y, A, B, x1, y1, screen, color ):
    d = 2*A + B

    while x <= x1:
        plot( screen, color, x, y )

        if ( d > 0 ):
            y += 1
            d += 2*B

        x += 1
        d += 2*A
        
def draw_o2( x, y, A, B, x1, y1, screen, color ):
    d = 2*B + A

    while y <= y1:
        plot( screen, color, x, y )

        if ( d < 0 ):
            x += 1
            d += 2*A

        y += 1
        d += 2*B

def draw_o8( x, y, A, B, x1, y1, screen, color ):
    d = 2*A - B

    while x <= x1:
        plot( screen, color, x, y )

        if ( d < 0 ):
            y -= 1
            d -= 2*B

        x += 1
        d += 2*A
    
def draw_o7( x, y, A, B, x1, y1, screen, color ):
    d = A - 2*B

    while y >= y1:
        plot( screen, color, x, y )

        if ( d > 0 ):
            x += 1
            d += 2*A

        y -= 1
        d -= 2*B

def draw_line( x0, y0, x1, y1, screen, color ):
    y = y0
    x = x0

    A = y1 - y0
    B = -(x1 - x0)

    if ( (A <= -B) and (A >= 0) ):
        draw_o1( x, y, A, B, x1, y1, screen, color )

    elif ( (A > -B) and (A > 0) ):
        draw_o2( x, y, A, B, x1, y1, screen, color )

    elif ( (A >= B) and (A < 0) ):
        draw_o8( x, y, A, B, x1, y1, screen, color )

    else:
        draw_o7( x, y, A, B, x1, y1, screen, color )

