'''
 Problem: https://csacademy.com/ieeextreme-practice/task/sierpinski/
 
 思路：
 将每次翻转时x的坐标列表保存，值为3*2^N，N从0到24，大于24超出题目输入范围
 首先映射坐标到另一坐标系，判断给定点是否为inverted blue triangle区域中，是则返回0，否则将坐标减去左侧最近的翻转点，再递归调用，直至x<3
'''

values = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 196608, 393216, 786432, 1572864, 3145728, 6291456, 12582912, 25165824, 50331648, 100663296, 201326592, 402653184, 805306368, 1610612736]

def map_coord(x, y):
    u = x - 1
    v = abs((y - 1) * 2 - (x - 1))
    return u, v

def is_below_or_on_line(u, v, b):
    return v <= -u + b

def find_interval(number):
    for i in range(len(values) - 1):
        if values[i] <= number < values[i + 1]:
            return (values[i], values[i + 1])
    return None

def sierpinski(x, y, depth=0):
    print(f"Current depth: {depth}:",x,y)
    if x < 3:
        return 1
    elif x in values:
        return 0
    else:
        interval = find_interval(x)
        print("        interval:",interval)
        u, v = map_coord(x, y)
        print("             u,v:",u, v)
        if is_below_or_on_line(u, v, interval[1]-1):
            return 0
        else:
            if y > interval[0]:
                return sierpinski(x - interval[0], abs(y - interval[0]), depth + 1)
            else:
                return sierpinski(x - interval[0], y, depth + 1)
        
def main():
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    for x, y in queries:
        print(sierpinski(x, y))
      
if __name__ == '__main__':
    main()
