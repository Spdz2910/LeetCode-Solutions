/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;
        
        while(l1 != null || l2 != null)
        {
            int x = (l1 != null)? l1.val :0;
            int y = (l2 != null)? l2.val :0;
            //tính tổng và phân dư
            int sum = x + y + carry;
            carry = sum /10;
            int digit = sum % 10;
            
            //tạo một node mới chứa kết quả và di chuyển đến node tiếp theo
            current.next = new ListNode(digit);
            current = current.next;

            //di chuyển đến node tiếp theo của 2 dannh sách nếu chúng còn
            if(l1 != null)
                l1 = l1.next;
            if(l2 != null)
                l2 = l2.next;
        }
        //nếu còn phần dư thêm 1 node mới chứa phần dư này 
        if(carry > 0)
            current.next = new ListNode(carry);
        return dummy.next;
    }
}