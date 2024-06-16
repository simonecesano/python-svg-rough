from typing import Any

class RoughCanvas:
    def __init__(self, canvas: Any, config: dict = None):
        self.canvas = canvas
        self.ctx = canvas.getContext('2d')  # type: CanvasRenderingContext2D
        if config is not None:
            self.gen = RoughGenerator(config)
        else:
            self.gen = RoughGenerator()

    def draw(self, drawable: Any) -> None:
        sets = drawable.get('sets', [])
        o = drawable.get('options', self.default_options())
        ctx = self.ctx
        precision = o.get('fixed_decimal_place_digits')
        for drawing in sets:
            if drawing.get('type') == 'path':
                ctx.save()
                ctx.strokeStyle = o.get('stroke', 'black') or 'transparent'
                ctx.lineWidth = o.get('stroke_width', 1)
                if 'stroke_line_dash' in o:
                    ctx.setLineDash(o['stroke_line_dash'])
                if 'stroke_line_dash_offset' in o:
                    ctx.lineDashOffset = o['stroke_line_dash_offset']
                self._draw_to_context(ctx, drawing, precision)
                ctx.restore()
            elif drawing.get('type') == 'fill_path':
                ctx.save()
                ctx.fillStyle = o.get('fill', '')
                fill_rule: str = 'evenodd' if (drawing.get('shape') in ['curve', 'polygon', 'path']) else 'nonzero'
                self._draw_to_context(ctx, drawing, precision, fill_rule)
                ctx.restore()
            elif drawing.get('type') == 'fill_sketch':
                self.fill_sketch(ctx, drawing, o)

    def _draw_to_context(self, ctx: Any, drawing: Any, fixed_decimals: int = 0, rule: str = 'nonzero') -> None:
        ctx.beginPath()
        for item in drawing.get('ops'):
            if isinstance(fixed_decimals, int) and fixed_decimals >= 0:
                data = [float(d).toFixed(fixed_decimals) for d in item['data']]
            else:
                data = item['data']
            if item['op'] == 'move':
                ctx.moveTo(data[0], data[1])
            elif item['op'] == 'bcurve_to':
                ctx.bezierCurveTo(*data)
            elif item['op'] == 'line_to':
                ctx.lineTo(*data)
        if drawing.get('type') == 'fill_path':
            ctx.fill(rule)
        else:
            ctx.stroke()

    def fill_sketch(self, ctx: Any, drawing: Any, o: dict) -> None:
        fweight = o.get('fill_weight', 0.5)
        if fweight < 0:
            fweight = o.get('stroke_width', 1) / 2
        ctx.save()
        if 'fill_line_dash' in o:
            ctx.setLineDash(o['fill_line_dash'])
        if 'fill_line_dash_offset' in o:
            ctx.lineDashOffset = o['fill_line_dash_offset']
        ctx.strokeStyle = o.get('fill', '')
        ctx.lineWidth = fweight
        self._draw_to_context(ctx, drawing, o.get('fixed_decimal_place_digits'), rule='nonzero')
        ctx.restore()

    def get_generator(self) -> Any:
        return self.gen

    def default_options(self) -> dict:
        return self.gen.default_options

    def line(self, x1: int, y1: int, x2: int, y2: int, options: dict = None) -> Any:
        d = self.gen.line(x1, y1, x2, y2, options)
        self.draw(d)
        return d

    def linear_path(self, points: list, options: dict = None) -> Any:
        d = self.gen.linear_path(points, options)
        self.draw(d)
        return d

    def polygon(self, points: list, options: dict = None) -> Any:
        d = self.gen.polygon(points, options)
        self.draw(d)
        return d

    def arc(self, x: int, y: int, width: int, height: int, start: float, stop: float, closed: bool = False, options: dict = None) -> Any:
        d = self.gen.arc(x, y, width, height, start, stop, closed, options)
        self.draw(d)
        return d

    def curve(self, points: list, options: dict = None) -> Any:
        d = self.gen.curve(points, options)
        self.draw(d)
        return d

    def path(self, d: str, options: dict = None) -> Any:
        drawing = self.gen.path(d, options)
        self.draw(drawing)
        return drawing
# ```

# In the above Python code:

# 1. The `RoughCanvas` class is defined with an initializer method that takes a canvas and optional configuration.
# 2. A `draw` method to draw shapes on the canvas based on provided options.
# 3. An `_draw_to_context` method is used internally by `draw` method for drawing paths.
# 4. The `fill_sketch` method is used for filling sketches with color.
# 5. The `get_generator`, `default_options` and other methods are implemented as per their TypeScript counterparts.

# Note that the Python code does not directly translate from TypeScript because of differences in language syntax, data types, and libraries. However, it provides an equivalent structure and functionality.
