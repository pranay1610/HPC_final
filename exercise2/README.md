# Mandelbrot Set Computation with MPI and OpenMP

## Introduction

This project aims to compute and visualize the Mandelbrot set using a hybrid approach that combines MPI (Message Passing Interface) for distributed memory parallelism and OpenMP (Open Multi-Processing) for shared memory parallelism. The goal is to leverage the strengths of both parallelization paradigms to efficiently compute the Mandelbrot set on a high-performance computing (HPC) cluster.

### C Implementation

The implementation consists of the following components:
- `main.c`: Initializes MPI, distributes the computation among MPI processes, and manages timing.
- `mandelbrot.c`: Contains functions for computing the Mandelbrot set using OpenMP for parallelization within each MPI process.
- `image_utils.c`: Provides functions for writing the computed Mandelbrot set to a PGM (Portable GrayMap) image file.


### Command-Line Arguments

The program accepts command-line arguments for the grid size (`nx` and `ny`), the bounds of the complex plane (`xmin`, `ymin`, `xmax`, `ymax`), and the maximum number of iterations (`Imax`). This flexibility allows users to customize the computation without modifying the code.

### Use of MPI Timing Functions

The `MPI_Wtime()` function is used to measure the execution time of the computation, ensuring accurate timing in a parallel environment.

## Final Report
The report can be found in  `NARSIPURAM_EX2c_report.pdf`

## Directory Structure
```
HPC_final/
├── exercise2/
│ ├── analysis/
│ │ ├── plot_scaling.py
│ │ ├── plot_mandelbrot.py
│ ├── jobs/
│ │ ├── mpi_strong_scaling.sh
│ │ ├── mpi_weak_scaling.sh
│ │ ├── omp_strong_scaling.sh
│ │ ├── omp_weak_scaling.sh
│ ├── results/
│ │ ├── mpi_strong_scaling/
│ │ ├── mpi_weak_scaling/
│ │ ├── omp_strong_scaling/
│ │ ├── omp_weak_scaling/
│ ├── src/
│ │ ├── main.c
│ │ ├── mandelbrot.c
│ │ ├── image_utils.c
│ ├── Makefile
│ ├── NARSIPURAM_EX2c_report.pdf
│ ├── exercise2.md
├── README.md
```

## Compiling and Running the Code

### Compilation

To compile the code, navigate to the `exercise2` directory and run:

```bash
make
```
### Running the Code
To submit the job scripts to the scheduler, use the following commands:

```bash
cd jobs/
sbatch submit_mpi_strong_scaling.sh
sbatch submit_mpi_weak_scaling.sh
sbatch submit_omp_strong_scaling.sh
sbatch submit_omp_weak_scaling.sh
```
### Plotting Results
To plot the scaling results, use the provided plot_scaling.py script in the analysis directory:

```bash
cd analysis/
python plot_scaling.py
```
