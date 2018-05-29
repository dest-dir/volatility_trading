from __future__ import print_function
from datetime import datetime

import matplotlib.pyplot as plt
import tradingWithPython as twp  
import pandas as pd
import numpy as np
import time

#Load csv as pandas dataframe, rename columns for pybacktest backend
svxy = pd.read_csv('~/quantalgo/svxy.csv', index_col='date')
svxy = svxy.rename(columns={'open': 'O', 'high': 'H', 'low': 'L','close': 'C','volume': 'V'})

uvxy = pd.read_csv('~/quantalgo/uvxy.csv', index_col='date')
uvxy = uvxy.rename(columns={'open': 'O', 'high': 'H', 'low': 'L','close': 'C','volume': 'V'})

tqqq = pd.read_csv('~/quantalgo/tqqq.csv', index_col='date')
tqqq = tqqq.rename(columns={'open': 'O', 'high': 'H', 'low': 'L','close': 'C','volume': 'V'})

vix = pd.read_csv('~/quantalgo/vix.csv', index_col='date')
spyg = pd.read_csv('~/quantalgo/spyg.csv', index_col='date')
spy = pd.read_csv('~/quantalgo/spy.csv', index_col='date')
vxv = pd.read_csv('~/quantalgo/vxv.csv', index_col='date')
vx1 = pd.read_csv('~/quantalgo/vx1.csv', index_col='date')
vx2 = pd.read_csv('~/quantalgo/vx2.csv', index_col='date')

# Calculating the gap between spot vix and the first month vix future
last_ratio_v_v1 = vix.close / vx1.settle

# Calculating the contango ratio of the front and second month VIX Futures 
last_ratio_v1_v2 = vx1.close / vx2.settle

# Blending the previous two ratios together using a weighted average
ratio_weight = 0.7
last_ratio = (ratio_weight*last_ratio_v_v1) + ((1-ratio_weight)*last_ratio_v1_v2) - 1
