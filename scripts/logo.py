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


def draw_path(vertices, ax=None):
    last_vertex = vertices[1]
    for vertex in vertices[:-1]:
        x1 = last_vertex[0]
        y1 = last_vertex[1]
        x2 = vertex[0]
        y2 = vertex[1]
        ax.plot([x1, x2], [y1, y2], color=LINE_COLOR, zorder=0)
        ax.scatter(x1, y1, color=BALL_COLOR, zorder=1)
        last_vertex = vertex


#%%
fig, ax = plt.subplots(1, 1, figsize=(8, 4))

n_path = TextPath((0, 0), "N", size=20)
draw_path(n_path.vertices, ax=ax)

d_path = TextPath((14, 0), "D", size=20)
draw_path(d_path.vertices[:23], ax=ax)
draw_path(d_path.vertices[23:], ax=ax)

s_path = TextPath((28, 0), "S", size=20)
draw_path(s_path.vertices, ax=ax)

#%%

from scipy.interpolate import splprep, splev

# vertices = n_path.vertices.copy()[0:-1].T
# vertices = d_path.vertices.copy().T
tck, u = splprep(vertices, u=None, s=5, per=1)
u_new = np.linspace(u.min(), u.max(), 1000)
x_new, y_new = splev(u_new, tck, der=0)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
plt.plot(vertices[0], vertices[1], "ro")
plt.plot(x_new, y_new, "b--")
