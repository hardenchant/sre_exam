import sys
from itertools import product
from math import sqrt


class ConvexPoly:
    def __init__(self, n, v_x, v_y):
        self.n = n
        self.points = []

        self.k = v_y / v_x
        self.v = sqrt(v_x ** 2 + v_y ** 2)

    def _add_point(self, x, y):
        self.points.append([x, y])

    @staticmethod
    def read_poly_from_stdin():
        n, v_x, v_y = [int(i) for i in sys.stdin.readline().strip().split(' ')]
        poly = ConvexPoly(n, v_x, v_y)
        for _ in range(n):
            point_x, point_y = [int(i) for i in sys.stdin.readline().strip().split(' ')]
            poly._add_point(point_x, point_y)
        return poly

    def _is_parallel_trajectory_with(self, other_poly) -> bool:
        """
        Check trajectory parallels
        :param other_poly:
        :return:
        """
        if self.k == other_poly.k:
            return True
        return False

    def _get_b_for_point(self, point):
        """

        :param point: (x, y)
        :return: b from y = kx + b
        """
        point_x, point_y = point
        return point_y - self.k * point_x

    def _get_cross_point(self, line_params1, line_params2):
        """

        :param line_params1: (k, b)
        :param line_params2: (k, b)
        :return: (x, y)
        """
        x = (line_params2[1] - line_params1[1]) / (line_params1[0] - line_params2[0])
        y = line_params1[0] * x + line_params1[1]
        return x, y

    def _get_distance(self, point1, point2):
        return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def _is_poly_point_faster_than(self, point, other_poly, other_poly_point):
        """

        :param point:
        :param other_poly:
        :param other_poly_point:
        :return: None - same speed, True - first one faster the other, False - other
        """
        cross_point = self._get_cross_point(
            (self.k, self._get_b_for_point(point)),
            (other_poly.k, other_poly._get_b_for_point(other_poly_point))
        )
        d1 = self._get_distance(point, cross_point)
        d2 = other_poly._get_distance(other_poly_point, cross_point)

        time_diff = d1 / self.v - d2 / other_poly.v
        if time_diff == 0:
            return None
        elif time_diff < 0:
            return True
        return False

    def _is_crossed_non_parallel(self, other_poly):
        is_first_faster = None
        for point_from_poly1, point_from_poly2 in product(self.points, other_poly.points):
            is_first_faster_now = self._is_poly_point_faster_than(point_from_poly1, other_poly, point_from_poly2)
            if is_first_faster_now is None:
                return True
            if is_first_faster is None:
                is_first_faster = is_first_faster_now
            elif is_first_faster != is_first_faster_now:
                return True
        return False

    def _is_crossed_parallel(self, other_poly):
        is_first_higher = None
        for point_from_poly1, point_from_poly2 in product(self.points, other_poly.points):
            b1 = self._get_b_for_point(point_from_poly1)
            b2 = other_poly._get_b_for_point(point_from_poly2)
            if b1 > b2:
                return True
            if is_first_higher is None:
                is_first_higher = b1 > b2
            elif (b1 > b2) != is_first_higher:
                return True
        return False

    def is_crossed(self, other_poly):
        if self._is_parallel_trajectory_with(other_poly):
            return self._is_crossed_parallel(other_poly)
        return self._is_crossed_non_parallel(other_poly)


def main():
    pasha_poly = ConvexPoly.read_poly_from_stdin()
    sasha_poly = ConvexPoly.read_poly_from_stdin()

    if pasha_poly.is_crossed(sasha_poly):
        sys.stdout.write('Yes')
    else:
        sys.stdout.write('No')


main()
