import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import csv

df_edges = pd.read_csv('Data/CtD.csv')[13:35]
df_diseases = pd.read_csv('Data/Diseases.csv')
df_compounds = pd.read_csv('Data/Compounds.csv')

df_edges = df_edges.loc[df_edges['doid_id'] != "DOID:8778"]
df_edges = df_edges.loc[df_edges['drugbank_id'] != "DB00850"]
df_edges = df_edges.loc[df_edges['drugbank_id'] != "DB00575"]
df_edges = df_edges.loc[df_edges['drugbank_id'] != "DB01186"]
df_edges = df_edges.loc[df_edges['drugbank_id'] != "DB00783"]

columns = list(df_edges)
unique_compounds = set(df_edges['drugbank_id'])

new_df_edges = pd.DataFrame(columns=columns)
for i in set(unique_compounds):
    new_df_edges = new_df_edges.append(df_edges.loc[df_edges['drugbank_id'] == i], ignore_index=True)

# for i in set(["DOID:10283","DOID:2531", "DOID:4481"]):
#     new_df_edges = new_df_edges.append(df_edges.loc[df_edges['doid_id'] == i], ignore_index=True)
# print(new_df_edges)

unique_diseases = set(new_df_edges['doid_id'])

G = nx.Graph()

cmp_disease = {}

for unique_dis in unique_diseases:
    compound_list = []
    for index, row in df_edges.iterrows():
        if unique_dis==row['doid_id']:
            compound_list.append(row['drugbank_id'])
    cmp_disease[unique_dis] = compound_list

nodes_edges = []
edges = {}
for key, value in cmp_disease.items():
    for L in range(0, len(value)+1):
      for subset in itertools.combinations(value, L):
        if len(subset)==2:
            compound_1 = df_compounds.loc[df_compounds['id'] == subset[0]].name.item()
            compound_2 = df_compounds.loc[df_compounds['id'] == subset[1]].name.item()
            G.add_edge(compound_1,compound_2)
            disease = df_diseases.loc[df_diseases['doid'] == key].name.item()
            edges[(compound_1,compound_2)]=disease
            nodes_edges.append([subset[0],subset[1],disease])

# print(edges)
    with open('Data/nodes_edges.csv', 'a') as new_Data:
        newdata_writer = csv.writer(new_Data, delimiter = ",")
        for row in nodes_edges:
            newdata_writer.writerow(row)

edges_list = [edge for edge in G.edges()]
# print(edges_list)

pos = nx.spring_layout(G)
plt.figure()
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size = 500,alpha=0.3)
nx.draw_networkx_edges(G, pos, edgelist=edges_list, edge_color='g',alpha=0.7,width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edges)
nx.draw_networkx_labels(G, pos)
plt.axis("off")
plt.show()



