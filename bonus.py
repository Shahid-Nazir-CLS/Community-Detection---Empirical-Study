# import networkx and its functions
import networkx as nx
import networkx.algorithms.community as nx_comm

# import girvan newman algorithm function
from q2 import girvan_newman

# import modularity based clustering algorithm function
from q2 import modularity_based_clustering

# import spectral clustering functionality from scikitt learn library
from sklearn.cluster import SpectralClustering

# import itertools for creating iterators for efficient looping
import itertools

# import warnings to remove any runtime warnings
import warnings
warnings.filterwarnings("ignore")

# import matplotlib for visualizations
import matplotlib.pyplot as plt

def find(lists, key):
    for i, list in enumerate(lists):
        if(key in list):
            return i


# read the datasets
g1 = nx.read_gml('karate.gml', label = 'id')
g2 = nx.read_gml('dolphins.gml', label = 'id')
g3 = nx.read_weighted_edgelist('jazz.net')


# First Graph i.e. karate dataset
print("\n================================ FIRST GRAPH ===================================")


# find communities in the graph using girvan-newman algorithm
c1 = girvan_newman(g1, 3)

# find the nodes forming the communities
clusters1 = []
for i in c1:
    clusters1.append(list(i))

# number of cluster formed
num_clusters = len(clusters1)


node_cluster_dict1 = {}
for x in g1.nodes():
    node_cluster_dict1[x] = find(clusters1, x)

# create a new graph for representative network
rep_network1 = nx.Graph()

# add nodes which number of clusters formed
rep_network1.add_nodes_from(range(num_clusters))
rep_network1.add_edges_from(itertools.combinations(range(num_clusters), 2))

nx.set_edge_attributes(rep_network1, values = 0, name = 'weight')

# convert graph into adjaceny list  
adj_list = nx.to_numpy_array(g1)

for i, node in enumerate(g1.nodes()):
    for j, val in enumerate(adj_list[i]):
        if(node_cluster_dict1[node] != node_cluster_dict1[j+1]):

            rep_network1[node_cluster_dict1[node]][node_cluster_dict1[j+1]]["weight"] += val*0.5

# print edges formed in the representative network
print(rep_network1.edges(data = True))

# write representative network to output file
nx.write_gml(rep_network1, "rep_network1.gml")


# visualize representative network of graph 1
pos=nx.spring_layout(rep_network1) 
nx.draw_networkx(rep_network1, pos)
labels = nx.get_edge_attributes(rep_network1,'weight')
nx.draw_networkx_edge_labels(rep_network1, pos, edge_labels=labels)
plt.show()



# Second Graph i.e. jazz dataset
print("\n================================ SECOND GRAPH ===================================")

# find communities in the graph using spectral-based algorithm

adj_list = nx.to_numpy_matrix(g2)


sc = SpectralClustering(4, affinity='precomputed', n_init=100)
sc.fit(adj_list)
lg = list(g2)
num_clusters = len(set(sc.labels_))
clusters = []
for i in range(num_clusters):
    clusters.append([])
for i , val in enumerate(sc.labels_):
    clusters[val].append(lg[i])
    

node_cluster_dict2 = {}
for x in g2.nodes():
    node_cluster_dict2[x] = find(clusters, x)

# create a new graph for representative network
rep_network2 = nx.Graph()

# add nodes which number of clusters formed
rep_network2.add_nodes_from(range(num_clusters))
rep_network2.add_edges_from(itertools.combinations(range(num_clusters), 2))

nx.set_edge_attributes(rep_network2, values = 0, name = 'weight')


adj_list = adj_list.tolist()

for i, node in enumerate(g2.nodes()):
    for j, val in enumerate(adj_list[i]):
        if(node_cluster_dict2[node] != node_cluster_dict2[j]):
            rep_network2[node_cluster_dict2[node]][node_cluster_dict2[j]]["weight"] += val*0.5


# print edges formed in the representative network
print(rep_network2.edges(data = True))

# write representative network to output file
nx.write_gml(rep_network2, "rep_network2.gml")


# visualize representative network of graph 2
pos=nx.spring_layout(rep_network2)
nx.draw_networkx(rep_network2, pos)
labels = nx.get_edge_attributes(rep_network2, 'weight')
nx.draw_networkx_edge_labels(rep_network2, pos,edge_labels=labels)
plt.show()




# Third Graph i.e. jazz dataset
print("\n================================ THIRD GRAPH ===================================")

adj_list = nx.to_numpy_array(g3)
# find communities in the graph using spectral-based clustering
c2 = modularity_based_clustering(g3)

# find the nodes forming the communities
clusters = (list(sorted(c) for c in c2))


node_cluster_dict3 = {}
for x in g3.nodes():
    node_cluster_dict3[x] = find(clusters, x)

# create a new graph for representative network
rep_network3 = nx.Graph()

# add nodes which number of clusters formed
rep_network3.add_nodes_from(range(num_clusters))
rep_network3.add_edges_from(itertools.combinations(range(num_clusters), 2))

nx.set_edge_attributes(rep_network3, values = 0, name = 'weight')

for i, node in enumerate(g3.nodes()):
    for j, val in enumerate(adj_list[i]):
        if(node_cluster_dict3[node] != node_cluster_dict3[str(j+1)]):
            rep_network3[node_cluster_dict3[node]][node_cluster_dict3[str(j+1)]]["weight"] += val*0.5


# print edges formed in the representative network
print(rep_network3.edges(data = True))

# write representative network to output file
nx.write_gml(rep_network3, "rep_network3.gml")


# visualize representative network of graph 3
pos=nx.spring_layout(rep_network3)
nx.draw_networkx(rep_network3,pos)
labels = nx.get_edge_attributes(rep_network3,'weight')
nx.draw_networkx_edge_labels(rep_network3,pos,edge_labels=labels)
plt.show()
