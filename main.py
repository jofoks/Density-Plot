import pandas as pds
from collections import deque

Atoms = pds.read_csv('Data/Periodic Table of Elements.csv')
# Delete Unimportant Data for this project
del Atoms['Year']
del Atoms['Discoverer']

Molecules = pds.read_csv('Data/Molecules.csv')

# A Dataframe only containing 3 columns:
Atoms_short = Atoms[['AtomicMass', 'Density', 'Symbol']]

def getAtoms(Symbol):
    def appendResult(char, multiplier):
        if not multiplier:
            multiplier = 1
        try:
            result[char] += int(multiplier)
        except (TypeError, KeyError):
            result[char] = int(multiplier)

    result = {}
    multiplier = ''
    Sym = (c for c in Symbol)
    char = next(Sym)
    assert char.isupper(), ValueError('Symbol is case sensative!')

    while True:
        try: 
            nextChar = next(Sym)
        except:
            appendResult(char, multiplier)
            break
        if nextChar.isupper():
            appendResult(char, multiplier)
            multiplier = ''
            char = nextChar
            continue
        if nextChar.islower():
            assert (char.isupper(), multiplier == '') == (True, True), ValueError('Symbol is case sensative!')
            char = char+nextChar
            continue
        if nextChar.isdigit():
            multiplier += nextChar
    return result

def getMolecularMass(Symbol):
    totalMass = 0
    atomDict = getAtoms(Symbol)
    for atom in atomDict:
       mass = findAtomMass(atom) * atomDict[atom]
       totalMass += mass
    return totalMass

def findAtomMass(atom):
    "Get the Atom's data from the Atom DataFrame"
    for _, row in Atoms_short.iterrows():
        if row['Symbol'] == atom:
            return row['AtomicMass']

def findMolecule(name):
    "Get the molecule's data from the Molecule DataFrame"
    for _, row in Molecules.iterrows():
        if row['Name'] == name.capitalize():
            return(row)

# the composition of air by their molecule and percentage in air
def getMassAir():
    air = [
        getMolecularMass('N2') * 0.78084,
        getMolecularMass('O2') * 0.20946,
        getMolecularMass('Ar') * 0.009340,
        getMolecularMass('CO2') * 0.00041332,
        getMolecularMass('Ne') * 0.00001818,
        getMolecularMass('He') * 0.00000524,
        getMolecularMass('CH4') * 0.00000187,
        getMolecularMass('Kr') * 0.00000114,
        getMolecularMass('H2O') * 0.02,
    ]
    return sum(air)

if __name__ == "__main__":
    print(getMolecularMass('CO2'))
    print(getMolecularMass('C6H12O6'))