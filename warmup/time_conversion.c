#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    char* time = (char *)malloc(10240 * sizeof(char));
    scanf("%s",time);
    
    int hr = (time[0] - '0')*10 + (time[1] - '0');
    int mn = (time[3] - '0')*10 + (time[4] - '0');
    int sc = (time[6] - '0')*10 + (time[7] - '0');
    int pm = 0;
    if (time[8] == 'P') { pm = 1; }
    
    //printf("%d:%d:%d:%d", hr, mn, sc, pm);
    
    if (pm == 1) {
        if (hr != 12) {
            hr += 12;
        }
    } else if (hr == 12) {
        hr = 0;
    }
    
    if (hr > 9) {        
        if (mn > 9) {
            printf((sc > 9) ? "%d:%d:%d" : "%d:%d:0%d", hr, mn, sc);
        } else {
            printf((sc > 9) ? "%d:0%d:%d" : "%d:0%d:0%d", hr, mn, sc); 
        }
    } else {
        if (mn > 9) {
            printf((sc > 9) ? "0%d:%d:%d" : "0%d:%d:0%d", hr, mn, sc);
        } else {
            printf((sc > 9) ? "0%d:0%d:%d" : "0%d:0%d:0%d", hr, mn, sc); 
        }
    }
    
    return 0;
}
