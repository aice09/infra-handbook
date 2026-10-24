project = "Infrastructure Engineering Handbook"
author = "Infrastructure Engineering"
release = "0.1.0"

extensions = ["myst_parser"]

root_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "sphinx_rtd_theme"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]