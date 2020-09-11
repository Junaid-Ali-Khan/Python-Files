import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/Sawari Data/newOutputFile.csv')

df['Distance Rank'] = round(df['Distance Diff'].rank(pct=True)*100,2)
df['Time Rank'] = round(df['Time Diff'].rank(pct=True)*100,2)

df['Time Diff'].hist(bins=50)
plt.title('NB vs ATA Time Difference', fontsize=15)
plt.xlabel('Time (min)', fontsize=12)
plt.show()

# df.to_csv('/home/junaid/Downloads/Bykea Technologies/NB and Google/ATA_analysis/NB_vs_ATA.csv')