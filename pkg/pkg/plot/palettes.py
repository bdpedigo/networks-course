import seaborn as sns

# Side specification
side_colors = sns.color_palette("Set2", n_colors=2)
side_specs = [["L", "R"], ["Left", "Right"], ["left", "right"]]

SIDE_PALETTE = {}
for spec in side_specs:
    SIDE_PALETTE = {**SIDE_PALETTE, **dict(zip(spec, side_colors))}

if __name__ == "__main__":
    print(SIDE_PALETTE)
