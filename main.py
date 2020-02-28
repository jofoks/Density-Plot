import pandas as pds

Atoms = pds.read_csv('Data/Periodic Table of Elements.csv')
# Delete Unimportant Data for this project
del Atoms['Year']
del Atoms['Discoverer']

Molecules = pds.read_csv('Data/Molecules.csv')

# A Dataframe only containing 3 columns:
Atoms_short = Atoms[['AtomicMass', 'Density', 'Symbol']]

def getAtoms(Symbol):
    '''Return the atoms from the Molecule Symbol
            ex. (CO2) -> [C, O, O]'''
    def parseSymbol():
        lst = []
        for char in list(Symbol):
            if char.islower():
                lst[-1] = ''.join([lst[-1], char])
            else:
                lst.append(char)
        return lst

    def solveMultipliers():
        '''Multiply last Atom in Symbol by the number after
                ex. (O2) -> 2 * O'''
        mol = []
        lst = parseSymbol()
        for num, atom in enumerate(lst):
            try:
                int(atom)
                lastAtom = lst[num-1].capitalize()
                for _ in range(int(atom)-1):
                    mol.append(lastAtom)
            except:
                mol.append(atom.capitalize())
        return mol
    return solveMultipliers()

def getMolecularMass(Symbol):
    atoms = []
    for atom in getAtoms(Symbol):
        atoms.append(findAtom(atom))
    mol_df = pds.DataFrame(atoms)
    return int(mol_df.sum(axis=0, skipna=True)['AtomicMass'])


def findAtom(atom):
    "Get the Atom's data from the Atom DataFrame"
    for _, row in Atoms_short.iterrows():
        if row['Symbol'] == atom:
            return row

def findMolecule(name):
    "Get the molecule's data from the Molecule DataFrame"
    for _, row in Molecules.iterrows():
        if row['Name'] == name.capitalize():
            return(row)

# the composition of air by their molecule and percentage in air
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
airMass = sum(air)

if __name__ == "__main__":
    print(getAtoms('CO2'))