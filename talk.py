# 기억 불러오기
with open("data/memory.txt", "r", encoding="utf-8") as f:
    memories = f.readlines()

print("=== 바오의 기억들 ===")
for line in memories:
    print("_", line.strip())

# 생명체 초기 상태
name = "바오"
energy = 7

# 사용자로부터 기분 입력받기
mood = input("바오의 현재 기분은 어떤가요? (happy/tired/angry/hungry):")
energy = int(input("바오의 에너지 값을 넣어주세요 (0~7).: "))

# 현재 상태 출력
print(f"\n{name}의 현재 상태:")
print(f"에너지: {energy}")
print(f"기분: {mood}")

# 조건에 따른 반응
if mood == "happy" and energy > 4:
    print("바오는 뛰어다니고 있어요! 🐾")
elif mood == "happy" and energy < 4:
    print("바오는 명상을 하고 있어요 🐾")
elif mood == "happy":
    print("바오는 웃고 있어요.")
