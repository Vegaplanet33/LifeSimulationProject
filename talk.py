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
user_input = input("바오에게 말을 걸어보세요.: ")

if "비" in user_input:
    print("☔️ 바오: ... (눈빛이 어두어진다.)")
elif "피자" in user_input:
    print("🍕 바오: 월월월!!! 좋아!! 피자!!!")
else:
    print("🤖 바오: ... (기억을 더 수집 중입니다.)")