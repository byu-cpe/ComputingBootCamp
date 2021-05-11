
#include "matrixmul.h"


void matrixmul(int A[N][M], int B[M][P], int AB[N][P]) {
#pragma HLS ARRAY_PARTITION variable=A cyclic factor=100 dim=2
#pragma HLS ARRAY_PARTITION variable=B cyclic factor=100 dim=1
#pragma HLS ARRAY_PARTITION variable=AB cyclic factor=100 dim=1
    /* for each row and column of AB */
    row: for(int i = 0; i < N; ++i) {
       col: for(int j = 0; j < P; ++j) {
    
    /* compute (AB)i,j */
            int ABij = 0;
            product: for(int k = 0; k < M; ++k) {
#pragma HLS UNROLL factor=100
            	ABij += A[i][k] * B[k][j];
            }
            AB[i][j] = ABij;
        }
    }
}
