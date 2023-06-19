public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2];// Giả sử giá trị gần nhất là tổng của ba  phần tử đầu tiên

        for(int i = 0 ; i < nums.Length -2 ;i++)
        {
            int left = i+1;// Vị trí bên trái
            int right = nums.Length-1;//Vị trí bên phải 

            while(left < right)
            {
                int sum = nums[i] + nums[left] + nums[right]; //Tổng của 3 số hiện tại

                if(sum == target)
                    return target;//Trường hợp tổng bằng targer trả về luôn kết quả
                if(Math.Abs(sum - target) < Math.Abs(closestSum - target))
                    closestSum = sum;//Cập nhật giá trị gần nhất nếu tổng hiện tại gần hơn với target
                if(sum < target)
                    left++;//Tăng vị trí bên trái nếu tổng nhỏ hơn target
                else
                    right--;//Giảm vị trí bên phải nếu tổng lớn hơn target
            }
        }
        return closestSum;//Trả về tổng gần nhất tìm dc
    }
}