def square(x):
    return x**2

def is_even(n):
    return n%2==0

def format_lap_time(seconds):
    minutes = int(seconds//60)
    seconds_ = (seconds%60)
    seconds_r =round(seconds_, 3)
    return f"{minutes}:{seconds_r}"

def make_greeting(name, sport="Формулу 1"):
    return f"{name} смотрит {sport}"

