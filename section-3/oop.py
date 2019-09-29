class PlayerCharacter:
    def __init__(self, name='Ammar', age=0):
        if age > 10:
            self.name = name
            self.age = age
        else:
            print('You are not old enough')

    def shout(self):
        print(f'My name is {self.name}')
        return self.age


p1 = PlayerCharacter('Ali', 10)
print(p1.name)
print(p1.shout())