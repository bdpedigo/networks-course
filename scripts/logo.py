#%%
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.textpath import TextPath
import numpy as np
from matplotlib.font_manager import FontProperties

fp = FontProperties(family="monospace", style="normal")


colors = sns.color_palette()

BALL_COLOR = colors[1]
LINE_COLOR = colors[0]


def draw_path(vertices, ax=None):
    last_vertex = vertices[1]
    for vertex in vertices[:]:
        x1 = last_vertex[0]
        y1 = last_vertex[1]
        x2 = vertex[0]
        y2 = vertex[1]
        ax.plot([x1, x2], [y1, y2], color=LINE_COLOR, zorder=0)
        ax.scatter(x1, y1, color=BALL_COLOR, zorder=1)
        last_vertex = vertex


#%%
n_path = TextPath((0, 0), "N", size=20)
d_path = TextPath((14, 0), "D", size=20)
s_path = TextPath((28, 0), "S", size=20)


n_vertices = n_path.vertices[:-1]
d_outer_vertices = d_path.vertices[:22]
d_inner_vertices = d_path.vertices[23:-1]
s_vertices = s_path.vertices[:-1]

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
draw_path(n_vertices, ax=ax)
draw_path(d_outer_vertices, ax=ax)
draw_path(d_inner_vertices, ax=ax)
draw_path(s_vertices, ax=ax)

#%%
from sklearn.metrics import pairwise_distances

vertices = d_outer_vertices
pdist = pairwise_distances(vertices)
n = pdist.shape[0]
i_indices = np.arange(n - 1)
j_indices = np.arange(1, n)
dists = pdist[(i_indices, j_indices)]
dists = np.array([0] + list(dists))
cum_dists = np.cumsum(dists) / dists.sum()
cum_dists


def sample_new_point():
    sample_dist = np.random.uniform()

    upper_ind = np.digitize(sample_dist, cum_dists)
    lower_ind = upper_ind - 1

    start = vertices[lower_ind]
    end = vertices[upper_ind]
    dist = pdist[lower_ind, upper_ind]

    subdist = np.random.uniform()

    new_point = subdist * start + (1 - subdist) * end
    return new_point


n_points = 100
points = []
for i in range(n_points):
    points.append(sample_new_point())

points = np.array(points)
points

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.scatter(points[:, 0], points[:, 1])
draw_path(vertices, ax=ax)


#%%

from scipy.interpolate import splprep, splev

# vertices = n_path.vertices.copy()[0:-1].T
# vertices = d_path.vertices.copy().T
n_vertices = n_path.vertices[:-1]
s_vertices = s_path.vertices[:-1]
d_outer_vertices = d_path.vertices[:22]
vertices = d_outer_vertices.T
tck, u = splprep(vertices.copy(), u=None, s=5, per=1)
u_new = np.linspace(u.min(), u.max(), 1000)
x_new, y_new = splev(u_new, tck, der=0)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
plt.plot(vertices[0], vertices[1], "ro")
plt.plot(x_new, y_new, "b--")

#%%
