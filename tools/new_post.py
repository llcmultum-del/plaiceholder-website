#!/usr/bin/env python3
"""Add one blog post to the live site without running build_site.py.

build_site.py is out of sync with the hand-edited HTML, so running it would
revert recent fixes. This script uses the live blog.html as the page shell.

Usage:  python3 tools/new_post.py post.json

post.json fields:
  slug         url-safe, e.g. "geo-for-b2b-websites"
  title        H1 and <title> (aim for under 60 characters)
  description  meta description (aim for 140-155 characters)
  tag          short category, e.g. "SEO", "GEO", "Machine Learning"
  date         ISO date, e.g. "2026-11-24"
  preview      1-2 sentence teaser for the blog index card
  body_html    the article body as HTML (h2/h3/p/ul/ol/a/strong only)
  faq          optional list of {"q": "...", "a": "..."} pairs (rendered + FAQPage schema)

What it does:
  - writes blog/<slug>.html (canonical, Open Graph, BlogPosting + FAQPage JSON-LD)
  - adds a card to the top of the grid in blog.html
  - rebuilds sitemap.xml and makes sure robots.txt points to it
Prints the public URL of the new post.
"""
import datetime
import html
import json
import os
import re
import sys

SITE = "https://plaiceholder.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_INDEX = os.path.join(ROOT, "blog.html")
BLOG_DIR = os.path.join(ROOT, "blog")
GRID_OPEN = '<div class="post-grid">'
PLACEHOLDER = '<p style="color:var(--muted);grid-column:1/-1;">Posts coming soon.</p>'


def die(msg):
    sys.exit(f"ERROR: {msg}")


def esc(s):
    return html.escape(s, quote=True)


def pretty_date(iso):
    d = datetime.date.fromisoformat(iso)
    return d.strftime("%B %-d, %Y")


def build_post(shell, p):
    url = f"{SITE}/blog/{p['slug']}.html"
    faq = p.get("faq") or []

    # <head>: base href so the shell's relative links work from /blog/
    head_extra = [
        f'  <link rel="canonical" href="{url}"/>',
        '  <meta property="og:type" content="article"/>',
        f'  <meta property="og:title" content="{esc(p["title"])}"/>',
        f'  <meta property="og:description" content="{esc(p["description"])}"/>',
        f'  <meta property="og:url" content="{url}"/>',
        '  <meta property="og:site_name" content="PlAIceholder"/>',
        f'  <meta property="article:published_time" content="{p["date"]}"/>',
        '  <meta name="twitter:card" content="summary"/>',
    ]
    ld = [{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p["title"],
        "description": p["description"],
        "datePublished": p["date"],
        "dateModified": p["date"],
        "mainEntityOfPage": url,
        "url": url,
        "keywords": p["tag"],
        "author": {"@type": "Organization", "name": "PlAIceholder", "url": SITE},
        "publisher": {"@type": "Organization", "name": "PlAIceholder", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/favicon.png"}},
    }]
    if faq:
        ld.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": f["q"],
                            "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faq],
        })
    for block in ld:
        head_extra.append('  <script type="application/ld+json">'
                          + json.dumps(block, ensure_ascii=False).replace("</", "<\\/")
                          + "</script>")

    out = shell
    out = re.sub(r"<title>.*?</title>", f"<title>{esc(p['title'])} | PlAIceholder</title>", out, count=1, flags=re.S)
    out, n = re.subn(r'<meta name="description" content=".*?"/>',
                     lambda m: f'<meta name="description" content="{esc(p["description"])}"/>\n' + "\n".join(head_extra),
                     out, count=1, flags=re.S)
    if n != 1:
        die("could not find meta description in blog.html")
    out = out.replace('<meta charset="UTF-8"/>', '<meta charset="UTF-8"/>\n  <base href="/"/>', 1)

    faq_html = ""
    if faq:
        faq_html = "\n<h2>Frequently asked questions</h2>\n" + "\n".join(
            f"<h3>{esc(f['q'])}</h3>\n<p>{esc(f['a'])}</p>" for f in faq)

    body = f"""<div class="page-banner">
  <div class="page-banner-inner" style="max-width:760px;">
    <span class="tag">{esc(p['tag'])}</span>
    <h1 style="margin-top:.75rem;">{esc(p['title'])}</h1>
    <p style="margin-top:.5rem;opacity:.7;"><time datetime="{p['date']}">{pretty_date(p['date'])}</time></p>
  </div>
</div>
<section class="section section-white">
  <div class="inner" style="max-width:760px;">
    <article class="post-body">
{p['body_html']}
{faq_html}
    </article>
    <div style="margin-top:3rem;padding-top:2rem;border-top:1.5px solid var(--border);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
      <a href="blog.html" style="color:var(--muted);font-size:.88rem;text-decoration:none;">&larr; All posts</a>
      <a href="contact.html" class="btn btn-grad">Book a free call &rarr;</a>
    </div>
  </div>
</section>
"""
    start = out.find('<div class="page-banner">')
    end = out.find("<footer>")
    if start < 0 or end < 0 or end < start:
        die("could not find the page-banner/footer markers in blog.html")
    return out[:start] + body + "\n" + out[end:], url


def add_card(index_html, p):
    card = f"""<a href="blog/{p['slug']}.html" class="post-card">
  <span class="post-tag">{esc(p['tag'])}</span>
  <h3>{esc(p['title'])}</h3>
  <p class="post-preview">{esc(p['preview'])}</p>
  <span class="post-date">{pretty_date(p['date'])}</span>
</a>"""
    if GRID_OPEN not in index_html:
        die("could not find the post grid in blog.html")
    index_html = index_html.replace(PLACEHOLDER + "\n", "").replace(PLACEHOLDER, "")
    return index_html.replace(GRID_OPEN + "\n", GRID_OPEN + "\n" + card + "\n", 1)


def write_sitemap():
    today = datetime.date.today().isoformat()
    urls = []
    for f in sorted(os.listdir(ROOT)):
        if f.endswith(".html"):
            loc = SITE + "/" if f == "index.html" else f"{SITE}/{f}"
            urls.append(loc)
    if os.path.isdir(BLOG_DIR):
        for f in sorted(os.listdir(BLOG_DIR)):
            if f.endswith(".html"):
                urls.append(f"{SITE}/blog/{f}")
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f"  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>" for u in urls]
    xml.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as fh:
        fh.write("\n".join(xml) + "\n")

    robots = os.path.join(ROOT, "robots.txt")
    line = f"Sitemap: {SITE}/sitemap.xml"
    text = open(robots).read() if os.path.exists(robots) else "User-agent: *\nAllow: /\n"
    if line not in text:
        text = text.rstrip("\n") + "\n\n" + line + "\n"
        with open(robots, "w") as fh:
            fh.write(text)


def main():
    if len(sys.argv) != 2:
        die("usage: python3 tools/new_post.py post.json")
    p = json.load(open(sys.argv[1]))
    for k in ("slug", "title", "description", "tag", "date", "preview", "body_html"):
        if not p.get(k):
            die(f"missing field: {k}")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", p["slug"]):
        die("slug must be lowercase letters, numbers and hyphens")
    datetime.date.fromisoformat(p["date"])

    os.makedirs(BLOG_DIR, exist_ok=True)
    target = os.path.join(BLOG_DIR, f"{p['slug']}.html")
    if os.path.exists(target):
        die(f"post already exists: blog/{p['slug']}.html")

    shell = open(BLOG_INDEX).read()
    page, url = build_post(shell, p)
    with open(target, "w") as fh:
        fh.write(page)
    with open(BLOG_INDEX, "w") as fh:
        fh.write(add_card(shell, p))
    write_sitemap()
    print(url)


if __name__ == "__main__":
    main()
