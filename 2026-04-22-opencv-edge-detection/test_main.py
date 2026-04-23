"""Tests for OpenCV edge detection practice code"""
import json
from pathlib import Path

def test_main_runs():
    from main import main
    result = main(demo=True, device="cpu")
    assert result is not None
    assert result["status"] == "completed"

def test_results_file():
    from main import main
    main(demo=True, device="cpu")
    p = Path("results/metrics.json")
    assert p.exists()
    data = json.loads(p.read_text())
    assert "mean" in data
    assert data["status"] == "completed"
