#include "matrixmul.h"
#include "test_data.h"
#include "test_results.h"

#include <stdio.h>
#include <fstream>
#include <iostream>

#define ROWS 100
#define COLS 100

bool checkmatrix(int testC[N][P], int trueC[N][P]){
  for (int i = 0; i < N; i++){
      for (int j = 0; j < P; j++){
          if (testC[i][j] != trueC[i][j]){
              return false;
          }
      }
  }
  return true;
}


int main(){
    int findC1[ROWS][COLS];
    int findC2[ROWS][COLS];
    int findC3[ROWS][COLS];

    matrixmul(A1, B1, findC1);
    matrixmul(A2, B2, findC2);
    matrixmul(A3, B3, findC3);

    if (checkmatrix(findC1, C1)){
        std::cout << "Test 1 was successfully completed. \n";
    }
    else{
        std::cout << "Test 1 had an error. \n";
    }
    if (checkmatrix(findC2, C2)){
        std::cout << "Test 2 was successfully completed. \n";
    }
    else{
        std::cout << "Test 2 had an error. \n";
    }
    if (checkmatrix(findC3, C3)){
        std::cout << "Test 3 was successfully completed. \n";
    }
    else{
        std::cout << "Test 3 had an error. \n";
    }
}
