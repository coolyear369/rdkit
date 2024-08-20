from rdkit import Chem
import requests
from rdkit.Chem import Draw
from rdkit.Chem import AllChem


#part 1 圖片
unknown = Chem.MolFromSmiles("CSNNSP")
img = Draw.MolToImage(unknown)
img.show()
AddH = Chem.AddHs(unknown) #AddH為unknown加上氫原子
AllChem.Compute2DCoords(AddH)
AddHP = Draw.MolToImage(AddH)
AddHP.show()



#part 2 分子座標
AllChem.EmbedMolecule(AddH)
AllChem.UFFOptimizeMolecule(AddH)
conformer = AddH.GetConformer()
atoms = AddH.GetAtoms()
with open("AddH.xyz", "w") as xyzfile:
    atomsn = len(atoms)
    xyzfile.write(f"{atomsn} atoms\n")
    for atom in atoms:
        pos = conformer.GetAtomPosition(atom.GetIdx())
        xyzfile.write(f"{atom.GetSymbol()} {pos.x:.4f} {pos.y:.4f} {pos.z:.4f}\n")
with open("AddH.xyz", "r") as xyzfile:
    content = xyzfile.read()
    print(content)