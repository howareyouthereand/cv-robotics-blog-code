# Robotics & CV Python 기초 실습

## 설치
```bash
pip install -r requirements.txt
```

## 실행 방법
1. 기본 실행 (CPU):
```bash
python main.py --demo
```

2. 테스트 실행:
```bash
pytest test_main.py
```

## 구조
- `main.py`: 로봇 좌표 변환 및 이미지 처리 메인 로직
- `utils.py`: 행렬 연산 및 파일 저장 헬퍼
- `results/`: 결과물(JSON, PNG) 저장 폴더
