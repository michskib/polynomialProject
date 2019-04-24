class Polynomial_3:
    def __init__(self, a, b, c, d):
        self.coefficients = [a, b, c, d]

    # print polynomial in standard form
    def printPoly(self):
        print(self.getString())

    # returns polynomial string in standard form, based on self.factors
    def getString(self):
        handledCoefficients = list( map(self.handleCoefficient, self.coefficients) )
        return self.joinCoefficients(handledCoefficients)
    
    # prepare single polynomial factor to be in proper way to be printed
    def handleCoefficient(self, x):
        result = str(x)
        if x == -1: result = '-'
        elif x == 1: result = '+'
        elif x > 0: result = '+' + result
        return result

    # create string from prepared factors
    def joinCoefficients(self, list_factor):
        result = ''
        coefficientDegree = 3
        for currentCoefficient in list_factor:
            if currentCoefficient != 0: result += currentCoefficient + 'x^' + str(coefficientDegree)
            coefficientDegree -= 1
        result = result.replace('x^0', '')
        result = result.replace('x^1', 'x')
        if result[0] == '+': result = result[1:]
        if result[-1] == '-': result += '1'
        return result

p = Polynomial_3(1,2,3,4)
p.printPoly()