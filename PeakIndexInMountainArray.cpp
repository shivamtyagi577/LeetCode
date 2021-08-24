class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int i =1;
        for(int i = 1; i < arr.size();){
            if(arr[i] > arr[i-1] and arr[i] > arr[i+1]){
                cout<<i<<endl;
                return i;
            }
            else{
                //cout<<i<<endl;
                i++;
            }
        }
        return {};
    }
};
