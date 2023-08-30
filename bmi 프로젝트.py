Body = []
Body.append(float(input("신장(m)를 입력하세요.: "))) #키를 입력하는곳
Body.append(int(input("몸무게(kg)를 입력하세요.: "))) #몸무게를 입력하는곳
print("키와 몸무게:", Body)
print("당신의 체질량(BMI)는 {:.2f} 입니다.".format(Body[1] / (Body[0] * Body[0])))