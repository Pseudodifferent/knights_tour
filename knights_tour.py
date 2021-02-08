from manim import *
import numpy as np
import math

from typing_extensions import runtime

###scale the mobject first, then position it

class Lec1(Scene):
	def construct(self):

		circ = Circle(stroke_color=YELLOW_D, fill_color=BLUE_A, radius=2, stroke_width=5, fill_opacity=0.8).to_edge(UL)

		eq1 = TexMobject("{x}^{2}+{y}^{2}={2}^{2}")
		eq1.next_to(circ, DOWN, buff=0.5)

		text = TextMobject("Mr ", "Schoen ", "Tutorials")
		text[0].set_color(BLUE)
		text[1].set_color(PINK)
		text[2].set_color(GREEN)

		text.next_to(circ, RIGHT, buff=1)

		und = Underline(text[2])

		num = TexMobject("\ln(2)").scale(2).next_to(text, DOWN, buff=0.1)

		self.play(DrawBorderThenFill(circ))
		self.play(Write(eq1))
		self.play(Write(text), ShowCreation(und))
		self.play(FadeIn(num))
		self.play(FadeOut(text[0]))
		self.play(eq1.animate.shift(RIGHT*4), run_time=5)
		self.play(circ.animate.next_to(eq1, UP))
		self.play(Transform(circ,num))

class Lec1_1(Scene):
	def construct(self):

		line = DashedLine(config.frame_width/2*LEFT,config.frame_width/2*RIGHT)

		text = TextMobject("This ", "number ", "is too good mate")
		und = Underline(text[1]).set_color(YELLOW_D)

		num = TexMobject("5").to_edge(DOWN)

		self.play(ShowCreation(line))
		self.play(Write(text),Write(num))

class Lec1_3(Scene):
	def construct(self):

		line = DashedLine(config.frame_width/2*LEFT,config.frame_width/2*RIGHT)

		self.add(line)


class Lec2_1(Scene):
	def construct(self):

		c = Circle(
			radius=1,
			stroke_width=6,
			stroke_color=YELLOW_D,
			fill_color=BLUE_D,
			fill_opacity=0.7,
		).scale(2).to_edge(UL, buff=0.5)

		eq = MathTex("\int \mathrm{e}^{-t^2} \, \mathrm{d}t=\sqrt{\pi}}").scale(1.8).next_to(c, RIGHT)

		text = Tex("Where is the circle?").shift(DOWN * 2)
		text2 = Text("Where is the circle?").shift(DOWN * 3)

		self.play(DrawBorderThenFill(c))
		self.play(Write(eq))
		self.play(Write(text),Write(text2))
		self.play(c.animate.scale(2), runtime=2)
		self.wait(1)