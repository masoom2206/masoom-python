class X:# pass
  N = 1
class Y:# pass
  N = 2
class Z:# pass
  N = 3
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass

# print(M.mro())
# print(M.__mro__)
m1 = M()
print(m1.N)