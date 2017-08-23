#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n, pd = 0, sd = 0; 
    scanf("%d",&n);
    int a[n][n];
    
    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){          
          scanf("%d",&a[a_i][a_j]);           
          if (a_i == a_j) {
              pd += a[a_i][a_j];
          } 
          if (a_i == (n - a_j - 1)) {
              sd += a[a_i][a_j];
          }
       }
    }
        
    int diff = pd - sd;
    
    printf("%d", (diff > 0) ? diff : -diff);
    
    return 0;
}
