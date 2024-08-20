from rdkit import Chem
import requests
from rdkit.Chem import Draw
from rdkit.Chem import AllChem


unknown = Chem.MolFromSmiles("CSNNSP")
img = Draw.MolToImage(unknown)
img.show()
AddH = Chem.AddHs(unknown)
AllChem.Compute2DCoords(AddH)
AddHP = Draw.MolToImage(AddH)
AddHP.show()