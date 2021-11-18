# import networkx and its functions
import networkx as nx
from networkx.algorithms import community
import networkx.algorithms.community as nx_comm
from networkx.algorithms.community.modularity_max import greedy_modularity_communities
import numbers

# import itertools for creating iterators for efficient looping
import itertools

# import spectral clustering functionality from scikitt learn library
from sklearn.cluster import SpectralClustering

#----------------------------------------------------------------------------------------------#
# 1 betweenness-based  clustering  using  the  Girvan-Newman algorithm

# girvan newman implementation
def girvan_newman(graph, no_of_iterations):

	# find communities in the graph
	comp = community.girvan_newman(graph)

	# empty list to add clusters
	clusters = []

	# find the nodes forming the communities
	for communities in itertools.islice(comp, no_of_iterations):
		clusters = list(sorted(c) for c in communities)

	return clusters


#----------------------------------------------------------------------------------------------#
# modularity-based clustering
def modularity_based_clustering(graph):

	# modularity based clusters
	clusters = greedy_modularity_communities(graph)

	return clusters

#----------------------------------------------------------------------------------------------#
#  spectral clustering
def spectral_clustering(graph, no_of_clusters):

	# convert graph to a list
	graph_list = list(graph)

	# convert graph into adjaceny matrix  because spectral clustering takes graph as a 2d matrix
	adj_matrix = nx.to_numpy_matrix(graph)

	# create spectral clustering model
	sc = SpectralClustering(n_clusters=no_of_clusters, affinity='precomputed', n_init=100)

	# find communities in the graph
	sc.fit(adj_matrix)
	
	# get a list which says which node belongs to which community
	labels = sc.labels_


	# create an empty list that will contain clusters formed
	clusters = [[] for i in range(no_of_clusters)]

	# convert above list to list of lists which contains different communities
	# i.e. find the nodes forming the communities

	i = 1
	#  for graph 1
	if(isinstance(graph_list[0], numbers.Integral)):
		
		for x in labels:
			clusters[x].append(i)
			i += 1

	# for second graph
	elif(graph_list[0] == "Beak"):
		i = 0
		for x in labels:
			clusters[x].append(graph_list[i])
			i += 1

	# for third graph       
	else:
		for x in labels:
			clusters[x].append(str(i))
			i += 1
	
	return clusters