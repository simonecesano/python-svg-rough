Here is the equivalent code in Python:

```python
import canvas

class RoughCanvas:
    def __init__(self, canvas: canvas.Canvas):
        self.canvas = canvas
        self.ctx = self.canvas.get_context('2d')

    def draw(self, drawable):
        if not hasattr(drawable, 'sets'):
            return
        
        for drawing in drawable.sets:
            if drawing.type == 'path':
                self.ctx.save()
                stroke_color = drawable.options.stroke or ''
                stroke_width = drawable.options.stroke_width
                line_dash = drawable.options.stroke_line_dash
                line_dash_offset = drawable.options.stroke_line_dash_offset

                if line_dash:
                    self.ctx.set_line_dash(line_dash)
                
                if line_dash_offset:
                    self.ctx.line_dash_offset = line_dash_offset
                
                self.ctx.stroke_style = stroke_color
                self.ctx.line_width = stroke_width
                self._draw_to_context(self.ctx, drawing)
                self.ctx.restore()
            elif drawing.type == 'fill_path':
                self.ctx.save()
                fill_color = drawable.options.fill or ''
                fill_rule = 'evenodd'
                if drawable.shape in ['curve', 'polygon', 'path']:
                    fill_rule = 'evenodd'
                
                self._draw_to_context(self.ctx, drawing)
                self.ctx.restore()
            elif drawing.type == 'fill_sketch':
                self.fill_sketch(self.ctx, drawing, drawable.options)

    def fill_sketch(self, ctx: canvas.CanvasRenderingContext2D, drawing: dict, options: dict):
        fweight = options.get('fill_weight', 0)
        if fweight < 0:
            fweight = options['stroke_width'] / 2
        
        ctx.save()
        
        if 'fill_line_dash' in options:
            ctx.set_line_dash(options['fill_line_dash'])
        
        if 'fill_line_dash_offset' in options:
            ctx.line_dash_offset = options['fill_line_dash_offset']
        
        ctx.stroke_style = options.get('fill', '')
        ctx.line_width = fweight
        self._draw_to_context(ctx, drawing)
        ctx.restore()

    def _draw_to_context(self, ctx: canvas.CanvasRenderingContext2D, drawing: dict):
        ctx.begin_path()
        for item in drawing['ops']:
            if isinstance(item['data'], list) and len(item['data']) == 6:
                ctx.bezier_curve_to(*item['data'])
            elif len(item['data']) == 2:
                ctx.move_to(*item['data'])
            elif len(item['data']) == 4:
                ctx.line_to(*item['data'])
        
        if drawing['type'] == 'fill_path':
            ctx.fill()
        else:
            ctx.stroke()

    def get_generator(self):
        return self.gen

    def get_default_options(self):
        return self.gen.default_options

    def line(self, x1: float, y1: float, x2: float, y2: float, options: dict=None) -> dict:
        drawable = self.gen.line(x1, y1, x2, y2, options)
        self.draw(drawable)
        return drawable

    def rectangle(self, x: float, y: float, width: float, height: float, options: dict=None) -> dict:
        drawable = self.gen.rectangle(x, y, width, height, options)
        self.draw(drawable)
        return drawable

    def ellipse(self, x: float, y: float, width: float, height: float, options: dict=None) -> dict:
        drawable = self.gen.ellipse(x, y, width, height, options)
        self.draw(drawable)
        return drawable

    def circle(self, x: float, y: float, diameter: float, options: dict=None) -> dict:
        drawable = self.gen.circle(x, y, diameter, options)
        self.draw(drawable)
        return drawable

    def linear_path(self, points: list[tuple[float, float]], options: dict=None) -> dict:
        drawable = self.gen.linear_path(points, options)
        self.draw(drawable)
        return drawable

    def polygon(self, points: list[tuple[float, float]], options: dict=None) -> dict:
        drawable = self.gen.polygon(points, options)
        self.draw(drawable)
        return drawable

    def arc(self, x: float, y: float, width: float, height: float, start: float, stop: float, closed: bool=False, options: dict=None) -> dict:
        drawable = self.gen.arc(x, y, width, height, start, stop, closed, options)
        self.draw(drawable)
        return drawable

    def curve(self, points: list[tuple[float, float]], options: dict=None) -> dict:
        drawable = self.gen.curve(points, options)
        self.draw(drawable)
        return drawable

    def path(self, d: str, options: dict=None) -> dict:
        drawable = self.gen.path(d, options)
        self.draw(drawable)
        return drawable
```

This code uses the `canvas` library to create a canvas and draw shapes on it. It defines several methods for drawing different types of shapes, such as lines, rectangles, ellipses, circles, polygons, arcs, curves, and paths. The methods take options dictionaries that can specify various properties of the shapes, such as their colors, widths, and fill patterns.