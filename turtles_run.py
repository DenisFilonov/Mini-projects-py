import turtle as t
import time
import random as r

# This is our constants
COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "black", "gray", "purple", "brown"]

# To define sizes of windows below
WIDTH, HEIGHT = 500, 500


def get_number_of_racers() -> int:
    while True:
        try:
            racers = int(input("Enter number of racers between including (2-10): "))
        except ValueError:
            print("Error! Please enter an integer between 2 and 10 next time\n")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter value between 2 and 10 next time\n")


def create_turtles(colors: list) -> list:
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = t.Turtle(shape='turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacing_x, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtles() -> None:
    # This is our window definition
    screen = t.Screen()

    # We're using our constants above
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("Turtle racing")


def race_begin(colors: list) -> str:
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            racer.forward(r.randrange(1, 20))

            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]


def main() -> None:
    print("Welcome to Turtle racing!")
    racers = get_number_of_racers()
    init_turtles()

    colors = COLORS[:racers]
    r.shuffle(colors)

    print(f"Racer won: {race_begin(colors).capitalize()}")
    time.sleep(2)


main()
