# Syllabus

## Course description
Networks represent data by describing a set of objects and the relations between them. Networks are ubiquitous in many fields of science; for example, they have been used to represent include social interactions, relationships between genes or protein sequences, and the interconnectivity of neurons in the brain. This project-based course will introduce students to the process of analyzing real-world network data in Python. Topics covered will include network representations, centrality and ranking measures, modularity and community detection, network embeddings, random graph models, graph matching, network hypothesis testing, and graph neural networks. Students will be expected to submit a very brief analysis (in Python) of some real-world network dataset for their final project. Familiarity with Python, statistics and linear algebra is very highly encouraged.

## Topics
- What is a network?
- Why should we care about networks?
- How do we represent networks?
- Centrality measures (e.g. PageRank)
- Modularity maximization and community detection
- Ranking/flow (e.g. MVR, SpringRank, signal flow, etc.) 
- Unsupervised network embedding
   - Spectral embedding, min-flow-max-cut
   - Node2vec and other... 
- Graph neural networks (message passing kind)
- Random graph models
   - ER
   - SBM and variants
   - RDPG
   - mention that there are many others like ERGMs
- Spectral clustering/fitting a stochastic block model 
- Graph matching 
- Network hypothesis testing
- Network kernels and other ways of comparing networks
- Extensions of networks (just mention them)
   - Hypergraphs
   - Multilayer networks

## Materials
### Code/software
#### Primary
- graspologic and its tutorials/documentation
- NetworkX
- scipy.sparse.csgraph

#### Also mentioned 
- graph-tool
- scikit-network
- python-igraph
- karateclub
- DGL
- pytorch-geometric
- stellargraph

### Books
The following books may be useful material during the course, but none of them are
required to rent or buy:
- Networks by Mark Newman
- Atlas for the Aspiring Network Scientist
- Hands-on book by NeuroData group
- https://staging.distill.pub/2021/gnn-intro/

## Prerequisites
The following prerequisites are highly recommended to take this course. Please talk to 
the instructor if you are unsure about your prior knowledge for any of these:
- Python programming experience 
- Linear algebra 
- Probability/statistics