class Variable:

    def __init__(self, name):
        self.name = name

    def evaluate(self, inputs):
        if not self.name in inputs:
            raise ValueError(f'Input does not contain a value for {self.name}')

        return inputs[self.name]

    def grad(self, respect_to, inputs):
        if self.name == respect_to:
            return 1

        return 0

    def __add__(self, other):
        return self.name + other.name

    def __mul__(self, other):
        return self.name * other.name

    def __pow__(self, other):
        return self.name ** other.name


class Constant:

    def __init__(self, value):
        self.value = value

    def evaluate(self, inputs):
        return self.value

    def grad(self, respect_to, inputs):
        return 0

    def __add__(self, other):
        return self.value + other.name

    def __mul__(self, other):
        return self.value * other.name

    def __pow__(self, other):
        return self.value ** other.name


# answers
'''
x = Variable(name='x')
m = Variable(name='m')
c = Constant(5)
y = m * x * c
y.evaluate(inputs={'m': 10, 'x': 15})
y.grad(respect_to='x', inputs={'m': 2, 'x': 5})
NOT done
'''