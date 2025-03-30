import turtle
import math

# екран
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("тяжкі квадрати")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Функція для малювання квадрата від центру з заданим кутом
def draw_square(center_x, center_y, side, angle):
    """
    side – це довжина сторони квадрата,
    angle – кут повороту квадрата відносно осі Х (горизонталі).
    """
    t.penup()
    # відстань від центру квадрата до вершини (половина діагоналі)
    diagonal_half = side * math.sqrt(2) / 2
    # переходимо до верхньої лівої вершини квадрата з урахуванням кута
    t.goto(center_x, center_y)
    t.setheading(angle)
    t.forward(diagonal_half)
    t.right(135)
    t.pendown()
    

    for _ in range(4):
        t.forward(side)
        t.right(90)


def draw_nested_rotating_squares(center_x, center_y, outer_size, alpha, direction, iterations):
    """
    center_x, center_y – центр великого квадрата,
    outer_size – розмір (сторона) описаного квадрата,
    alpha – кут повороту (в градусах),
    direction – напрямок (1 або -1),
    iterations – кількість вписаних квадратів.
    """
    # спочатку малюємо «описаний» квадрат (горизонтально орієнтований)
    t.penup()
    t.goto(center_x - outer_size / 2, center_y + outer_size / 2)
    t.setheading(0)
    t.pendown()
    for _ in range(4):
        t.forward(outer_size)
        t.right(90)

    # сторона першого вписаного квадрата:
    # обираємо її так, щоб квадрат гарантовано вміщався при обертанні
    # (найкритичніший випадок – це поворот на 45, тоді діагональ = outer size)
    side = outer_size / math.sqrt(2)

    # малюємо вкладені квадрати з поступовим зменшенням
    for i in range(iterations):
        angle = direction * alpha * i
        draw_square(center_x, center_y, side, angle)
        side *= 0.8  # коефіцієнт зменшення

# сіітка 2х2
def draw_2x2_grid(square_size, alpha, iterations):
    """
    square_size – це половина сторони одного «блоку»,
    фактичний розмір квадрата, який ми малюємо в кожному блоці, буде square_size*2.
    """
    start_x = -square_size
    start_y = square_size

    for row in range(2):
        for col in range(2):
            cx = start_x + col * square_size * 2
            cy = start_y - row * square_size * 2
            # задаємо напрямок обертання: +1 або -1
            direction = 1 if (row + col) % 2 == 0 else -1
            # малюємо вкладені квадрати
            draw_nested_rotating_squares(cx, cy, square_size * 2, alpha, direction, iterations)

# параметри
alpha = float(input("Введіть кут повороту (в градусах): "))
iterations = int(input("Введіть кількість вкладених квадратів: "))
square_size = 150  # половина розміру одного блоку


draw_2x2_grid(square_size, alpha, iterations)

turtle.done()
