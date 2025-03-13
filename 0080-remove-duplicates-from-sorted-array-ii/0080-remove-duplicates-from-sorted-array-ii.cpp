class Solution {
public:
    int removeDuplicates(vector<int> & numbers) {
        if (numbers.empty()) {
            return 0;
        }
        
        auto current_number = numbers.front();
        auto current_count = 0;
        return distance(begin(numbers), remove_if(begin(numbers), end(numbers),
            [&](auto && number) {
                if (number != current_number) {
                    current_number = number;
                    current_count = 1;
                    return false;
                }
                ++current_count;
                return (current_count > 2);
            }));
    }
};
