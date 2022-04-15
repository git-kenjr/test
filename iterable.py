# def test():
#     yield 5
# gen=test() #產生 生成器
# for i in gen:
#     print(i) 

result = (x ** 2 for x in range(1, 6))
print(next(result)) # 輸出 1
print(next(result)) # 輸出 4
print(next(result)) # 輸出 9
print(next(result)) # 輸出 16
print(next(result)) # 輸出 25
# print(next(result)) # 輸出 "StopIteration"
print(result)  # TypeError: 'generator' object is not subscriptable
