import sys
import pandas as pd
import matplotlib.pyplot as plt

def process_and_plot(file_path):
    data = pd.read_csv(file_path)
    
    # Plotting the results
    plt.figure(figsize=(12, 8))
    for algo_name in data['ALGO_NAME'].unique():
        algo_data = data[data['ALGO_NAME'] == algo_name]
        plt.plot(algo_data['Size'], algo_data['Avg Latency(us)'], label=algo_name)
    
    plt.xlabel('Message Size (bytes)')
    plt.ylabel('Average Latency (us)')
    plt.title('Latency Comparison for Different Algorithms')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"latency_comparison_{file_path.split('/')[-1].split('.')[0]}.png")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 plot_benchmarks.py <output_file>")
        sys.exit(1)
    
    output_file = sys.argv[1]
    process_and_plot(output_file)
