import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from canvass import Base

penguins = pd.read_csv("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/c19a904462482430170bfe2c718775ddb7dbb885/inst/extdata/penguins.csv")
penguins.dropna(inplace=True)

var = penguins.species.value_counts().index
val = penguins.species.value_counts().values


fig = plt.figure(FigureClass=Base, header="Penguins: Specie Size", pagenumber=1)
fig.subplots_adjust(bottom=0.25, top=0.75, left=0.2, hspace=0.3, right=0.8, wspace=0.1)

color = ['#1974D2', '#0D3AA9', '#000080']

ax = fig.add_subplot()



y_pos = 2.5*np.arange(len(var))
ax.bar(y_pos, val, align='center', width=2, alpha=0.95, color=color, zorder=100)


# Ticks
ax.set_xticks(y_pos)
xtick_labels = [f'{_},  {__}' for _,__ in zip(var, val)]
ax.set_xticklabels(xtick_labels, fontsize="x-small", fontweight='bold')


# for ax in [ax1, ax2]:
ax.set_yticks([50, 100, 150])
ax.set_yticklabels([50, 100, 150], fontsize="x-small", fontweight='bold')


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='both', colors="#000080")
for spine in ax.spines.values():
    spine.set_edgecolor("#000080")
    spine.set_linewidth(2)


for y in [50, 100, 150]:
    ax.axhline(y=y, color='#000080', alpha=0.2, zorder=5)


# Annotations
caption1 = "Add comments here"
fig.text(.5, .15, caption1, ha='center',va='top', fontsize='small', linespacing=1.5)



plt.savefig("page1.pdf")