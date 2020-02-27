class Triangle:
    def __init__(self, a1, b1, c1):
        self.a = a1  # First length
        self.b = b1  # Second length
        self.c = c1  # Thired Length

    def equilateralTriangle(self):
        """This function is used to test if ALL sides in a Traingel are equals in length"""
        flag = True
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            flag = False
        if self.a != self.b or self.b != self.c or self.a != self.c:
            flag = False
        return flag

    def isoscelesTriangle(self):
        """This function is used to test if TWO sides in a Traingel are equals in length"""
        flag = True
        if self.a+self.b <= self.c or self.a+self.c <= self.b or self.b+self.c <= self.a:
            flag = False
        if (self.a != self.b) and (self.b != self.c) and (self.a != self.c):
            flag = False
        return flag

    def scaleneTriangle(self):
        """This function is used to test if all sides in a Traingel are different in length"""
        flag = True
        if self.a+self.b <= self.c or self.a+self.c <= self.b or self.b+self.c < self.a:
            flag = False
        if self.a == self.b or self.b == self.c or self.a == self.c:
            flag = False
        return flag

    def rightTriangle(self):
        """This function is used to test if a triangle have three sides with lengths, a, b, and c where a2 + b2 = c2"""
        flag = False
        if self.a**2+self.b**2 == self.c**2:
            flag = True
        if self.a ** 2 + self.c ** 2 == self.b ** 2:
            flag = True
        if self.b ** 2 + self.c ** 2 == self.a ** 2:
            flag = True
        return flag


