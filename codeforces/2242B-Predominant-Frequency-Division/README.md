# 2242B-Predominant-Frequency-Division

**Problem:** [2242B-Predominant-Frequency-Division](https://codeforces.com/contest/2242/problem/B)

**time limit per test:** 2 seconds

**memory limit per test:** 512 megabytes

---

You are given an array a consisting of the numbers 1, 2, and 3. Check whether it is possible to split it into three contiguous non-empty parts such that, for each part i from 1 to 3, the following condition holds:

 
-  the number of elements greater than i is at most half of the part. 
In other words, you need to divide the array a into three pairwise disjoint contiguous non-empty parts so that in the left part the number of ones is at least the total number of twos and threes, in the middle part the total number of ones and twos is at least the number of threes, and the right part can be anything, but it must be non-empty.

For example, the array [2, 1, 1, 3, 3, 1, 2, 3] can be split into three parts: [2, 1, 1, 3], [3, 1, 2], and [3]. And the array [2, 1, 3, 3, 3, 2, 3] cannot be split in such a way.


**Input**

Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10⁴). The description of the test cases follows.

The first line of each test case contains an integer n (3 ≤ n ≤ 2 ⋅ 10^{5}) — the length of the array.

The second line of each test case contains n integers a_{i} (1 ≤ a_{i} ≤ 3).

Additional constraints on the input data: 

 
-  the sum of n over all test cases does not exceed 2 ⋅ 10^{5}.


**Output**

For each test case, print YES if there exists a way to split the array as required, and NO otherwise.

You may print the answer in any case. For example, YeS, YES, NO, nO will also be accepted.


**Example**

**Input**

```
10
8
2 1 1 3 3 1 2 3
7
2 1 3 3 3 2 3
4
1 3 3 2
6
2 2 2 1 1 1
8
3 2 1 2 1 1 2 3
3
2 1 2
3
1 2 3
5
1 3 3 1 1
5
1 1 3 3 1
3
1 3 1
```

**Output**

```
YES
NO
NO
NO
YES
NO
YES
YES
YES
NO
```


**Note**

The first two test cases are explained in the statement.

In the third test case, the left part may be [1], but then any choice of the middle part ([3], [3, 3], [3, 3, 2]) does not work. The left part may also be [1, 3]; then the middle part must be [3, 2], and in this case the right part is empty. Therefore, the answer for the third example is NO.

In the fourth test case, the only valid left part is the entire array, because on any non-empty shorter prefix the number of ones is less than the number of twos, so the middle and right parts cannot both be non-empty.

In the fifth test case, the split [3, 2, 1, 2, 1, 1], [2], [3] works.

In the sixth test case, the only possible split is [2], [1], [2], but the left part does not work.

In the seventh test case, the split [1], [2], [3] works.

In the eighth test case, the split [1, 3], [3, 1], [1] works.

In the ninth test case, the split [1], [1], [3, 3, 1] works.

In the tenth test case, the only possible split is [1], [3], [1], but the middle part does not work.
