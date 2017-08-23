#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n;
    double pos = 0.0, neg = 0.0, zer = 0.0; 
    scanf("%d",&n);
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
       if (arr[arr_i] > 0) {
           pos++;
       } else if (arr[arr_i] < 0) {
           neg++;
       } else {
           zer++;
       }
    }
    
    double nn = (double) n;
    printf("%.6f\n%.6f\n%.6f\n", pos/nn, neg/nn, zer/nn);
    
    return 0;
}
