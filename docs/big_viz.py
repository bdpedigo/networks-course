#%%
import pandas as pd
import networkx as nx
import numpy as np
import graspologic as gs

data_path = "networks-course/data/celegans/male_chem_A_self_undirected.csv"
meta_path = "networks-course/data/celegans/master_cells.csv"
cells_path = "networks-course/data/celegans/male_chem_self_cells.csv"
adj = pd.read_csv(data_path, header=None)
meta = pd.read_csv(meta_path, header=None, index_col=0)
cells = np.squeeze(pd.read_csv(cells_path, header=None).values)
meta = meta.reindex(cells)
A = adj.values

#%%
from scipy.sparse import csr_matrix

A_ptr = gs.utils.pass_to_ranks(A)  # can skip for an unweighted network
A_sparse = csr_matrix(A)

n_components = 16
ase = gs.embed.AdjacencySpectralEmbed(n_components=n_components, check_lcc=False)
ase_embedding = ase.fit_transform(A_sparse)

#%%
from umap import UMAP

umapper = UMAP(n_neighbors=15, metric="cosine", min_dist=0.8)
umap_embedding = umapper.fit_transform(ase_embedding)

#%%

gs.plot.networkplot(
    A_sparse,
    x=umap_embedding[:, 0],
    y=umap_embedding[:, 1],
    edge_linewidth=0.2,
    edge_alpha=0.4,
    node_kws=dict(
        s=50,  # s will change the size of nodes)
    ),
)
