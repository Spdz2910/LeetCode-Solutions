<h2><a href="https://leetcode.com/problems/merge-k-sorted-lists">23. Merge k Sorted Lists</a></h2><h3>Hard</h3><hr><p>You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list is sorted in ascending order.</p>

<p><em>Merge all the linked-lists into one sorted linked-list and return it.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> lists = [[1,4,5],[1,3,4],[2,6]]
<strong>Output:</strong> [1,1,2,3,4,4,5,6]
<strong>Explanation:</strong> The linked-lists are:
[
  1-&gt;4-&gt;5,
  1-&gt;3-&gt;4,
  2-&gt;6
]
merging them into one sorted list:
1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> lists = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> lists = [[]]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>k == lists.length</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= lists[i].length &lt;= 500</code></li>
	<li><code>-10<sup>4</sup> &lt;= lists[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>lists[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>The sum of <code>lists[i].length</code> will not exceed <code>10<sup>4</sup></code>.</li>
</ul>


Cách giải bài toán
Đầu tiên, ta tạo một min-heap rỗng. Min-heap được sử dụng để lưu trữ các nút từ các danh sách liên kết theo thứ tự tăng dần.

Tiếp theo, ta thêm nút đầu tiên từ mỗi danh sách liên kết vào min-heap. Ta sử dụng giá trị của nút làm tiêu chí để so sánh và sắp xếp trong min-heap.

Sau đó, ta tạo một nút giả (dummy node) và đặt nó làm nút hiện tại. Nút giả này sẽ được sử dụng để xây dựng danh sách liên kết kết quả.

Tiến hành lặp cho đến khi min-heap trống. Trong mỗi vòng lặp, ta thực hiện các bước sau:

Loại bỏ nút có giá trị nhỏ nhất từ min-heap (là nút nhỏ nhất trong tất cả các danh sách liên kết).
Gắn nút đã loại bỏ vào con trỏ next của nút hiện tại.
Di chuyển nút hiện tại đến nút vừa gắn.
Nếu nút đã loại bỏ có một nút tiếp theo, ta thêm nút đó vào min-heap.
Khi min-heap trống, ta đã hoàn thành việc hợp nhất tất cả các danh sách liên kết thành một danh sách liên kết duy nhất đã được sắp xếp. Ta trả về nút giả (dummy node) làm đầu của danh sách liên kết kết quả
