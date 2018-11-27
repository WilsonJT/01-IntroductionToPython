"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jack Wilson.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

one = rg.SimpleTurtle('turtle')
one.Pen = rg.Pen('black', 100)
two = rg.SimpleTurtle('turtle')
two.Pen = rg.Pen('black', 100)
three = rg.SimpleTurtle('turtle')
three.Pen = rg.Pen('black', 100)
four = rg.SimpleTurtle('turtle')
four.Pen = rg.Pen('black', 100)
one.forward(200)
one.right(90)
one.forward(200)
one.right(90)
one.forward(200)
two.right(90)
two.forward(200)
two.right(90)
two.forward(200)
two.right(90)
two.forward(200)
three.right(180)
three.forward(200)
three.right(90)
three.forward(200)
three.right(90)
three.forward(200)
four.right(270)
four.forward(200)
four.right(90)
four.forward(200)
four.right(90)
four.forward(200)

window.close_on_mouse_click()
