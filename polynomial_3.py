class Polynomial_3:
    def __init__(self, a, b, c, d):
        self.factors = [a, b, c, d]

    # print polynomial in standard form
    def printPoly(self):
        print(self.getString())

    # returns polynomial string in standard form, based on self.factors
    def getString(self):
        handledFactors = list( map(self.handleFactor, self.factors) )
        return self.joinFactors(handledFactors)
    
    # prepare single polynomial factor to be in proper way to be printed
    def handleFactor(self, x):
        result = str(x)
        if x == -1: result = '-'
        elif x == 1: result = '+'
        elif x > 0: result = '+' + result
        return result

    # create string from prepared factors
    def joinFactors(self, list_factor):
        result = ''
        if list_factor[0] != '0': result += list_factor[0] + 'x^3'
        if list_factor[1] != '0': result += list_factor[1] + 'x^2'
        if list_factor[2] != '0': result += list_factor[2]+ 'x'
        if list_factor[3] != '0': result += list_factor[3]
        if result[0] == '+': result = result[1:]
        if result[-1] == '-': result += '1'
        return result