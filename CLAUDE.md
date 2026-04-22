# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A French-language machine learning tutorial series for the YouTube channel **Monty Python with Brice**. Notebooks cover the Python data science stack from basics to EDA, intended for beginners.

GitHub: https://github.com/boodscode237/apprentissageautomatique.git

## Build & preview

Uses MyST (mystmd.org) with JupyterLite — notebooks run directly in the browser.

```bash
# Build the site
myst build

# Build and serve locally
myst start
```

## Auto-push to GitHub

`watcher.py` watches the root directory and auto-commits/pushes any new `.ipynb` file added. Run it via:

```bash
python watcher.py
# or on Windows:
start_watcher.bat
```

Requires `watchdog` (`pip install watchdog`).

## Content structure

Each module lives in its own numbered subfolder with a single notebook:

| Folder | Notebook | Topic |
|--------|----------|-------|
| `00 Les bases du langage Python, les notebooks Jupyter` | `Les bases du langage Python et les notebooks Jupyter.ipynb` | Python basics & Jupyter |
| `01 NUMPY` | `NUMPY.ipynb` | NumPy |
| `02 MATPLOTLIB` | `Matplotlib.ipynb` | Matplotlib |
| `03 PANDAS` | `pandas.ipynb` | Pandas |
| `04 EDA` | *(in progress)* | Exploratory Data Analysis |

`correction_*.ipynb` files should be excluded from the site build via `myst.yml` `exclude`.

## MyST configuration

When setting up `myst.yml`, use:
- Site template: `book-theme`
- `jupyter: lite: true` (in-browser execution)
- Logo/favicon: `logo.svg` / `favicon.svg` (YouTube channel branding: Monty Python with Brice)
