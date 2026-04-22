class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self, i):		
		    print((self.printChar *  i)) # This will print a right-angled triangle with 5 rows, where the first row has 0 characters, the second row has 1 character, and so on until the fifth row has 4 characters.	
			


# square = Square()
# square.print()
tr = Triangle()
tr.print()