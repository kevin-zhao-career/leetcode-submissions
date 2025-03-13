class Solution {
public:
    int removeDuplicates(vector<int>& numbers) {
        unordered_set<int> number_set;
        return distance(begin(numbers), remove_if(begin(numbers), end(numbers),
        [&](auto && number) {
            auto number_exists = (number_set.find(number) != end(number_set));
            if (!number_exists) {
                number_set.insert(number);
            }
            return number_exists;
        }));
    }
};
