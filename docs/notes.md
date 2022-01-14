# Notes 

Use `nx.to_scipy_sparse_matrix(g, nodelist=nodelist)` to directly create a sparse array. If a sparse array is necessary, you never want to go through a 
dense representation first.

Heatmaps won't make much sense for very big networks with more than a few thousand nodes.

