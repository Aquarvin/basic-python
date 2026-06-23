def format_lap_time(seconds):
    minutes = int(seconds//60)
    seconds_ = (seconds%60)
    seconds_r =round(seconds_, 3)
    return f"{minutes}:{seconds_r}"