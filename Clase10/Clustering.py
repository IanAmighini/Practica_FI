import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
import numpy as np
from scipy import stats

datos = pd.read_csv("https://raw.githubusercontent.com/AJVelezRueda/Fundamentos_de_informatica/master/Ciencia_de_datos/practicos/recursos/practico4.csv")

datos.info()

sns.heatmap(datos.isnull(), cmap='viridis')
#Para ver cuantos datos faltan

datos.describe()

columnas = list(datos.columns)
columnas

del(columnas[0:2])
#Elimina columnas innecesarias

def verificacion_de_medias(lista):
    test = {}
    for columna in lista:
        w, p = stats.shapiro(datos[columna].dropna())
        test[columna] = p
    return test
verificacion_de_medias(columnas)

sns.pairplot(datos)

datos.quantile(0.05).to_dict()

Cs1 = datos["Actividad (en hs)"].quantile(0.95)
Ci1 = datos["Actividad (en hs)"].quantile(0.05)
Cs2 = datos["Acceso a Instagram (en hs)"].quantile(0.95)
Ci2 = datos["Acceso a Instagram (en hs)"].quantile(0.05)

datos1 = datos[(datos["Actividad (en hs)"] >= Ci1) & (datos["Actividad (en hs)"] <= Cs1) & (datos["Acceso a Instagram (en hs)"] >= Ci2) & (datos["Acceso a Instagram (en hs)"] <= Cs2)].reset_index(drop=True)
datos1

#Con esto elimino los datos 5% mas altos y bajos que suelen ser anomalias

datos2 = datos1.dropna().reset_index(drop=True)

datos3 = datos2.drop_duplicates().reset_index(drop=True)
datos3

sns.pairplot(datos3)

scaler = StandardScaler()
datos_escaleado = scaler.fit_transform(datos3[columnas])

def inercias_por_k(df_escalado):
    inercias = {}
    for i in range(1,11):
        kmeans = KMeans(n_clusters = i, init="random", n_init=10, max_iter=300, random_state=123457)
        kmeans.fit(df_escalado)
        inercias[i] = kmeans.inertia_
    return inercias

inercias = inercias_por_k(datos_escaleado)
inercias

df_inercias = pd.DataFrame(inercias.items(), columns=["K", "inercia"])
sns.pointplot(data = df_inercias, x = "K", y = "inercia")

#Con este grafico se ve donde se corta la pendiente y sacar el valor de k

k = 2
kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans.fit(datos_escaleado)

colores = ["red", "green"]
sns.scatterplot(x = datos_escaleado[:, 2], y = datos_escaleado[:, 0], hue = kmeans.labels_, palette = colores, alpha = 0.5)
sns.scatterplot(x = kmeans.cluster_centers_[:, 2], y = kmeans.cluster_centers_[:, 0], zorder = 10, palette = colores, hue = [0, 1], legend = False, marker=6, s=200)

silhouette_avg = silhouette_score(datos_escaleado, kmeans.labels_)
sample_silhouette_values = silhouette_samples(datos_escaleado, kmeans.labels_)

def graficarSilhouette (k, labels, sample_silhouette_values, silhouette_avg):
  fig, ax1 = plt.subplots(1, 1)
  y_lower = 10
  for i in range(k):
      ith_cluster_silhouette_values = \
          sample_silhouette_values[labels == i]

      ith_cluster_silhouette_values.sort()

      size_cluster_i = ith_cluster_silhouette_values.shape[0]
      y_upper = y_lower + size_cluster_i

      color = cm.nipy_spectral(float(i) / k)
      ax1.fill_betweenx(np.arange(y_lower, y_upper),
                        0, ith_cluster_silhouette_values,
                        facecolor=color, edgecolor=color, alpha=0.7)
      ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
      y_lower = y_upper + 10

  ax1.set_title("Plot del silhouette de cada cluster")
  ax1.set_xlabel("Coeficiente de silhouette")
  ax1.set_ylabel("Etiqueta del cluster")
  ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
  ax1.set_yticks([])

graficarSilhouette (k, kmeans.labels_, sample_silhouette_values, silhouette_avg)
#El grafico de barritas que muestra si hiciste bien el clustering
 