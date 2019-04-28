from decimal import *

class Polynomial_3:
    def __init__(self, a, b, c, d):
        self.coefficients = [a, b, c, d]
        self.nwd = self.__maxCommonDivisor()
        self.workOnCoefficients = list( map(self.__divide, self.coefficients) ) 
        self.delta = 18*self.workOnCoefficients[0]*self.workOnCoefficients[1]*self.workOnCoefficients[2]*self.workOnCoefficients[3]-4*pow(self.workOnCoefficients[1],3)*self.workOnCoefficients[3]+pow(self.workOnCoefficients[1]*self.workOnCoefficients[2], 2)-4*self.workOnCoefficients[0]*pow(self.workOnCoefficients[2],3)-27*pow(self.workOnCoefficients[0]*self.workOnCoefficients[3], 2)

    # returns polynomial string in standard form, based on self.factors
    def getString(self):
        handledCoefficients = list( map(self.__handleCoefficient, self.coefficients) )
        return self.__joinCoefficients(handledCoefficients)
    
    # prepare single polynomial factor to be in proper way to be printed in standard form
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
        if len(roots) != 0:
            roots = self.__filtrRoots(roots)
        if len(roots) == 0: return self.__calculateApproximateRoots()
        elif len(roots) == 1 and self.delta > 0: return self.__calculateApproximateRoots()
        elif len(roots) == 1 and self.delta == 0: return self.__checkForSecondRoot()
        elif len(roots) == 1 and self.delta < 0: return roots
        elif len(roots) == 2 and self.delta > 0: return self.__calculateApproximateRoots()
        elif len(roots) == 2 and self.delta == 0: return self.__findDoubleRoot()
        elif len(roots) == 2 and self.delta < 0: return 'Fuck you math'
        elif len(roots) == 3 and self.delta > 0: return roots
        elif len(roots) == 3 and self.delta <=0: return 'Fuck you math'
        
        return roots
    
    def __calculateApproximateRoots(self):
        return 0

    def __checkForSecondRoot(self):
        return 0

    def __findDoubleRoot(self):
        return 0

    def __calculateRoots(self):
        getcontext().prec = 10
        p = self.__findDivisors(self.workOnCoefficients[3])
        q = self.__findDivisors(self.workOnCoefficients[0])
        result = []
        for current_p in p:
            for current_q in q:
                check = self.__polynomialValue(current_p, current_q)
                if check == 0: result.append(current_p/current_q)
                check = self.__polynomialValue(-1*current_p, current_q)
                if check == 0: result.append(-current_p/current_q)
        return result

    def __maxCommonDivisor(self):
        result = self.coefficients[0]
        for x in range(1, 4):
            if self.coefficients[x] != 0: result = self.__NWD(result, self.coefficients[x])
        if result < 0: result *= -1
        return result

    def __NWD(self, m, n):
         while True:
            r = m % n
            if not r: return n
            m, n = n, r

    def __findDivisors(self, numb):
        divisorsList = []
        if numb < 0: numb *= -1
        numb = int(numb)
        for x in range(1, round( pow(numb, 1/2) ) + 1):
            if numb%x == 0: divisorsList.append(x)
        divisorsList = self.__fillInOpposite(divisorsList, numb)
        return divisorsList

    def __filtrRoots(self, roots):
        i = len(roots)
        indexesToRemove = []
        for x in range(0, i):
            for y in range(x+1, i):
                if roots[x] == roots[y]: 
                    indexesToRemove.append(x)
                    break
        indexesToRemove.reverse()
        return self.__removeIndexesFromList(roots, indexesToRemove)   

    def __divide(self, m):
        return m/self.nwd    

    def __fillInOpposite(self, divisorsList, numb):
        i = 0
        while True:
            divisor = numb/divisorsList[i]
            if divisor in divisorsList: return divisorsList
            else: divisorsList.append(divisor)
            i += 1

    def __polynomialValue(self, p, q):
        getcontext().prec = 100
        a = Decimal(self.workOnCoefficients[0]*pow(p,3)/pow(q,3))
        b = Decimal(self.workOnCoefficients[1]*pow(p,2)/pow(q, 2))
        c = Decimal(self.workOnCoefficients[2]*p/q)
        d = Decimal(self.workOnCoefficients[3])
        return Decimal(a + b + c +d)

    def __removeIndexesFromList(self, toHandleList, indexList):
        for x in indexList:
            toHandleList.pop(x)
        return toHandleList

p = Polynomial_3(1, 1, 0, -2)
s = p.findRoots()
print(str(s))