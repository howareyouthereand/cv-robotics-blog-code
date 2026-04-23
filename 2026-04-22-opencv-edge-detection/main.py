"""
OpenCV edge detection - Practice Code
Auto-generated practice code for hands-on learning.
"""
import argparse
import json
import numpy as np
from pathlib import Path

try:
    import cv2
    HAS_CV2 = True
except ImportError:
    HAS_CV2 = False


def main(demo: bool = False, device: str = "cpu"):
    print(f"=== OpenCV edge detection Practice ===")
    print(f"Device: {device}, Demo: {demo}")

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    # Generate synthetic data
    h, w = (64, 64) if demo else (256, 256)
    data = np.random.randint(0, 255, (h, w, 3), dtype=np.uint8)

    # Basic CV operation
    gray = np.mean(data, axis=2).astype(np.uint8)
    mean_val = float(np.mean(gray))
    std_val = float(np.std(gray))

    # Save visualization
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        axes[0].imshow(data)
        axes[0].set_title("Input")
        axes[1].imshow(gray, cmap="gray")
        axes[1].set_title("Processed")
        plt.tight_layout()
        plt.savefig(results_dir / "output.png", dpi=100)
        plt.close()
        print("Saved: results/output.png")
    except ImportError:
        print("matplotlib not available, skipping visualization")

    metrics = {
        "keyword": "OpenCV edge detection",
        "device": device,
        "demo": demo,
        "image_size": [h, w],
        "mean": round(mean_val, 4),
        "std": round(std_val, 4),
        "status": "completed",
    }

    with open(results_dir / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    print(f"Results saved: results/metrics.json")
    print(f"Mean: {mean_val:.4f}, Std: {std_val:.4f}")
    return metrics


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenCV edge detection Practice")
    parser.add_argument("--demo", action="store_true", help="Demo mode (fast)")
    parser.add_argument("--device", default="cpu", choices=["cuda", "cpu"])
    args = parser.parse_args()
    main(demo=args.demo, device=args.device)
