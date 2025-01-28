I spent a lot of time trying to get this to work, so I'm going to document the process here.

- First, make sure you just get something working with Sphinx and `sphinx_rtd_theme`. See if it works in browser.
Here is how you can see it in browser:
```bash
python -m http.server --directory build/html
```
Always use command line to see it in browser becausse if you download it and open it in Chrome browser it does not work.

This is the quick start:

```
sphinx-quickstart
```
I cannot use `make build` because I want to create html files in the docs folder.

(2025-01-28) Next step:
- I will create all html files in the docs folder and see how I can use `make html` to build them.

How can I do it? I need to change the `conf.py` file.


# Quick Guide: Setting up Sphinx Docs on GitHub

1. Create docs structure:
```bash
mkdir docs
cd docs
sphinx-quickstart  # Answer 'yes' to separate source and build
```

2. Edit `docs/source/conf.py`:
```python
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
html_static_path = []  # Remove static path warning
```

3. Build HTML directly in docs:
```bash
cd docs
sphinx-build -b html source .
```

4. Add `.nojekyll` file:
```bash
touch docs/.nojekyll
```

5. Update `.gitignore` to track HTML:
```
!docs/*.html
!docs/_static/
!docs/_sources/
```

6. Enable GitHub Pages:
- Settings → Pages
- Select branch and /docs folder
- Save

To enable GitHub Pages:

1. For "Source", select "Deploy from a branch"
2. For "Branch", select "docs" from the dropdown
3. Leave the folder selection as "/ (root)" since we built our documentation directly in the docs folder
4. Click "Save"

The settings should look like this:
- Branch: docs
- Folder: / (root)

After saving, GitHub will start deploying your site. It may take a few minutes before your documentation is available at `https://<username>.github.io/<repository-name>/`.