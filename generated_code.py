import turtle
import matplotlib.pyplot as plt
import numpy as np

# ───── Setup ─────
t = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink']

def reset_turtle():
    t.reset()
    t.speed(1)
    t.width(2)
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

# ───── Drawing Functions ─────

def drawRainbowStripes():
    t.setheading(0)
    t.speed(3)
    t.width(6)
    y = 100
    for color in colors:
        t.penup()
        t.goto(-150, y)
        t.pendown()
        t.color(color)
        t.forward(300)
        y -= 10
    t.penup()
    t.goto(-150, 110)
    t.hideturtle()

def drawBox():
    t.setheading(0)
    t.speed(1)
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.penup()
    t.hideturtle()

def drawStarburst():
    t.setheading(0)
    t.speed(3)
    t.penup()
    t.goto(0, 0)
    t.color('orange')
    t.width(2)
    t.pendown()
    for _ in range(0, 360, 45):
        t.forward(100)
        t.backward(100)
        t.right(45)
    t.penup()
    t.hideturtle()

def drawFlower():
    t.setheading(0)
    t.speed(10)
    t.penup()
    t.goto(0, 0)
    t.width(3)
    t.pendown()
    for _ in range(0, 360, 60):
        for color in ['pink', 'red', 'yellow', 'orange']:
            t.color(color)
            t.forward(100)
            t.backward(100)
        t.right(60)
    t.penup()
    t.hideturtle()

def drawWave():
    t.setheading(0)
    t.speed(3)
    t.penup()
    t.goto(-150, 0)
    t.width(2)
    t.pendown()
    for _ in range(6):
        t.color('blue')
        t.forward(50)
        t.left(45)
        t.color('green')
        t.forward(50)
        t.right(45)
    t.penup()
    t.hideturtle()

def drawL():
    t.speed(1)
    t.penup()
    t.goto(100, 100)
    t.setheading(270)
    t.color('blue')
    t.width(5)
    t.pendown()
    t.forward(50)
    t.setheading(0)
    t.forward(100)
    t.penup()
    t.hideturtle()

def drawZigzag():
    t.speed(2)
    t.penup()
    t.goto(-100, 100)
    t.setheading(0)
    t.pendown()
    t.right(45)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.penup()
    t.hideturtle()

def drawSpiral():
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.color('purple')
    t.width(2)
    t.pendown()
    for i in range(60):
        t.forward(i * 2)
        t.left(15)
    t.penup()
    t.hideturtle()

def drawFlowerBurst():
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    for i in range(72):
        t.color(colors[i % len(colors)])
        t.circle(100)
        t.left(5)
    t.penup()
    t.hideturtle()

def drawRainbowSpiral():
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    t.width(2)
    for i in range(100):
        t.color(colors[i % len(colors)])
        t.forward(i)
        t.left(20)
    t.penup()
    t.hideturtle()

def draw_flowerburst_matplotlib():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_facecolor("white")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(False)

    num_petals = 72
    radius = 100
    theta = np.linspace(0, 2 * np.pi, num_petals, endpoint=False)

    for i, angle in enumerate(theta):
        color = plt.cm.hsv(i / num_petals)
        ax.plot([angle] * 100, np.linspace(0, radius, 100), color=color, linewidth=1)

    output_path = "drawing_output_flowerburst.png"
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0, dpi=150)
    plt.close()
    print(f"✅ Image saved to {output_path}")

# ───── Launcher ─────
if __name__ == "__main__":
    options = [
        "drawL",
        "drawZigzag",
        "drawSpiral",
        "drawBox",
        "drawStarburst",
        "drawFlower",
        "drawWave",
        "drawRainbowStripes",
        "drawFlowerBurst",
        "drawRainbowSpiral",
        "draw_flowerburst_matplotlib"
    ]

    print("🎨 Welcome to the Turtle Design Studio!")

    while True:
        print("Which turtle function would you like to run?")
        for idx, name in enumerate(options, 1):
            print(f"{idx}. {name}")
        print("0. Exit")
        print("99. Run all")

        choice = input("Enter number (0–11 or 99): ")

        try:
            selection = int(choice)
            if selection == 0:
                print("👋 Exiting turtle mode...")
                break
            elif selection == 99:
                for name in options:
                    reset_turtle()
                    print(f"🎬 Running: {name}...")
                    globals()[name]()
                    input(f"✅ {name} complete! Press Enter for next...")
                    t.clear()
            elif 1 <= selection <= len(options):
                print(f"🌀 Running: {options[selection - 1]}...")
                reset_turtle()
                globals()[options[selection - 1]]()
                input("✅ Drawing complete! Press Enter to return to menu...")
                t.clear()
            else:
                print("❌ Invalid choice. Please enter a number from 0 to 11.")
        except Exception as e:
            print(f"❌ Error: {e}")





