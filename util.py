import matplotlib.pyplot as plt
import pandas as pd

"""
Utility function to plot clusters
"""
def plot_clusters(X, columns, labels, centers, feature_x, feature_y):
  df = pd.DataFrame(X, columns=columns)
  df['Cluster'] = labels  # Add cluster labels

  # Plot samples
  plt.scatter(df[feature_x], df[feature_y], 
            c=df['Cluster'], cmap='viridis', s=75, label='Samples')

  # Plot cluster centers
  plt.scatter(centers[:, df.columns.get_loc(feature_x)], 
            centers[:, df.columns.get_loc(feature_y)], 
            c='red', s=50, marker='*', label='Cluster centroids')

  # Plot formatting
  plt.xlabel(feature_x)
  plt.ylabel(feature_y)
  plt.title(f'Cluster by {feature_x} vs {feature_y}')
  plt.legend()
  plt.colorbar(label='Cluster')
  plt.show()