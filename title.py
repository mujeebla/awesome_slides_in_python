import matplotlib.pyplot as plt
from canvass import Base
import matplotlib.lines as lines


fig = plt.figure(FigureClass=Base)

fig.add_artist(lines.Line2D([0.04, 0.04], [0.6, 0.65], c="black", linewidth=3))

fig.text(0.045, 0.6, "Penguin Species", fontsize="xx-large", 
	name="helvetica", ha="left", va="baseline", weight="bold")
fig.text(0.045, 0.54, "Analysis", fontsize="large",
	ha="left", va="baseline")

plt.savefig("title.pdf")