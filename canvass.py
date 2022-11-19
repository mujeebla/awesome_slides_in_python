import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.patches as patches
import matplotlib.lines as lines
import numpy as np
import matplotlib.image as image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from datetime import datetime




plt.rcParams['font.size']=18
plt.rcParams['font.family']="Arial"


class Base(Figure):

	def __init__(self,*args, header=None, pagenumber=None,**kwargs):
		super().__init__(*args, **kwargs)
		"""
		Define Base Class
		"""
		# Header section, added horizontal line
		if header is not None:
			self.add_artist(lines.Line2D([0.05, 0.05], [0.9, 0.95], c="black", linewidth=3))
			self.text(0.06, 0.9, header, fontsize="xx-large", ha="left", va="baseline",
				fontweight="bold")

		self.subplots_adjust(bottom=0.1, top=0.85)
		self.set_size_inches(13.333,7.5)
		self.set_facecolor("#FBFBFB")
		self.text(0.5, 0.015, "Propert of Penguins", fontsize="x-small", 
			ha="center", va="baseline")

		# Page Number
		if pagenumber is not None:
			self.pagenumber=pagenumber
			self.text(0.045, 0.015, self.pagenumber, fontsize="medium", 
				ha="center", va="baseline")
		else:
			self.pagenumber=pagenumber

