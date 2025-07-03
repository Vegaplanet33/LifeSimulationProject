# 생명체 초기 설정
name="바오"         # 생명체 이름
energy = 8         # 에너지 수치 (0~10)
mood = "happy"     # 기분상태

print(f"{name}이(가) 태어났습니다.")
print(f"에너지: {energy}, 기분: {mood}")


# 시간 경과 시뮬레이션
energy -= 2
mood = "tired"

print("\n시간이 흘렀습니다...")
print(f"{name}의 현재 에너지: {energy}")
print(f"{name}의 기분은 이제 {mood}입니다.")