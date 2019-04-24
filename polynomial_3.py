class Polynomial_3:
    def __init__(self, a, b, c, d):
        self.monomials = [a, b, c, d]

    # print polynomial in standard form
    def printPoly(self):
        print(self.getString())

    # returns polynomial string in standard form, based on self.factors
    def getString(self):
        handledMonomials = list( map(self.handleMonomial, self.monomials) )
        return self.joinMonomials(handledMonomials)
    
    # prepare single polynomial factor to be in proper way to be printed
    def handleMonomial(self, x):
        result = str(x)
        if x == -1: result = '-'
        elif x == 1: result = '+'
        elif x > 0: result = '+' + result
        return result

    # create string from prepared factors
    def joinMonomials(self, list_factor):
        result = ''
        monomialDegree = 3
        for currentMonomial in list_factor:
            if currentMonomial != 0: result += currentMonomial + 'x^' + str(monomialDegree)
            monomialDegree -= 1
        result = result.replace('x^0', '')
        result = result.replace('x^1', 'x')
        if result[0] == '+': result = result[1:]
        if result[-1] == '-': result += '1'
        return result

p = Polynomial_3(1,2,3,4)
p.printPoly()