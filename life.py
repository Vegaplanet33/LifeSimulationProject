from modules.actions import act
from modules.memory import save_memory
from modules.memory import load_memory

print("\n--- 과거 기억 확인 ---")
load_memory()


# 기본 설정
name = "바오"
mood = "sleepy"
energy = 5

# act 함수 실행 / 행동 실행
act(name, mood, energy)

# 조건부 저장: 졸리고 에너지가 낮을 때만 기억 저장
if energy < 6 and mood == "sleepy":
    save_memory(name, energy, mood, "산책 후 졸음이 몰려와요.")

from modules.memory import summarize_memory

print("\n--- 과거 기억 요약 ---")
summarize_memory()