project = "Infrastructure Engineering Handbook"
author = "Carl Angelo Nievarez"
release = "0.1.0"
year = 2026
copyright = f"{year}, {author}"

extensions = ["myst_parser"]

root_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "sphinx_rtd_theme"
html_js_files = [
    ("/_vercel/speed-insights/script.js", {"defer": "defer"}),
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]