"""Smoke test: every notebook runs top to bottom without an error cell."""

from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = sorted(ROOT.glob("[0-9][0-9]-*.ipynb"))


def test_notebooks_found():
    assert len(NOTEBOOKS) == 4


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_executes(path: Path):
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(
        notebook, timeout=300, kernel_name="python3", resources={"metadata": {"path": str(ROOT)}}
    )
    client.execute()  # raises CellExecutionError on the first failing cell
