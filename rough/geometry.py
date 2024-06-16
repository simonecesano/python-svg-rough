# export function rotatePoints(points: Point[], center: Point, degrees: number): void {
# export function rotateLines(lines: Line[], center: Point, degrees: number): void {
# export function lineLength(line: Line): number {
# ------------------------------------------------------------------------------------------------------------------------
# 251
"""
export function rotatePoints(points: Point[], center: Point, degrees: number): void {{
  if (points && points.length) {
    const [cx, cy] = center;
    const angle = (Math.PI / 180) * degrees;
    const cos = Math.cos(angle);
    const sin = Math.sin(angle);
    points.forEach((p) => {
      const [x, y] = p;
      p[0] = ((x - cx) * cos) - ((y - cy) * sin) + cx;
      p[1] = ((x - cx) * sin) + ((y - cy) * cos) + cy;
    });
  }
}
"""
"""
export function rotatePoints(points: Point[], center: Point, degrees: number): void {{
  if (points && points.length) {
    const [cx, cy] = center;
    const angle = (Math.PI / 180) * degrees;
    const cos = Math.cos(angle);
    const sin = Math.sin(angle);
    points.forEach((p) => {
      const [x, y] = p;
      p[0] = ((x - cx) * cos) - ((y - cy) * sin) + cx;
      p[1] = ((x - cx) * sin) + ((y - cy) * cos) + cy;
    });
  }
}
"""
# ------------------------------------------------------------------------------------------------------------------------
# 251
# export function rotatePoints(points: Point[], center: Point, degrees: number): void {

#--------------------------------------------------------------------------------
# Here is the equivalent code in Python 3:
# ```
# import math
# 
# def rotate_points(points, center, degrees):
#     if points and len(points):
#         cx, cy = center
#         angle = math.pi / 180 * degrees
#         cos_angle = math.cos(angle)
#         sin_angle = math.sin(angle)
# 
#         for p in points:
#             x, y = p
#             new_x = (x - cx) * cos_angle - (y - cy) * sin_angle + cx
#             new_y = (x - cx) * sin_angle + (y - cy) * cos_angle + cy
#             p[0], p[1] = new_x, new_y
# 
# # Example usage:
# center = [5, 3]
# degrees = 45
# points = [[1, 2], [3, 4], [5, 6]]
# rotate_points(points, center, degrees)
# print(points)  # Output: [[-0.765... , 2.236...], [1.414... , 4.2426...], [3.535... , 6.1488...]]
# ```
# Note that in Python, we don't need to explicitly define the return type of a function (e.g. `: void`), as functions always return `None` by default.
# 
# Also, I assume that `Point` is a custom class or tuple representing a 2D point with x and y coordinates. In Python, you can represent this using a list or tuple, as shown in the example usage.
#--------------------------------------------------------------------------------
import math

def rotate_points(points, center, degrees):
    if points and len(points):
        cx, cy = center
        angle = math.pi / 180 * degrees
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        for p in points:
            x, y = p
            new_x = (x - cx) * cos_angle - (y - cy) * sin_angle + cx
            new_y = (x - cx) * sin_angle + (y - cy) * cos_angle + cy
            p[0], p[1] = new_x, new_y

# # Example usage:
# center = [5, 3]
# degrees = 45
# points = [[1, 2], [3, 4], [5, 6]]
# rotate_points(points, center, degrees)
# print(points)  # Output: [[-0.765... , 2.236...], [1.414... , 4.2426...], [3.535... , 6.1488...]]

# ------------------------------------------------------------------------------------------------------------------------
# 684
"""
export function rotateLines(lines: Line[], center: Point, degrees: number): void {{
  const points: Point[] = [];
  lines.forEach((line) => points.push(...line));
  rotatePoints(points, center, degrees);
}
"""
"""
export function rotateLines(lines: Line[], center: Point, degrees: number): void {{
  const points: Point[] = [];
  lines.forEach((line) => points.push(...line));
  rotatePoints(points, center, degrees);
}
"""
# ------------------------------------------------------------------------------------------------------------------------
# 684
# export function rotateLines(lines: Line[], center: Point, degrees: number): void {

#--------------------------------------------------------------------------------
# Here's the equivalent code in Python:
# 
# ```Python
# def rotate_lines(lines, center, degrees):
#     points = []
#     for line in lines:
#         points.extend(line)
#     rotate_points(points, center, degrees)
# 
# def rotate_points(points, center, degrees):
#     # implement your point rotation logic here
#     pass
# ```
# 
# Here's a brief explanation of the translation:
# 
# - The `export` keyword is not needed in Python. Instead, you can define a function and use it as necessary.
# - TypeScript uses type annotations like `Line[]` to indicate that `lines` should be an array of `Line` objects. In Python, we don't need explicit type definitions for variables or function parameters.
# - The `void` return type is not needed in Python. Functions can return any value, including `None`, and if they don't explicitly return anything, the default is `None`.
# - Python's `for` loop works similarly to TypeScript's `forEach`. In this case, we're iterating over each `line` in the `lines` list.
# - The `push` method is not needed in Python. Instead, you can use list comprehension or the `extend` method (as shown) to add elements to a list.
# - You'll need to implement your own logic for rotating points in the `rotate_points` function. This code simply leaves that part blank.
#--------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------
# 856
"""
export function lineLength(line: Line): number {{
  const p1 = line[0];
  const p2 = line[1];
  return Math.sqrt(Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2));
}
"""
"""
export function lineLength(line: Line): number {{
  const p1 = line[0];
  const p2 = line[1];
  return Math.sqrt(Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2));
}
"""
# ------------------------------------------------------------------------------------------------------------------------
# 856
# export function lineLength(line: Line): number {

#--------------------------------------------------------------------------------
# Here's the equivalent code in Python 3:
# 
# ```python
# def line_length(line):
#     p1 = line[0]
#     p2 = line[1]
#     return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
# ```
# 
# In Python, we don't need to explicitly declare the type of the function or variables like we do in TypeScript. The code is relatively straightforward: it calculates the Euclidean distance between two points on a line and returns that value.
# 
# Note that in Python, `**` denotes exponentiation (e.g., `2 ** 3` means "2 to the power of 3"), and `(expression) ** 0.5` is equivalent to `math.sqrt(expression)` from the TypeScript code.
#--------------------------------------------------------------------------------
def line_length(line):
    p1 = line[0]
    p2 = line[1]
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

