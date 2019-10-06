class Pearson:
    def set_name(self, new_name, age):
        self.name = new_name
        self.age = age


# Pearson.do_workd = lambda self: f"do_workd called from {self}"

p = Pearson()

p.set_name('Ammar', 99)
Pearson.do_work = lambda self: f"do_work called from {self}"
