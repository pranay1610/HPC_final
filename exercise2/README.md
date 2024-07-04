## Exercise 2c: Hybrid MPI+OpenMP Mandelbrot Set

### Introduction
This report analyzes the implementation of the Mandelbrot set using a hybrid MPI+OpenMP approach and evaluates its performance in terms of strong and weak scalability.

### Implementation
The Mandelbrot set was implemented using MPI for inter-process communication and OpenMP for intra-process parallelism. The complex plane was divided among MPI processes, and each process used OpenMP to parallelize the computation of the Mandelbrot set.


### Conclusions
The hybrid MPI+OpenMP implementation of the Mandelbrot set demonstrated good scalability. Potential improvements include optimizing the load balancing and reducing communication overhead.
