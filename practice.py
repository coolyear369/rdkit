import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
from rdkit import Chem
import requests

morphine_url = "https://go.drugbank.com/structures/small_molecule_drugs/DB00295.mol"
morphine_mol = requests.get(morphine_url).text
morphine = Chem.MolFromMolBlock(morphine_mol)

from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors

morphinep = Draw.MolToImage(morphine)
morphinep.show()
morphineH = Chem.AddHs(morphine)
AllChem.Compute2DCoords(morphineH)
morphineHp = Draw.MolToImage(morphineH)
morphineHp.show()
AllChem.EmbedMolecule(morphine)
AllChem.UFFOptimizeMolecule(morphine)
conformer = morphine.GetConformer()
atoms = morphine.GetAtoms()
with open("morphine_xyz", "w") as xyzfile:
    atomsn = len(atoms)
    for atom in atoms:
        pos = conformer.GetAtomPosition(atom.GetIdx())
        xyzfile.write(f"{atom.GetSymbol()} {pos.x:.4f} {pos.y:.4f} {pos.z:.4f}\n")
with open("morphine_xyz", "r") as xyzfile:
    content = xyzfile.read()
    print(content)





