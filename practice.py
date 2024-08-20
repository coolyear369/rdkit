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

img2 = Draw.MolToImage(morphine)
print(morphine.GetNumAtoms())
H = Chem.AddHs(morphine)
AllChem.Compute2DCoords(H)
Hp = Draw.MolToImage(H)
print(Descriptors.NumRotatableBonds(morphine))





