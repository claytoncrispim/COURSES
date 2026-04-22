# --- Code given by the instructor ---

# Parent class for all shapes.
# Defines shared properties and the print() loop.
# printRow() is intentionally left unimplemented — child classes must override it.
class Shape:
	width = 5       # Can be overridden by child classes
	height = 5      # Can be overridden by child classes
	printChar = '#' # Character used to draw the shape

	# Must be overridden by each child class.
	# i = current row index, starting at 0 (top) and going up to height-1 (bottom).
	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	# Drives the output: loops i from 0 to height-1 and calls printRow(i) each time.
	# Rows are printed TOP to BOTTOM — i=0 is the first line printed (top),
	# i=height-1 is the last line printed (bottom).
	def print(self):
		for i in range(self.height):
			self.printRow(i)

# Every row is identical: printChar repeated width times.
class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)


# --- Instructor's solutions ---

# Solution 1: Right-angled triangle.
# Row i prints (i + 1) characters, so it grows from top to bottom:
#   i=0 → #
#   i=1 → ##
#   i=2 → ###  ... and so on.
# Using (i + 1) instead of i ensures the top row has 1 char, not 0.
class TriangleA(Shape):
	def printRow(self, i):
		print(self.printChar * (i + 1))

print("Triangle A:")
trA = TriangleA()
trA.print()


# Solution 2: Equilateral-ish (centered/isosceles) triangle.
# Each row grows by 2 chars and is padded with spaces to stay centered.
#   i=0 → triangleWidth=1, centered in width=10  →     #
#   i=1 → triangleWidth=3, centered             →    ###
#   i=2 → triangleWidth=5, centered             →   #####  ... and so on.
# width is set to 2 * height so there's always enough room for padding.
class TriangleB(Shape):
	height = 5
	width = 2 * height  # Total canvas width; must be at least 2*height - 1

	def printRow(self, i):
		triangleWidth = i * 2 + 1                      # Grows: 1, 3, 5, 7, 9
		padding = int((self.width - triangleWidth) / 2) # Centers the row
		print(' ' * padding + self.printChar * triangleWidth)

print("\nTriangle B:")
trB = TriangleB()
trB.print()