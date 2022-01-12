#Tests_panda
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
df = pd.read_csv('https://bit.ly/ds-house-price-clean')
gp=df['분양가'].plot(kind='line')

