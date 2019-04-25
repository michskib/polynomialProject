class Polynomial_3:
    def __init__(self, a, b, c, d):
        self.coefficients = [a, b, c, d]
        self.delta = 18*a*b*c*d-4*pow(b,3)*d+pow(b*c, 2)-4*a*pow(c,3)-27*pow(a*d, 2)
        self.g = 1

    # returns polynomial string in standard form, based on self.factors
    def getString(self):
        handledCoefficients = list( map(self.__handleCoefficient, self.coefficients) )
        return self.__joinCoefficients(handledCoefficients)
    
    # prepare single polynomial factor to be in proper way to be printed
    def __handleCoefficient(self, x):
        result = str(x)
        if x == -1: result = '-'
        elif x == 1: result = '+'
        elif x > 0: result = '+' + result
        return result

    # create string from prepared factors
    def __joinCoefficients(self, list_factor):
        result = ''
        coefficientDegree = 3
        for currentCoefficient in list_factor:
            if currentCoefficient != '0': result += currentCoefficient + 'x^' + str(coefficientDegree)
            coefficientDegree -= 1
        result = result.replace('x^0', '')
        result = result.replace('x^1', 'x')
        if result[0] == '+': result = result[1:]
        if result[-1] == '-' or result[-1] == '+': result += '1'
        return result

    def findRoots(self):
        roots = self.__calculateRoots()
        if len(roots) == 3 and self.delta > 0: return roots
        if len(roots) == 2 and self.delta == 0: return roots #handleDoubleRoots(roots)
        if len(roots) == 1 and self.delta == 0: return roots #handleTripleRoot(roots)
        if len(roots) == 1 and self.delta < 0: return roots
        else:
            roots = ['error']


    def __calculateRoots(self):
        p = self.__findDivisors(self.coefficients[3])
        q = self.__findDivisors(self.coefficients[0])
        check = 0
        result = []
        for current_p in p:
            for current_q in q:
                check = self.coefficients[0]*pow(current_p/current_q,3)+self.coefficients[1]*pow(current_p/current_q,2)+self.coefficients[2]*current_p/current_q+self.coefficients[3]
                if check == 0: result.append(current_p/current_q)
                check = self.coefficients[0]*pow(-current_p/current_q,3)+self.coefficients[1]*pow(-current_p/current_q,2)+self.coefficients[2]*current_p/(-current_q)+self.coefficients[3]
                if check == 0: result.append(current_p/current_q)

        return result

    def __findDivisors(self, numb):
        divisorsList = []
        if numb < 0: numb *= -1
        for x in range(1, numb + 1):
            if numb%x == 0: divisorsList.append(x)
        return divisorsList

p = Polynomial_3(1, 1, 0, -2)
roots = p.findRoots()
print(str(roots))
