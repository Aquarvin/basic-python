import datetime

def with_logging(func):
    def wrapper():
        now =datetime.datetime.now()
        print(f"→ Перед вызовом {now}")
        func()
        now =datetime.datetime.now()
        print(f"→ После вызова {now}")
    return wrapper

@with_logging
def say_hi():
    print("Привет!")

say_hi()