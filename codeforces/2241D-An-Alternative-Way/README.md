# 2241D-An-Alternative-Way

**Problem:** [2241D-An-Alternative-Way](https://codeforces.com/contest/2241/problem/D)

**time limit per test:** 2 seconds

**memory limit per test:** 256 megabytes

---

You are given two arrays a and b, each of length n. You are allowed to perform the following operation on array a any number of times (including zero):

 
-  Choose two indices l and r such that 1 ≤ l ≤ r ≤ n; 
-  For each index i from l to r (both inclusive), 
 
-  Set a_i := a_i - 1 if i - l is odd. 
-  Set a_i := a_i + 1 if i - l is even. 
 Determine whether you can make the array a equal to the array b by performing the operation any number of times.


**Input**

The first line contains a single integer t (1 ≤ t ≤ 10⁴) — the number of test cases. Description of each test case follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10⁵) — the length of the arrays a and b.

The second line of each test case contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10⁹) — the elements of the array a.

The third line of each test case contains n integers b_1, b_2, …, b_n (1 ≤ b_i ≤ 10⁹) — the elements of the array b.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10⁵.


**Output**

For each test case, print "YES" if you can make array a equal to array b and "NO" otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).


**Example**

**Input**

```
7
3
1 2 3
1 2 3
4
1 4 5 2
1 5 4 3
1
9
8
6
6 7 6 7 6 7
7 6 7 6 7 6
9
9 8 7 6 5 4 3 2 1
9 9 8 2 4 4 3 5 3
3
1 1 2
2 1 1
2
1 2
1 1
```

**Output**

```
YES
YES
NO
YES
NO
YES
NO
```


**Note**

For the first test case, arrays a and b are already equal.

For the second test case, let us choose l = 2 and r = 4. Now, we update the array a in the following manner:

 
-  For i = 2, we have i - l = 2 - 2 = 0, which is even. Hence, set a_2 := a_2 + 1 = 4 + 1 = 5. 
-  For i = 3, we have i - l = 3 - 2 = 1, which is odd. Hence, set a_3 := a_3 - 1 = 5 - 1 = 4. 
-  For i = 4, we have i - l = 4 - 2 = 2, which is even. Hence, set a_4 := a_4 + 1 = 2 + 1 = 3. 
Finally, we have array a = [1, 5, 4, 3] and array b = [1, 5, 4, 3].

For the third test case, it can be shown that it is impossible to make array a equal to array b.
