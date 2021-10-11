import nbformat as nbf
import numpy as np
import sys

ipath = sys.argv[1]
# Collect a list of all notebooks in the content folder
# notebooks = glob(loc)

# Text to look for in adding tags
# text_search_dict = {
#     "# HIDDEN": "remove-cell",  # Remove the whole cell
#     "# NO CODE": "remove-input",  # Remove only the input
#     "# HIDE CODE": "hide-input",  # Hide the input w/ a button to show
# }

ntbk = nbf.read(ipath, nbf.NO_CONVERT)
for cell in ntbk.cells:
    if cell.get("cell_type") == "code":
        cell_tags = cell.get("metadata", {}).get("tags", [])
        cell_tags = list(np.unique(cell_tags))
        if "hide-input" not in cell_tags:
            cell_tags.append("hide-input")
        # for key, val in text_search_dict.items():
        #     if key in cell["source"]:
        #         if val not in cell_tags:
        #             cell_tags.append(val)
        if len(cell_tags) > 0:
            cell["metadata"]["tags"] = cell_tags

nbf.write(ntbk, ipath)
