"""
File: 
Name:Sung mien huang
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title : Le Petite Prince
    This is my favorite story and recently I went to france for business trip which remind me of this story.
    """
    window = GWindow(800,500, title='LePetitePrince')
    line = GLine(200,250,600,250)
    window.add(line)
    arc_l = GArc(30, 20, 90, 180)
    window.add(arc_l, 195, 230)
    arc_r = GArc(30, 20, 270, 180)
    window.add(arc_r, 590, 230)
    oval_right = GOval(5,5, x = 585, y = 235)
    oval_right.filled = True
    window.add(oval_right)
    line2 = GLine(200, 230, 230, 230)
    window.add(line2)
    arc = GArc(155,900, 270, 60)
    window.add(arc,196,5)
    arc2 = GArc(155,900, 90,67 )
    window.add(arc2, 255, 95)
    arc3 = GArc(85, 90, 30, 130)
    window.add(arc3, 288, 85)
    arc4 = GArc(300, 100, 195, 70)
    window.add(arc4, 355, 68)
    arc5 = GArc(155,280,30,70)
    window.add(arc5, 380, 104)
    arc6 = GArc(155, 300, 0, 70)
    window.add(arc6, 421, 116)
    arc7 = GArc(155, 400, 180, 46)
    window.add(arc7, 472, 108)
    line3 = GLine(477, 230, 600, 230)
    window.add(line3)
    arc_e = GArc(155,900, 270, 60)
    window.add(arc_e,206,6)
    arce2 = GArc(155,900, 90,67 )
    window.add(arce2, 265, 95)
    arce3 = GArc(85, 90, 30, 130)
    window.add(arce3, 288, 90)
    arce4 = GArc(300, 100, 195, 70)
    window.add(arce4, 355, 73)
    arce5 = GArc(155, 280, 30, 70)
    window.add(arce5, 380, 109)
    arce6 = GArc(155, 300, 0, 70)
    window.add(arce6, 417, 116)
    arce7 = GArc(155, 400, 180, 46)
    window.add(arce7, 468, 108)
    arc_e8 = GArc(155, 900, 270, 60)
    window.add(arc_e8, 230, 14)
    line4 = GLine(239, 232, 264, 240)
    window.add(line4)
    arc_e9 = GArc(20, 80, 270,140)
    window.add(arc_e9, 284, 175)
    arc_e10 = GArc(20, 80, 265, 130)
    window.add(arc_e10, 315, 185)
    arc_e11 = GArc(90, 60, 180, 155)
    window.add(arc_e11, 325, 184)
    arc_e12 = GArc(20, 80, 270,120)
    window.add(arc_e12, 400, 190)
    arc_e13 = GArc(20, 80, 270, 120)
    window.add(arc_e13, 435, 190)
    arc_e14 = GArc(155, 400, 180, 46)
    window.add(arc_e14, 457, 108)
    arc_e15 = GArc(50, 200, 270, 75)
    window.add(arc_e15, 432, 133)
    oval_e = GOval(10, 10)
    oval_e.filled = True
    window.add(oval_e, 295, 120)
    rect = GRect(390, 17)
    rect.filled = True
    rect.fill_color = 'burlywood'
    rect.color = 'burlywood'
    window.add(rect, 205, 431)

    rect2 = GRect(178, 115)
    rect2.filled = True
    rect2.fill_color = 'burlywood'
    rect2.color = 'burlywood'
    window.add(rect2, 274, 318)
    triangle = GPolygon()
    triangle.add_vertex((255,431))
    triangle.add_vertex((274,318))
    triangle.add_vertex((274,431))
    triangle.filled = True
    triangle.fill_color = 'burlywood'
    triangle.color = 'burlywood'
    window.add(triangle)
    triangle2 = GPolygon()
    triangle2.add_vertex((453, 318))
    triangle2.add_vertex((453, 431))
    triangle2.add_vertex((473, 431))
    triangle2.filled = True
    triangle2.fill_color = 'burlywood'
    triangle2.color = 'burlywood'
    window.add(triangle2)

    oval_c = GOval(120,80)
    oval_c.filled = True
    oval_c.fill_color = 'burlywood'
    oval_c.color = 'burlywood'
    window.add(oval_c, 272, 290)

    oval_c2 = GOval(120, 80)
    oval_c2.filled = True
    oval_c2.fill_color = 'burlywood'
    oval_c2.color = 'burlywood'
    window.add(oval_c2, 300, 300)

    oval_c3 = GOval(120, 100)
    oval_c3.filled = True
    oval_c3.fill_color = 'burlywood'
    oval_c3.color = 'burlywood'
    window.add(oval_c3, 347, 304)

    oval_c4 = GOval(80, 110)
    oval_c4.filled = True
    oval_c4.fill_color = 'burlywood'
    oval_c4.color = 'burlywood'
    window.add(oval_c4, 390, 333)

    line = GLine(200, 450, 600, 450)
    window.add(line)
    arc_l = GArc(30, 20, 90, 180)
    window.add(arc_l, 195, 430)
    arc_r = GArc(30, 20, 270, 180)
    window.add(arc_r, 590, 430)
    # oval_right = GOval(5, 5, x=585, y=435)
    # oval_right.filled = True
    # window.add(oval_right)
    line2 = GLine(200, 430, 230, 430)
    window.add(line2)
    arc = GArc(155, 900, 270, 60)
    window.add(arc, 196, 205)
    arc2 = GArc(155, 900, 90, 67)
    window.add(arc2, 255, 295)
    arc3 = GArc(85, 90, 30, 130)
    window.add(arc3, 288, 285)
    arc4 = GArc(300, 100, 195, 70)
    window.add(arc4, 355, 268)
    arc5 = GArc(155, 280, 30, 70)
    window.add(arc5, 380, 304)
    arc6 = GArc(155, 300, 0, 70)
    window.add(arc6, 421, 316)
    arc7 = GArc(155, 400, 180, 46)
    window.add(arc7, 472, 308)
    line3 = GLine(477, 430, 600, 430)
    window.add(line3)


    label = GLabel('L'+'\''+'essentiel')
    label.font = 'Newtimesrome-40'
    window.add(label, 278,355)
    label2 = GLabel('est invisible pour les yeux')
    label2.font = 'Newtimesrome-15'
    window.add(label2,282,376)





if __name__ == '__main__':
    main()
