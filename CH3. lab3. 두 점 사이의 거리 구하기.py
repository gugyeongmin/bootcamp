# 추가 연습문제 03장 - 2번) 두 점 사이의 거리 구하기

x1 = int(input("x1의 값:")) # x1 안내 메시지 출력 & 수 입력 받기 (예시: x1=0)
y1 = int(input("y1의 값:")) # y1 안내 메시지 출력 & 수 입력 받기 (예시: y1=0)
x2 = int(input("x2의 값:")) # x2 안내 메시지 출력 & 수 입력 받기 (예시: x2=100)
y2 = int(input("y2의 값:")) # y2 안내 메시지 출력 & 수 입력 받기 (예시: y2=100)

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5 # 두 점 사이의 거리 구하기 공식 (제곱근: 0.5승)

print("두 점 사이의 거리 = ", distance)   # 두 점 사이의 거리 구하기 정리
