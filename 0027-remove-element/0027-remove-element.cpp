class Solution {
public:
    int removeElement(vector<int> & numbers, int value) {
        return distance(begin(numbers), remove(begin(numbers), end(numbers), value));
    }
};
