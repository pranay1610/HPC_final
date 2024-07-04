## Exercise 2c: Hybrid MPI+OpenMP Mandelbrot Set

### Introduction
This report analyzes the implementation of the Mandelbrot set using a hybrid MPI+OpenMP approach and evaluates its performance in terms of strong and weak scalability.

### Implementation
The Mandelbrot set was implemented using MPI for inter-process communication and OpenMP for intra-process parallelism. The complex plane was divided among MPI processes, and each process used OpenMP to parallelize the computation of the Mandelbrot set.

### Performance Analysis
The performance of the implementation was measured for strong and weak scaling.

#### Strong Scaling
| Number of Threads | Execution Time (s) |
|-------------------|---------------------|
| 1                 | ...                 |
| 2                 | ...                 |
| 4                 | ...                 |
| 8                 | ...                 |
| 16                | ...                 |

#### Weak Scaling
| Number of MPI Tasks | Execution Time (s) |
|---------------------|---------------------|
| 2                   | ...                 |
| 4                   | ...                 |
| 8                   | ...                 |
| 16                  | ...                 |

### Conclusions
The hybrid MPI+OpenMP implementation of the Mandelbrot set demonstrated good scalability. Potential improvements include optimizing the load balancing and reducing communication overhead.
