jupytext --to notebook --output maggot_connectome/docs/$1.ipynb maggot_connectome/scripts/$1.py
jupyter nbconvert --to notebook --inplace --execute --ExecutePreprocessor.timeout=-1 maggot_connectome/docs/$1.ipynb 
python maggot_connectome/docs/add_cell_tags.py maggot_connectome/docs/$1.ipynb
# {'metadata': {'path': run_path}}
# https://github.com/jupyter/nbconvert/blob/7ee82983a580464b0f07c68e35efbd5a0175ff4e/nbconvert/preprocessors/execute.py#L63
# --ExecutePreprocessor.record_timing=True