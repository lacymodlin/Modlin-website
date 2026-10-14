# Modlin Designs website

The site for modlindesigns.com, published by Netlify.

- `site/` is the live website. Netlify publishes this folder (see `netlify.toml`).
- `source/` holds the pieces it's built from. Edit those, then run `python3 source/build.py` to rebuild `site/`.
- The inquiry form uses Netlify Forms (form name `inquiry`). A Zap sends each submission to the Notion Leads Tracking board.
