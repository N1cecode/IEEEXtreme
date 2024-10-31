import matplotlib.pyplot as plt

# Provided functions

values = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536, 3072, 6144, 12288, 24576, 49152, 98304, 
          196608, 393216, 786432, 1572864, 3145728, 6291456, 12582912, 25165824, 50331648, 
          100663296, 201326592, 402653184, 805306368, 1610612736]

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
    if x < 3:
        return 1
    elif x in values:
        return 0
    else:
        interval = find_interval(x)
        u, v = map_coord(x, y)
        if is_below_or_on_line(u, v, interval[1]-1):
            return 0
        else:
            if y > interval[0]:
                return sierpinski(x - interval[0], abs(y - interval[0]), depth + 1)
            else:
                return sierpinski(x - interval[0], y, depth + 1)


# Prepare data for plotting with (u, v) coordinates
u_values, v_values, colors = [], [], []
for x in range(1, 100):        # Limiting x < 100
    for y in range(1, x + 1):  # Limiting y ≤ x
        color = sierpinski(x, y)
        u, v = map_coord(x, y)  # Map (x, y) to (u, v) coordinates
        u_values.append(u)
        v_values.append(v)
        colors.append('red' if color == 1 else 'blue')

# Plotting the results with (u, v) coordinates
plt.figure(figsize=(8, 8))
plt.scatter(u_values, v_values, c=colors, s=10, marker='s')
plt.title("Sierpinski Triangle Points in (u, v) Coordinates for x < 100")
plt.xlabel("u")
plt.ylabel("v")
# plt.gca().invert_yaxis()
plt.show()
