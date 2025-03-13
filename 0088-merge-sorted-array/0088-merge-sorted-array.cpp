class Solution {
public:
    void merge(vector<int>& numbers_1, int numbers_1_size, vector<int>& numbers_2, int numbers_2_size) {
        auto numbers_1_index = numbers_1_size - 1;
        auto numbers_2_index = numbers_2_size - 1;
        auto final_numbers_index = numbers_1_size + numbers_2_size - 1;

        while (numbers_2_index >= 0) {
            if (numbers_1_index >= 0 && numbers_1[numbers_1_index] > numbers_2[numbers_2_index]) {
                numbers_1[final_numbers_index--] = numbers_1[numbers_1_index--];
            } else {
                numbers_1[final_numbers_index--] = numbers_2[numbers_2_index--];
            }
        }
    }
};
