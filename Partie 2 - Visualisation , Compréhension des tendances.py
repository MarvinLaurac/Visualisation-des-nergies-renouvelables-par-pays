#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[140]:


#je commence par importer le DataFrame
df = pd.read_csv("/Users/octoberone/Desktop/DataFrame GitHub/DataFrame/Visualisation des énergies renouvelables par pays.csv")


# In[141]:


#affichage des 5 premières lignes
df.head()


# In[142]:


#voici le nombre de lignes et de colonnes sans le détail
df.shape


# In[143]:


#voici les détails des colonnes avec beaucoup plus d'informations (variables, types, le nombre de valeurs nulles)
df.info()


# In[144]:


#dans cette partie, j'ai affiché les pays pour pouvoir visualiser quels étaient les pays présents dans ces data
#après observation, je constate qu'il n'y a pas tous les pays, dont la suisse ou l'allemagne
print(df["LOCATION"].unique())


# In[145]:


#j'ai utilisé cette commande pour être sûr qu'il n'y a pas de valeurs manquantes
df.isnull().sum()
#je constate que les colonnes "Value" et "Flag Codes" disposent de None


# In[146]:


#dans cette partie, je décide de supprimer les valeurs None pour avoir des données exploitables et justes 
df.dropna(subset=["Value"], inplace=True)


# In[147]:


#je décide d'afficher les données dans la colonne "Flag Codes" car j'ai rencontré un problème lors de l'affichage
#en supprimant les données None, cela fausse tous les résultats suivants 
print(df["Flag Codes"])
#j'observe qu'il y a beaucoup de données None et donc cette colonne risque de ne pas être pertinente pour pouvoir être exploitée


# In[148]:


#je vérifie par la suite si les données de la colonne "Value" ont bien été supprimées 
#les données ont bien été supprimées car nous avons 0
df.isnull().sum()


# In[149]:


#Afin d'avoir plus de détails statistiques, j'affiche les colonnes numériques

#count%:nombre de valeurs nulles
#mean%:la moyenne des valeurs
#std%:l'écart type (dispersion valeurs)
#min%:le min de la colonne 
#25%:1er quatile à moins de 25
#50%:2er quatile à moins de 25
#75%:3er quatile à moins de 25
#max:le maxi de la colonne 

print(df.describe())


# In[163]:


#dans cette première visualisation, je compte les 20 premiers pays avec le plus de données pertinentes en comptant dans la data 
#de plus, pour avoir une meilleure visualisation, je les classe par ordre décroissant 
#j'en déduis que nous avons WLD, que je suppose représenter le monde 
#G20 pour les pays du G20 
#OECD est une organisation par pays
#ces 3 données sont des données regroupées

#mais nous pouvons observer que la Chine est en première position, l'Inde en 2ème, les USA en 4ème, le Canada en 9ème et la France en 12ème 
df_top = df.groupby("LOCATION")["Value"].sum().nlargest(20).sort_values(ascending=True)

plt.figure(figsize=(12, 8))
df_top.plot(kind="barh", color=["lightblue", "darkgreen", "blue", "salmon", "yellow"], label = "LOCATION")
plt.title("Énergies renouvelables par pays")
plt.ylabel("Pays")
plt.xlabel("Valeur totale")
plt.tight_layout()
plt.legend()
plt.show()


# In[134]:


#afin de me concentrer seulement sur les pays voisins de la France, je crée un nouveau dataframe regroupant ces voisins 
#malheureusement, tous les pays voisins ne sont pas enregistrés dans la data
location_euro = ["FRA", "ESP", "BEL", "ITA"]
df_proche_france = df[df['LOCATION'].isin(location_euro)]
df_proche_france.head()


# In[135]:


#dans cette dernière partie, j'affiche les pays que j'ai regroupés afin de visualiser les pays proches de la France 
#j'en déduis que la France est le pays qui utilise le plus d'énergie renouvelable contrairement à ses confrères 
plt.figure(figsize=(12, 8))
sns.barplot(data=df_proche_france, x="Value", y="LOCATION")
plt.title("Énergies renouvelables par pays (autour de la France)")
plt.xlabel("Valeur totale")
plt.ylabel("Pays")
plt.tight_layout()
plt.show()

