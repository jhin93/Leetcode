

# Leetcode
```python
# === Python ===
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

#Slicing
lst = [1, 2, 3, 4, 5]
print(lst[::-1])  # 출력: [5, 4, 3, 2, 1]

test = 'abcde'
print(test[1:4:-1])  # 출력: ''
print(test[4:1:-1])  # 출력: 'edc'

test = 'abcde'
print(test[::2])  # 출력: 'ace' (2칸씩 앞으로)
print(test[::-2])  # 출력: 'eca' (2칸씩 뒤로)

#lambda function

## lambda의 역할은 함수 이름 없이 간단하게 함수를 만들고 싶을 때 사용합니다. 보통 콜백 함수나 한 번만 쓸 간단한 함수를 만들 때 많이 씁니다.
def add(x, y):
    return x + y

add = lambda x, y: x + y

```
