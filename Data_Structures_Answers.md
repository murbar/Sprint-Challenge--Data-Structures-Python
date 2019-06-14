Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

   > O(1), just writing to an element in an existing array

2. What is the space complexity of your ring buffer's `append` function?

   > O(n) where n is the capacity of the buffer

3. What is the runtime complexity of your ring buffer's `get` method?

   > O(n), we have to iterate of the array and filter out None values

4. What is the space complexity of your ring buffer's `get` method?

   > O(n) where n is the number of non-None values in the buffer

5. What is the runtime complexity of the provided code in `names.py`?

   > O(1 + n \* n + 1 + 1) -> O(n^2)

6. What is the space complexity of the provided code in `names.py`?

   > O(n1 + n2 + d) -> O(n) where n is size of of input lists and d is number of duplicates

7. What is the runtime complexity of your optimized code in `names.py`?

   > O(n + n \* 1) -> O(2n) -> O(n) with a hash table

8. What is the space complexity of your optimized code in `names.py`?
   > O(n + d) -> O(n) where n is size of of input lists and d is number of duplicates
