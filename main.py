from classeFraction import Fraction

def main():
    fract=Fraction(1,3)
    fract2=Fraction(2,3)
    diff= fract.__sub__(fract2)
    print(abs(diff.numerator))
    print(abs(diff.denominator))





if __name__ == "__main__":
    main()