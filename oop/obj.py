from types import MethodType


class Person:
    def __init__(self, name):
        self.name = name

    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))

    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)

        if do_work_method:
            return do_work_method()
        else:
            raise ArithmeticError('You must first register a do_work method')


math_teacher = Person('Ohood')
english_teacher = Person('Ammar')


def work_math(self):
    return f'{self.name} will teach differentials today.'


math_teacher.register_do_work(work_math)


print(math_teacher.__dict__)
math_teacher.do_work()