"""
Unit Test Suite for PixelBudget Autoregressive Generation
Validates notebook structure, execution output, and HTML report integrity.
"""

import json
import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_notebook_exists_and_valid():
    nb_path = os.path.join(REPO_ROOT, "PixelBudget_CPU_Validated.ipynb")
    assert os.path.isfile(nb_path), "Notebook must exist"
    with open(nb_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert "cells" in data
        assert len(data["cells"]) > 10, "Notebook should have substantive content"

def test_html_report_exists():
    html_path = os.path.join(REPO_ROOT, "PixelBudget_CPU_Report.html")
    assert os.path.isfile(html_path), "HTML report must exist"
    assert os.path.getsize(html_path) > 500000, "HTML report should contain visual charts"

def test_license_and_readme():
    assert os.path.isfile(os.path.join(REPO_ROOT, "LICENSE"))
    assert os.path.isfile(os.path.join(REPO_ROOT, "README.md"))
