---
marp: true
theme: default
paginate: true
style: |
    section {
        justify-content: flex-start;
        --orange: #ed7d31;
        --left: #66c2a5;
        --right: #fc8d62;
        --source: #8da0cb;
        --target: #e78ac3;
    }
    img[alt~="center"] {
        display: block;
        margin: 0 auto;
    }
    header {
        top: 0px;
        margin-top: 0 auto;
    }
    div.twocols {
        margin-top: 0px;
        column-count: 2;
    }
    div.twocols p:first-child,
    div.twocols h1:first-child,
    div.twocols h2:first-child,
    div.twocols ul:first-child,
    div.twocols ul li:first-child,
    div.twocols ul li p:first-child {
        margin-top: 0 !important;
    }
    div.twocols p.break {
        break-before: column;
        margin-top: 0;
    }
---

<style scoped>
section {
    justify-content: center;
    text-align: center;
}
</style>

# What are networks (and why should you care)?

---
# What are networks?
- Networks are a mathematical way of representing a set of objects and the relationships among them.
- These "objects" are termed **nodes** or **vertices**.
- These relationships are termed **edges** or, less often, **links**.
- Networks are also called **graphs**.

---

<style scoped>
section {
    justify-content: center;
    text-align: center;
}
</style>

# Example networks / applications

---
# Connectome

Nodes: neurons, edges: some # of synapses

---
# More connectome 

![center w:850](./slide_images/mcc-main.png)

<footer>

</footer>


---
# Enron anomaly prediction
![center h:500](./slide_images/enron-deltacon.png)

---
# MSR communication

<!-- Nodes: email accounts, edges: some # of emails -->

<div class="twocols">

![](./slide_images/msr-layout.jpeg)

<p class="break"></p>

![](./slide_images/modularity-covid.png)

</div>


<footer>

[*Advancing organizational science using network machine learning to measure innovation in the workplace*](https://www.microsoft.com/en-us/research/blog/advancing-organizational-science-using-network-machine-learning-to-measure-innovation-in-the-workplace/)
[Zuzul et al. arXiv:2104.00641 (2021)](https://arxiv.org/abs/2104.00641)

</footer>


---
# Faculty hiring and other dominance hierarchies

<div class="twocols">

![](./slide_images/fac-network.png)

<p class="break"></p>

![](./slide_images/fac-network-sorted.png)

</div>

<footer>


</footer>

---
# Pandemic spread


<div class="twocols">

![](./slide_images/germany-covid-geo.png)

<p class="break"></p>

![w:350](./slide_images/germany-covid-model-top.png)
![w:350](./slide_images/germany-covid-model-bottom.png)

</div>

<footer>


</footer>

---
# Protein-protein interaction
![center h:475](slide_images/ppi.jpeg)

<footer>

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4898894/#!po=16.6667

</footer>

---
# What are NOT networks? - Hypergraphs
- Networks represent **dyadic** relationships: interactions between *two* things.
  - Example: an email from me to you  
- **Polyadic** relationships (interactions between more than two things) are common.
  - Example: an email from me to you AND someone else
- We could ignore this: 
  - Make an edge from me to you.
  - Make another, separate edge from me to someone else.
- **Hypergraphs** are a mathematical way of representing general polyadic relationships.

---
# What are NOT networks? - Multigraphs
- Graphs (strictly speaking) usually have at most one edge between node $i$ and node $j$.
- There may be multiple relationships between two nodes in data that we want to model.
  - Example: An email from me to you, and a phone call from me to you.
- Sometimes we can compress this information into at most one edge, and still use a graph.
  - Example: Create an edge if there was an email OR a phone call.
- **Multigraphs** allow for more than one edge from node $i$ to node $j$.

---
<style scoped>
section {
    justify-content: center;
    text-align: center;
}
</style>

# Every time we represent something in the real world with a network, we're making a modeling choice

---
# What can we do with networks? (i.e. What is this class about?)

## [Class Calendar](https://bdpedigo.github.io/networks-course/calendar.html)

---
# Appendix

---
# The Wire

--- 
# Sports


--- 
# Prediction/supervised learning 

---
# Networks are a backbone in many modern ML algorithms

