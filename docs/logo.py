#%%
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.textpath import TextPath
import numpy as np
from matplotlib.font_manager import FontProperties

fp = FontProperties(family="monospace", style="normal")


fig, ax = plt.subplots(1, 1, figsize=(8, 4))

colors = sns.color_palette()

BALL_COLOR = colors[1]
LINE_COLOR = colors[0]


def draw_path(path):
    last_vertex = path.vertices[1]
    for vertex in path.vertices[:-1]:
        x1 = last_vertex[0]
        y1 = last_vertex[1]
        x2 = vertex[0]
        y2 = vertex[1]
        ax.plot([x1, x2], [y1, y2], color=LINE_COLOR, zorder=0)
        ax.scatter(x1, y1, color=BALL_COLOR, zorder=1)
        last_vertex = vertex


path = TextPath((0, 0), "N", size=20)
draw_path(path)
path = TextPath((14, 0), "D", size=20)
draw_path(path)
path = TextPath((28, 0), "S", size=20)
draw_path(path)
