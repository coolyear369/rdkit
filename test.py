from rdkit import Chem
import requests
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

morphine_url = "https://go.drugbank.com/structures/small_molecule_drugs/DB00295.mol"
morphine_mol = requests.get(morphine_url).text
morphine = Chem.MolFromMolBlock(morphine_mol)
ms = Chem.MolToSmiles(morphine)
ms2 = Chem.MolToSmiles(morphine, isomericSmiles = False)
print(ms2)