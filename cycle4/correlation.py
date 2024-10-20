#Experiment4.5:= Compute pearson product-moment correlation coefficients of two given NumPy arrays
import numpy as np
from scipy.stats import pearsonr 
corr,p = pearsonr(np.array([1,2,3,4,5,6,7,8,9,10]),np.array([10,9,8,7,6,5,4,3,2,1]))
print("Pearson product-moment correlation coefficient is",corr)
