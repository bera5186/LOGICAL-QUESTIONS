// for this problem recursive approach is best

#include<stdio.h>

// function declaration
int func(int n);

int main(){
    func(1); // function call
    return 0 ;
}

int func(int n){
    int counter = n ; // counter variable
    printf("%d\n",n);
    if(counter<1000){
        func(n+1); // recursive call
    }
    else{
        return 0 ;
    }
}
