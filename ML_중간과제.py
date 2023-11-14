import random
import matplotlib.pyplot as plt
import numpy as np

# Step 1: 중복되지 않는 200개의 2차원 좌표 생성
random_coordinates = set()

while len(random_coordinates) < 200:
    x = random.randint(0, 400)  # 0에서 400까지의 정수 난수 생성
    y = random.randint(0, 400) 
    random_coordinates.add((x, y))

x_values, y_values = zip(*random_coordinates)

# 차트로 표시
plt.figure(figsize=(8, 8))
plt.scatter(x_values, y_values, color='black')  
plt.title("Step 1: 200개의 좌표값 생성")  
plt.xlabel("X")  
plt.ylabel("Y")
plt.show()

# Step 2: 좌표를 A그룹과 B그룹으로 나누어 각각의 평균값 계산
coordinates = list(random_coordinates)  # 좌표 목록으로 변환
random.shuffle(coordinates)  # 좌표를 섞기

A_group = coordinates[:100]  # 처음 100개의 좌표를 A그룹으로 할당
B_group = coordinates[100:]  # 나머지 100개의 좌표를 B그룹으로 할당

A_avg_x = np.mean([point[0] for point in A_group])  # A그룹 x 좌표 평균
A_avg_y = np.mean([point[1] for point in A_group])  # A그룹 y 좌표 평균

B_avg_x = np.mean([point[0] for point in B_group])  # B그룹 x 좌표 평균
B_avg_y = np.mean([point[1] for point in B_group])  # B그룹 y 좌표 평균

# Step 3 & Step 4: 빨강 그룹과 파랑 그룹의 평균값을 기준으로 반복적으로 계산
def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)  # 두 좌표 사이의 거리 계산 함수

# 결과를 저장할 리스트
A_groups_history = []  
B_groups_history = []  

while True:
    A_distances = [distance(point, (A_avg_x, A_avg_y)) for point in coordinates]  # A 그룹과의 거리 계산
    B_distances = [distance(point, (B_avg_x, B_avg_y)) for point in coordinates]  # B 그룹과의 거리 계산

    A_group = [coordinates[i] for i in range(200) if A_distances[i] < B_distances[i]]  # 거리에 따라 좌표를 A 또는 B 그룹으로 할당
    B_group = [coordinates[i] for i in range(200) if A_distances[i] >= B_distances[i]]

    new_A_avg_x = np.mean([point[0] for point in A_group])  # 새로운 A 그룹의 x 좌표 평균
    new_A_avg_y = np.mean([point[1] for point in A_group])  # 새로운 A 그룹의 y 좌표 평균

    new_B_avg_x = np.mean([point[0] for point in B_group])  # 새로운 B 그룹의 x 좌표 평균
    new_B_avg_y = np.mean([point[1] for point in B_group])  # 새로운 B 그룹의 y 좌표 평균

    A_groups_history.append(A_group)  # 현재 상태를 이력에 추가
    B_groups_history.append(B_group)

    if (A_avg_x, A_avg_y) == (new_A_avg_x, new_A_avg_y) and (B_avg_x, B_avg_y) == (new_B_avg_x, new_B_avg_y):  # 평균값이 변하지 않으면 종료
        break

    A_avg_x, A_avg_y = new_A_avg_x, new_A_avg_y  # 새로운 평균값으로 갱신
    B_avg_x, B_avg_y = new_B_avg_x, new_B_avg_y

# 결과 그래프 
for i, (A_group, B_group) in enumerate(zip(A_groups_history, B_groups_history)):  # 반복
    plt.figure(figsize=(8, 8))
    plt.scatter([point[0] for point in A_group], [point[1] for point in A_group], color='red', label='A')
    plt.scatter([point[0] for point in B_group], [point[1] for point in B_group], color='blue', label='B')
    plt.scatter([A_avg_x, B_avg_x], [A_avg_y, B_avg_y], color='green', label='A Group and B Groups average', s=200)
    plt.legend()
    plt.title(f"반복 {i + 1}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
