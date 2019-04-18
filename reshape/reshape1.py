import numpy as np
import pandas as pd

df = np.random.randn(12)
print(df)
print("")
df_reshape = df.reshape(3, 4)
print(df_reshape)
pd.DataFrame(df).to_excel('out.xlsx')
