import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('QA.csv')

# 결과 저장용 딕셔너리
result = {}

cnt = 0
cnt1 = -1
# 각 열마다 'A' 비율 계산

for column in df.columns:
    cnt += 1
    cnt1 += 1
    if cnt1 > 14:
        cnt1 = 0
    col_data = df[column].dropna()
    total = len(col_data)
    if cnt == 1 or cnt == 2 or cnt == 3:
        correct = 'B'
    elif cnt == 4 or cnt == 5 or cnt == 6:
        correct = 'A'
    elif cnt == 7 or cnt == 8 or cnt == 9:
        correct = 'B'
    elif cnt == 10 or cnt == 11 or cnt == 12:
        correct = 'B'
    elif cnt == 13 or cnt == 14 or cnt == 15:
        correct = 'B'
    elif cnt == 16 or cnt == 17 or cnt == 18:
        correct = 'B'
    elif cnt == 19 or cnt == 20 or cnt == 21:
        correct = 'B'
    elif cnt == 22 or cnt == 23 or cnt == 24:
        correct = 'A'
    elif cnt == 25 or cnt == 26 or cnt == 27:
        correct = 'A'
    elif cnt == 28 or cnt == 29 or cnt == 30:
        correct = 'B'
    elif cnt == 31 or cnt == 32 or cnt == 33:
        correct = 'B'
    elif cnt == 34 or cnt == 35 or cnt == 36:
        correct = 'B'
    elif cnt == 37 or cnt == 38 or cnt == 39:
        correct = 'A'
    elif cnt == 40 or cnt == 41 or cnt == 42:
        correct = 'A'
    elif cnt == 43 or cnt == 44 or cnt == 45:
        correct = 'A'
    elif cnt == 46 or cnt == 47 or cnt == 48:
        correct = 'B'
    elif cnt == 49 or cnt == 50 or cnt == 51:
        correct = 'B'
    elif cnt == 52 or cnt == 53 or cnt == 54:
        correct = 'B'
    elif cnt == 55 or cnt == 56 or cnt == 57:
        correct = 'A'
    elif cnt == 58 or cnt == 59 or cnt == 60:
        correct = 'A'
    elif cnt == 61 or cnt == 62 or cnt == 63:
        correct = 'B'
    elif cnt == 64 or cnt == 65 or cnt == 66:
        correct = 'B'
    elif cnt == 67 or cnt == 68 or cnt == 69:
        correct = 'B'
    elif cnt == 70 or cnt == 71 or cnt == 72:
        correct = 'A'
    elif cnt == 73 or cnt == 74 or cnt == 75:
        correct = 'A'
    elif cnt == 76 or cnt == 77 or cnt == 78:
        correct = 'B'
    elif cnt == 79 or cnt == 80 or cnt == 81:
        correct = 'B'
    elif cnt == 82 or cnt == 83 or cnt == 84:
        correct = 'B'
    elif cnt == 85 or cnt == 86 or cnt == 87:
        correct = 'A'
    elif cnt == 88 or cnt == 89 or cnt == 90:
        correct = 'A'
    elif cnt == 91 or cnt == 92 or cnt == 93:
        correct = 'B'
    elif cnt == 94 or cnt == 95 or cnt == 96:
        correct = 'B'
    elif cnt == 97 or cnt == 98 or cnt == 99:
        correct = 'B'
    elif cnt == 100 or cnt == 101 or cnt == 102:
        correct = 'B'
    elif cnt == 103 or cnt == 104 or cnt == 105:
        correct = 'B'
    elif cnt == 106 or cnt == 107 or cnt == 108:
        correct = 'A'
    elif cnt == 109 or cnt == 110 or cnt == 111:
        correct = 'A'
    elif cnt == 112 or cnt == 113 or cnt == 114:
        correct = 'A'
    elif cnt == 115 or cnt == 116 or cnt == 117:
        correct = 'A'
    elif cnt == 118 or cnt == 119 or cnt == 120:
        correct = 'A'
    elif cnt == 121 or cnt == 122 or cnt == 123:
        correct = 'B'
    elif cnt == 124 or cnt == 125 or cnt == 126:
        correct = 'B'
    elif cnt == 127 or cnt == 128 or cnt == 129:
        correct = 'B'
    elif cnt == 130 or cnt == 131 or cnt == 132:
        correct = 'B'
    elif cnt == 133 or cnt == 134 or cnt == 135:
        correct = 'B'
    elif cnt == 136 or cnt == 137 or cnt == 138:
        correct = 'B'
    elif cnt == 139 or cnt == 140 or cnt == 141:
        correct = 'B'
    elif cnt == 142 or cnt == 143 or cnt == 144:
        correct = 'B'
    elif cnt == 145 or cnt == 146 or cnt == 147:
        correct = 'B'
    elif cnt == 148 or cnt == 149 or cnt == 150:
        correct = 'B'

    count_A = (col_data == correct).sum()
    ratio = round((float(count_A) / float(total)) * 100, 1) if total > 0 else None

    # 컬럼 이름 포맷 1-1, 1-2, ..., 2-1, ...
    group = cnt // 15 + 1
    sub1 = cnt1 // 3 + 1 
    sub2 = cnt % 3
    col_name = f"{group}-{sub1}-{sub2}"

    result[col_name] = ratio

# 결과를 데이터프레임으로 변환c
result_df = pd.DataFrame([result])

# CSV로 저장
result_df.to_csv('output_ratio.csv', index=False)

print("✅ 'output_ratio.csv' 파일로 저장되었습니다.")