def act(name, mood, energy):
    print(">> act() 함수 실행 시작")
    if mood == "happy" and energy > 5:
        print(f"{name}는 산책 나갔어요!🚶‍♂️")
    elif mood == "tired" or energy < 3:
        print(f"{name}는 조용히 누워서 자고 있어요 😴")
    elif mood == "angry":
        print(f"{name}는 화가 나서 으르릉~~! 소리를 냈어요. 😡💥")
    elif mood == "sleepy" or energy <= 5:
        print(f"{name}는 졸려서 바닥에 누워 자고 있어요.😪💤")
    else:
        print(f"{name}는 멍하니 창 밖을 바라보고 있어요. 😶")