import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the text file
file_path_fixed = "/home/probis/Documents/exercise1/gather_fixed.txt"
file_path_full = "/home/probis/Documents/exercise1/gather_full.txt"

# Reading the fixed data
df_fixed = pd.read_csv(file_path_fixed)
df_full = pd.read_csv(file_path_full)

# Define the function to create the plots
def create_plots(df, title):
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))
    fig.suptitle(title, fontsize=16)

    # Average Latency plot
    axes[0].plot(df['NP_total'], df['Avg Latency(us)'], marker='o')
    axes[0].set_xlabel('Number of Processes')
    axes[0].set_ylabel('Average Latency (us)')
    axes[0].set_title('Average Latency vs Number of Processes')
    axes[0].grid(True)

    # Minimum Latency plot
    axes[1].plot(df['NP_total'], df['Min Latency(us)'], marker='o', color='g')
    axes[1].set_xlabel('Number of Processes')
    axes[1].set_ylabel('Minimum Latency (us)')
    axes[1].set_title('Minimum Latency vs Number of Processes')
    axes[1].grid(True)

    # Maximum Latency plot
    axes[2].plot(df['NP_total'], df['Max Latency(us)'], marker='o', color='r')
    axes[2].set_xlabel('Number of Processes')
    axes[2].set_ylabel('Maximum Latency (us)')
    axes[2].set_title('Maximum Latency vs Number of Processes')
    axes[2].grid(True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Filter data based on the selected algorithms
algo_names_fixed = df_fixed['ALGO_NAME'].unique()
algo_names_full = df_full['ALGO_NAME'].unique()

# Create plots for each algorithm in the fixed file
for algo in algo_names_fixed:
    create_plots(df_fixed[df_fixed['ALGO_NAME'] == algo], f'Gather Fixed - {algo}')

# Create plots for each algorithm in the full file
for algo in algo_names_full:
    create_plots(df_full[df_full['ALGO_NAME'] == algo], f'Gather Full - {algo}')
