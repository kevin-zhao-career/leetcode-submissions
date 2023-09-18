class Solution {
public:
  long long maximumSum(vector<int>& nums) {
    const int N = nums.size();
    int64_t answer = 0;
    for (int i = 1; i <= N; ++i) {
      int64_t value = nums[i - 1];
      if (value < 0) {  // Not a key number.
        continue;
      }
      for (int j = 2; true; ++j) {
        int index = i * j * j;
        if (index > N) {
          break;
        }
        value += nums[index - 1];
        nums[index - 1] = -1;  // Mark not key
      }
      answer = max(answer, value);
    }
    return answer;
  }
};
