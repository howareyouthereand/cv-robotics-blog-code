import os
import pytest
import json
from main import main
from argparse import Namespace

def test_main_execution():
    # Demo 모드 실행 테스트
    args = Namespace(demo=True, device='cpu')
    main(args)
    
    # 결과 파일 생성 확인
    assert os.path.exists('results/metrics.json')
    assert os.path.exists('results/output.png')
    
    # 메트릭 데이터 검증
    with open('results/metrics.json', 'r') as f:
        data = json.load(f)
        assert 'robotics_time' in data
        assert 'cv_time' in data
        assert len(data['rotated_vector']) == 2
