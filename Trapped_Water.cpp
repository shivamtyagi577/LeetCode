#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<unordered_set>
using namespace std;

int trappedWater(vector<int> heights){
    int n = heights.size();
    if(n<=2){
        return 0;
    }

    //Left Max, Right Max
    vector<int> left(n,0) , right(n,0);
    left[0] = heights[0];
    right[n-1] = heights[n-1];

    //Filling up Max values left & right vectors
    for(int i=1; i<n; i++){
        left[i] = max(left[i-1],heights[i]);
        right[n-i-1] = max(right[n-i],heights[n-i-1]);
    }

    //water
    int water = 0;
    for(int i=0;i<n;i++){
        water+=min(left[i],right[i]) - heights[i];
    }

    return water;
}

int main(){

    vector<int> heights{0,1,0,2,1,0,4,2,1,2,0};

    int result = trappedWater(heights);
    cout<<result<<endl;

    return 0;
}
