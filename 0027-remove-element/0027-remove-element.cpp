class Solution {
public:
    int removeElement(vector<int> & numbers, int value) {
        auto last_non_value_iterator = remove(begin(numbers), end(numbers), value);
        return distance(begin(numbers), last_non_value_iterator);
    }
};
