import random

def rainy_day_activity():
    activities = [
        "Stay indoors and read a book by the fireplace.",
        "Watch movies and enjoy some hot cocoa.",
        "Bake cookies or your favorite treats.",
        "Have a board game marathon with family or friends.",
        "Write poetry or work on a creative project.",
        "Listen to calming music and relax with a warm blanket.",
        "Experiment with cooking a new recipe.",
        "Do some indoor exercises or yoga.",
        "Organize and declutter your living space.",
        "Take a nap and enjoy the sound of rain outside."
    ]
    return random.choice(activities)

# Example usage:
print("On this rainy day, you could:")
print(rainy_day_activity())
