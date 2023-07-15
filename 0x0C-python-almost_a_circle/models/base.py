#!/usr/bin/python3
"""Base module"""
import json
import csv


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to convert list of dictionaries to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method to save instances to a file in JSON format"""
        filename = cls.__name__ + ".json"
        objects = []
        if list_objs is not None:
            objects = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(objects)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Static method to convert JSON string to list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method to create an instance with pre-set attributes"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)  # Create a "dummy" instance with default attributes
        elif cls.__name__ == "Square":
            obj = cls(1)  # Create a "dummy" instance with default attributes
        else:
            return None
        obj.update(**dictionary)  # Update the instance with the given attributes
        return obj

    @classmethod
    def load_from_file(cls):
        """Class method to load instances from a file in JSON format"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method to save instances to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Class method to load instances from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    instance = cls.from_csv_row(row)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    def to_csv_row(self):
        """Converts object attributes to a CSV row"""
        raise NotImplementedError("to_csv_row method must be implemented in child classes")

    @classmethod
    def from_csv_row(cls, row):
        """Creates an instance from a CSV row"""
        raise NotImplementedError("from_csv_row method must be implemented in child classes")

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Static method to draw the rectangles and squares"""
        import turtle

        def draw_shape(shape, color):
            turtle.fillcolor(color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(shape.size)
                turtle.right(90)
            turtle.end_fill()

        turtle.speed(2)
        turtle.bgcolor("lightgray")

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            draw_shape(rectangle, "blue")

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            draw_shape(square, "red")

        turtle.exitonclick()
