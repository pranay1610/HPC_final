import os
import re
import pandas as pd
import matplotlib.pyplot as plt

# Function to read execution times from output files
def read_execution_times(directory):
    times = []
    tasks = []
    for filename in os.listdir(directory):
        if filename.startswith('output_'):
            task_count = int(re.findall(r'\d+', filename)[0])
            with open(os.path.join(directory, filename), 'r') as f:
                for line in f:
                    if "Execution time" in line:
                        time_in_sec = float(re.findall(r'[\d.]+', line)[0])
                        time_in_ms = time_in_sec * 1000
                        tasks.append(task_count)
                        times.append(time_in_ms)
    return tasks, times

# Function to plot scaling data
def plot_scaling(tasks, times, x_label, y_label, title, output_file):
    df = pd.DataFrame({'Tasks': tasks, 'Time': times})
    df.sort_values(by='Tasks', inplace=True)
    plt.figure(figsize=(10, 6))
    plt.plot(df['Tasks'], df['Time'], marker='o', linestyle='-', color='b')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.savefig(output_file)
    plt.show()

# Read and plot MPI Strong Scaling
mpi_strong_tasks, mpi_strong_times = read_execution_times('~/assignments/exercise2/results/mpi_strong_scaling/')
plot_scaling(
    mpi_strong_tasks,
    mpi_strong_times,
    'Number of MPI Tasks',
    'Execution Time (ms)',
    'MPI Strong Scaling',
    '~/assignments/exercise2/images_plots/mpi_strong_scaling_plot.png'
)

# Read and plot MPI Weak Scaling
mpi_weak_tasks, mpi_weak_times = read_execution_times('~/assignments/exercise2/results/mpi_weak_scaling/')
plot_scaling(
    mpi_weak_tasks,
    mpi_weak_times,
    'Number of MPI Tasks',
    'Execution Time (ms)',
    'MPI Weak Scaling',
    '~/assignments/exercise2/images_plots/mpi_weak_scaling_plot.png'
)

# Read and plot OMP Strong Scaling
omp_strong_tasks, omp_strong_times = read_execution_times('~/assignments/exercise2/results/omp_strong_scaling/')
plot_scaling(
    omp_strong_tasks,
    omp_strong_times,
    'Number of OpenMP Threads',
    'Execution Time (ms)',
    'OMP Strong Scaling',
    '~/assignments/exercise2/images_plots/omp_strong_scaling_plot.png'
)

# Read and plot OMP Weak Scaling
omp_weak_tasks, omp_weak_times = read_execution_times('~/assignments/exercise2/results/omp_weak_scaling/')
plot_scaling(
    omp_weak_tasks,
    omp_weak_times,
    'Number of OpenMP Threads',
    'Execution Time (ms)',
    'OMP Weak Scaling',
    '~/assignments/exercise2/images_plots/omp_weak_scaling_plot.png'
)
