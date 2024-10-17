# Linear Algebra
This basic object-oriented linear algebra library provides essential operations for vectors, matrices, and systems of equations, including addition, multiplication, transposition, eigenvalue computation, and solving linear systems.

## Vectors
- Vector addition and subtraction: Add or subtract two vectors of the same size.
- Scalar multiplication: Multiply a vector by a scalar.
- Dot product: Compute the dot product of two vectors.
- Cross product (for 3D vectors): Compute the cross product.
- Norm (magnitude): Calculate the Euclidean norm (magnitude) of a vector.
- Unit vector: Normalize a vector.
- Projection: Project one vector onto another.

## Matrices
- Matrix addition and subtraction: Add or subtract matrices of the same dimensions.
- Scalar multiplication: Multiply a matrix by a scalar.
- Matrix multiplication: Multiply two matrices.
- Transpose: Compute the transpose of a matrix.
- Determinant: Calculate the determinant of a matrix (for square matrices).
- Inverse: Compute the inverse of a matrix (if it exists).
- Identity matrix: Generate an identity matrix.
- Matrix rank: Determine the rank of a matrix.
- Trace: Compute the trace of a matrix (sum of diagonal elements).
- Row operations: Perform elementary row operations (e.g., swapping, scaling, adding rows).

## Systems of Linear Equations
- Solve linear systems: Use Gaussian elimination or LU decomposition to solve systems of linear equations $Ax=b$.
- LU decomposition: Decompose a matrix into the product of a lower and upper triangular matrix.
- QR decomposition: Factor a matrix into an orthogonal matrix Q and an upper triangular matrix R.

## Eigenvalues and Eigenvectors
- Eigenvalue computation: Compute the eigenvalues of a square matrix.
- Eigenvector computation: Compute the eigenvectors corresponding to the eigenvalues.

## Other Useful Operations
- Matrix power: Raise a matrix to a given integer power.
- Gram-Schmidt orthogonalization: Create an orthogonal set of vectors from a set of linearly independent vectors.
- Singular Value Decomposition (SVD): Decompose a matrix into three matrices $U, \sum, V^*$ for advanced applications.
- Norms: Compute different matrix norms (Frobenius norm, infinity norm, etc.).

## Utility Functions
- Matrix creation: Functions to create matrices like zeros, ones, and random matrices.
- Diagonal matrix: Create a diagonal matrix from a vector.
- Reshaping: Reshape a matrix into different dimensions.
- Block matrices: Combine smaller matrices into a block matrix.

*Note: This outline was created by ChatGPT and may not be fully implemented here*