class Sinif:
    def __iter__(self):
        self.deger = 1
        return self
    def __next__(self):
        x = self.deger
        self.deger += 1
        return x

number = Sinif()
yineleyici = iter(number)

print(next(yineleyici))
print(next(yineleyici))
print(next(yineleyici))
print(next(yineleyici))
print(next(yineleyici))
print(next(yineleyici))
