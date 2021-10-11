import numpy as np


def select_nice_nodes(mg):
    mg = mg[mg.nodes["paper_clustered_neurons"] | mg.nodes["accessory_neurons"]]
    mg = mg[mg.nodes["hemisphere"].isin(["L", "R"])]
    mg.to_largest_connected_component(verbose=True)
    out_degrees = np.count_nonzero(mg.sum.adj, axis=0)
    in_degrees = np.count_nonzero(mg.sum.adj, axis=1)
    max_in_out_degree = np.maximum(out_degrees, in_degrees)
    # TODO we could OOS these back in?
    keep_inds = np.arange(len(mg.nodes))[max_in_out_degree > 2]
    remove_ids = np.setdiff1d(mg.nodes.index, mg.nodes.index[keep_inds])
    print(f"Removed {len(remove_ids)} nodes when removing pendants.")
    mg.nodes = mg.nodes.iloc[keep_inds]
    mg.g.remove_nodes_from(remove_ids)
    mg.to_largest_connected_component(verbose=True)
    mg.nodes.sort_values("hemisphere", inplace=True)
    mg.nodes["_inds"] = range(len(mg.nodes))
    return mg
