def save_memory(name, energy, mood, action):
    new_line = f"{name}, {energy}, {mood}, {action}".strip()
    
    try:
        with open("data/memory.txt", "r") as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        lines = []

    if new_line not in lines:
        with open("data/memory.txt", "a") as f:
             f.write(new_line + "\n")


def load_memory():
    try:
        with open("data/memory.txt", "r") as f:
            lines = [line.strip() for line in f.readlines()]
        print("🧠 기억을 불러옵니다:")
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("🌀 기억이 아직 없어요.")