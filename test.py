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
fin = {"lol" : 1}
p.addCommitment(fin)
print(fin)

p,q = elastico.Identity('172' , 'pk1' , 1 , '1092' ) , elastico.Identity('172' , 'pk1' , 1 , '1092')
print(p.isEqual(q))

t = input()
print(t, type(t))
