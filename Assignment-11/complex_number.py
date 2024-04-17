# complex number : z = x1 + iy1
class Complex_Number:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    # sum two complex number
    def sum(self, Cn):
        sum_x = self.x + Cn.x
        sum_y = self.y + Cn.y
        c_n = Complex_Number(sum_x, sum_y)
        return c_n
    
    # sub two complex number
    def sub(self, Cn):
        sum_x = self.x - Cn.x
        sum_y = self.y - Cn.y
        c_n = Complex_Number(sum_x, sum_y)
        return c_n
    
    # mul two complex number
    def mul(self, Cn):
        mul_1 = (self.x * Cn.x) - (self.y * Cn.y)
        mul_2 = (self.x * Cn.y) + (self.y * Cn.x)
        c_n = Complex_Number(mul_1, mul_2)
        return c_n

    def show(self):
        if self.y<0:
            op = '-'
        else:
            op = '+'
        print(self.x, op, str(self.y) +  "i")

cn1 = Complex_Number(7,4)
cn1.show()

cn2 = Complex_Number(5,3)
cn2.show()

cn3 = cn1.sum(cn2)
cn3.show()

cn4 = cn1.mul(cn2)
cn4.show()

cn5 = cn1.sub(cn2)
cn5.show()