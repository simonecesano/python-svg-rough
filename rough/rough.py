# Here's the equivalent Python code for the provided TypeScript code:

# ```Python
import pygame

class RoughCanvas:
    def __init__(self, canvas: pygame.Surface, config=None):
        self.canvas = canvas
        self.ctx = canvas.get_surface()
        if config is None:
            self.config = {}
        else:
            self.config = config

    def draw(self, drawable):
        sets = drawable.sets or []
        o = drawable.options or self.default_options()
        ctx = self.ctx
        precision = drawable.options.fixed_decimal_place_digits
        for drawing in sets:
            if drawing.type == 'path':
                ctx.save()
                ctx.strokestyle = o['stroke'] if o['stroke'] != 'none' else 'transparent'
                ctx.linewidth = o['stroke_width']
                if 'stroke_line_dash' in o:
                    ctx.set_line_dash(o['stroke_line_dash'])
                if 'stroke_line_dash_offset' in o:
                    ctx.line_dash_offset = o['stroke_line_dash_offset']
                self._draw_to_context(ctx, drawing, precision)
                ctx.restore()
            elif drawing.type == 'fill_path':
                ctx.save()
                ctx.fillstyle = o['fill'] or ''
                fill_rule = 'evenodd' if drawable.shape in ['curve', 'polygon', 'path'] else 'nonzero'
                self._draw_to_context(ctx, drawing, precision, fill_rule)
                ctx.restore()
            elif drawing.type == 'fill_sketch':
                self.fill_sketch(ctx, drawing, o)

    def _draw_to_context(self, ctx, drawing, fixed_decimals=0, rule='nonzero'):
        ctx.begin_path()
        for item in drawing.ops:
            if isinstance(fixed_decimals, int) and fixed_decimals >= 0:
                data = [round(x, fixed_decimals) for x in item.data]
            else:
                data = item.data
            op_type = item.op
            if op_type == 'move':
                ctx.move_to(data[0], data[1])
            elif op_type == 'bcurve_to':
                ctx.bezier_curve_to(*data)
            elif op_type == 'line_to':
                ctx.line_to(*data)
        if drawing.type == 'fill_path':
            ctx.fill(rule)
        else:
            ctx.stroke()

    def fill_sketch(self, ctx, drawing, o):
        fweight = o['fill_weight']
        if fweight < 0:
            fweight = o['stroke_width'] / 2
        ctx.save()
        if 'fill_line_dash' in o:
            ctx.set_line_dash(o['fill_line_dash'])
        if 'fill_line_dash_offset' in o:
            ctx.line_dash_offset = o['fill_line_dash_offset']
        ctx.strokestyle = o['fill'] or ''
        ctx.linewidth = fweight
        self._draw_to_context(ctx, drawing, o.get('fixed_decimal_place_digits'))
        ctx.restore()

    @property
    def generator(self):
        return self.config['generator']

    def default_options(self):
        return self.config.get('default_options')

    def line(self, x1: int, y1: int, x2: int, y2: int, options=None):
        d = self.generator.line(x1, y1, x2, y2, options or {})
        self.draw(d)
        return d

    def rectangle(self, x: int, y: int, width: int, height: int, options=None):
        d = self.generator.rectangle(x, y, width, height, options or {})
        self.draw(d)
        return d

    def ellipse(self, x: int, y: int, width: int, height: int, options=None):
        d = self.generator.ellipse(x, y, width, height, options or {})
        self.draw(d)
        return d

    def circle(self, x: int, y: int, radius: int, options=None):
        d = self.generator.circle(x, y, radius, options or {})
        self.draw(d)
        return d

    def linear_path(self, points: list[tuple[int, int]], options=None):
        d = self.generator.linear_path(points, options or {})
        self.draw(d)
        return d

    def polygon(self, points: list[tuple[int, int]], options=None):
        d = self.generator.polygon(points, options or {})
        self.draw(d)
        return d

    def arc(self, x: int, y: int, width: int, height: int, start: float, stop: float, closed=False, options=None):
        d = self.generator.arc(x, y, width, height, start, stop, closed, options or {})
        self.draw(d)
        return d

    def curve(self, points: list[tuple[int, int]], options=None):
        d = self.generator.curve(points, options or {})
        self.draw(d)
        return d

    def path(self, d: str, options=None):
        drawing = self.generator.path(d, options or {})
        self.draw(drawing)
        return drawing
# ```

# This code assumes you are using the `pygame` library for graphics. The equivalent TypeScript code is a class-based implementation with methods that mirror the provided TypeScript code.
