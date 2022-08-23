class perimeter:
    def rectangle(self, l, b):
        self.l = l
        self.b = b
        area = l * b
        peri = 2 * (l + b)
        print(area)
        print(peri)

    def circle(self, r):
        self.r = r
        area = 3.14 * r * r
        peri = 2 * 3.14 * r
        print(area)
        print(peri)

    def triangle(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h
        area = 0.5 * b * h
        peri = l + b + h
        print(area)
        print(peri)
s = perimeter()
s.rectangle(int(input()), int(input()))
s.circle(int(input()))
s.triangle(int(input()), int(input()), int(input()))
