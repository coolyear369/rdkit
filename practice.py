import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns


df = pd.read_csv("cardata.csv")
x = df.iloc[:, :3 + 4]
y = df.iloc[:, 3]