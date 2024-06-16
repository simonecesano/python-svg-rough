# Here's the translation of your TypeScript code to Python:

# ```Python
import math

class RoughCanvas:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ctx = self.canvas.getContext('2d')

    def draw(self, drawable):
        if 'sets' in drawable and isinstance(drawable['sets'], list):
            for drawing in drawable['sets']:
                if 'type' in drawing:
                    if drawing['type'] == 'path':
                        self._draw_path(self.ctx, drawing)
                    elif drawing['type'] == 'fillPath':
                        self._draw_fill_path(self.ctx, drawing)
                    elif drawing['type'] == 'fillSketch':
                        self.fill_sketch(self.ctx, drawing)
        else:
            if drawable['type'] == 'path':
                self._draw_path(self.ctx, drawable)
            elif drawable['type'] == 'fillPath':
                self._draw_fill_path(self.ctx, drawable)

    def _draw_path(self, ctx, drawing):
        ctx.beginPath()
        for item in drawing['ops']:
            if 'data' in item:
                data = [float(d) for d in item['data']]
                if item['op'] == 'move':
                    ctx.moveTo(data[0], data[1])
                elif item['op'] == 'bcurveTo':
                    ctx.bezierCurveTo(*data)
                elif item['op'] == 'lineTo':
                    ctx.lineTo(*data)
        if 'type' in drawing and drawing['type'] == 'fillPath':
            ctx.fill()
        else:
            ctx.stroke()

    def _draw_fill_path(self, ctx, drawing):
        self._draw_path(ctx, drawing)

    def fill_sketch(self, ctx, drawing):
        fweight = drawing['options']['fillWeight']
        if fweight < 0:
            fweight = drawing['options']['strokeWidth'] / 2
        ctx.save()
        if 'fillLineDash' in drawing['options']:
            ctx.setLineDash(drawing['options']['fillLineDash'])
        if 'fillLineDashOffset' in drawing['options']:
            ctx.lineDashOffset = drawing['options']['fillLineDashOffset']
        ctx.strokeStyle = drawing['options']['fill'] or ''
        ctx.lineWidth = fweight
        self._draw_path(ctx, drawing)
        ctx.restore()

    def get_generator(self):
        return self.gen

    def get_default_options(self):
        return self.gen.defaultOptions

    def line(self, x1, y1, x2, y2, options=None):
        d = self.gen.line(x1, y1, x2, y2, options)
        self.draw(d)
        return d

    def rectangle(self, x, y, width, height, options=None):
        d = self.gen.rectangle(x, y, width, height, options)
        self.draw(d)
        return d

    def ellipse(self, x, y, width, height, options=None):
        d = self.gen.ellipse(x, y, width, height, options)
        self.draw(d)
        return d

    def circle(self, x, y, diameter, options=None):
        d = self.gen.circle(x, y, diameter, options)
        self.draw(d)
        return d

    def linear_path(self, points, options=None):
        d = self.gen.linearPath(points, options)
        self.draw(d)
        return d

    def polygon(self, points, options=None):
        d = self.gen.polygon(points, options)
        self.draw(d)
        return d

    def arc(self, x, y, width, height, start, stop, closed=False, options=None):
        d = self.gen.arc(x, y, width, height, start, stop, closed, options)
        self.draw(d)
        return d

    def curve(self, points, options=None):
        d = self.gen.curve(points, options)
        self.draw(d)
        return d

    def path(self, d, options=None):
        drawing = self.gen.path(d, options)
        self.draw(drawing)
        return drawing
# ```

# In this code, I've used the built-in Python functions for drawing such as `moveTo`, `lineTo`, and `bezierCurveTo`. I've also used the `fill` and `stroke` methods of the canvas context to draw shapes.
