import tkinter as tk 

window = tk.Tk()

window.title("🚀Space Explorer")
window.geometry("700x500")
window.configure(bg="#0E1949")

space = tk.Canvas(
    window,
    bg="#0B1026",
    highlightthickness=0
)

space = tk.Canvas(
    window,
    bg="#0B1026",
    highlightthickness=0
)

space.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)

stars = [
    (50, 80),
    (120, 150),
    (200, 60),
    (300, 120),
    (400, 70),
    (500, 180),
    (600, 100),
    (650, 250),
    (80, 350),
    (250, 400),
    (450, 350),
    (580, 420)
]

for x, y in stars:
    space.create_oval(
        x, y, x + 3, y + 3,
        fill="white",
        outline=""
    )

planet_card = tk.Frame(
    window,
    bg="#0E1949",
    width=500,
    height=250
)

planet_card.pack(pady=20)

title = tk.Label(
    window, 
    text="SPACE EXPLORER",
    font=("ARIAL", 28, "bold"),
    bg="#0E1949",
    fg="white"
)


title.pack(pady=40)

planet = tk.Label(
    window,
    text="🌍 Earth",
    font=("Arial", 24, "bold"),
    bg="#0E1949",
    fg="white"
)

planet.pack(pady=20)

info = tk.Label(
    window,
    text="Our home planet",
    font=("Arial", 16),
    bg ="#0E1949",
    fg="white"
)

info.pack(pady=10)

planet_number = tk.Label(
    planet_card,
    text="1/8",
     font=("Arial", 16),
    bg = "#0E1949",
    fg="white"
)

planet_number.pack(pady=8)

search_entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=25
)

search_entry.pack(pady=10)

planets = [
    "☿ Mercury",
    "♀ Venus",
    "🌍 Earth",
    "🔴 Mars",
    "♃ Jupiter",
    "🪐 Saturn",
    "♅ Uranus",
    "♆ Neptune"
]

full_infos = [
    "Mercury is the smallest planet in the Solar System and the closest planet to the Sun. It has extreme temperature changes and completes an orbit around the Sun in only 88 Earth days.",

    "Venus is similar in size to Earth, but it is the hottest planet in the Solar System. Its thick carbon-dioxide atmosphere creates an extreme greenhouse effect.",

    "Earth is the only known planet with life. About 71% of its surface is covered by water, and its atmosphere contains mostly nitrogen and oxygen. Earth has one Moon.",

    "Mars is known as the Red Planet. It has a thin atmosphere, two small moons, and features including Olympus Mons, the largest volcano in the Solar System.",

    "Jupiter is the largest planet in the Solar System. It has a famous Great Red Spot, a huge storm, and many moons including Ganymede, the largest moon in the Solar System.",

    "Saturn is famous for its spectacular rings, which are made mostly of ice and rock. It is the least dense planet and has many moons, including Titan.",

    "Uranus is an ice giant with a blue-green color caused by methane in its atmosphere. It rotates almost on its side and has a faint ring system and many moons.",

    "Neptune is the farthest planet from the Sun and has the strongest winds in the Solar System. It is a blue ice giant with dark storms and a faint ring system."
]

current_planet = 0




infos = [
    "The closest planet to the Sun.",
    "The hottest planet in the solar system.",
    "Our home planet and the only known planet with life.",
    "The Red Planet, famous for Olympus Mons.",
    "The largest planet in the solar system.",
    "Famous for its beautiful rings.",
    "An ice giant that rotates on its side.",
    "The farthest planet and the windiest planet."
]

current_planet = 0

def show_previous_planet():
    global current_planet

    if current_planet > 0:
        current_planet -= 1
        planet.config(text=planets[current_planet])
        info.config(text=infos[current_planet])
        planet_number.config(text=f"{current_planet + 1} / {len(planets)}")

def show_more_info():
    info_window = tk.Toplevel(window)

    info_window.title("Planet Information")
    info_window.geometry("600x400")

    text = tk.Label(
        info_window,
        text=full_infos[current_planet],
        font=("Arial", 13),
        wraplength=520,
        justify="left"
    )

    text.pack(padx=30, pady=30)

def show_next_planet():
    global current_planet

    if current_planet < len(planets) - 1:
       current_planet+=1

       planet.config(text=planets[current_planet])
       info.config(text=infos[current_planet])
       planet_number.config(text=f"{current_planet + 1} / {len(planets)}")

def search_planet():
    global current_planet

    search = search_entry.get().lower()

    for i in range(len(planets)):
        if search in planets[i].lower():
            current_planet = i

            planet.config(text=planets[current_planet])
            info.config(text=infos[current_planet])
            planet_number.config(
                text=f"{current_planet + 1} / {len(planets)}"
            )

            break       

previous_button = tk.Button(
    window,
    text="◀ Previous",
    font=("Arial", 12, "bold")
)

previous_button = tk.Button(
    window,
    text="◀ Previous",
    font=("Arial", 12, "bold"),
    command=show_previous_planet
)

previous_button.pack(side="left", padx=20, pady=20)

next_button = tk.Button(
    window,
    text="Next Planet",
    command=show_next_planet
)

next_button.pack(pady=20)

more_button = tk.Button(
    window,
    text="🔭 More Info",
    font=("Arial", 12, "bold"),
    command=show_more_info
)

more_button.pack(pady=10)

search_button = tk.Button(
    window,
    text="🔍 Search Planet",
    command=search_planet
)

search_button.pack(pady=5)

window.mainloop()