from classeFraction import Fraction

def main():
    fract=Fraction(8,6)
    fract2=Fraction(3,4)
    print(fract.__sub__(Fraction(1,5))) # fract - 1/5 = 17/15
    print(Fraction(1,2).is_integer()) #false
    print(fract2.__add__(fract)) #25/12
    try: #Other must be an instance of class Fraction
        print(fract.__mul__(8/4))
    except Exception as error :
        print(error)



if __name__ == "__main__":
    main()
