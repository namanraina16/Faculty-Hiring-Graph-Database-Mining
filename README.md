# Graph Data and Pattern Mining
Exploratory task for FORWARD Data Mining Group under Professor Kevin Chang.
## Table of Contents
- [Directory Structure](#directory-structure)
- [Description](#description)

  
## Directory Structure

Four different directories.
- `/data`: Two types of text files: vertex and edges. Vertex text files display sampled universities per major and edge text files show a directed connection between University X and University Y.

- `/material`: Contains the main research paper referred to, its supplementary paper, and my 2-page research report.
  
- `/results`: CSV contains network DAG for Computer Science along with other attributes. The rest are resultant files displaying predicted university ranking based on two algorithms - Page Rank and Minimum Violation Rankings (a type of Monte Carlo Markov Chain algorithm) as described in the research paper.

- `/scripts`: Python files to parse text files into CSV as well as to implement both algorithms. CQL files to run Cypher queries to load the network or find the shortest weighted path between nodes on the network using the Neo4j software.
## Description
The main task was to replicate the method implemented in the main research paper on the provided dataset and use a well-known algorithm like PageRank to compare the findings. The sub-task was to initialize the network from the dataset with the help of Python scripts, Neo4j software, and Cypher queries. Then some interesting queries were run on the network to extract meaningful information. Finally, the main method was implemented which tried to maximize the number of edges that go downward (from a high-ranked university to a lower one) by minimizing the number of violations in a network permutation, and its findings were compared with that of the PageRank algorithm.
