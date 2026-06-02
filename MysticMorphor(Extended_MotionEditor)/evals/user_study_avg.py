import pandas as pd
import re
from collections import defaultdict

# CSV 불러오기
df = pd.read_csv('output_ratio.csv')  # 파일명 수정

# 결과 저장용
results = defaultdict(lambda: defaultdict(list))  # results[model][question_type] = [score1, score2, ...]

for col in df.columns:
    try:
        # 1-2-0 같이 생긴 이름에서 추출
        match = re.match(r"(\d+)-(\d+)-(\d+)", col)
        if match:
            sample_id, model_id, qtype = match.groups()
            print(sample_id, model_id)

            # 샘플별로 수동으로 모델 지정
            if sample_id == '1':
                print('1')
                if model_id == '1':
                    print('control')
                    model = 'ControlVideo'
                elif model_id == '2':
                    model = 'MotionEditor'
                elif model_id == '3':
                    model = 'FYP'
                elif model_id == '4':
                    model = 'MC'
                elif model_id == '5':
                    model = 'MotionDirector'
            elif sample_id == '2':
                if model_id == '1':
                    print('control')
                    model = 'ControlVideo'
                elif model_id == '2':
                    print('MC')
                    model = 'MC'
                elif model_id == '3':
                    model = 'FYP'
                elif model_id == '4':
                    model = 'MotionDirector'
                elif model_id == '5':
                    model = 'MotionEditor'
            else:
                if model_id == '1':
                    model = 'ControlVideo'
                elif model_id == '2':
                    model = 'FYP'
                elif model_id == '3':
                    model = 'MC'
                elif model_id == '4':
                    model = 'MotionDirector'
                elif model_id == '5':
                    model = 'MotionEditor'
                

            values = pd.to_numeric(df[col], errors='coerce').dropna()
            results[model][qtype].extend(values.tolist())
    except:
        continue
print(results)
# 평균 계산 결과 저장
output_rows = []
for model, q_dict in results.items():
    row = {'Model': model}
    for qtype, values in q_dict.items():
        row[f'Q{qtype}'] = round(sum(values) / len(values), 1) if values else None
    output_rows.append(row)

# 결과 DataFrame으로
result_df = pd.DataFrame(output_rows)
result_df.to_csv('model_question_type_scores.csv', index=False)

print("✅ 결과가 'model_question_type_scores.csv'에 저장되었습니다.")