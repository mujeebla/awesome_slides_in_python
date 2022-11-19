import matplotlib.pyplot as plt
from canvass import Base



fig = plt.figure(FigureClass=Base, header="Penguins", pagenumber=3)
fig.subplots_adjust(bottom=0.15, top=0.8, left=0.1, hspace=0.3, right=0.95, wspace=0.1)



plt.savefig("sample.pdf")
