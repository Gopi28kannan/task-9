def fibonacci(c):
          a=[1, 1]
          any(map(lambda _: a.append(sum(a[-2:])), range(1, c)))
          return a[:c]
print(fibonacci(50))
