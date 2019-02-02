#include <stdio.h>

int main(void){
    for(int i=0; i<64; i++){
        printf("a");
    }
    printf("\x64\x63\x62\x61");
}