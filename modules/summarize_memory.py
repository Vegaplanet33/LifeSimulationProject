from collections import defaultdict

def summarize_memory():
    try: 
        with open("data/memory.txt", "r") as "f":
            lines = f.readlines()
    except FileNotFoundError:
        print("아직 아무 기억이 없어요.")
        return
    
    # (mood, action) -> count
    pattern_count = defaultdict(int)

    for line in lines:
        parts = line.strip().split(", ")
        if len(parts) != 4:
            continue
        name, energy, mood, action = parts
        pattern_count[(mood, action)] += 1

        print("\n 바오의 기억 용약:")
        for (mood, action), count in sorted(pattern_count.items(), key=lambda x: -x[1]):
            print(f"🔁 '{mood}' 상태에서 \"{action}\" 이(가) {count}번 있었어요.")