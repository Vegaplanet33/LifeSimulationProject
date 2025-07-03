# 생명체 초기 설정
name="바오"         # 생명체 이름
energy = 8         # 에너지 수치 (0~10)
mood = "happy"     # 기분상태

def act(name, mood, energy):
    if mood == "happy" and energy >5:
        print(f"{name}는 산책 나갔어요!🚶‍♂️")
    elif mood == "tired" or energy < 3:
        print(f"{name}는 조용히 누워서 자고 있어요 😴")
    elif mood == "angry":
        print(f"{name}는 화가 나서 으르릉~~! 소리를 냈어요. 😡💥")
    else:
        print(f"{name}는 멍하니 창 밖을 바라보고 있어요. 😶")

    act(name, mood, energy)
