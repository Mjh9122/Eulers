# include <iostream>
# include <fstream>
# include <math.h>
using namespace std;

struct rarer_tonga{
    int base;
    long doubles;
    double log;
};


int prep_skip(int n, rarer_tonga arr[]){
    int count = 0;
    while(arr[0].log * 2 < arr[n-2].log){
        count++;
        arr[0].log *= 2;
        arr[0].doubles++;
        for(int i = 0; i < n - 2; i ++){
            if(arr[i].log < arr[i+1].log){
                break;
            }else{
                rarer_tonga temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }
    }
    return count;
}

int skip(int n, int m, int count, rarer_tonga arr[]){
    int whole_rounds = (m-count)/(n-1);
    for(int i = 0; i < n - 1; i++){
        arr[i].doubles += whole_rounds;
    }
    return (m-count)%(n-1);
}

int post_skip(int n, int left, rarer_tonga arr[]){
    for(int i = 0; i < left; i++){
        arr[0].log *= 2;
        arr[0].doubles++;
        for(int i = 0; i < n - 2; i ++){
            if(arr[i].log < arr[i+1].log){
                break;
            }else{
                rarer_tonga temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
            }
        }
    }
    return 1;
}

void append(int len, long arr[], long app){
    long newarr[len+1];
    for(int i = 0; i < len-1; i ++){
        newarr[i] = arr[i];
    }
    newarr[len] = app;
    arr = newarr;

}

bool contains(int len, long arr[], long test){
    for(int i = 0; i < len; i++){
        if(arr[i] == test){
            return true;
        }
    }
    return false;
}

void generate_strings(int n, rarer_tonga arr[]){
    long exps[0];
    for(int i = 0; i < n - 1; i ++){
        if(!contains(n-1, exps, arr[i].doubles)){
            append(sizeof(exps), exps, arr[i].doubles);
        }
    }
    cout << sizeof(exps);
    return;
} 

int main(){
    // Init vars
    int n = 1000;
    int m = 1000;
    rarer_tonga* arr = new rarer_tonga[n-1];
    // Create array to store all of our custom objects
    for(int i = 2; i <= n; i++){
        arr[i-2].base = i;
        arr[i-2].doubles = 0;
        arr[i-2].log = log(i);
    }
    // next we run the doubling until the logs of the smallest is larger than the largest
    int count = prep_skip(n, arr);
    // we then skip most of the iteration as it now forms a cycle
    int left = skip(n, m, count, arr);
    // we finish the iteration here
    int done = post_skip(n, left, arr);
    // next we generate some helpful strings
    generate_strings(n, arr);

    cout << count << " " << left << " " << done;

    // Free allocated memory
    delete [] arr;
    return 0;
}