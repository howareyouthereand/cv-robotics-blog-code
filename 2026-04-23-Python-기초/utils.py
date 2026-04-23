import numpy as np
import os
import json

def save_results(metrics, output_path, data=None):
    """결과를 저장하는 유틸리티"""
    os.makedirs('results', exist_ok=True)
    
    # JSON 메트릭 저장
    with open('results/metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    
    # 이미지 저장
    if data is not None:
        import cv2
        cv2.imwrite(output_path, data)

def get_rotation_matrix(angle_deg):
    theta = np.radians(angle_deg)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s], [s, c]])
