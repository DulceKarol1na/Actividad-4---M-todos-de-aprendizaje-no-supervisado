import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargar los datos desde un archivo Excel
df_distancias = pd.read_excel('RedTransporte.xlsx')

# Eliminar cualquier fila con valores NaN, si los hay
df_distancias.dropna(inplace=True)

# Normalizar los datos (opcional)
df_distancias['Kilometros'] = (df_distancias['Kilometros'] - df_distancias['Kilometros'].mean()) / df_distancias['Kilometros'].std()

# Aplicar K-Means para agrupar las ciudades en clusters
kmeans = KMeans(n_clusters=5)  # Especifica el número de clusters deseado
kmeans.fit(df_distancias[['Kilometros']])

# Agrega una columna al DataFrame para indicar el cluster asignado a cada ciudad
df_distancias['Cluster'] = kmeans.labels_

# Imprime el DataFrame con la asignación de clusters
print(df_distancias)

# Visualizar los clusters
plt.scatter(df_distancias['Origen'], df_distancias['Destino'], c=df_distancias['Cluster'], cmap='viridis')
plt.xlabel('Origen')
plt.ylabel('Destino')
plt.title('Clusters de la Red de Transporte')
plt.show()
