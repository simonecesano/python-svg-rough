# export function line(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions): OpSet {
# export function linearPath(points: Point[], close: boolean, o: ResolvedOptions): OpSet {
# export function polygon(points: Point[], o: ResolvedOptions): OpSet {
# export function rectangle(x: number, y: number, width: number, height: number, o: ResolvedOptions): OpSet {
# export function curve(inputPoints: Point[] | Point[][], o: ResolvedOptions): OpSet {
# export function ellipse(x: number, y: number, width: number, height: number, o: ResolvedOptions): OpSet {
# export function generateEllipseParams(width: number, height: number, o: ResolvedOptions): EllipseParams {
# export function ellipseWithParams(x: number, y: number, o: ResolvedOptions, ellipseParams: EllipseParams): EllipseResult {
# export function arc(x: number, y: number, width: number, height: number, start: number, stop: number, closed: boolean, roughClosure: boolean, o: ResolvedOptions): OpSet {
# export function svgPath(path: string, o: ResolvedOptions): OpSet {
# export function solidFillPolygon(polygonList: Point[][], o: ResolvedOptions): OpSet {
# export function patternFillPolygons(polygonList: Point[][], o: ResolvedOptions): OpSet {
# export function patternFillArc(x: number, y: number, width: number, height: number, start: number, stop: number, o: ResolvedOptions): OpSet {
# export function randOffset(x: number, o: ResolvedOptions): number {
# export function randOffsetWithRange(min: number, max: number, o: ResolvedOptions): number {
# export function doubleLineFillOps(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions): Op[] {
# function cloneOptionsAlterSeed(ops: ResolvedOptions): ResolvedOptions {
# function random(ops: ResolvedOptions): number {
# function _offset(min: number, max: number, ops: ResolvedOptions, roughnessGain = 1): number {
# function _offsetOpt(x: number, ops: ResolvedOptions, roughnessGain = 1): number {
# function _doubleLine(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions, filling = false): Op[] {
# function _line(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions, move: boolean, overlay: boolean): Op[] {
# function _curveWithOffset(points: Point[], offset: number, o: ResolvedOptions): Op[] {
# function _curve(points: Point[], closePoint: Point | null, o: ResolvedOptions): Op[] {
# function _computeEllipsePoints(increment: number, cx: number, cy: number, rx: number, ry: number, offset: number, overlap: number, o: ResolvedOptions): Point[][] {
# function _arc(increment: number, cx: number, cy: number, rx: number, ry: number, strt: number, stp: number, offset: number, o: ResolvedOptions) {
# function _bezierTo(x1: number, y1: number, x2: number, y2: number, x: number, y: number, current: Point, o: ResolvedOptions): Op[] {
# ------------------------------------------------------------------------------------------------------------------------
# 9085
"""
function _offset(min: number, max: number, ops: ResolvedOptions, roughnessGain = 1): number {{
  return ops.roughness * roughnessGain * ((random(ops) * (max - min)) + min);
}
"""
"""
function _offset(min: number, max: number, ops: {}, roughnessGain = 1): number {{
  return ops.roughness * roughnessGain * ((random(ops) * (max - min)) + min);
}
"""
# ------------------------------------------------------------------------------------------------------------------------
# 9085
# function _offset(min: number, max: number, ops: ResolvedOptions, roughnessGain = 1): number {
# --------------------------------------------------------------------------------
# Here is the equivalent Python code for the given TypeScript function:
# ```python
# import random
# 
# def _offset(min, max, ops, roughness_gain=1):
#     def inner_offset(min, max, ops, roughness_gain=1):
#         return (ops.get('roughness', 0) * roughness_gain * ((random.random() * (max - min)) + min))
#     return inner_offset(min, max, ops, roughness_gain)
# ```
# Note the following changes:
# 
# * In Python, we don't need to declare the function type or use the `:` symbol to indicate the return type.
# * We replaced `resolvedOptions` with a plain dictionary (`ops`) and used the `.get()` method to access its values (or default to 0 if the key is not present).
# * We replaced `random(ops)` with `random.random()`, which generates a random floating-point number between 0 and 1.
# * We removed the TypeScript-specific syntax for defining the inner function, as Python does not require explicit function definitions.
# 
# The function now takes four arguments: `min` and `max` (the minimum and maximum values), `ops` (a dictionary of options), and `roughness_gain` (an optional parameter with a default value of 1). The inner function is defined using the `def` statement, and the outer function returns the result of calling the inner function.
# --------------------------------------------------------------------------------
import random

def _offset(min, max, ops, roughness_gain=1):
    def inner_offset(min, max, ops, roughness_gain=1):
        return (ops.get('roughness', 0) * roughness_gain * ((random.random() * (max - min)) + min))
    return inner_offset(min, max, ops, roughness_gain)

# --------------------------------------------------------------------------------
# 9248
"""
function _offsetOpt(x: number, ops: ResolvedOptions, roughnessGain = 1): number {{
  return _offset(-x, x, ops, roughnessGain);
}
"""
"""
function _offsetOpt(x: number, ops: {}, roughnessGain = 1): number {{
  return _offset(-x, x, ops, roughnessGain);
}
"""
# ------------------------------------------------------------------------------------------------------------------------
# 9248
# function _offsetOpt(x: number, ops: ResolvedOptions, roughnessGain = 1): number {
# --------------------------------------------------------------------------------
# Here is the equivalent Python code:
# ```
# def offset_opt(x, ops, roughness_gain=1):
#     def _offset_opt(x, ops, roughness_gain=1):
#         return _offset(-x, x, ops, roughness_gain)
#     return _offset_opt(x, ops, roughness_gain)
# 
# # assuming you have a separate function `_offset` defined elsewhere
# def _offset(min_x: float, max_x: float, ops: dict, roughness_gain: float) -> float:
#     pass  # implement this function as needed
# ```
# Here's a brief explanation of the translation:
# 
# * In TypeScript, `function` is used to define a function. In Python, we use the `def` keyword.
# * The type annotations for `x`, `ops`, and `roughness_gain` are removed, since Python is dynamically typed.
# * The default value for `roughness_gain` is specified using the `= 1` syntax.
# * The inner function `_offset_opt` is defined as a closure within the outer function. In Python, we don't need to use a separate scope or return this function; instead, we can simply define the inner logic inside the outer function.
# * The `_offset` function is assumed to be implemented elsewhere in your code.
# 
# Note that this translation assumes you have a separate implementation for the `_offset` function, which is not shown here. You will need to implement this function as needed for your specific use case.
# --------------------------------------------------------------------------------
def offset_opt(x, ops, roughness_gain=1):
    def _offset_opt(x, ops, roughness_gain=1):
        return _offset(-x, x, ops, roughness_gain)
    return _offset_opt(x, ops, roughness_gain)

# assuming you have a separate function `_offset` defined elsewhere
def _offset(min_x: float, max_x: float, ops: dict, roughness_gain: float) -> float:
    pass  # implement this function as needed

# ------------------------------------------------------------------------------------------------------------------------
# 9410
"""
function _doubleLine(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions, filling = false): Op[] {{
  const singleStroke = filling ? o.disableMultiStrokeFill : o.disableMultiStroke;
  const o1 = _line(x1, y1, x2, y2, o, true, false);
  if (singleStroke) {
    return o1;
  }
  const o2 = _line(x1, y1, x2, y2, o, true, true);
  return o1.concat(o2);
}
"""
"""
function _doubleLine(x1: number, y1: number, x2: number, y2: number, o: {}, filling = false): Op[] {{
  const singleStroke = filling ? o.disableMultiStrokeFill : o.disableMultiStroke;
  const o1 = _line(x1, y1, x2, y2, o, true, false);
  if (singleStroke) {
    return o1;
  }
  const o2 = _line(x1, y1, x2, y2, o, true, true);
  return o1.concat(o2);
}
"""
# ------------------------------------------------------------------------------------------------------------------------
# 9410
# function _doubleLine(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions, filling = false): Op[] {
# --------------------------------------------------------------------------------
# Here is the equivalent code in Python3:
# ```
# def double_line(x1: float, y1: float, x2: float, y2: float, options: dict, filling=False):
#     def _double_line(x1: float, y1: float, x2: float, y2: float, options: dict, filling=False) -> list:
#         single_stroke = options.get('disableMultiStrokeFill', options['disableMultiStroke']) if filling else options['disableMultiStroke']
#         o1 = line(x1, y1, x2, y2, options, True, False)
#         if single_stroke:
#             return [o1]
#         o2 = line(x1, y1, x2, y2, options, True, True)
#         return [o1] + o2
# 
#     return _double_line(x1, y1, x2, y2, options, filling)
# 
# def line(x1: float, y1: float, x2: float, y2: float, options: dict, stroke: bool, fill: bool) -> object:
#     # Implement your line drawing logic here
#     pass
# ```
# Note that:
# 
# * In Python, we don't need to declare the types of variables explicitly like in TypeScript. Instead, we can use type hints for documentation purposes.
# * The `Op[]` array is replaced with a Python list (`list`) and an object (`object`).
# * The `_doubleLine` function is defined inside the `double_line` function, which is equivalent to the original code's nested function definition.
# * We use the `.get()` method to access dictionary values in Python, which is equivalent to TypeScript's optional chaining operator (`?.`).
# --------------------------------------------------------------------------------
def double_line(x1: float, y1: float, x2: float, y2: float, options: dict, filling=False):
    def _double_line(x1: float, y1: float, x2: float, y2: float, options: dict, filling=False) -> list:
        single_stroke = options.get('disableMultiStrokeFill', options['disableMultiStroke']) if filling else options['disableMultiStroke']
        o1 = line(x1, y1, x2, y2, options, True, False)
        if single_stroke:
            return [o1]
        o2 = line(x1, y1, x2, y2, options, True, True)
        return [o1] + o2

    return _double_line(x1, y1, x2, y2, options, filling)

def line(x1: float, y1: float, x2: float, y2: float, options: dict, stroke: bool, fill: bool) -> object:
    # Implement your line drawing logic here
    pass

# ------------------------------------------------------------------------------------------------------------------------
# 9787
"""
function _line(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions, move: boolean, overlay: boolean): Op[] {{
  const lengthSq = Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2);
  const length = Math.sqrt(lengthSq);
  let roughnessGain = 1;
  if (length < 200) {
    roughnessGain = 1;
  } else if (length > 500) {
    roughnessGain = 0.4;
  } else {
    roughnessGain = (-0.0016668) * length + 1.233334;
  }

  let offset = o.maxRandomnessOffset || 0;
  if ((offset * offset * 100) > lengthSq) {
    offset = length / 10;
  }
  const halfOffset = offset / 2;
  const divergePoint = 0.2 + random(o) * 0.2;
  let midDispX = o.bowing * o.maxRandomnessOffset * (y2 - y1) / 200;
  let midDispY = o.bowing * o.maxRandomnessOffset * (x1 - x2) / 200;
  midDispX = _offsetOpt(midDispX, o, roughnessGain);
  midDispY = _offsetOpt(midDispY, o, roughnessGain);
  const ops: Op[] = [];
  const randomHalf = () => _offsetOpt(halfOffset, o, roughnessGain);
  const randomFull = () => _offsetOpt(offset, o, roughnessGain);
  const preserveVertices = o.preserveVertices;
  if (move) {
    if (overlay) {
      ops.push({
        op: 'move', data: [
          x1 + (preserveVertices ? 0 : randomHalf()),
          y1 + (preserveVertices ? 0 : randomHalf()),
        ],
      });
    } else {
      ops.push({
        op: 'move', data: [
          x1 + (preserveVertices ? 0 : _offsetOpt(offset, o, roughnessGain)),
          y1 + (preserveVertices ? 0 : _offsetOpt(offset, o, roughnessGain)),
        ],
      });
    }
  }
  if (overlay) {
    ops.push({
      op: 'bcurveTo',
      data: [
        midDispX + x1 + (x2 - x1) * divergePoint + randomHalf(),
        midDispY + y1 + (y2 - y1) * divergePoint + randomHalf(),
        midDispX + x1 + 2 * (x2 - x1) * divergePoint + randomHalf(),
        midDispY + y1 + 2 * (y2 - y1) * divergePoint + randomHalf(),
        x2 + (preserveVertices ? 0 : randomHalf()),
        y2 + (preserveVertices ? 0 : randomHalf()),
      ],
    });
  } else {
    ops.push({
      op: 'bcurveTo',
      data: [
        midDispX + x1 + (x2 - x1) * divergePoint + randomFull(),
        midDispY + y1 + (y2 - y1) * divergePoint + randomFull(),
        midDispX + x1 + 2 * (x2 - x1) * divergePoint + randomFull(),
        midDispY + y1 + 2 * (y2 - y1) * divergePoint + randomFull(),
        x2 + (preserveVertices ? 0 : randomFull()),
        y2 + (preserveVertices ? 0 : randomFull()),
      ],
    });
  }
  return ops;
}
"""
"""
function _line(x1: number, y1: number, x2: number, y2: number, o: {}, move: boolean, overlay: boolean): Op[] {{
  const lengthSq = Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2);
  const length = Math.sqrt(lengthSq);
  let roughnessGain = 1;
  if (length < 200) {
    roughnessGain = 1;
  } else if (length > 500) {
    roughnessGain = 0.4;
  } else {
    roughnessGain = (-0.0016668) * length + 1.233334;
  }

  let offset = o.maxRandomnessOffset || 0;
  if ((offset * offset * 100) > lengthSq) {
    offset = length / 10;
  }
  const halfOffset = offset / 2;
  const divergePoint = 0.2 + random(o) * 0.2;
  let midDispX = o.bowing * o.maxRandomnessOffset * (y2 - y1) / 200;
  let midDispY = o.bowing * o.maxRandomnessOffset * (x1 - x2) / 200;
  midDispX = _offsetOpt(midDispX, o, roughnessGain);
  midDispY = _offsetOpt(midDispY, o, roughnessGain);
  const ops: Op[] = [];
  const randomHalf = () => _offsetOpt(halfOffset, o, roughnessGain);
  const randomFull = () => _offsetOpt(offset, o, roughnessGain);
  const preserveVertices = o.preserveVertices;
  if (move) {
    if (overlay) {
      ops.push({
        op: 'move', data: [
          x1 + (preserveVertices ? 0 : randomHalf()),
          y1 + (preserveVertices ? 0 : randomHalf()),
        ],
      });
    } else {
      ops.push({
        op: 'move', data: [
          x1 + (preserveVertices ? 0 : _offsetOpt(offset, o, roughnessGain)),
          y1 + (preserveVertices ? 0 : _offsetOpt(offset, o, roughnessGain)),
        ],
      });
    }
  }
  if (overlay) {
    ops.push({
      op: 'bcurveTo',
      data: [
        midDispX + x1 + (x2 - x1) * divergePoint + randomHalf(),
        midDispY + y1 + (y2 - y1) * divergePoint + randomHalf(),
        midDispX + x1 + 2 * (x2 - x1) * divergePoint + randomHalf(),
        midDispY + y1 + 2 * (y2 - y1) * divergePoint + randomHalf(),
        x2 + (preserveVertices ? 0 : randomHalf()),
        y2 + (preserveVertices ? 0 : randomHalf()),
      ],
    });
  } else {
    ops.push({
      op: 'bcurveTo',
      data: [
        midDispX + x1 + (x2 - x1) * divergePoint + randomFull(),
        midDispY + y1 + (y2 - y1) * divergePoint + randomFull(),
        midDispX + x1 + 2 * (x2 - x1) * divergePoint + randomFull(),
        midDispY + y1 + 2 * (y2 - y1) * divergePoint + randomFull(),
        x2 + (preserveVertices ? 0 : randomFull()),
        y2 + (preserveVertices ? 0 : randomFull()),
      ],
    });
  }
  return ops;
}
"""
# ------------------------------------------------------------------------------------------------------------------------
# 9787
# function _line(x1: number, y1: number, x2: number, y2: number, o: ResolvedOptions, move: boolean, overlay: boolean): Op[] {
