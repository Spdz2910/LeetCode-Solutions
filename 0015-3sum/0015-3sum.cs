public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums)
{
    Array.Sort(nums); // Sắp xếp mảng nums

    List<IList<int>> result = new List<IList<int>>();
    int n = nums.Length;

    for (int i = 0; i < n - 2; i++)
    {
        if (i > 0 && nums[i] == nums[i - 1])
            continue; // Bỏ qua trường hợp trùng lặp

        int left = i + 1;
        int right = n - 1;

        while (left < right)
        {
            int total = nums[i] + nums[left] + nums[right];

            if (total < 0)
                left++;
            else if (total > 0)
                right--;
            else
            {
                result.Add(new List<int> { nums[i], nums[left], nums[right] });

                // Bỏ qua trường hợp trùng lặp của nums[left] và nums[right]
                while (left < right && nums[left] == nums[left + 1])
                    left++;
                while (left < right && nums[right] == nums[right - 1])
                    right--;

                left++;
                right--;
            }
        }
    }
    return result;
}
}