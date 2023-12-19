import unittest
from classeFraction import Fraction

class TestFractionInitialization(unittest.TestCase):

    #__init__
    def test_normal_fraction(self):
        fraction = Fraction(1, 2)
        self.assertEqual((fraction.numerator, fraction.denominator), (1, 2))

    def test_zero_numerator(self):
        fraction = Fraction(0, 3)
        self.assertEqual((fraction.numerator, fraction.denominator), (0, 1))

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_fraction_reduction(self):
        fraction = Fraction(2, 4)
        self.assertEqual((fraction.numerator, fraction.denominator), (1, 2))

    def test_negative_denominator(self):
        fraction = Fraction(1, -2)
        self.assertEqual((fraction.numerator, fraction.denominator), (-1, 2))

    def test_both_negative(self):
        fraction = Fraction(-1, -2)
        self.assertEqual((fraction.numerator, fraction.denominator), (1, 2))

    def test_negative_numerator(self):
        fraction = Fraction(-1, 2)
        self.assertEqual((fraction.numerator, fraction.denominator), (-1, 2))

    #as_mixed_number()
    def test_mixed_number_mix(self):
        fraction = Fraction(5, 3)
        self.assertEqual(fraction.as_mixed_number(), "1 + 2/3")

    def test_integer_equivalent_mix(self):
        fraction = Fraction(4, 2)
        self.assertEqual(fraction.as_mixed_number(), "2 + 0/1")

    def test_negative_fraction_mix(self):
        fraction = Fraction(-5, 3)
        self.assertEqual(fraction.as_mixed_number(), "-2 + 1/3")

    def test_zero_numerator_mix(self):
        fraction = Fraction(0, 3)
        self.assertEqual(fraction.as_mixed_number(), "0 + 0/1")

    def test_reduced_fraction_mix(self):
        fraction = Fraction(2, 3)
        self.assertEqual(fraction.as_mixed_number(), "0 + 2/3")



    # __add__()
    def test_addition_same_denominator(self):
        # Teste l'addition de fractions ayant le même dénominateur.
        frac1 = Fraction(1, 3)
        frac2 = Fraction(2, 3)
        result = frac1 + frac2
        self.assertEqual((result.numerator, result.denominator), (1, 1))

    def test_addition_different_denominators(self):
        # Teste l'addition de fractions avec différents dénominateurs.
        frac1 = Fraction(1, 4)
        frac2 = Fraction(1, 2)
        result = frac1 + frac2
        self.assertEqual((result.numerator, result.denominator), (3, 4))

    def test_addition_negative_fraction(self):
        # Teste l'addition impliquant des fractions négatives.
        frac1 = Fraction(-1, 3)
        frac2 = Fraction(1, 3)
        result = frac1 + frac2
        self.assertEqual((result.numerator, result.denominator), (0, 1))

    def test_addition_with_zero(self):
        # Teste l'addition d'une fraction avec une fraction ayant un numérateur de zéro.
        frac1 = Fraction(0, 3)
        frac2 = Fraction(1, 3)
        result = frac1 + frac2
        self.assertEqual((result.numerator, result.denominator), (1, 3))

    def test_addition_incompatible_type(self):
        # Teste l'addition avec un type non-Fraction pour vérifier si une exception est levée.
        frac1 = Fraction(1, 2)
        with self.assertRaises(TypeError):
            frac1 + 3

    def test_self_addition(self):
        # Teste l'auto-addition (une fraction additionnée à elle-même).
        frac = Fraction(1, 2)
        result = frac + frac
        self.assertEqual((result.numerator, result.denominator), (1, 1))

    
    # Tests pour __sub__
    def test_subtraction_same_denominator(self):
        # Soustraction de fractions avec le même dénominateur
        frac1 = Fraction(3, 4)
        frac2 = Fraction(1, 4)
        result = frac1 - frac2
        self.assertEqual((result.numerator, result.denominator), (1, 2))

    def test_subtraction_different_denominators(self):
        # Soustraction de fractions avec des dénominateurs différents
        frac1 = Fraction(1, 3)
        frac2 = Fraction(1, 6)
        result = frac1 - frac2
        self.assertEqual((result.numerator, result.denominator), (1, 6))

    def test_subtraction_negative_fraction(self):
        # Soustraction impliquant une fraction négative
        frac1 = Fraction(-1, 4)
        frac2 = Fraction(1, 4)
        result = frac1 - frac2
        self.assertEqual((result.numerator, result.denominator), (-1, 2))

    def test_subtraction_incompatible_type(self):
        # Gestion des erreurs pour un type non compatible
        frac1 = Fraction(1, 2)
        with self.assertRaises(TypeError):
            frac1 - 3


    # Tests pour __mul__
    def test_multiplication(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        result = frac1 * frac2
        self.assertEqual((result.numerator, result.denominator), (1, 3))

    def test_multiplication_negative(self):
        frac1 = Fraction(-1, 2)
        frac2 = Fraction(2, 3)
        result = frac1 * frac2
        self.assertEqual((result.numerator, result.denominator), (-1, 3))

    def test_multiplication_incompatible_type(self):
        frac = Fraction(1, 2)
        with self.assertRaises(TypeError):
            frac * "test"

    # Tests pour __truediv__
    def test_division(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        result = frac1 / frac2
        self.assertEqual((result.numerator, result.denominator), (3, 4))

    def test_division_by_zero(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(0, 1)
        with self.assertRaises(ZeroDivisionError):
            frac1 / frac2

    def test_division_incompatible_type(self):
        frac = Fraction(1, 2)
        with self.assertRaises(TypeError):
            frac / "test"

    # Tests pour __pow__
    def test_power_positive(self):
        frac = Fraction(1, 2)
        result = frac ** 2
        self.assertEqual((result.numerator, result.denominator), (1, 4))

    def test_power_zero(self):
        frac = Fraction(1, 2)
        result = frac ** 0
        self.assertEqual((result.numerator, result.denominator), (1, 1))

    def test_power_incompatible_type(self):
        frac = Fraction(1, 2)
        with self.assertRaises(TypeError):
            frac ** 0.5

    # Tests pour __eq__
    def test_equality(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 4)
        self.assertTrue(frac1 == frac2)

    def test_inequality(self):
        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        self.assertFalse(frac1 == frac2)

    def test_equality_incompatible_type(self):
        frac = Fraction(1, 2)
        with self.assertRaises(TypeError):
            frac == "test"

    # Tests pour __float__
    def test_float_conversion(self):
        frac = Fraction(1, 2)
        self.assertEqual(float(frac), 0.5)

    
    # Tests pour __lt__ (moins que)
    def test_less_than_same_denominator(self):
        self.assertTrue(Fraction(1, 3) < Fraction(2, 3))

    def test_less_than_different_denominators(self):
        self.assertTrue(Fraction(1, 4) < Fraction(1, 2))

    def test_less_than_incompatible_type(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) < 3

    # Tests pour __gt__ (plus grand que)
    def test_greater_than_same_denominator(self):
        self.assertTrue(Fraction(2, 3) > Fraction(1, 3))

    def test_greater_than_different_denominators(self):
        self.assertTrue(Fraction(1, 2) > Fraction(1, 4))

    def test_greater_than_incompatible_type(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) > 3

    # Tests pour __ne__ (non égal)
    def test_not_equal(self):
        self.assertTrue(Fraction(1, 2) != Fraction(2, 3))

    def test_not_equal_same_fraction(self):
        self.assertFalse(Fraction(1, 2) != Fraction(1, 2))

    def test_not_equal_incompatible_type(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) != "test"

    # Tests pour __le__ (moins que ou égal)
    def test_less_than_or_equal_same_denominator(self):
        self.assertTrue(Fraction(1, 3) <= Fraction(1, 3))

    def test_less_than_or_equal_different_denominators(self):
        self.assertTrue(Fraction(1, 4) <= Fraction(1, 2))

    def test_less_than_or_equal_incompatible_type(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) <= 3

    # Tests pour __ge__ (plus grand que ou égal)
    def test_greater_than_or_equal_same_denominator(self):
        self.assertTrue(Fraction(2, 3) >= Fraction(2, 3))

    def test_greater_than_or_equal_different_denominators(self):
        self.assertTrue(Fraction(1, 2) >= Fraction(1, 4))

    def test_greater_than_or_equal_incompatible_type(self):
        with self.assertRaises(TypeError):
            Fraction(1, 2) >= 3

    # Tests pour is_zero
    def test_is_zero_true(self):
        self.assertTrue(Fraction(0, 3).is_zero())

    def test_is_zero_false(self):
        self.assertFalse(Fraction(1, 3).is_zero())

    # Tests pour is_integer
    def test_is_integer_true(self):
        self.assertTrue(Fraction(2, 2).is_integer())

    def test_is_integer_false(self):
        self.assertFalse(Fraction(1, 3).is_integer())

    # Tests pour is_proper
    def test_is_proper_true(self):
        self.assertTrue(Fraction(1, 3).is_proper())

    def test_is_proper_false(self):
        self.assertFalse(Fraction(5, 4).is_proper())

    # Tests pour is_unit
    def test_is_unit_true(self):
        self.assertTrue(Fraction(1, 3).is_unit())

    def test_is_unit_false(self):
        self.assertFalse(Fraction(2, 3).is_unit())

    # Tests pour is_adjacent_to
    def test_is_adjacent_to_false(self):
        self.assertFalse(Fraction(1, 2).is_adjacent_to(Fraction(1, 2)))

    def test_is_adjacent_to_true(self):
        self.assertTrue(Fraction(1, 3).is_adjacent_to(Fraction(2, 3)))


    #__str__
    def test_reduced_fraction(self):
        # Tester une fraction déjà réduite
        fraction = Fraction(1, 3)
        self.assertEqual(str(fraction), "1/3")

    def test_negative_fraction(self):
        # Tester la représentation textuelle d'une fraction négative
        fraction = Fraction(-1, 3)
        self.assertEqual(str(fraction), "-1/3")

    def test_zero_numerator(self):
        # Tester une fraction avec un numérateur de zéro
        fraction = Fraction(0, 3)
        self.assertEqual(str(fraction), "0")
            
if __name__ == '__main__':
    unittest.main()
