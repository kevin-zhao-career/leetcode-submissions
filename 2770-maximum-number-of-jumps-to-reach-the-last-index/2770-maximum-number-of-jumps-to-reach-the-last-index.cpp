class Solution {
public:
    int maximumJumps(const vector<int> & numbers, const int target) {
        auto number_size = numbers.size();
        
        vector<int> number_queue(number_size, -1);
        number_queue[0] = 0;
        for (auto source_index = 0; source_index != number_size; ++source_index) {
            if(number_queue[source_index] == -1) {
                continue;
            }
            for(auto destination_index = source_index + 1; destination_index != number_size; ++destination_index) {
                if(abs(numbers[destination_index] - numbers[source_index]) <= target) {
                    number_queue[destination_index] = max(number_queue[source_index] + 1, number_queue[destination_index]);
                }  
            }
        }
        return number_queue[number_size - 1];
    }
};
