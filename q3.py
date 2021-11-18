# import networkx and its functions
import networkx as nx
import networkx.algorithms.community as nx_comm

# import girvan newman algorithm function
from q2 import girvan_newman

# import modularity based clustering algorithm function
from q2 import modularity_based_clustering

# import spectral clustering algorithm function
from q2 import spectral_clustering

# import time for calculating the run time of the algorithm
import time

# import warnings to remove any runtime warnings
import warnings
warnings.filterwarnings("ignore")



# read the datasets
g1 = nx.read_gml('karate.gml', label = 'id')
g2 = nx.read_gml('dolphins.gml')
g3 = nx.read_weighted_edgelist('jazz.net')


#---------------------------------------------------------------------------------#
print("=============================================== GIRVAN NEWMAN ALGORITHM =========================================\n")

# First Graph i.e. karate dataset
print("\n================================ FIRST GRAPH ===================================")

# time in seconds before running the algorithm
seconds_old = time.time()

# find communities in the graph
c1 = girvan_newman(g1, 3)

# find the nodes forming the communities
node_groups1 = []
for i in c1:
    node_groups1.append(list(i))

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(node_groups1))    

# print modularity score for this clustering algorithm
print("Modularity score: " + str(nx_comm.modularity(g1, node_groups1)))


#----------------------------------------------------------------------------------------------#
# Second Graph i.e. dolphins dataset

print("\n\n\n================================ SECOND GRAPH ===================================")

# time in seconds before running the algorithm
seconds_old = time.time()

# find communities in the graph
c2 = girvan_newman(g2, 3)

# find the nodes forming the communities
node_groups2 = []
for i in c2:
    node_groups2.append(list(i))
    

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)


# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(node_groups2)) 

# print modularity score for this clustering algorithm
print("Modularity score: " + str(nx_comm.modularity(g2, node_groups2)))


#----------------------------------------------------------------------------------------------------#
# Third Graph i.e. jazz dataset

print("\n\n\n================================ THIRD GRAPH ===================================")

# time in seconds before running the algorithm
seconds_old = time.time()

# find communities in the graph
c3 = girvan_newman(g3, 4)

# find the nodes forming the communities
node_groups3 = []
for i in c3:
    node_groups3.append(list(i))

# time in seconds after running the algorithm    
seconds_new = time.time()

# print run time of algorithm
print("Time taken : ", seconds_new - seconds_old)

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(node_groups3)) 

# print modularity score for this clustering algorithm
print("Modularity score: " + str(nx_comm.modularity(g3, node_groups3)))








#---------------------------------------------------------------------------------#
print("\n\n\n============================================ MODULARITY BASED CLUSTERING ===========================================\n")

# First Graph i.e. karate dataset
print("\n================================ FIRST GRAPH ===================================")

# time in seconds before running the algorithm
seconds_old = time.time()

# find communities in the graph
c1 = modularity_based_clustering(g1)

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)

# find the nodes forming the communities
node_groups1 = (list(sorted(c) for c in c1))

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(node_groups1))

# print modularity score for this clustering algorithm
print("Modularity score: " + str(nx_comm.modularity(g1, node_groups1)))


#----------------------------------------------------------------------------------------------#
# Second Graph i.e. dolphins dataset

print("\n\n\n================================SECOND GRAPH ===================================")

# time in seconds before running the algorithm
seconds_old = time.time()

# find communities in the graph
c2 = modularity_based_clustering(g2)

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)

# find the nodes forming the communities
node_groups2 = (list(sorted(c) for c in c2))

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(node_groups2))  

# print modularity score for this clustering algorithm
print("Modularity score: " + str(nx_comm.modularity(g2, node_groups2)))

#----------------------------------------------------------------------------------------------------#
# Third Graph i.e. jazz dataset

print("\n\n\n================================ THIRD GRAPH ===================================")

# time in seconds before running the algorithm
seconds_old = time.time()

# find communities in the graph
c3 = modularity_based_clustering(g3)

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)

# find the nodes forming the communities
node_groups3 = (list(sorted(c) for c in c3))

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(node_groups3))   

# print modularity score for this clustering algorithm
print("Modularity score: " + str(nx_comm.modularity(g3, node_groups3)))








#---------------------------------------------------------------------------------#
print("\n\n\n============================================ SPECTRAL CLUSTERING ===========================================\n")

# First Graph i.e. karate dataset
print("\n================================ FIRST GRAPH ===================================")

# time in seconds before running the algorithm
seconds_old = time.time()

# create spectral clustering model
clusters = spectral_clustering(g1, no_of_clusters=4)

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)
        

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(clusters))

# print modularity score for this clustering algorithm
print("Modularity score : " + str(nx_comm.modularity(g1, clusters)))


#----------------------------------------------------------------------------------------------------#
# Second Graph i.e. dolphins dataset
print("\n\n\n================================ SECOND GRAPH ===================================")


# time in seconds before running the algorithm
seconds_old = time.time()

# create spectral clustering model
clusters = spectral_clustering(g2, no_of_clusters=4)

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)
        

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(clusters))

# print modularity score for this clustering algorithm
print("Modularity score : " + str(nx_comm.modularity(g2, clusters)))


#----------------------------------------------------------------------------------------------------#
# Third Graph i.e. jazz dataset
print("\n\n\n================================ THIRD GRAPH ===================================")


# time in seconds before running the algorithm
seconds_old = time.time()

# create spectral clustering model
clusters = spectral_clustering(g3, no_of_clusters=3)

# time in seconds after running the algorithm
seconds_new = time.time()

# print run time of the algorithm
print("Time taken : ", seconds_new - seconds_old)
        

# print number of clusters formed
print("Number of clusters formed : ", end="")
print(len(clusters))

# print modularity score for this clustering algorithm
print("Modularity score : " + str(nx_comm.modularity(g3, clusters)))



