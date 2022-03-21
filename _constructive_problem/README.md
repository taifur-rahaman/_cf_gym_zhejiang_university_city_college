<h1 align="center">3. Constructive Problem</h1>

    Time limit per test: 1 second
    Memory limit per test: 256 megabytes
    Input: standard input
    Output: standard output

<hr>

Adam has an array a consisting of n integers a0,a1,...,an−1. We call this array beautiful if the number of occurrences of i is ai for $i∈[0,n−1].$

**For example:**

$[1,2,1,0]$ is beautiful. In this array, 0 appears 1 time, 1 appears 2 times, 2 appears 1 time, and 3 appears 0 times, and $a0=1$,$a1=2$,$a2=1$,$a3=0$.
$[0,1]$ is not beautiful. Because $a0=0$ but in fact 0 appears 1 time.
Find a beautiful array of length n. If there are multiple answers, output any. If there is no beautiful array of length n, output −1.

**Input**
The input contains an integer $n (1≤n≤10^6)$ — the length of the beautiful array.

**Output**
Output a beautiful array of length n. If there are multiple answers, output any. If there is no beautiful array of length n, output −1.
