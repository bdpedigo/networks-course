(page:calendar)=
# Calendar 
```{note}
Schedule below is approximate and subject to change
```

## Week 1
### Jan 9th (Monday)
- [Introductions and welcome](https://bdpedigo.github.io/networks-course/welcome.html)
- Set up [development environments](python.md)
- Work on the [mini-assignment](mini_assignment.md)
- [What are networks (and why should we care)](https://bdpedigo.github.io/networks-course/what_are_networks.html)?
- Course roadmap (go over this calendar)
- [Representing networks](representing_networks.ipynb)
- Look at datasets (if time)

### Jan 10th (Tuesday)

```{admonition} Due during class
:class: important

Have a working Python environment to use for this course (during class).
```

```{admonition} Due end of day
:class: important

Complete the [mini-assignment](mini_assignment.md).
```
- [Plotting networks](plotting_networks.ipynb)
- [Connected components](connected_components.ipynb)
- [Centrality measures](centrality.ipynb)
   - Degree, strength
   - Eigenvector centrality
   - PageRank
   - Betweenness centrality
- Look at datasets (if time)

### Jan 11th (Wednesday)
```{admonition} Due during class
:class: important

Know what dataset you'll be working on for the final project.

Complete [exit survey](https://forms.gle/xgyoCM9wuKUmcY6S7) to submit this info.
```

- [Random graph models](random_graphs.ipynb)
   - ER
   - DCER
   - SBM
   - DCSBM
   - RDPG
   - Barabasi-Albert
   - Extensions


### Jan 12th (Thursday)

```{admonition} Due during class
:class: important

Be able to load in and somehow plot your dataset(s) in Python.
```

- [Community detection](community_detection.ipynb)
   - Modularity
     - Simple node-moving
     - Spectral
     - Louvain, Leiden
     - Issues with modularity maximization
       - Resolution limit
       - Overfitting
   - Brief tour of other approaches
   - Application to finding communities in ___


### Jan 13th (Friday)
- [Network embedding (Part 1)](embedding.ipynb)
   - Word2Vec to DeepWalk to Node2Vec
   - Recommendations using an embedding 

## Week 2
### Jan 16th (Monday)

```{warning}

NO CLASS - Martin Luther King, Jr. Day

```


### Jan 17th (Tuesday)
- [Graph matching](graph_matching.ipynb)
   - When could we use it 
   - Why is it hard?
   - Fast approximate quadratic algorithm
   - Code in `graspologic`
     - Basic
     - Adding seeds
     - Graphs of different sizes
   - Application example
- [Ranking](ranking.ipynb)
  - Simple rankings (A, A squared)
  - Eigenvector ranking
  - Minimum violations ranking
  - Applications of ranking to study hierarchies

### Jan 18th (Wednesday)
- [Network embeddings (Part 2)](embedding.ipynb)
  - Spectral methods
    - Adjacency spectral embedding
    - Laplacian spectral embedding
    - Two truths

### Jan 19th (Thursday)

```{admonition} Due by beginning of class
:class: important

Submit final project notebooks.
```

- [Multiple network embedding](multiple_embedding.ipynb)
   - ASE x 2 
   - Omnibus embedding
   - Multiple ASE

### Friday
```{admonition} Due in class
:class: important

Final project presentations
```

```{admonition} Due by end of day
:class: important

Complete exit survey.
```

- Final project presentations


<!-- 
- [One-sample testing (external link)](https://docs.neurodata.io/maggot_connectome/feedforwardness_data.html)
  - [Example of COVID effects on organizational communication from MSFT](http://116.203.245.78/studii/sars-cov-2/2104.00641.pdf) 
- [Two-sample testing (external link)](https://docs.neurodata.io/bilateral-connectome/nmc.pdf)
  - Code and more info can be found [here](https://github.com/neurodata/bilateral-connectome).
- [Network kernels](https://ysig.github.io/GraKeL/0.1a8/classes.html#kernels) -->
<!-- ### Topics we didn't get to
- Clustering embeddings
- Graph neural networks + supervised embeddings -->