class Fraction:
    # initial function ---> constructor
    def __init__(self, ss, mm):
        self.s = int(ss)
        self.m = int(mm)

    # sum to fractions
    def sum(self, kasr2):
        result_s = (self.s * kasr2.m) + (self.m * kasr2.s)
        result_m = self.m * kasr2.m
        x = Fraction(result_s, result_m)
        return x

    # multiply to fractions
    def mul(self, kasr2):
        result_s = self.s * kasr2.s
        result_m = self.m * kasr2.m
        x = Fraction(result_s, result_m)
        return x

    # divide to fractions
    def div(self, kasr2):
        result_s = self.s * kasr2.m
        result_m = self.m * kasr2.s
        x = Fraction(result_s, result_m)
        return x

    # subtrac to fraction
    def sub(self, kasr2):
        result_s = (self.s * kasr2.m) - (self.m * kasr2.s)
        result_m = self.m * kasr2.m
        x = Fraction(result_s, result_m)
        return x

    # convert fraction to number by dividing numerator to denominator
    def fraction_to_number(self):
        result = self.s / self.m
        return result

    # simplifying fractions (find biggest The Greatest Common Divisor {B.m.m})
    def simplifying_fractions(self):
        bmm = 0
        for i in range(2, self.s + 1):
            if self.s % i == 0 and self.m % i == 0:
                if i > bmm :
                    bmm = i
        x = Fraction(self.s / bmm, self.m / bmm)
        return x
            
    # show numerator and denominator in fraction template
    def show(self):
        print(self.s, "/", self.m)


k1 = Fraction(72, 90)

k2 = Fraction(1, 3)

k3 = k1.sum(k2)

k4 = k3.fraction_to_number()

k5 = k1.simplifying_fractions()


k1.show()
print("--------------")
k2.show()
print("--------------")
k3.show()
print("--------------")
print(k4)
print("--------------")
k5.show()
