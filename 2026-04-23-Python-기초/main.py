import argparse
import numpy as np
import cv2
import time
import json
from utils import save_results, get_rotation_matrix

def run_robotics_task(angle=90):
    v = np.array([10.0, 0.0])
    R = get_rotation_matrix(angle)
    start = time.time()
    rotated = R.dot(v)
    return rotated, time.time() - start

def run_cv_task(use_cuda=False):
    # 합성 데이터 생성 (100x100 RGB 이미지)
    img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    
    start = time.time()
    # 그레이스케일 변환 (Vectorized operation)
    weights = np.array([0.299, 0.587, 0.114])
    gray = np.dot(img.astype(np.float32), weights).astype(np.uint8)
    duration = time.time() - start
    
    return gray, duration

def main(args):
    print(f"Running on device: {args.device}")
    
    # 1. Robotics Task
    vec, t1 = run_robotics_task()
    
    # 2. CV Task
    img, t2 = run_cv_task(args.device == 'cuda')
    
    metrics = {
        "robotics_time": t1,
        "cv_time": t2,
        "rotated_vector": vec.tolist()
    }
    
    save_results(metrics, 'results/output.png', img)
    print("Task completed. Results saved to results/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="Run in demo mode")
    parser.add_argument("--device", choices=["cpu", "cuda"], default="cpu")
    args = parser.parse_args()
    
    try:
        main(args)
    except Exception as e:
        print(f"Error occurred: {e}")
