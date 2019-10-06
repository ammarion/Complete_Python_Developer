class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('getting att')
        return self._name

    def set_name(self, value):
        print('setting att')
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()

        else:
            raise ValueError('Name must be a non-empty string')

    name = property(fget=get_name, fset=set_name)


p = Person('Alex')
p.