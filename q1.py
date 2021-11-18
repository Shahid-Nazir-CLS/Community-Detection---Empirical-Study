# import networkx and its functions
import networkx as nx

# import tabulate for tabulating the statistics
from tabulate import tabulate


# read the datasets
g1 = nx.read_gml('karate.gml', label = 'id')
g2 = nx.read_gml('dolphins.gml')
g3 = nx.read_weighted_edgelist('jazz.net')



# tabulate the statistics
table = [['Datasets', 'No. of nodes', 'No. of edges', 'Avg. path length', 'Avg. clustering coefficient'], 
         ['Karate Club Network', g1.number_of_nodes(), g1.number_of_edges(), nx.average_shortest_path_length(g1), nx.average_clustering(g1)], 
         ['Dolphins social Network', g2.number_of_nodes(), g2.number_of_edges(), nx.average_shortest_path_length(g2), nx.average_clustering(g2)], 
         ['Jazz musicians network', g3.number_of_nodes(), g3.number_of_edges(), nx.average_shortest_path_length(g3), nx.average_clustering(g3)]]

# print the statistics in table form
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))