import elastico
global c
c = []
class A:

	def __init__(self):
		self.x = 9

	def func(self):
		c.append(self)

a  = A()
a.func()
print (c)
print(c[0].x)

p = elastico.Elastico()
s = p.get_IP()
print(type(s))
