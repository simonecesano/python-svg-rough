# from core import Config, Options, Drawable, OpSet, ResolvedOptions, PathInfo
# from geometry import Point
# from renderer import line, solidFillPolygon, patternFillPolygons, rectangle, ellipseWithParams, generateEllipseParams, linearPath, arc, patternFillArc, curve, svgPath
# from math import randomSeed
# from points_on_curve.lib.curve_to_bezier import curveToBezier
# from points_on_curve import pointsOnBezierCurves, pointsOnPath

NOS = 'none'

class RoughGenerator:
    def __init__(self, config=None):
        self.config = config or {}
        self.defaultOptions = {
            'maxRandomnessOffset': 2,
            'roughness': 1,
            'bowing': 1,
            'stroke': '#000',
            'strokeWidth': 1,
            'curveTightness': 0,
            'curveFitting': 0.95,
            'curveStepCount': 9,
            'fillStyle': 'hachure',
            'fillWeight': -1,
            'hachureAngle': -41,
            'hachureGap': -1,
            'dashOffset': -1,
            'dashGap': -1,
            'zigzagOffset': -1,
            'seed': 0,
            'disableMultiStroke': False,
            'disableMultiStrokeFill': False,
            'preserveVertices': False,
            'fillShapeRoughnessGain': 0.8
        }
        if self.config.get('options'):
            self.defaultOptions.update(self._o(self.config['options']))

    @staticmethod
    def newSeed():
        return randomSeed()

    def _o(self, options=None):
        return {**self.defaultOptions, **(options or {})}

    def _d(self, shape, sets=None, options=None):
        return {'shape': shape, 'sets': sets or [], 'options': options or self.defaultOptions}

    def line(self, x1, y1, x2, y2, options=None):
        o = self._o(options)
        return self._d('line', [line(x1, y1, x2, y2, o)], o)

    def rectangle(self, x, y, width, height, options=None):
        o = self._o(options)
        paths = []
        outline = rectangle(x, y, width, height, o)
        if o['fill']:
            points = [[x, y], [x + width, y], [x + width, y + height], [x, y + height]]
            if o['fillStyle'] == 'solid':
                paths.append(solidFillPolygon([points], o))
            else:
                paths.append(patternFillPolygons([points], o))
        if o['stroke'] != NOS:
            paths.append(outline)
        return self._d('rectangle', paths, o)

    def ellipse(self, x, y, width, height, options=None):
        o = self._o(options)
        paths = []
        ellipseParams = generateEllipseParams(width, height, o)
        ellipseResponse = ellipseWithParams(x, y, o, ellipseParams)
        if o['fill']:
            if o['fillStyle'] == 'solid':
                shape = ellipseWithParams(x, y, o, ellipseParams)['opset']
                shape['type'] = 'fillPath'
                paths.append(shape)
            else:
                paths.append(patternFillPolygons([ellipseResponse['estimatedPoints']], o))
        if o['stroke'] != NOS:
            paths.append(ellipseResponse['opset'])
        return self._d('ellipse', paths, o)

    def circle(self, x, y, diameter, options=None):
        ret = self.ellipse(x, y, diameter, diameter, options)
        ret['shape'] = 'circle'
        return ret

    def linearPath(self, points, options=None):
        o = self._o(options)
        return self._d('linearPath', [linearPath(points, False, o)], o)

    def arc(self, x, y, width, height, start, stop, closed=False, options=None):
        o = self._o(options)
        paths = []
        outline = arc(x, y, width, height, start, stop, closed, True, o)
        if closed and o['fill']:
            if o['fillStyle'] == 'solid':
                fillOptions = {**o, 'disableMultiStroke': True}
                shape = arc(x, y, width, height, start, stop, True, False, fillOptions)
                shape['type'] = 'fillPath'
                paths.append(shape)
            else:
                paths.append(patternFillArc(x, y, width, height, start, stop, o))
        if o['stroke'] != NOS:
            paths.append(outline)
        return self._d('arc', paths, o)

    def curve(self, points, options=None):
        o = self._o(options)
        paths = []
        outline = curve(points, o)
        if o['fill'] and o['fill'] != NOS:
            if o['fillStyle'] == 'solid':
                fillShape = curve(points, {**o, 'disableMultiStroke': True, 'roughness': o['roughness'] + o['fillShapeRoughnessGain'] if o['roughness'] else 0})
                paths.append({'type': 'fillPath', 'ops': self._mergedShape(fillShape['ops'])})
            else:
                polyPoints = []
                inputPoints = points
                if len(inputPoints):
                    p1 = inputPoints[0]
                    pointsList = [inputPoints] if isinstance(p1[0], (int, float)) else inputPoints
                    for points in pointsList:
                        if len(points) < 3:
                            polyPoints.extend(points)
                        elif len(points) == 3:
                            polyPoints.extend(pointsOnBezierCurves(curveToBezier([points[0], points[0], points[1], points[2]]), 10, (1 + o['roughness']) / 2))
                        else:
                            polyPoints.extend(pointsOnBezierCurves(curveToBezier(points), 10, (1 + o['roughness']) / 2))
                if polyPoints:
                    paths.append(patternFillPolygons([polyPoints], o))
        if o['stroke'] != NOS:
            paths.append(outline)
        return self._d('curve', paths, o)

    def polygon(self, points, options=None):
        o = self._o(options)
        paths = []
        outline = linearPath(points, True, o)
        if o['fill']:
            if o['fillStyle'] == 'solid':
                paths.append(solidFillPolygon([points], o))
            else:
                paths.append(patternFillPolygons([points], o))
        if o['stroke'] != NOS:
            paths.append(outline)
        return self._d('polygon', paths, o)

    def path(self, d, options=None):
        o = self._o(options)
        paths = []
        if not d:
            return self._d('path', paths, o)
        d = d.replace('\n', ' ').replace('- ', '-').replace('  ', ' ')
       
