/* 
Time complexity: O(n) : O(3n) that reduces to O(n)
Space complexity: O(1) : there is no extra space allocated*/
int firstMissingPositive(int* nums, int numsSize) {
    
    // First pass: replace negative numbers with 0 (to ignore them)
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] <= 0) {
            nums[i] = numsSize + 1;
        }
    }

    // Second pass: negate the positive elements that were traversed
    for (int i = 0; i < numsSize; i++) {
        int absVal = abs(nums[i]);
        if(absVal <= numsSize) {
            nums[absVal - 1] = -abs(nums[absVal - 1]);
        }
    }

    // Third pass: find the first missing positive
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= 0) {
            return i + 1;  // i+1 is the first missing positive number
        }
    }

    return numsSize + 1;  // If all numbers from 1 to numsSize are present
}
        