# Time Complexity: The Complete Ground-Up Master Guide

If time complexity feels like a mystery, let's strip away all the complicated math jargon. At its core, **time complexity is just counting how many times a line of code inside your loops runs as the input size ($N$) gets bigger.**

---

### Step 1: What is $N$ and What are We Counting?
Imagine you write a program that takes a list of numbers. The total number of items in that list is called **$N$**. 

If $N = 10$, your list has 10 items. If $N = 1,000,000$, your list has a million items.

When a computer runs code, different loops take different amounts of work. Instead of counting exact seconds (which depends on whether you use a fast laptop or an old phone), we count **operations** in terms of $N$.

---

### Step 2: The Three Most Common Patterns

#### 1. Linear Time: $\mathcal{O}(N)$
A single loop that goes from $0$ to $N$ runs $N$ times.
```cpp
for(int i = 0; i < n; i++) {
    // runs 1 time per item -> O(N)
}