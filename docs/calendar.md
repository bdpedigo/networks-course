(page:calendar)=
# Calendar 
```{note}
Schedule below is approximate and subject to change
```

## Week 1
### Jan 4th (Tuesday)
- [Introductions and welcome](https://bdpedigo.github.io/networks-course/welcome.html)
- [What are networks (and why should we care)]([what_are_networks](https://bdpedigo.github.io/networks-course/what_are_networks.html))?
- Course roadmap (go over this calendar)


### Jan 5th (Wednesday)
```{warning} 
Ben can't make it to this class, but you are encouraged to come to the class via zoom and help each other complete the mini-assignment.
```

```{admonition} Due
:class: important

Complete the [mini-assignment](mini_assignment.md).
```

### Jan 6th (Thursday)
- [Representing networks](representing_networks.ipynb)
- [Plotting networks](plotting_networks.ipynb)

### Jan 7th (Friday)
- [Centrality measures](centrality.ipynb)
   - Degree, strength
   - Eigenvector centrality
   - PageRank
   - Betweenness centrality

```{admonition} Due
:class: important

Know what dataset you'll be working on for the final project.

Complete [exit survey](https://forms.gle/xgyoCM9wuKUmcY6S7) to submit this info.
```

## Week 2
### Jan 10th (Monday)
- [Random graph models](random_graphs.ipynb)
   - ER
   - DCER
   - SBM
   - DCSBM
   - RDPG
   - Barabasi-Albert
   - Extensions

```{admonition} Due
:class: important

Be able to load in and somehow plot your dataset(s) in Python.
```

### Jan 11th (Tuesday)
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

### Jan 12th (Wednesday)
- [Network embedding (Part 1)](embedding.ipynb)
   - Word2Vec to DeepWalk to Node2Vec
   - Recommendations using an embedding 

### Jan 13th (Thursday)
- [Connected components](connected_components.ipynb)
- [Network embeddings (Part 2)](embedding.ipynb)
  - Spectral methods
    - Adjacency spectral embedding
    - Laplacian spectral embedding
    - Two truths
  

### Jan 14th (Friday)
- [Graph matching](graph_matching.ipynb)
   - When could we use it 
   - Why is it hard?
   - Fast approximate quadratic algorithm
   - Code in `graspologic`
     - Basic
     - Adding seeds
     - Graphs of different sizes
   - Application example

```{admonition} Due
:class: important

Complete [exit survey](https://forms.gle/hSB9Z6r773VkXXQx6) for this week.
```

## Week 3
### Jan 17th (Monday)
```{warning} 
**No class**

Martin Luther King Jr. Day
```

### Jan 18th (Tuesday)
- Review of embeddings
- [Multiple network embedding](multiple_embedding.ipynb)
   - ASE x 2 
   - Omnibus embedding
   - Multiple ASE

### Jan 19th (Wednesday)
- [Ranking](ranking.ipynb)
   - Simple rankings (A, A squared)
   - Eigenvector ranking
   - Minimum violations ranking
   - Applications of ranking to study hierarchies

### Jan 20th (Thursday)
- [One-sample testing (external link)](https://docs.neurodata.io/maggot_connectome/feedforwardness_data.html)
  - [Example of COVID effects on organizational communication from MSFT](http://116.203.245.78/studii/sars-cov-2/2104.00641.pdf) 
- [Two-sample testing (external link)](https://docs.neurodata.io/bilateral-connectome/nmc.pdf)
  - Code and more info can be found [here](https://github.com/neurodata/bilateral-connectome).

### Jan 21th (Friday)
- Project presentations

### Topics we didn't get to
- Clustering embeddings
- Graph neural networks + supervised embeddings