import itertools
from manim import *
import math

class Chessboard(VGroup):
    def __init__(self, sq_size=0.5, board_dim=(8,8), colors=[LIGHT_GREY, DARK_GREY],**kwargs):
        super().__init__(**kwargs)
        self.sq_size = sq_size
        self.board_dim = board_dim
        nc, nr = board_dim
        self.colors = colors

        square = Square(stroke_width=0,fill_opacity=1).scale(sq_size)

        self.add(*[square.copy() for x in range(nc * nr)])
        self.arrange_in_grid(nr, nc, buff=0.05)

        for i, j in itertools.product(range(nr), range(nc)):
            color = colors[(i + j) % 2]
            self[i * nc + j].set_color(color)

        self.center()

class Chess(Scene):
    def construct(self):

        my_yellow = "#FFFF99"

        my_green = "#99FF99"

        my_size = 0.41

        my_runtime = 0.7

        my_pause = 0.2

        my_buff = 0.05

        my_trans = my_size + my_buff * (1/2)


        c = Chessboard(sq_size=my_size, board_dim=(8,8))
        c2 = c.copy()

        
		# Path for the SVG knight

        knight = SVGMobject("ADD_YOUR_PATH").rotate(TAU/2).scale(0.3).set_color(BLACK)
        knight.move_to(c[34])
        c[34].set_color(RED)

        knight2 = knight.copy().move_to(c[34])

        fig_A_1 = VGroup(c[34],c[40],c[57],c[51])
        fig_B_1 = VGroup(c[3],c[9],c[18],c[24])
        fig_C_1 = VGroup(c[5],c[15],c[20],c[30])
        fig_D_1 = VGroup(c[36],c[46],c[53],c[63])

        move_order_A = (40,57,51,61,55,38,44,29,23,6,12,2,8,25,19)
        move_order_B = (13,7,22,28,45,39,54,60,50,56,41,35,18,24,9,3)
        move_order_C = (20,5,15,30,47,62,52,37,43,58,48,33,16,1,11,26)
        move_order_D = (32,49,59,42,36,53,63,46,31,14,4,21,27,10,0,17)

        self.add(c)
        self.add(knight)

        for k in move_order_A:
            self.play(knight.animate.move_to(c[k]),c[k].animate.set_color(RED),run_time=my_runtime)

        fig_A_1_cop = fig_A_1.copy()

        self.play(fig_A_1_cop.animate.shift(RIGHT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_A_1_cop.animate.shift(UP * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_A_1_cop.animate.shift(LEFT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_A_1_cop.animate.shift(DOWN * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_A_1_cop.animate.shift(1.03 * LEFT * 8 * my_trans))
        self.wait(my_pause)


        for k in move_order_B:
            self.play(knight.animate.move_to(c[k]),c[k].animate.set_color(my_green),run_time=my_runtime)

        fig_B_1_cop = fig_B_1.copy()

        self.play(fig_B_1_cop.animate.shift(DOWN * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_B_1_cop.animate.shift(RIGHT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_B_1_cop.animate.shift(UP * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_B_1_cop.animate.shift(LEFT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_B_1_cop.animate.shift(1.03 * LEFT * 8 * my_trans))
        self.wait(my_pause)


        for k in move_order_C:
            self.play(knight.animate.move_to(c[k]),c[k].animate.set_color(BLUE),run_time=my_runtime)

        fig_C_1_cop = fig_C_1.copy()

        self.play(fig_C_1_cop.animate.shift(LEFT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_C_1_cop.animate.shift(DOWN * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_C_1_cop.animate.shift(RIGHT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_C_1_cop.animate.shift(UP * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_C_1_cop.animate.shift(1.03 * RIGHT * 8 * my_trans))
        self.wait(my_pause)


        for k in move_order_D:
            self.play(knight.animate.move_to(c[k]),c[k].animate.set_color(my_yellow),run_time=my_runtime)

        fig_D_1_cop = fig_D_1.copy()

        self.play(fig_D_1_cop.animate.shift(LEFT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_D_1_cop.animate.shift(UP * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_D_1_cop.animate.shift(RIGHT * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_D_1_cop.animate.shift(DOWN * 8 * my_trans))
        self.wait(my_pause)

        self.play(fig_D_1_cop.animate.shift(1.03 * RIGHT * 8 * my_trans))
        self.wait(my_pause)

        self.play(FadeOut(knight),FadeOut(fig_A_1_cop),FadeOut(fig_B_1_cop),FadeOut(fig_C_1_cop),FadeOut(fig_D_1_cop),FadeOut(c),FadeIn(c2),FadeIn(knight2))
        
