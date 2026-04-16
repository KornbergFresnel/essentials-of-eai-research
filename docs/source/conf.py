from __future__ import annotations

from pathlib import Path

project = "Essentials of Embodied AI Research"
author = "Ming Zhou"
copyright = "2026, Ming Zhou"

root_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = project

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "substitution",
]

myst_heading_anchors = 3

language = "en"
locale_dirs = ["locale/"]
gettext_compact = False

_static_dir = Path(__file__).parent / "_static"
_static_dir.mkdir(exist_ok=True)
