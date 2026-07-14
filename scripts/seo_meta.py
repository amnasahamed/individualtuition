"""Shared SEO head markup for individualtuition.in pages."""

BASE = "https://individualtuition.in"
OG_IMAGE = f"{BASE}/assets/img/new-img.png"
SITE_NAME = "CLAPS Individual Tuition"


def seo_head(
    *,
    title: str,
    description: str,
    canonical: str,
    asset_prefix: str = "",
    lang: str = "en",
    keywords: str = "",
    robots: str = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
) -> str:
    kw = keywords or "individual tuition, CLAPS, ClapsLearn, online tuition, one to one tuition, Kerala tuition, CBSE tuition"
    hreflang = "ml" if lang == "ml" else "en"
    alt_lang = "en" if lang == "ml" else "ml"

    return f"""  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#ffffff">
  <meta name="robots" content="{robots}">
  <meta name="googlebot" content="{robots}">
  <meta name="format-detection" content="telephone=yes">

  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{kw}">
  <meta name="author" content="CLAPS Individual Tuition (ClapsLearn)">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="{hreflang}" href="{canonical}">
  <link rel="alternate" hreflang="{alt_lang}" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:locale" content="en_IN">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta property="og:image:width" content="800">
  <meta property="og:image:height" content="800">
  <meta property="og:image:alt" content="CLAPS Individual Tuition — one teacher, one student online classes">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{OG_IMAGE}">
  <meta name="twitter:image:alt" content="CLAPS Individual Tuition — one-to-one online tuition">

  <link href="{asset_prefix}assets/img/favviconn.png" rel="icon">
  <link href="{asset_prefix}assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Malayalam:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">"""


def robots_txt() -> str:
    return f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /cgi-bin/
Disallow: /awstats/
Disallow: /stats/

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: {BASE}/sitemap.xml
"""
