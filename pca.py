import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.cluster import KMeans
import pandas as pd


def Pca_Vulnerability(data):
	# print(data)
	X_std = MinMaxScaler().fit_transform(data)
	df_3 = pd.DataFrame(X_std)

	# print(df_3.shape[1])
	# sys.exit(0)
	# df = pd.read_csv('2013_2014_cleaned.csv')# Standardize the data to have a mean of ~0 and a variance of 1
	# Create a PCA instance: pca
	pca = PCA(n_components=min(df_3.shape[0],df_3.shape[1]))
	principalComponents = pca.fit_transform(df_3)# Plot the explained variances
	features = range(pca.n_components_)
	plt.bar(features, pca.explained_variance_ratio_, color='black')
	plt.xlabel('PCA features')
	plt.ylabel('variance %')
	plt.xticks(features)# Save components to a DataFrame
	PCA_components = pd.DataFrame(principalComponents)
	return PCA_components


def Pca_Criticality(data):
	# print(data)
	ss2 = MinMaxScaler().fit_transform(data)
	dfx = pd.DataFrame(ss2)
	# df = pd.read_csv('2013_2014_cleaned.csv')# Standardize the data to have a mean of ~0 and a variance of 1
	# Create a PCA instance: pca
	pca = PCA(n_components=min(dfx.shape[0],dfx.shape[1]))
	principalComponents = pca.fit_transform(ss2)# Plot the explained variances
	features = range(pca.n_components_)
	plt.bar(features, pca.explained_variance_ratio_, color='black')
	plt.xlabel('PCA features')
	plt.ylabel('variance %')
	plt.xticks(features)# Save components to a DataFrame
	PCA_components = pd.DataFrame(principalComponents)
	return PCA_components
