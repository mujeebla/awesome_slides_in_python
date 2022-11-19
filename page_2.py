import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

from canvass import Base

penguins = pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/c19a904462482430170bfe2c718775ddb7dbb885/inst/extdata/penguins.csv")
penguins.dropna(inplace=True)

df = penguins.groupby(['species','island']).size().unstack().fillna(0)
df2 = df.apply(lambda x : x.div(x.sum())*100, axis=1)

fig = plt.figure(FigureClass=Base, header="Penguins: Species over Islands", pagenumber=2)
fig.subplots_adjust(bottom=0.25, top=0.75, left=0.2, hspace=0.3, right=0.8, wspace=0.1)


ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)


ax1.matshow(df2.values,cmap='Blues', aspect='auto')
im = ax2.matshow(df2.values,cmap='Blues', aspect='auto')


# Ticks
for ax in [ax1, ax2]:
    ax.set_xticks(range(len(df.columns)))
    ax.set_xticklabels(df.columns, fontsize="small")

ax1.set_yticks(range(len(df.index)))
ax1.set_yticklabels(df.index, fontsize="small")

ax2.set_yticks([])

divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="5%", pad=0.5)

for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax1.text(j, i, f'{df.iloc[i, j]:.0f}', size="x-small",
                       ha="center", va="center", color="black")

for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax2.text(j, i, f'{df2.iloc[i, j]:.0f}%', size="x-small",
                       ha="center", va="center", color="black")
plt.colorbar(im, cax=cax)


# Annotations
caption1 = "Add comments here."
fig.text(.5, .15, caption1, ha='center',va='top', fontsize='small', linespacing=1.5)



plt.savefig("page2.pdf")