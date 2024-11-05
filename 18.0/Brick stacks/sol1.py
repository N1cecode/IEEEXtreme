import numpy as np
def solve(N, x, A_list):
    bricks = sorted(A_list, reverse=True)
    rest_num_bricks = N
    stack_list = []
    rest_indices = list(range(N))
    try:
        while bricks:
            current_brick = bricks[rest_indices.pop(0)]
            rest_num_bricks -= 1
            current_stack = []
            current_stack.append(current_brick)
            for i in rest_indices.copy():
                if current_brick >= bricks[i] + x:
                    current_brick = bricks[i]
                    rest_indices.remove(i)
                    rest_num_bricks -= 1
                    current_stack.append(current_brick)
                elif i == rest_num_bricks:
                    break
                
            stack_list.append(current_stack)
    except:
        return stack_list
    return stack_list

def main():
    N, x = map(int, input().split())
    A_list = list(map(int, input().split()))
    stack_list = solve(N, x, A_list)
    print(len(stack_list))
    for i in range(len(stack_list)):
        print(len(stack_list[i]), " ".join(map(str, stack_list[i])))

if __name__ == '__main__':
    main()
