from classeFraction import Fraction

def main():
    f=Fraction(8,6)
    f2=Fraction(3,4)
    print(f.__sub__(Fraction(1,5)))
    print(Fraction(1,2).is_integer())


if __name__ == "__main__":
    main()