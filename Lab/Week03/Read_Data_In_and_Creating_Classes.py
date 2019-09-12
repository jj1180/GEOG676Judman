Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> open("C:\lab3.txt", "r")
<_io.TextIOWrapper name='C:\\lab3.txt' mode='r' encoding='cp1252'>
>>> class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w

>>> class Circle:
	def __init__(self, r):
		self.r = r
	def getArea(self):
		return self.radius**2*3.14

	
>>> class Triangle:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
	def getArea(self):
		return self.p1*self.p2*.5

	
>>> 
