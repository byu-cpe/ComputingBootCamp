//===========================================================================
// matrixmul.h
//===========================================================================
// @brief: This header file defines the interface for the core functions.

#ifndef MATRIXMUL_H
#define MATRIXMUL_H

#define N 100
#define M 100
#define P 100

// Multiplys two matrices, matrix AB is result
void matrixmul(int A[N][M], int B[M][P], int AB[N][P]);


#endif