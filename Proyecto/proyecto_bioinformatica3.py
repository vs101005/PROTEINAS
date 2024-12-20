from biopandas.pdb import PandasPdb
import matplotlib.pyplot as plt
import streamlit as st
#from Bio import SeqIO
#from Bio import Entrez
#from Bio.PDB import PDBParser, PDBList
#from Bio.SeqUtils import seq1
#from Bio.PDB.Polypeptide import CaPPBuilder
#from Bio.PDB.Atom import Atom
#from biopandas.pdb import PandasPdb
#import plotly.express as px
#import matplotlib.pyplot as plt

"""### **INSULINA**

B FACTOR
"""

pdb = PDBList()
pdb.retrieve_pdb_file('1ZEI', pdir='.', file_format='pdb')

ppdb=PandasPdb().read_pdb("/content/1zei.pdb")

ppdb.df["ATOM"]["b_factor"].plot(kind="line",color="pink",figsize=(10,5))
plt.title("B_factor")
plt.xlabel("Número de residuo")
plt.ylabel("B_factor en $A^2$")
plt.show()

df_atomos = ppdb.df['ATOM']
fig=px.scatter_3d(df_atomos, x="x_coord", y="y_coord", z="z_coord", color="b_factor", template="plotly_dark")
fig.update_traces(marker=dict(size=3))

"""PROPORCION DE ATOMOS"""

conteo_atomos = df_atomos['element_symbol'].value_counts()
proporcion_atomos = conteo_atomos / conteo_atomos.sum()
print(proporcion_atomos)

ppdb.df["ATOM"]["element_symbol"].value_counts().plot(kind="barh",color="pink",figsize=(10,5))
plt.title("Distribución de elementos")
plt.xlabel("Cantidad")
plt.ylabel("element_symbol")
plt.show()

fig=px.scatter_3d(df_atomos,x="x_coord",y="y_coord",z="z_coord",color="element_symbol",template="plotly_dark",
                  color_discrete_sequence = ["blue", "gray", "pink", "red"])
fig.update_coloraxes(showscale=True)
fig.update_traces(marker=dict(size=3))
fig.show()

"""SECUENCIA DE AMINOACIDOS"""

Entrez.email = "a223201128@unison.mx"

id_proteina = "NP_001278826.1"
proteina_raw = Entrez.efetch(id = id_proteina, db = "protein", rettype="gb", retmode="text")
Proteina= SeqIO.read(proteina_raw, "genbank") # lee un solo archivo
handle = Entrez.efetch(db="protein", id=id_proteina, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
secuencia_aminoacidos = record.seq
print(secuencia_aminoacidos)

fig=px.scatter_3d(df_atomos,x="x_coord",y="y_coord",z="z_coord",color="residue_name",template="plotly_dark")
fig.update_traces(marker=dict(size=3))
fig.update_coloraxes(showscale=True)
fig.show()

"""### **Glucagon**

B FACTOR
"""

pdb2 = PDBList()
pdb2.retrieve_pdb_file('7LCK', pdir='.', file_format='pdb')

ppdb2=PandasPdb().read_pdb("/content/7lck.pdb")

ppdb2.df["ATOM"]["b_factor"].plot(kind="line",color="purple",figsize=(10,5))
plt.title("B_factor")
plt.xlabel("Número de residuo")
plt.ylabel("B_factor en $A^2$")
plt.show()

df_atomos2 = ppdb2.df['ATOM']
fig=px.scatter_3d(df_atomos2, x="x_coord", y="y_coord", z="z_coord", color="b_factor", template="plotly_dark")
fig.update_traces(marker=dict(size=3))

"""PROPORCION DE ATOMOS"""

df_atomos2 = ppdb2.df['ATOM']
conteo_atomos = df_atomos2['element_symbol'].value_counts()
proporcion_atomos = conteo_atomos / conteo_atomos.sum()
print(proporcion_atomos)

ppdb2.df["ATOM"]["element_symbol"].value_counts().plot(kind="barh",color="purple",figsize=(10,5))
plt.title("Distribución de elementos")
plt.xlabel("Cantidad")
plt.ylabel("element_symbol")
plt.show()

fig=px.scatter_3d(df_atomos2,x="x_coord",y="y_coord",z="z_coord",color="element_symbol",template="plotly_dark",
                  color_discrete_sequence = ["purple", "green", "yellow", "orange"])
fig.update_coloraxes(showscale=True)
fig.update_traces(marker=dict(size=3))
fig.show()

"""SECUENCIA DE AMINOACIDOS"""

id_proteina = "KAI4036670.1"
proteina_raw = Entrez.efetch(id = id_proteina, db = "protein", rettype="gb", retmode="text")
Proteina= SeqIO.read(proteina_raw, "genbank")
handle = Entrez.efetch(db="protein", id=id_proteina, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
secuencia_aminoacidos = record.seq
print(secuencia_aminoacidos)

fig=px.scatter_3d(df_atomos2,x="x_coord",y="y_coord",z="z_coord",color="residue_name",template="plotly_dark")
fig.update_traces(marker=dict(size=3))
fig.update_coloraxes(showscale=True)
fig.show()

"""HEMOGLOBINA

Factor B
"""

pdb3 = PDBList()
pdb3.retrieve_pdb_file('1SHR', pdir='.', file_format='pdb')

ppdb3=PandasPdb().read_pdb("/content/1shr.pdb")

ppdb3.df["ATOM"]["b_factor"].plot(kind="line",color="blue",figsize=(10,5))
plt.title("B_factor")
plt.xlabel("Número de residuo")
plt.ylabel("B_factor en $A^2$")
plt.show()

df_atomos3 = ppdb3.df['ATOM']
fig=px.scatter_3d(df_atomos3, x="x_coord", y="y_coord", z="z_coord", color="b_factor", template="plotly_dark")
fig.update_traces(marker=dict(size=3))

"""Proporcion de atomos"""

df_atomos = ppdb.df['ATOM']
conteo_atomos = df_atomos3['element_symbol'].value_counts()
proporcion_atomos = conteo_atomos / conteo_atomos.sum()
print(proporcion_atomos)

ppdb3.df["ATOM"]["element_symbol"].value_counts().plot(kind="barh",color="blue",figsize=(10,5))
plt.title("Distribución de elementos")
plt.xlabel("Cantidad")
plt.ylabel("element_symbol")
plt.show()

fig=px.scatter_3d(df_atomos3,x="x_coord",y="y_coord",z="z_coord",color="element_symbol",template="plotly_dark",
                  color_discrete_sequence = ["crimson", "powderblue", "darksalmon", "purple"])
fig.update_coloraxes(showscale=True)
fig.update_traces(marker=dict(size=3))
fig.show()

"""Secuencia de aminoacidos"""

id_proteina = "WMZ92120.1"
proteina_raw = Entrez.efetch(id = id_proteina, db = "protein", rettype="gb", retmode="text")
Proteina= SeqIO.read(proteina_raw, "genbank")
handle = Entrez.efetch(db="protein", id=id_proteina, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
secuencia_aminoacidos = record.seq
print(secuencia_aminoacidos)

fig=px.scatter_3d(df_atomos3,x="x_coord",y="y_coord",z="z_coord",color="residue_name",template="plotly_dark")
fig.update_traces(marker=dict(size=3))
fig.update_coloraxes(showscale=True)
fig.show()

"""### COLAGENO

Factor B
"""

pdb4 = PDBList()
pdb4.retrieve_pdb_file('5NB1', pdir='.', file_format='pdb')

ppdb4=PandasPdb().read_pdb("/content/5nb1.pdb")

ppdb4.df["ATOM"]["b_factor"].plot(kind="line",color="thistle",figsize=(10,5))
plt.title("B_factor")
plt.xlabel("Número de residuo")
plt.ylabel("B_factor en $A^2$")
plt.show()

df_atomos4 = ppdb4.df['ATOM']
fig=px.scatter_3d(df_atomos4, x="x_coord", y="y_coord", z="z_coord", color="b_factor", template="plotly_dark")
fig.update_traces(marker=dict(size=3))

"""Proporcion de atomos"""

conteo_atomos = df_atomos4['element_symbol'].value_counts()
proporcion_atomos = conteo_atomos / conteo_atomos.sum()
print(proporcion_atomos)

ppdb4.df["ATOM"]["element_symbol"].value_counts().plot(kind="barh",color="thistle",figsize=(10,5))
plt.title("Distribución de elementos")
plt.xlabel("Cantidad")
plt.ylabel("element_symbol")
plt.show()

fig=px.scatter_3d(df_atomos4,x="x_coord",y="y_coord",z="z_coord",color="element_symbol",template="plotly_dark",
                  color_discrete_sequence = ["cornflowerblue", "blue", "pink", "mediumpurple"])
fig.update_coloraxes(showscale=True)
fig.update_traces(marker=dict(size=3))
fig.show()

"""Secuencia de aminoacios"""

id_proteina = "BAA04809.1"
proteina_raw = Entrez.efetch(id = id_proteina, db = "protein", rettype="gb", retmode="text")
Proteina= SeqIO.read(proteina_raw, "genbank")
handle = Entrez.efetch(db="protein", id=id_proteina, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
secuencia_aminoacidos = record.seq
print(secuencia_aminoacidos)

fig=px.scatter_3d(df_atomos4,x="x_coord",y="y_coord",z="z_coord",color="residue_name",template="plotly_dark")
fig.update_traces(marker=dict(size=3))
fig.update_coloraxes(showscale=True)
fig.show()
