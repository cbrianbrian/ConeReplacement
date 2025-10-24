import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import os

fn = 'SourceFlowData112624.csv'

df = pd.read_csv(fn)
print(df.columns)

fig = sns.relplot(df,x = 'CONE PSI',y='INLET FLOW (SLPM)', hue='SOURCE', kind = "scatter", height = 8, aspect = 1, s=30)
plt.suptitle('Kara Flow Measurements on LP4',y=1.05, fontsize = 15)

# Access the legend texts and title
legend_texts = fig._legend.get_texts()
legend_title = fig._legend.get_title()

# Set the font size for legend labels and title
plt.setp(legend_texts, fontsize='10')
plt.setp(legend_title, fontsize='10')

fig.set_axis_labels("CONE PSI", "INLET FLOW (SLPM)", fontsize=10)

for ax in fig.axes.flatten():
    ax.grid()
    ax.tick_params(labelsize=10)
    
fig.savefig(os.path.join(os.path.split(fn)[0],"Kara Flow Measurements on LP4"),dpi=300,transparent=True) 
