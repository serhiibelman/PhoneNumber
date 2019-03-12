class PhoneNumber:
    """
    Z - Country code
    YY - City/operator code
    N - Seven-digit number
    """

    def __init__(self, Z, YY, N):
        self.Z = Z
        self.YY = YY
        self.N = N

    @classmethod
    def fromstring(cls, number):
        """ number format: '+380YYNNNNNNN' """
        try:
            Z, YY, N = number[1:4], number[4:6], number[6:]
            if len(Z) == 3 and len(YY) == 2 and len(N) == 7:
                return cls(Z, YY, N)
        except TypeError:
            return None

    @property
    def international(self):
        return '{}{}{}'.format(self.Z, self.YY, self.N)

    def __str__(self):
        return self.international


if __name__ == '__main__': 
    num = '+380660000666'
    phone = PhoneNumber.fromstring(num)
    print(phone.Z)
    print(phone.YY)
    print(phone.N)
    print(phone)
