import numpy as np
import pandas as pd
castDf = pd.read_stata('cast.dta')
print(castDf['id12anm_ihds2_upd'][46950])
