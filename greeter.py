import datetime

# print a welcome message
# ask user for their name
# say hello back

# Plant wisdom quotes - generated with AI assistance
plant_wisdom = [ 
    "Even the tallest tree started as a tiny seed. Keep growing!",
    "Roots before branches. Build your foundation first.",
    "A little water and sunlight goes a long way. So does rest.",
    "Not every leaf grows the same way, and that's what makes a plant beautiful.",
    "Patience is a gardener's greatest tool.",
    "You cannot rush growth, but you can nurture it.",
    "Every season has a purpose, even the dormant ones.",
    ]

# ASCII art of Anna (my oldest plant in my collection, a Pothos) - generated with AI assistance
print('Hello...')
print("""          .  *    .       *    .
       *    __|__    *       .
           /     \\
      .   / ~   ~ \\    .
         /  ~   ~  \\       *
        |  ~ ~ ~ ~  |
        |   ~   ~   |   .
         \\ ~ ~ ~ ~ /
     *    \\_______/       *
              | |
         ~~~~| |~~~~
              | |
      """)
print('Welcome to my Software Portfolio!')
print('I am Anna the Golden Pothos')

# Anna asks for the user name, then gives greeting based on the time of day.
name = input('What is your name? ')
print()

# wrote a function for the logic
def time_of_day():

    hour = datetime.datetime.now().hour

    if hour < 12:
        print('Good morning', name)

    elif hour >= 12 and hour < 17:
        print('Good afternoon', name)

    else:
        print('Good evening', name)    
time_of_day()

# Anna then imparts wisdom depending on which day of the week it is.
day = datetime.datetime.now().weekday()
print (plant_wisdom[day])
print()
print('Come back another day for more plant wisdom!')
print()