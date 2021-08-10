#include<iostream>
#include<vector>
#include<unordered_set>
#include<string>
using namespace std;

vector<int> pairSum(vector<int> arr, int Sum){
    unordered_set<int> s;
    vector<int> result;

    for(int i=0;i<arr.size();i++){
        int x = Sum - arr[i];

        // int y = s.find(x);
        // cout<<y<<endl;
        if(s.find(x)!=s.end()){
            result.push_back(arr[i]);
            result.push_back(x);
            return result;
        }
        s.insert(arr[i]);
    }
    return {};
}

int main(){
    vector<int> arr = {10, 5, 2 , 3, -6, 9 , 11};
	int S = 4;
    // cout<<arr.find(11)<<endl;
	auto p = pairSum(arr,S);
	if(p.size()==0){
		cout<<"No such pair";
	}
	else{
		cout<<p[0]<<","<<p[1]<<endl;
	}

	return 0;
}
