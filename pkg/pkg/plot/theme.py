import matplotlib as mpl
import seaborn as sns

preset_themes = {}

preset_themes["light_edge"] = {
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.spines.left": True,
    "axes.spines.bottom": True,
    "axes.edgecolor": "lightgrey",
    "ytick.color": "grey",
    "xtick.color": "grey",
    "axes.labelcolor": "dimgrey",
    "text.color": "dimgrey",
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "pdf.fonttype": 42,  # for photoshop - Michael
    "ps.fonttype": 42,  # for photoshop - Michael
    "font.family": "sans-serif",  # for photoshop - Michael
    "font.sans-serif": ["Arial"],  # for photoshop - Michael
}

preset_themes["clean"] = {
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.spines.left": False,
    "axes.spines.bottom": False,
    "axes.edgecolor": "lightgrey",
    "ytick.color": "grey",
    "xtick.color": "grey",
    "axes.labelcolor": "black",
    "text.color": "black",
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "pdf.fonttype": 42,  # for photoshop - Michael
    "ps.fonttype": 42,  # for photoshop - Michael
    "font.family": "sans-serif",  # for photoshop - Michael
    "font.sans-serif": ["Arial"],  # for photoshop - Michael
}


def set_theme(
    theme=None,
    spine_right=False,
    spine_top=False,
    spine_left=True,
    spine_bottom=True,
    axes_edgecolor="black",
    tick_color="black",
    axes_labelcolor="black",
    text_color="black",
    context="talk",
    tick_size=0,
    font_scale=1,
):
    if theme is None:
        rc_dict = {
            "axes.spines.right": spine_right,
            "axes.spines.top": spine_top,
            "axes.spines.left": spine_left,
            "axes.spines.bottom": spine_bottom,
            "axes.edgecolor": axes_edgecolor,
            "ytick.color": tick_color,
            "xtick.color": tick_color,
            "axes.labelcolor": axes_labelcolor,
            "text.color": text_color,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial"],
            "xtick.major.size": tick_size,
            "ytick.major.size": tick_size,
        }
    else:
        rc_dict = preset_themes[theme]

    for key, val in rc_dict.items():
        mpl.rcParams[key] = val
    context = sns.plotting_context(context=context, font_scale=font_scale, rc=rc_dict)
    sns.set_context(context)