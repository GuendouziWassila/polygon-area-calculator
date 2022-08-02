class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            shape = ''
            for i in range(self.height):
                for _ in range(self.width):
                    shape = shape + '*'

                shape = shape + '\n'
        return shape

    def get_amount_inside(self, rectangle):
        return int(self.width / rectangle.width) * int(
            self.height / rectangle.height)

    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(
            self.height) + ')'


#-------------------------------------------


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, s):
        self.width = s
        self.height = s

    def set_height(self, s):
        self.width = s
        self.height = s

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'
