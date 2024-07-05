# Performance Evaluation of High Performance Computing with OpenMPI Standards

This repository contains the implementation and results for the performance evaluation of OpenMPI Collective Operations as part of the HPC Final Assignment.

## Exercise 1: HPC Final Assignment

### Exercise Description
Please refer to `exercise1.md` for the detailed description of the exercise.

### Final Report
The comprehensive report can be found in `NARSIPURAM_report.pdf`.

### Project Structure

- `benchmark_job.sh`: The main script used to run the benchmarks on the Orfeo cluster.
- `linear_regression_model.py`: Script to train and evaluate the performance models.
- `results`: Directory containing the benchmark result files (`broadcast_fixed.txt`, `broadcast_full.txt`, `gather_fixed.txt`, `gather_full.txt`).
- `plots`: Contains the plots and visualizations.
- `exercise1.md`: Exercise description.
- `NARSIPURAM_report.pdf`: Final report.

### Usage

To reproduce the reported latencies and timings, use the provided `benchmark_job.sh` script. This work is accomplished in multiple iterations due to time constraints on the Orfeo execution environment.

```bash
sbatch benchmark_job.sh [operation_type] [benchmark_type]
