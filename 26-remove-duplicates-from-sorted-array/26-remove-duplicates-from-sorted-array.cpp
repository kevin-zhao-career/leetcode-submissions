class Solution {
public:
    int removeDuplicates(vector<int>& numbers) {
    int count = 0;
    int n = numbers.size();
    for(int i = 1; i < n; i++){
        if(numbers[i] == numbers[i-1]) count++;
        else numbers[i-count] = numbers[i];
    }
        return n-count;
    }
};
