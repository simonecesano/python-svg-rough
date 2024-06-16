kHere's the equivalent Python code for your TypeScript class:

```Python
import tkinter as tk
from typing import List, Tuple, Optional

class RoughCanvas:
    def __init__(self, canvas: tk.Canvas, config: Optional[dict] = None):
        self.canvas = canvas
        self.ctx = self.canvas.create_undo_context()
        self.config = config if config is not None else {}
        self.gen = RoughGenerator(self.config)

    def draw(self, drawable: dict) -> None:
        for drawing in drawable.get('sets', []):
            self._draw_to_context(drawing)

    def _draw_to_context(self, drawing: dict) -> None:
        ctx = self.canvas.create_undo_context()
        if 'fill' in drawing:
            ctx.set_fill_color(drawing['fill'])
        else:
            ctx.set_stroke_color(self.config.get('stroke', '#000'))
        if 'stroke_width' in drawing:
            ctx.set_line_width(drawing['stroke_width'])
        if 'line_dash' in drawing:
            ctx.set_line_dash(drawing['line_dash'])
        if 'line_dash_offset' in drawing:
            ctx.set_line_dash_offset(drawing['line_dash_offset'])

        for item in drawing.get('ops', []):
            self._draw_operation(ctx, item)

        ctx.stroke()
        ctx.restore()

    def _draw_operation(self, ctx: tk.Canvas, item: dict) -> None:
        if 'move' == item['op']:
            ctx.move_to(item['data'][0], item['data'][1])
        elif 'bcurve_to' == item['op']:
            ctx.bezier_curve_to(*item['data'])
        elif 'line_to' == item['op']:
            ctx.line_to(*item['data'])

    def fill_sketch(self, ctx: tk.Canvas, drawing: dict) -> None:
        fweight = self.config.get('fill_weight', 1)
        if fweight < 0:
            fweight = self.config.get('stroke_width') / 2
        ctx.set_fill_color(drawing['fill'])
        ctx.set_line_width(fweight)

        for item in drawing.get('ops', []):
            self._draw_operation(ctx, item)

        ctx.fill()

    def line(self, x1: float, y1: float, x2: float, y2: float, options: Optional[dict] = None) -> dict:
        return self.gen.line(x1, y1, x2, y2, options)

    def rectangle(self, x: float, y: float, width: float, height: float, options: Optional[dict] = None) -> dict:
        return self.gen.rectangle(x, y, width, height, options)

    def ellipse(self, x: float, y: float, width: float, height: float, options: Optional[dict] = None) -> dict:
        return self.gen.ellipse(x, y, width, height, options)

    def circle(self, x: float, y: float, diameter: float, options: Optional[dict] = None) -> dict:
        return self.gen.circle(x, y, diameter, options)

    def linear_path(self, points: List[Tuple[float, float]], options: Optional[dict] = None) -> dict:
        return self.gen.linear_path(points, options)

    def polygon(self, points: List[Tuple[float, float]], options: Optional[dict] = None) -> dict:
        return self.gen.polygon(points, options)

    def arc(self, x: float, y: float, width: float, height: float, start: float, stop: float, closed: bool = False, options: Optional[dict] = None) -> dict:
        return self.gen.arc(x, y, width, height, start, stop, closed, options)

    def curve(self, points: List[Tuple[float, float]], options: Optional[dict] = None) -> dict:
        return self.gen.curve(points, options)

    def path(self, d: str, options: Optional[dict] = None) -> dict:
        return self.gen.path(d, options)
```

Note that the code is written in Python 3. The main differences from TypeScript are:

1. Instead of using interfaces, we use Python's built-in type hints for functions and variables.

2. We use `tkinter` instead of `Canvas` to create a canvas object.

3. We have used `create_undo_context()` method to set the context for drawing.

4. The methods like `_draw_to_context`, `_draw_operation`, `fill_sketch`, etc., are used to draw on the canvas based on the input drawings.

5. We use `set_fill_color` and `set_line_width` methods to set the color and width of the brush.

6. The drawing operations are then executed using these methods, and finally, we call the `stroke` method to draw on the canvas.
