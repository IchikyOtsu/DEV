from classeFraction import Fraction

def main():
    fract=Fraction(8,6)
    fract2=Fraction(3,4)
    print(fract.__sub__(Fraction(1,5))) # fract - 1/5 
    print(Fraction(1,2).is_integer())


if __name__ == "__main__":
    main()
