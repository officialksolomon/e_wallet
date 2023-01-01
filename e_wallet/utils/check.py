# Dummy file for testing out code...


class A:
    def funcA(self):
        return [1, 2, 3]


class B:
    def funcb(self):
        return A()


b = B()
b.funcb()
