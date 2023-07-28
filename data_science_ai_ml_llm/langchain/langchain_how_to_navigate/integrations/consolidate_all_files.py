import pandas as pd
import glob

df_consolidated = pd.DataFrame()

for file in glob.glob("./*_sub.csv"):
    df_current = pd.read_csv(file)
    df_consolidated = pd.concat([df_consolidated,df_current])
    del df_current

df_consolidated.to_csv("CONSOLIDATED_INTEGRATIONS.csv",index=False)
