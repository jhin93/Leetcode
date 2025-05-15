

# Leetcode
```python
# List comprehension 
squares = [x**2 for x in range(10)]
print(squares)  # 출력: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # 출력: [2, 4, 6, 8, 10]

words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)  # 출력: [5, 5, 6]

numbers = [1, 2, 3, 4]
strings = [str(num) for num in numbers]
print(strings)  # 출력: ['1', '2', '3', '4']
```
