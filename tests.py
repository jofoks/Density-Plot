import unittest
from main import getAtoms, getMolecularMass

class GetAtomsCase(unittest.TestCase):
    def setUp(self):
        self.single = 'O'
        self.short = 'N2'
        self.double = 'Ar2'
        self.long = 'CF2HCH3'
        self.complex = 'C8H10N4O2'
        self.implossible = 'CH9875N18'
        self.short_inv_case = 'co2'
        self.long_inv_case = 'C6h12O6'

    def test_output(self):
        self.assertEqual( getAtoms(self.single)         , {'O':1}, "Should be: {'O':1}")
        self.assertEqual( getAtoms(self.short)          , {'N':2}, "Should be: {'N':2}")
        self.assertEqual( getAtoms(self.double)         , {'Ar':2}, "Should be: {'Ar':2}")
        self.assertEqual( getAtoms(self.long)           , {'C':2,'F':2,'H':4}, "Should be: {'C':2,'F':2,'H':4}")
        self.assertEqual( getAtoms(self.complex)        , {'C':8,'H':10,'N':4,'O':2,}, "Should be: {'C':8,'H':10,'N':4,'O':2,}")
        self.assertEqual( getAtoms(self.implossible)    , {'C':1,'H':9875,'N':18}, "Should be: {'C':8,'H':10,'N':4,'O':2,}")

    def test_exceptions(self):
        self.assertRaises(AssertionError,  getAtoms, self.short_inv_case)
        self.assertRaises(AssertionError,  getAtoms, self.long_inv_case)

class GetMassCase(unittest.TestCase):
    def setUp(self):
        self.single = 'O'
        self.short = 'N2'
        self.double = 'Ar2'
        self.long = 'CF2HCH3'

    def test_output(self):
        self.assertEqual( getMolecularMass(self.single)         , 15.999)
        self.assertEqual( getMolecularMass(self.short)          , 28.014)
        self.assertEqual( getMolecularMass(self.double)         , 79.896)
        self.assertEqual( getMolecularMass(self.long)           , 66.046)

if __name__ == '__main__':
    unittest.main()