import warnings


def set_warnings():
    warnings.filterwarnings("ignore", category=UserWarning, module="umap")


