import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Function to read and prepare data from files
def read_and_prepare_data(file_path, algo_name):
    df = pd.read_csv(file_path, sep=',')
    df['ALGO_NAME'] = algo_name
    return df

# Read data
broadcast_fixed_data = read_and_prepare_data('/home/probis/Documents/exercise1/broadcast_fixed.txt', 'broadcast_fixed')
broadcast_full_data = read_and_prepare_data('/home/probis/Documents/exercise1/broadcast_full.txt', 'broadcast_full')
gather_fixed_data = read_and_prepare_data('/home/probis/Documents/exercise1/gather_fixed.txt', 'gather_fixed')
gather_full_data = read_and_prepare_data('/home/probis/Documents/exercise1/gather_full.txt', 'gather_full')

# Combine data into a single DataFrame
combined_data = pd.concat([broadcast_fixed_data, broadcast_full_data, gather_fixed_data, gather_full_data], ignore_index=True)

# Ensure 'Avg Latency(us)' is numeric and filter out non-numeric values
combined_data['Avg Latency(us)'] = pd.to_numeric(combined_data['Avg Latency(us)'], errors='coerce')
combined_data = combined_data.dropna(subset=['Avg Latency(us)'])

# Train multivariate linear regression models
def train_model(df):
    models = {}
    for algorithm in df['ALGO_NAME'].unique():
        subset = df[df['ALGO_NAME'] == algorithm]
        X = subset[['NP_total', 'Size']].values
        y = subset['Avg Latency(us)'].values
        model = LinearRegression()
        model.fit(X, y)
        models[algorithm] = model
    return models

models = train_model(combined_data)

# Evaluate the models
def evaluate_model(models, df):
    results = {}
    for algorithm, model in models.items():
        subset = df[df['ALGO_NAME'] == algorithm]
        X = subset[['NP_total', 'Size']].values
        y = subset['Avg Latency(us)'].values
        y_pred = model.predict(X)
        mse = mean_squared_error(y, y_pred)
        results[algorithm] = mse
    return results

evaluation_results = evaluate_model(models, combined_data)

print("Evaluation Results:", evaluation_results)

# Visualize the model's predictions with lines instead of points
def plot_model_with_lines(models, df, title):
    plt.figure(figsize=(12, 8))
    colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']
    algo_names = {
        'broadcast_fixed': 'Broadcast Fixed',
        'broadcast_full': 'Broadcast Full',
        'gather_fixed': 'Gather Fixed',
        'gather_full': 'Gather Full'
    }
    
    for i, (algorithm, model) in enumerate(models.items()):
        subset = df[df['ALGO_NAME'] == algorithm]
        X = subset[['NP_total', 'Size']].values
        y = subset['Avg Latency(us)'].values
        y_pred = model.predict(X)
        algo_name = algo_names[algorithm]
        plt.plot(subset['NP_total'], y, label=f'{algo_name} actual', alpha=0.5, color=colors[i])
        plt.plot(subset['NP_total'], y_pred, label=f'{algo_name} predicted', linestyle='--', color=colors[i])
    plt.title(title)
    plt.xlabel('Number of Cores')
    plt.ylabel('Avg Latency (us)')
    plt.legend()
    plt.show()

plot_model_with_lines(models, combined_data, 'Combined Latency Model with Lines')


