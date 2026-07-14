# individualtuition.in

Static website for [individualtuition.in](https://individualtuition.in) — a directory of
individual tuition / home-tutor listings across India and the UAE.

## Layout

- **`public_html/`** — the live website. Plain HTML, CSS, and JS served as static files.
  Uploaded to the web host as-is.
- **`scripts/`** — Python generators used to produce the program-level SEO pages and
  related meta content.

## Local development

The site is plain static files — open `public_html/index.html` in a browser, or serve
the folder with any static HTTP server, e.g.:

```sh
cd public_html
python3 -m http.server 8000
```

## Generating SEO pages

The scripts in `scripts/` regenerate the program/location pages. Run from the repo
root:

```sh
python3 scripts/pseo_generator.py
```

Output is written under `public_html/`.

## Deployment

Sync `public_html/` to the host (e.g. via FTP/rsync). Server-side artifacts
(`logs/`, `awstats/`, `stats/`, `.htpasswd`, `public_ftp/`) live outside the repo
and are excluded via `.gitignore`.

## Theme

Based on the [Bocor](https://bootstrapmade.com/bocor-bootstrap-template-nice-animation/)
Bootstrap template by [BootstrapMade](https://bootstrapmade.com/), licensed under
their [license terms](https://bootstrapmade.com/license/).
