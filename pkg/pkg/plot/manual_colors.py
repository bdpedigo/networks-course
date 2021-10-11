import matplotlib.pyplot as plt
import numpy as np

import colorcet as cc

CLASS_IND_DICT = {
    "KC": 0,
    "KC-1claw": 28,
    "KC-2claw": 32,
    "KC-3claw": 92,
    "KC-4claw": 91,
    "KC-5claw": 78,
    "KC-6claw": 61,
    "APL": 24,
    "MBIN": 121,
    "MBIN-DAN": 58,
    "MBIN-OAN": 5,
    "MBON": 172,
    "MBON-av": 200,
    "MBON-app": 234,
    "MBON-neith": 172,  # 43,
    "sens-AN": 1,
    "sens-MN": 12,
    "sens-ORN": 51,
    "Sens": 51,
    "sens-PaN": 76,
    "sens-photoRh5": 84,
    "sens-photoRh6": 106,
    "sens-thermo": 55,
    "sens-vtd": 145,
    "mPN-multi": 3,
    "mPN-olfac": 88,
    "mPN;FFN-multi": 3,
    "tPN": 186,
    "uPN": 36,
    "PN": 36,
    "pLN": 57,
    "bLN-Duet": 216,
    "bLN-Trio": 8,
    "keystone": 157,
    "cLN": 232,
    "FAN": 2,
    "FB2N": 21,
    "FBN": 50,
    "FFN": 52,
    "dSEZ;FB2N": 21,
    "dSEZ;FFN": 52,
    "RG-CA-LP": 42,
    "RGN-CA-LP": 42,
    "RG-IPC": 42,
    "RGN-IPC": 42,
    "RG-ITP": 42,
    "RGN-ITP": 42,
    "RG": 42,
    "RGN": 42,
    "dSEZ": 124,
    "dSEZ;CN": 124,
    "dSEZ;LHN": 124,
    "LHN;dSEZ": 124,
    "dVNC": 38,
    "dVNC;CN": 38,
    "dVNC;RG": 38,
    "dVNC;RGN": 38,
    "RG;dVNC": 38,
    "dVNC;dSEZ": 38,
    "dSEZ;dVNC": 38,
    "Outs": 124,
    "PreO": 114,
    "dUnk": 105,
    "unk": 190,
    "LHN": 123,
    "LHN2": 65,
    "CN": 206,
    "CN2": 95,
    "LHN;CN": 108,
    "CN;LHN": 108,
    "vPN": 33,
    "LON": 159,
    "CX": 228,
    "AN2": 125,
    "AN2;MN2": 215,
    "FB2N;AN2": 21,
    "FBN;AN2": 50,
    "MN2": 112,
    "vtd2;AN2": 125,
    "vtd2": 54,
    "A00c": 37,
    "super-brain": 80,
    "super-sez": 137,
    "super-vnc": 161,
    "Sens2o": 33,
    "LN": 49,
}

name_map = {
    "Sens": "Sensory",
    "LN": "Local",
    "PN": "Projection",
    "KC": "Kenyon cell",
    "LHN": "Lateral horn",
    "MBIN": "MBIN",
    "Sens2o": "2nd order sensory",
    "unk": "Unknown",
    "MBON": "MBON",
    "FBN": "MB feedback",
    "CN": "Convergence",
    "PreO": "Pre-output",
    "Outs": "Output",
    "Motr": "Motor",
}

names = []
color_inds = []

for key, val in CLASS_IND_DICT.items():
    names.append(key)
    color_inds.append(val)

colors = np.array(cc.glasbey_light)[color_inds]
CLASS_COLOR_DICT = dict(zip(names, colors))
CLASS_COLOR_DICT["motor-VAN"] = "#000000"
CLASS_COLOR_DICT["motor-AN"] = "#000000"
CLASS_COLOR_DICT["motor-PaN"] = "#000000"
CLASS_COLOR_DICT["motor-MN"] = "#000000"
CLASS_COLOR_DICT["Motr"] = "#000000"

for old_name, new_name in name_map.items():
    CLASS_COLOR_DICT[new_name] = CLASS_COLOR_DICT[old_name]


def plot_colors():
    from src.visualization import palplot

    fig, axs = plt.subplots(1, 6, figsize=(6, 10))
    n_per_col = 40
    for i, ax in enumerate(axs):
        pal = cc.glasbey_light[i * n_per_col : (i + 1) * n_per_col]
        palplot(n_per_col, pal, figsize=(1, 10), ax=ax, start=i * n_per_col)
    plt.savefig(
        "./maggot_models/notebooks/outs/colors.png", dpi=300, bbox_inches="tight"
    )


def plot_class_colormap():
    from src.visualization import palplot
    from src.data import load_metagraph

    mg = load_metagraph("G")
    uni_class, counts = np.unique(mg["merge_class"], return_counts=True)
    count_map = dict(zip(uni_class, counts))
    names = []
    colors = []
    for key, val in CLASS_COLOR_DICT.items():
        if key in uni_class:
            names.append(f"{key} ({count_map[key]})")
            colors.append(val)
    for uc in uni_class:
        if uc not in CLASS_COLOR_DICT:
            print(f"{uc} not in colormap")
    fig, ax = plt.subplots(1, 1, figsize=(3, 15))
    palplot(len(colors), colors, ax=ax)
    ax.yaxis.set_major_formatter(plt.FixedFormatter(names))
    plt.savefig(
        "./maggot_models/notebooks/outs/current_cmap.png", dpi=300, bbox_inches="tight"
    )


if __name__ == "__main__":
    plot_colors()
    plot_class_colormap()
