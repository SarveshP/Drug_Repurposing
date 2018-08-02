import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import csv


df_edges = pd.read_csv('Data/Compound-Gene.csv')[3900:4000]
df_compounds = pd.read_csv('Data/Compounds.csv')
df_genes = pd.read_csv('Data/Genes.csv')

# df_edges = df_edges.loc[df_edges['source'] != "DB00246"]
# df_edges = df_edges.loc[df_edges['target'] != "1576"]
# df_edges = df_edges.loc[df_edges['target'] != "5743"]
# df_edges = df_edges.loc[df_edges['target'] != "6579"]
# df_edges = df_edges.loc[df_edges['target'] != "3290"]

columns = list(df_edges)
unique_compounds = set(df_edges['source'])

new_df_edges = pd.DataFrame(columns=columns)
for i in set(unique_compounds):
    new_df_edges = new_df_edges.append(df_edges.loc[df_edges['source'] == i], ignore_index=True)

unique_genes = set(new_df_edges['target'])

G = nx.Graph()

cmp_gene = {}

for unique_gen in unique_genes:
    compound_list = []
    for index, row in df_edges.iterrows():
        if unique_gen==row['target']:
            compound_list.append(row['source'])
    cmp_gene[unique_gen] = compound_list

nodes_edges = []
edges = {}
for key, value in cmp_gene.items():
    for L in range(0, len(value)+1):
      for subset in itertools.combinations(value, L):
        if len(subset)==2:
            try:
                compound_1 = df_compounds.loc[df_compounds['id'] == subset[0]].name.item()
                compound_2 = df_compounds.loc[df_compounds['id'] == subset[1]].name.item()
                G.add_edge(compound_1,compound_2)
                gene = df_genes.loc[df_genes['GeneID'] == key].Symbol.item()
                edges[(compound_1,compound_2)]=gene
                nodes_edges.append([subset[0],subset[1],gene])
            except:
                pass

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



