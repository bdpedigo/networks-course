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

def draw_path(vertices, ax=None, scatter=True, color=None):
    last_vertex = vertices[1]
    for vertex in vertices[:]:
        x1 = last_vertex[0]
        y1 = last_vertex[1]
        x2 = vertex[0]
        y2 = vertex[1]
        ax.plot([x1, x2], [y1, y2], color=color, zorder=0, linewidth=3)
        if scatter:
            ax.scatter(x1, y1, color=color, zorder=1)
        last_vertex = vertex

from sklearn.metrics import euclidean_distances, pairwise_distances
from sklearn.metrics.pairwise import cosine_distances


def sample_new_points(vertices, n_points=100):
    pdist = pairwise_distances(vertices)
    n = pdist.shape[0]
    i_indices = np.arange(n - 1)
    j_indices = np.arange(1, n)
    dists = pdist[(i_indices, j_indices)]
    dists = np.array([0] + list(dists))
    cum_dists = np.cumsum(dists)
    norm_cum_dists = cum_dists / dists.sum()

    uniform_dists = np.linspace(0, 0.99999, n_points)
    points = []
    segs = []
    for dist in uniform_dists:
        upper_ind = np.digitize(dist, norm_cum_dists)
        lower_ind = upper_ind - 1
        start = vertices[lower_ind]
        end = vertices[upper_ind]

        point_dist_from_base = (dist - norm_cum_dists[lower_ind]) * dists.sum()
        span_dist = pdist[lower_ind, upper_ind]
        subdist = point_dist_from_base / span_dist

        new_point = subdist * start + (1 - subdist) * end

        segs.append(end - start)

        points.append(new_point)

    return np.array(points), np.array(segs)
    # def sample_new_point():
    #     sample_dist = np.random.uniform()

    #     upper_ind = np.digitize(sample_dist, cum_dists)
    #     lower_ind = upper_ind - 1

    #     start = vertices[lower_ind]
    #     end = vertices[upper_ind]
    #     dist = pdist[lower_ind, upper_ind]

    #     subdist = np.random.uniform()

    #     new_point = subdist * start + (1 - subdist) * end
    #     return new_point

    # points = []
    # for i in range(n_samples):
    #     points.append(sample_new_point())

    # points = np.array(points)
    # return points
    return


def draw_edges(points, n_edges=5, n_max_tries=100):
    for point in points:
        edge_counter = 0
        try_counter = 0
        while edge_counter < n_edges and try_counter < n_max_tries:
            try_counter += 1

            target_index = np.random.choice(len(points))
            target_point = points[target_index]

            cdist = cosine_distances(point.reshape(1, -1), target_point.reshape(1, -1))
            edist = euclidean_distances(
                point.reshape(1, -1), target_point.reshape(1, -1)
            )

            if cdist < 0.5 and edist < 2.75:
                ax.plot(
                    [point[0], target_point[0]],
                    [point[1], target_point[1]],
                    color="dimgrey",
                    linewidth=1,
                    zorder=-1,
                )
                edge_counter += 1


fig, ax = plt.subplots(1, 1, figsize=0.005 * np.array([1800, 700]))

colors = sns.color_palette()
N_COLOR = colors[0]
D_COLOR = colors[1]
S_COLOR = colors[2]

points, segs = sample_new_points(n_vertices, 50)
ax.scatter(points[:, 0], points[:, 1], color=N_COLOR)
draw_path(n_vertices, ax=ax, scatter=False, color=N_COLOR)
draw_edges(points)

outer_points, outer_segs = sample_new_points(d_outer_vertices, 25)
inner_points, inner_segs = sample_new_points(d_inner_vertices, 25)
points = np.concatenate((outer_points, inner_points), axis=0)
ax.scatter(points[:, 0], points[:, 1], color=D_COLOR)
draw_path(d_outer_vertices, ax=ax, scatter=False, color=D_COLOR)
draw_path(d_inner_vertices, ax=ax, scatter=False, color=D_COLOR)
draw_edges(points)

# ax.scatter(target_points[:, 0], target_points[:, 1])

points, segs = sample_new_points(s_vertices, 50)
ax.scatter(points[:, 0], points[:, 1], color=S_COLOR)
draw_path(s_vertices, ax=ax, scatter=False, color=S_COLOR)
draw_edges(points)


ax.axis("equal")
ax.axis("off")

plt.savefig(
    "networks-course/docs/images/logo.png",
    format="png",
    dpi=300,
    facecolor="w",
    pad_inches=0,
    bbox_inches="tight",
)

# draw_path(vertices, ax=ax, scatter=False)


# #%%

# from scipy.interpolate import splprep, splev

# # vertices = n_path.vertices.copy()[0:-1].T
# # vertices = d_path.vertices.copy().T
# n_vertices = n_path.vertices[:-1]
# s_vertices = s_path.vertices[:-1]
# d_outer_vertices = d_path.vertices[:22]
# vertices = d_outer_vertices.T
# tck, u = splprep(vertices.copy(), u=None, s=5, per=1)
# u_new = np.linspace(u.min(), u.max(), 1000)
# x_new, y_new = splev(u_new, tck, der=0)

# fig, ax = plt.subplots(1, 1, figsize=(8, 4))
# plt.plot(vertices[0], vertices[1], "ro")
# plt.plot(x_new, y_new, "b--")

# #%%
