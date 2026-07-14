#!/usr/bin/env python3
"""
pSEO generator for individualtuition.in
Generates combinatorial landing pages:
  - city × subject
  - city × class
  - subject × syllabus
  - class × syllabus
"""

import os
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public_html"
BASE = "https://individualtuition.in"
WA   = "https://wa.me/918610416147?text=Hi%20%2C%20how%20can%20we%20join%20CLAPS%3F"
GA   = "G-0WRLE4YHZW"

# ── DATA ─────────────────────────────────────────────────────────────────────

CITIES = [
    # Kerala cities
    {"key": "kochi",        "name": "Kochi",        "also": "Ernakulam",           "state": "Kerala",      "blurb": "Kochi (Ernakulam) is Kerala's commercial hub. Students follow CBSE, Kerala State, and ICSE boards in a fast-paced urban environment."},
    {"key": "trivandrum",   "name": "Trivandrum",   "also": "Thiruvananthapuram",   "state": "Kerala",      "blurb": "Trivandrum is Kerala's capital with a strong culture of academic excellence. Students compete for top ranks in SSLC, Plus Two, and entrance exams."},
    {"key": "kozhikode",    "name": "Kozhikode",    "also": "Calicut",              "state": "Kerala",      "blurb": "Kozhikode (Calicut) is a major education centre in North Kerala with a mix of Kerala State, CBSE, and ICSE schools."},
    {"key": "thrissur",     "name": "Thrissur",     "also": "the cultural capital of Kerala", "state": "Kerala", "blurb": "Thrissur is the cultural and educational heart of central Kerala, with many high-performing students targeting SSLC distinction and Plus Two entrance exams."},
    {"key": "kannur",       "name": "Kannur",       "also": "Cannanore",            "state": "Kerala",      "blurb": "Kannur in North Kerala has a strong tradition of education. Many Kannur families have NRI connections, making flexible online tuition especially popular."},
    {"key": "kollam",       "name": "Kollam",       "also": "Quilon",               "state": "Kerala",      "blurb": "Kollam is a major city in South Kerala. Students follow Kerala State and CBSE syllabuses and benefit from one-to-one coaching for board exams."},
    {"key": "palakkad",     "name": "Palakkad",     "also": "Palghat",              "state": "Kerala",      "blurb": "Palakkad is a significant educational district in Kerala, with students from both Kerala State and CBSE schools seeking focused individual coaching."},
    {"key": "malappuram",   "name": "Malappuram",   "also": "Tirur region",         "state": "Kerala",      "blurb": "Malappuram has one of the highest student populations in Kerala. Many families have Gulf NRI connections, making online tuition a natural fit."},
    {"key": "kottayam",     "name": "Kottayam",     "also": "the land of letters",  "state": "Kerala",      "blurb": "Kottayam is known as the land of letters, latex, and lakes. The district has exceptionally high literacy and academic aspiration among students."},
    {"key": "alappuzha",    "name": "Alappuzha",    "also": "Alleppey",             "state": "Kerala",      "blurb": "Alappuzha students follow Kerala State and CBSE boards. Individual tuition helps bridge gaps during the critical secondary and higher secondary years."},
    {"key": "pathanamthitta", "name": "Pathanamthitta", "also": "Konni region",     "state": "Kerala",      "blurb": "Pathanamthitta has a strong NRI presence and high educational aspirations. Online individual tuition fits the lifestyle of families with Gulf connections."},
    {"key": "ernakulam",    "name": "Ernakulam",    "also": "Greater Kochi",        "state": "Kerala",      "blurb": "Ernakulam district (Greater Kochi area) has a dense concentration of CBSE and ICSE schools alongside Kerala State institutions."},
    {"key": "kasaragod",    "name": "Kasaragod",    "also": "North Kerala",         "state": "Kerala",      "blurb": "Kasaragod is the northernmost district of Kerala with a multilingual population. Students follow Kerala State, CBSE and Kannada medium boards."},
    # Indian metros
    {"key": "bangalore",    "name": "Bangalore",    "also": "Bengaluru",            "state": "Karnataka",   "blurb": "Bangalore's competitive school environment means students need focused individual coaching to keep pace with CBSE board exams and entrance preparation."},
    {"key": "chennai",      "name": "Chennai",      "also": "Madras",               "state": "Tamil Nadu",  "blurb": "Chennai has a large Malayali community and strong CBSE school presence. Individual tuition is popular for board exam preparation and subject mastery."},
    {"key": "hyderabad",    "name": "Hyderabad",    "also": "Cyberabad",            "state": "Telangana",   "blurb": "Hyderabad's tech-savvy families embrace online individual tuition for CBSE students preparing for board exams and JEE/NEET foundations."},
    {"key": "mumbai",       "name": "Mumbai",       "also": "Bombay",               "state": "Maharashtra", "blurb": "Mumbai families demand flexible, high-quality online tuition. CBSE and ICSE both popular. Individual coaching helps students stand out in India's most competitive city."},
    {"key": "delhi",        "name": "Delhi",        "also": "New Delhi",            "state": "Delhi NCR",   "blurb": "Delhi NCR has India's highest concentration of CBSE schools. Individual tuition for board exams and JEE/NEET foundation is in strong demand."},
    {"key": "pune",         "name": "Pune",         "also": "Poona",                "state": "Maharashtra", "blurb": "Pune's growing student population and tech-sector families drive demand for quality online individual tuition for CBSE and ICSE board preparation."},
    # NRI / Gulf
    {"key": "dubai",        "name": "Dubai",        "also": "the UAE",              "state": "UAE",         "blurb": "Dubai has a large Indian expat community following CBSE and ICSE through Indian schools. Flexible Gulf-timezone online classes are in high demand."},
    {"key": "abu-dhabi",    "name": "Abu Dhabi",    "also": "the UAE capital",      "state": "UAE",         "blurb": "Abu Dhabi's Indian community follows CBSE through Indian schools. Online individual tuition with Gulf-evening slots is ideal for working expat families."},
    {"key": "saudi-arabia", "name": "Saudi Arabia", "also": "the Kingdom",          "state": "Saudi Arabia","blurb": "Saudi Arabia has a large Malayali and Indian community across Riyadh, Jeddah, and Dammam. CBSE and Kerala State both followed. Gulf time zone slots available."},
    {"key": "qatar",        "name": "Qatar",        "also": "Doha",                 "state": "Qatar",       "blurb": "Qatar's Indian community in Doha and surrounding areas follows CBSE and Kerala State. Flexible Gulf time zone scheduling makes online tuition very convenient."},
    {"key": "kuwait",       "name": "Kuwait",       "also": "Kuwait City",          "state": "Kuwait",      "blurb": "Kuwait has a large Indian and Malayali expat community. CBSE curriculum is common and Gulf-evening online tuition slots align perfectly with school schedules."},
    {"key": "uk",           "name": "UK",           "also": "United Kingdom",       "state": "UK",          "blurb": "The UK has a large Indian diaspora community. Many families seek Indian syllabus tutors for children who attend Indian curriculum schools or are relocating."},
]

SUBJECTS = [
    {"key": "maths",           "name": "Maths",           "full": "Mathematics",          "blurb": "Mathematics is the subject where individual attention matters most — gaps in one chapter directly cause struggles in the next."},
    {"key": "physics",         "name": "Physics",         "full": "Physics",              "blurb": "Physics demands understanding of both theory and numericals. One-to-one tuition lets the teacher diagnose exactly where a student is stuck."},
    {"key": "chemistry",       "name": "Chemistry",       "full": "Chemistry",            "blurb": "Chemistry combines equations, reactions, and organic concepts that benefit hugely from personalised explanation and frequent Q&A."},
    {"key": "biology",         "name": "Biology",         "full": "Biology",              "blurb": "Biology requires diagram mastery, long-answer technique, and NEET-oriented practice that individual tuition tailors perfectly."},
    {"key": "english",         "name": "English",         "full": "English",              "blurb": "English tuition covers grammar, writing, comprehension, and literature — paced to each student's current level and board requirements."},
    {"key": "science",         "name": "Science",         "full": "Science",              "blurb": "Integrated Science (Classes 6–10) covers Physics, Chemistry, and Biology concepts best reinforced through focused individual sessions."},
    {"key": "social-science",  "name": "Social Science",  "full": "Social Science",       "blurb": "Social Science spans History, Geography, Civics, and Economics — subjects where essay technique and map skills need personal guidance."},
    {"key": "accountancy",     "name": "Accountancy",     "full": "Accountancy",          "blurb": "Accountancy in Class 11–12 Commerce requires step-by-step journal and ledger practice best delivered in one-to-one sessions."},
    {"key": "hindi",           "name": "Hindi",           "full": "Hindi",                "blurb": "Hindi as a second language needs focused grammar, essay, and comprehension practice — especially for South Indian students unfamiliar with the script and vocabulary."},
    {"key": "malayalam",       "name": "Malayalam",       "full": "Malayalam",            "blurb": "Malayalam as a subject requires board-specific answer writing, grammar, and literature text study that one-to-one tuition can tailor exactly."},
    {"key": "computer-science","name": "Computer Science","full": "Computer Science",     "blurb": "Computer Science covers Python, data structures, algorithms, and board practicals — all of which benefit from individual coding guidance and debugging sessions."},
    {"key": "economics",       "name": "Economics",       "full": "Economics",            "blurb": "Economics in Class 11–12 requires understanding of macro and micro theory, graphs, and data interpretation — areas where individual tutoring builds exam confidence."},
    {"key": "business-studies","name": "Business Studies","full": "Business Studies",     "blurb": "Business Studies for Class 11–12 Commerce involves case studies, definitions, and structured long answers that individual tuition coaches step by step."},
    {"key": "commerce",        "name": "Commerce",        "full": "Commerce",             "blurb": "Commerce stream tuition (Accountancy, Business Studies, Economics) is best done with one dedicated teacher who can move between subjects as exam needs demand."},
]

CLASSES = [
    {"key": "kg",        "name": "KG",              "level": "kindergarten",        "blurb": "KG (LKG/UKG) is the foundation year. Individual tuition builds phonics, number sense, and school readiness through short, playful sessions with patient teachers."},
    {"key": "class-1",   "name": "Class 1",         "level": "primary",             "blurb": "Class 1 sets the academic foundation. One-to-one tuition ensures reading, writing, and arithmetic are mastered before gaps can form."},
    {"key": "class-2",   "name": "Class 2",         "level": "primary",             "blurb": "Class 2 builds on primary fundamentals. Individual tuition catches any gaps early and keeps pace with school curriculum across Maths, English, and languages."},
    {"key": "class-3",   "name": "Class 3",         "level": "primary",             "blurb": "Class 3 introduces more complex reading, multiplication, and basic Science. One-to-one coaching ensures no chapter is skipped or misunderstood."},
    {"key": "class-4",   "name": "Class 4",         "level": "primary",             "blurb": "Class 4 is a busy year with more subjects and longer answers. Individual tuition helps students keep pace and build writing fluency."},
    {"key": "class-5",   "name": "Class 5",         "level": "upper primary",       "blurb": "Class 5 bridges primary and middle school. Strong foundations in Maths and English here prevent struggles in Classes 6–8."},
    {"key": "class-6",   "name": "Class 6",         "level": "middle school",       "blurb": "Class 6 introduces specialised subjects — Science, Social Science, and advanced Maths. Individual tuition helps students adapt to the higher workload."},
    {"key": "class-7",   "name": "Class 7",         "level": "middle school",       "blurb": "Class 7 deepens abstract thinking in Maths and Science. One-to-one tuition addresses specific chapter gaps before they compound in Class 8–9."},
    {"key": "class-8",   "name": "Class 8",         "level": "middle school",       "blurb": "Class 8 is a critical transition year where Maths, Science, and Social Science become more abstract. Early individual support prevents board-year crises."},
    {"key": "class-9",   "name": "Class 9",         "level": "secondary",           "blurb": "Class 9 introduces board-pattern topics. One-to-one tuition builds the exam skills students need for Class 10."},
    {"key": "class-10",  "name": "Class 10",        "level": "board year",          "blurb": "Class 10 is a milestone board year. Individual tuition gives focused chapter-wise revision and mock-test practice."},
    {"key": "class-11",  "name": "Class 11 (Plus One)", "level": "higher secondary","blurb": "Class 11 (Plus One) is the most challenging transition in school — new advanced topics in Science and Commerce need individual support from day one."},
    {"key": "class-12",  "name": "Class 12 (Plus Two)", "level": "board + entrance year", "blurb": "Class 12 (Plus Two) is the culmination of school — board exams and entrance exam foundations both require dedicated one-to-one coaching."},
]

SYLLABUSES = [
    {"key": "cbse",         "name": "CBSE",         "full": "Central Board of Secondary Education",  "blurb": "CBSE is India's most widely followed board, with NCERT textbooks forming the foundation. Students benefit from individual tuition aligned to NCERT chapters and board exam patterns."},
    {"key": "kerala-state", "name": "Kerala State", "full": "Kerala State (SCERT)", "slug_word": "kerala-state", "blurb": "Kerala State syllabus (SCERT) has its own textbook sequence and SSLC/Plus Two exam patterns. Individual tuition follows this board's unique chapter flow."},
    {"key": "icse",         "name": "ICSE",         "full": "Indian Certificate of Secondary Education", "blurb": "ICSE's detailed and literature-heavy syllabus benefits greatly from one-to-one teaching that can cover the extra depth required per subject."},
    {"key": "isc",          "name": "ISC",          "full": "Indian School Certificate (Class 11–12)", "blurb": "ISC (Class 11–12) is the senior secondary level of the ICSE board, with a rigorous subject depth that benefits significantly from individual one-to-one coaching."},
]

# Approximate geo coords per city key (lat, lon)
GEO_COORDS = {
    "kochi":         (9.9312,  76.2673),
    "trivandrum":    (8.5241,  76.9366),
    "kozhikode":     (11.2588, 75.7804),
    "thrissur":      (10.5276, 76.2144),
    "kannur":        (11.8745, 75.3704),
    "kollam":        (8.8932,  76.6141),
    "palakkad":      (10.7867, 76.6548),
    "malappuram":    (11.0510, 76.0711),
    "kottayam":      (9.5916,  76.5222),
    "alappuzha":     (9.4981,  76.3388),
    "pathanamthitta":(9.2648,  76.7870),
    "ernakulam":     (9.9816,  76.2999),
    "kasaragod":     (12.4996, 74.9869),
    "bangalore":     (12.9716, 77.5946),
    "chennai":       (13.0827, 80.2707),
    "hyderabad":     (17.3850, 78.4867),
    "mumbai":        (19.0760, 72.8777),
    "delhi":         (28.6139, 77.2090),
    "pune":          (18.5204, 73.8567),
    "dubai":         (25.2048, 55.2708),
    "abu-dhabi":     (24.4539, 54.3773),
    "saudi-arabia":  (23.8859, 45.0792),
    "qatar":         (25.3548, 51.1839),
    "kuwait":        (29.3759, 47.9774),
    "uk":            (51.5074, -0.1278),
}

# ── HTML HELPERS ──────────────────────────────────────────────────────────────

NAV_ITEMS = [
    ("Home", "../index.html"),
    ("Online Tuition", "../individual-tuition-online/index.html"),
    ("Research", "../research-individual-tuition/index.html"),
    ("Syllabuses", "../syllabuses/index.html"),
    ("Classes", "../classes/index.html"),
    ("FAQ", "../faq/index.html"),
    ("About", "../about/index.html"),
]

WA_SVG = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'


def nav_html():
    items = "\n".join(f'    <li><a href="{url}">{label}</a></li>' for label, url in NAV_ITEMS)
    return f"""<nav class="topbar__nav" id="site-nav" aria-label="Main">
    <ul class="topbar__nav-list">
{items}
    </ul></nav>"""


def schema_json(slug, title, description, breadcrumb_name, city_name="Kerala", geo_lat=10.8505, geo_lon=76.2711):
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "EducationalOrganization",
            "name": "CLAPS Individual Tuition",
            "url": BASE,
            "parentOrganization": {"@type": "Organization", "name": "ClapsLearn", "url": "https://clapslearn.com"},
            "description": "One-to-one online individual tuition KG to Plus Two",
            "telephone": "+91-86104-16147",
            "areaServed": ["IN", "AE", "SA", "QA", "US", "GB"],
            "sameAs": ["https://clapslearn.com"],
        },
        {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "CLAPS Individual Tuition",
            "description": description,
            "url": f"{BASE}/{slug}/",
            "telephone": "+91-86104-16147",
            "image": f"{BASE}/assets/img/new-img.png",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": city_name,
                "addressCountry": "IN",
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": geo_lat,
                "longitude": geo_lon,
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "reviewCount": "1000",
                "bestRating": "5",
            },
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": breadcrumb_name, "item": f"{BASE}/{slug}/"},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Is CLAPS online or does a tutor come home?",
                    "acceptedAnswer": {"@type": "Answer", "text": "CLAPS is fully online — live one-to-one video classes from your home. No travel required."},
                },
                {
                    "@type": "Question",
                    "name": "Which syllabuses do you teach?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Kerala State (SCERT), CBSE, ICSE, and ISC from KG through Plus Two (+2)."},
                },
                {
                    "@type": "Question",
                    "name": "Can I pick just one subject?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Yes — choose any individual subject or a combination. Pay only for what you need."},
                },
                {
                    "@type": "Question",
                    "name": "What timings are available?",
                    "acceptedAnswer": {"@type": "Answer", "text": "Flexible slots after school (4 PM–9 PM IST), weekends, and Gulf-friendly timings for NRI families."},
                },
            ],
        },
    ]
    return json.dumps(schema, ensure_ascii=False)


def faq_html():
    return """<div class="content-block"><h2>Common questions</h2>
<details class="faq-item"><summary>Is CLAPS online or does a tutor come home?</summary><div class="faq-item__body"><p>CLAPS is fully online — live one-to-one video classes from your home. No travel required.</p></div></details>
<details class="faq-item"><summary>Which syllabuses do you teach?</summary><div class="faq-item__body"><p>Kerala State (SCERT), CBSE, ICSE, and ISC from KG through Plus Two (+2).</p></div></details>
<details class="faq-item"><summary>Can I pick just one subject?</summary><div class="faq-item__body"><p>Yes — choose any subject individually. Pay only for what you need.</p></div></details>
<details class="faq-item"><summary>What timings are available?</summary><div class="faq-item__body"><p>Flexible after-school slots (4 PM–9 PM IST), weekends, and Gulf-friendly timings for NRI families.</p></div></details>
</div>"""


def cta_band():
    return f"""<section class="cta-band">
      <h2>Start individual tuition today</h2>
      <p>Message us on WhatsApp — we'll match an expert teacher for your child's class and syllabus.</p>
      <a class="btn btn--wa" href="{WA}">{WA_SVG} WhatsApp — Join CLAPS</a>
    </section>"""


def build_page(*, slug, title, description, h1, lede, cite, sections, related, breadcrumb_name,
               city_key="", city_display="Kerala"):
    """Render a complete HTML page string."""
    canonical = f"{BASE}/{slug}/"
    geo_lat, geo_lon = GEO_COORDS.get(city_key, (10.8505, 76.2711))

    # head
    head = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{GA}');
  </script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#ffffff">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="format-detection" content="telephone=yes">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="individual tuition, CLAPS, ClapsLearn, online tuition, one to one tuition, {h1.lower()}">
  <meta name="author" content="CLAPS Individual Tuition (ClapsLearn)">
  <meta name="dateModified" content="2026-07-15">
  <meta name="geo.region" content="IN-KL">
  <meta name="geo.placename" content="{city_display}, India">
  <meta name="geo.position" content="{geo_lat};{geo_lon}">
  <meta name="ICBM" content="{geo_lat}, {geo_lon}">
  <link rel="alternate" type="text/plain" href="{BASE}/llms.txt" title="LLM-readable site summary">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{canonical}">
  <link rel="alternate" hreflang="ml" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CLAPS Individual Tuition">
  <meta property="og:locale" content="en_IN">
  <meta property="og:locale:alternate" content="ml_IN">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{BASE}/assets/img/new-img.png">
  <meta property="og:image:width" content="800">
  <meta property="og:image:height" content="800">
  <meta property="og:image:alt" content="CLAPS Individual Tuition — one teacher, one student online classes">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{BASE}/assets/img/new-img.png">
  <meta name="twitter:image:alt" content="CLAPS Individual Tuition — one-to-one online tuition">
  <link href="../assets/img/favviconn.png" rel="icon">
  <link href="../assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Malayalam:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link href="../assets/css/style.css" rel="stylesheet">
  <link href="../assets/css/footer.css" rel="stylesheet">
  <script type="application/ld+json">{schema_json(slug, title, description, breadcrumb_name, city_display, geo_lat, geo_lon)}</script>
</head>"""

    # nav
    nav = nav_html()

    # related links
    related_items = "\n".join(
        f'<li><a href="../{r["slug"]}/index.html">{r["label"]}<span>{r["sub"]}</span></a></li>'
        for r in related
    )

    # section blocks
    section_blocks = "\n".join(
        f'<section class="content-block"><h2>{s["heading"]}</h2>{s["body"]}</section>'
        for s in sections
    )

    # footer (minimal — links to main assets)
    footer = f"""<footer class="site-footer" id="site-footer">
    <div class="site-footer__inner">
      <div class="site-footer__brand site-footer__block">
        <a class="site-footer__logo-link" href="../index.html">
          <img src="../assets/img/Asset 5.png" alt="CLAPS Individual Tuition" class="site-footer__logo" width="439" height="242" loading="lazy" decoding="async">
        </a>
        <p class="site-footer__tagline">One-to-one online individual tuition from KG to Plus Two — CBSE, Kerala State &amp; ICSE.</p>
        <p class="site-footer__badge"><span class="site-footer__stars" aria-hidden="true">★★★★★</span> <span>4.9/5 on Google · 1,000+ reviews</span></p>
      </div>
      <section class="site-footer__contact-block site-footer__block" aria-labelledby="footer-contact-heading">
        <h2 class="site-footer__heading" id="footer-contact-heading">Contact</h2>
        <p>WhatsApp: <a href="{WA}">+91 86104 16147</a></p>
        <p>Parent company: <a href="https://clapslearn.com" rel="noopener">ClapsLearn</a></p>
      </section>
      <nav class="site-footer__nav site-footer__block" aria-label="Footer">
        <h2 class="site-footer__heading">Pages</h2>
        <ul>
          <li><a href="../individual-tuition-online/index.html">Online Tuition</a></li>
          <li><a href="../cbse-individual-tuition/index.html">CBSE Tuition</a></li>
          <li><a href="../kerala-state-syllabus-tuition/index.html">Kerala State Syllabus</a></li>
          <li><a href="../maths-individual-tuition/index.html">Maths Tuition</a></li>
          <li><a href="../class-10-individual-tuition/index.html">Class 10</a></li>
          <li><a href="../plus-two-individual-tuition/index.html">Plus Two</a></li>
          <li><a href="../nri-individual-tuition/index.html">NRI Tuition</a></li>
          <li><a href="../faq/index.html">FAQ</a></li>
          <li><a href="../about/index.html">About</a></li>
        </ul>
      </nav>
    </div>
    <div class="site-footer__bottom">
      <p>&copy; 2026 CLAPS Individual Tuition · A <a href="https://clapslearn.com" rel="noopener">ClapsLearn</a> brand · <a href="../index.html">individualtuition.in</a></p>
    </div>
  </footer>"""

    return f"""{head}
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="topbar">
    <a class="topbar__brand" href="../index.html">
      <img src="../assets/img/Asset 5.png" alt="CLAPS Individual Tuition" class="topbar__logo" width="439" height="242">
    </a>
    <div class="topbar__actions">
      {nav}
      <button type="button" class="topbar__nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
      <a class="topbar__wa" href="{WA}" aria-label="Chat on WhatsApp">{WA_SVG}</a>
    </div>
  </header>
  <main id="main" class="page content-page">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <ol><li><a href="../index.html">Home</a></li><li aria-current="page">{breadcrumb_name}</li></ol>
    </nav>
    <header class="page-hero">
      <h1 class="page-hero__title">{h1}</h1>
      <p class="page-hero__lede">{lede}</p>
    </header>
    <aside class="cite-box" role="note"><p>{cite}</p></aside>
{section_blocks}
{faq_html()}
    <section class="content-block"><h2>Related pages</h2>
      <ul class="link-grid">{related_items}</ul>
    </section>
    {cta_band()}
  </main>
  {footer}
  <script src="../assets/js/main.js"></script>
  <script src="../assets/js/footer.js"></script>
</body>
</html>"""


# ── PAGE RECORD BUILDERS ──────────────────────────────────────────────────────

def city_subject_page(city, subject):
    """e.g. maths-individual-tuition-kochi"""
    slug = f"{subject['key']}-individual-tuition-{city['key']}"
    h1  = f"{subject['name']} Individual Tuition in {city['name']}"
    title = f"{subject['name']} Individual Tuition {city['name']} | One-to-One Online | CLAPS"
    desc  = (
        f"Individual {subject['name'].lower()} tuition in {city['name']} — one-to-one online classes, "
        f"CBSE, Kerala State & ICSE. KG to +2. Expert teachers. WhatsApp to join CLAPS."
    )
    lede = (
        f"Dedicated one-to-one {subject['name']} tuition for {city['name']} students — "
        f"online, flexible timings, expert subject teachers from KG to Plus Two."
    )
    cite = (
        f"CLAPS provides online individual {subject['name']} tuition to students in {city['name']} "
        f"({city['also']}) with one teacher per student for all syllabuses and classes."
    )
    sections = [
        {
            "heading": f"{subject['name']} tuition for {city['name']} students",
            "body": (
                f"<p>{city['blurb']} {subject['blurb']}</p>"
                f"<p>CLAPS Individual Tuition connects {city['name']} students with dedicated "
                f"{subject['name']} teachers — fully online, one-to-one, and scheduled around school hours.</p>"
            ),
        },
        {
            "heading": "What we cover",
            "body": (
                "<ul>"
                f"<li>Primary {subject['name']} (Classes 1–5) — foundations and confidence</li>"
                f"<li>Middle school {subject['name']} (Classes 6–8) — concept deepening</li>"
                f"<li>Class 9–10 {subject['name']} — board exam preparation</li>"
                f"<li>Plus One & Plus Two {subject['name']} — senior secondary mastery</li>"
                "</ul>"
            ),
        },
        {
            "heading": "Why individual tuition works for " + subject['name'],
            "body": (
                f"<p>{subject['blurb']} A CLAPS teacher identifies the exact gap, rebuilds understanding, "
                f"and practises exam patterns — all in a private session at your child's pace.</p>"
                f"<p><a href=\"../research-individual-tuition/index.html\">See the research on one-to-one tutoring →</a></p>"
            ),
        },
        {
            "heading": "Syllabuses available",
            "body": (
                "<ul>"
                "<li><strong>CBSE / NCERT</strong> — board-aligned chapter coverage</li>"
                "<li><strong>Kerala State (SCERT)</strong> — exam pattern and textbook sequence</li>"
                "<li><strong>ICSE / ISC</strong> — detailed and application-based approach</li>"
                "</ul>"
            ),
        },
    ]
    related = [
        {"slug": f"{subject['key']}-individual-tuition", "label": f"{subject['name']} Tuition", "sub": "All locations"},
        {"slug": f"individual-tuition-{city['key']}", "label": f"Individual Tuition {city['name']}", "sub": "All subjects"},
        {"slug": "individual-tuition-online", "label": "Online Tuition", "sub": "How classes work"},
        {"slug": "research-individual-tuition", "label": "Research", "sub": "Evidence base"},
    ]
    return dict(slug=slug, title=title, description=desc, h1=h1, lede=lede,
                cite=cite, sections=sections, related=related, breadcrumb_name=h1, city_key=city['key'], city_display=city['name'])


def city_class_page(city, cls):
    """e.g. class-10-individual-tuition-kochi"""
    slug = f"{cls['key']}-individual-tuition-{city['key']}"
    h1   = f"{cls['name']} Individual Tuition in {city['name']}"
    title = f"{cls['name']} Individual Tuition {city['name']} | One-to-One Online | CLAPS"
    desc  = (
        f"Individual tuition for {cls['name']} students in {city['name']} — one-to-one online, "
        f"CBSE, Kerala State & ICSE. All subjects. WhatsApp to join CLAPS."
    )
    lede = (
        f"One-to-one {cls['name']} tuition for {city['name']} students — online, flexible timings, "
        f"covering all major subjects for {cls['level']} learners."
    )
    cite = (
        f"CLAPS provides {cls['name']} individual online tuition to students in {city['name']} "
        f"({city['also']}) with dedicated subject teachers across all boards."
    )
    sections = [
        {
            "heading": f"{cls['name']} tuition for {city['name']} students",
            "body": (
                f"<p>{city['blurb']}</p>"
                f"<p>{cls['blurb']}</p>"
                f"<p>CLAPS matches {city['name']} students in {cls['name']} with expert subject teachers "
                f"for focused one-to-one online sessions.</p>"
            ),
        },
        {
            "heading": "Subjects available",
            "body": (
                "<ul>"
                "<li>Mathematics — algebra, geometry, and board-exam problem sets</li>"
                "<li>Science — Physics, Chemistry, Biology (integrated or split)</li>"
                "<li>English — grammar, writing, literature</li>"
                "<li>Social Science / Humanities</li>"
                "<li>Second languages — Malayalam, Hindi, and others</li>"
                "</ul>"
            ),
        },
        {
            "heading": "Syllabuses",
            "body": (
                "<ul>"
                "<li><strong>CBSE</strong> — NCERT-aligned, board-pattern focus</li>"
                "<li><strong>Kerala State (SCERT)</strong> — Kerala textbook sequence and SSLC/Plus Two exams</li>"
                "<li><strong>ICSE / ISC</strong> — detailed curriculum support</li>"
                "</ul>"
            ),
        },
        {
            "heading": "How it works",
            "body": (
                "<p>Message CLAPS on WhatsApp with your child's class and subject needs. "
                "We assign a dedicated teacher, confirm a timeslot, and classes begin on video. "
                "Academic coordinators are available 10 AM – 10 PM for any questions.</p>"
            ),
        },
    ]
    related = [
        {"slug": f"{cls['key']}-individual-tuition", "label": f"{cls['name']} Tuition", "sub": "All locations"},
        {"slug": f"individual-tuition-{city['key']}", "label": f"Individual Tuition {city['name']}", "sub": "All classes"},
        {"slug": "individual-tuition-online", "label": "Online Tuition", "sub": "How it works"},
        {"slug": "faq", "label": "FAQ", "sub": "Common questions"},
    ]
    return dict(slug=slug, title=title, description=desc, h1=h1, lede=lede,
                cite=cite, sections=sections, related=related, breadcrumb_name=h1, city_key=city['key'], city_display=city['name'])


def subject_syllabus_page(subject, syllabus):
    """e.g. maths-individual-tuition-cbse"""
    syl_key = syllabus.get("slug_word", syllabus["key"])
    slug = f"{subject['key']}-individual-tuition-{syl_key}"
    h1   = f"{subject['name']} Individual Tuition — {syllabus['name']} Syllabus"
    title = f"{subject['name']} {syllabus['name']} Individual Tuition | One-to-One Online | CLAPS"
    desc  = (
        f"Individual {subject['name'].lower()} tuition for {syllabus['name']} students — one-to-one online, "
        f"KG to Plus Two. Expert {subject['name']} teachers. WhatsApp to join CLAPS."
    )
    lede = (
        f"Dedicated one-to-one {subject['name']} tuition aligned to the {syllabus['full']} — "
        f"covering the full syllabus from primary through Plus Two with expert teachers."
    )
    cite = (
        f"CLAPS offers {syllabus['name']} {subject['name']} individual tuition online, "
        f"following the board's textbook structure and exam patterns from KG through Class 12."
    )
    sections = [
        {
            "heading": f"{subject['name']} tuition for {syllabus['name']} students",
            "body": (
                f"<p>{syllabus['blurb']}</p>"
                f"<p>{subject['blurb']}</p>"
                f"<p>CLAPS teachers are selected for their expertise in the {syllabus['name']} board "
                f"and know exactly which {subject['name']} chapters need extra time at each level.</p>"
            ),
        },
        {
            "heading": "Classes covered",
            "body": (
                "<ul>"
                f"<li><strong>Primary (1–5):</strong> {subject['name']} foundations for {syllabus['name']}</li>"
                f"<li><strong>Middle school (6–8):</strong> concept depth per {syllabus['name']} chapters</li>"
                f"<li><strong>Class 9–10:</strong> {syllabus['name']} board exam preparation</li>"
                f"<li><strong>Plus One & Plus Two:</strong> advanced {subject['name']} for {syllabus['name']}</li>"
                "</ul>"
            ),
        },
        {
            "heading": "Why one-to-one works best",
            "body": (
                f"<p>{subject['blurb']} Individual tuition lets the teacher spend every minute on "
                f"your child's exact chapters and weaknesses — not a batch average.</p>"
                f"<p><a href=\"../research-individual-tuition/index.html\">Read the research evidence →</a></p>"
            ),
        },
    ]
    related = [
        {"slug": f"{subject['key']}-individual-tuition", "label": f"{subject['name']} Tuition", "sub": "All syllabuses"},
        {"slug": f"{syl_key}-individual-tuition", "label": f"{syllabus['name']} Tuition", "sub": "All subjects"},
        {"slug": "individual-tuition-online", "label": "Online Tuition", "sub": "How it works"},
        {"slug": "research-individual-tuition", "label": "Research", "sub": "Evidence base"},
    ]
    return dict(slug=slug, title=title, description=desc, h1=h1, lede=lede,
                cite=cite, sections=sections, related=related, breadcrumb_name=h1, city_key='', city_display='India')


def class_syllabus_page(cls, syllabus):
    """e.g. class-10-individual-tuition-cbse"""
    syl_key = syllabus.get("slug_word", syllabus["key"])
    slug = f"{cls['key']}-individual-tuition-{syl_key}"
    h1   = f"{cls['name']} Individual Tuition — {syllabus['name']}"
    title = f"{cls['name']} {syllabus['name']} Individual Tuition | One-to-One Online | CLAPS"
    desc  = (
        f"Individual tuition for {cls['name']} {syllabus['name']} students — one-to-one online, "
        f"all subjects. Expert teachers. WhatsApp to join CLAPS."
    )
    lede = (
        f"One-to-one {cls['name']} tuition tailored to the {syllabus['full']} — "
        f"covering all subjects with dedicated teachers and flexible online scheduling."
    )
    cite = (
        f"CLAPS provides {cls['name']} individual tuition for {syllabus['name']} students online, "
        f"with board-aligned lesson plans and one teacher per student."
    )
    sections = [
        {
            "heading": f"{cls['name']} {syllabus['name']} — why individual tuition helps",
            "body": (
                f"<p>{cls['blurb']}</p>"
                f"<p>{syllabus['blurb']}</p>"
                f"<p>CLAPS pairs your child with a teacher who knows the {syllabus['name']} {cls['name']} "
                f"syllabus in depth — covering chapters at your child's pace, not a fixed batch schedule.</p>"
            ),
        },
        {
            "heading": "Subjects available",
            "body": (
                "<ul>"
                "<li>Mathematics — chapter-wise coverage and problem practice</li>"
                "<li>Science — Physics, Chemistry, Biology (individual or combined)</li>"
                "<li>English — language, grammar, and literature</li>"
                "<li>Social Science / Humanities</li>"
                "<li>Languages — Malayalam, Hindi, and others</li>"
                "</ul>"
            ),
        },
        {
            "heading": "How to enrol",
            "body": (
                "<p>WhatsApp CLAPS with your child's class, board, and subject requirements. "
                "We'll confirm a teacher and timeslot — classes start within days. "
                "Coordinators available 10 AM – 10 PM IST.</p>"
            ),
        },
    ]
    related = [
        {"slug": f"{cls['key']}-individual-tuition", "label": f"{cls['name']} Tuition", "sub": "All syllabuses"},
        {"slug": f"{syl_key}-individual-tuition", "label": f"{syllabus['name']} Tuition", "sub": "All classes"},
        {"slug": "individual-tuition-online", "label": "Online Tuition", "sub": "How it works"},
        {"slug": "faq", "label": "FAQ", "sub": "Common questions"},
    ]
    return dict(slug=slug, title=title, description=desc, h1=h1, lede=lede,
                cite=cite, sections=sections, related=related, breadcrumb_name=h1, city_key='', city_display='India')


# ── NEW PAGE BUILDERS ─────────────────────────────────────────────────────────

def city_syllabus_page(city, syllabus):
    """e.g. cbse-individual-tuition-kochi"""
    syl_key = syllabus.get("slug_word", syllabus["key"])
    slug = f"{syl_key}-individual-tuition-{city['key']}"
    h1   = f"{syllabus['name']} Individual Tuition in {city['name']}"
    title = f"{syllabus['name']} Individual Tuition {city['name']} | One-to-One Online | CLAPS"
    desc  = (
        f"Individual {syllabus['name']} tuition in {city['name']} — one-to-one online classes "
        f"KG to Plus Two, all subjects. Expert teachers. WhatsApp to join CLAPS."
    )
    lede = (
        f"One-to-one {syllabus['name']} tuition for {city['name']} students — "
        f"online, all subjects, all classes from KG to Plus Two."
    )
    cite = (
        f"CLAPS provides {syllabus['name']} individual tuition online to students in {city['name']} "
        f"({city['also']}) with dedicated teachers for every subject and class."
    )
    sections = [
        {
            "heading": f"{syllabus['name']} tuition for {city['name']} students",
            "body": (
                f"<p>{city['blurb']}</p>"
                f"<p>{syllabus['blurb']}</p>"
                f"<p>CLAPS Individual Tuition pairs {city['name']} students with specialist {syllabus['name']} "
                f"teachers — fully online, one-to-one, and scheduled around school hours.</p>"
            ),
        },
        {
            "heading": "Classes covered",
            "body": (
                "<ul>"
                f"<li>KG & Primary (Classes 1–5) — foundations aligned to {syllabus['name']}</li>"
                f"<li>Middle school (Classes 6–8) — deepening {syllabus['name']} chapter coverage</li>"
                f"<li>Secondary (Classes 9–10) — board exam preparation</li>"
                f"<li>Higher secondary (Plus One & Plus Two) — advanced {syllabus['name']} subjects</li>"
                "</ul>"
            ),
        },
        {
            "heading": "Subjects available",
            "body": (
                "<ul>"
                "<li>Maths, Physics, Chemistry, Biology, Science</li>"
                "<li>English, Hindi, Malayalam, Social Science</li>"
                "<li>Accountancy, Economics, Business Studies, Computer Science</li>"
                "</ul>"
            ),
        },
    ]
    related = [
        {"slug": f"{syl_key}-individual-tuition", "label": f"{syllabus['name']} Tuition", "sub": "All locations"},
        {"slug": f"individual-tuition-{city['key']}", "label": f"Tuition in {city['name']}", "sub": "All syllabuses"},
        {"slug": "individual-tuition-online", "label": "Online Tuition", "sub": "How it works"},
        {"slug": "faq", "label": "FAQ", "sub": "Common questions"},
    ]
    return dict(slug=slug, title=title, description=desc, h1=h1, lede=lede,
                cite=cite, sections=sections, related=related, breadcrumb_name=h1, city_key=city['key'], city_display=city['name'])


def subject_class_page(subject, cls):
    """e.g. maths-individual-tuition-class-10"""
    slug = f"{subject['key']}-individual-tuition-{cls['key']}"
    h1   = f"{subject['name']} Individual Tuition for {cls['name']}"
    title = f"{subject['name']} Individual Tuition {cls['name']} | One-to-One Online | CLAPS"
    desc  = (
        f"Individual {subject['name'].lower()} tuition for {cls['name']} students — one-to-one online, "
        f"CBSE, Kerala State & ICSE. Expert teachers. WhatsApp to join CLAPS."
    )
    lede = (
        f"Focused one-to-one {subject['name']} tuition for {cls['name']} — "
        f"online, all syllabuses, taught by subject experts at your child's pace."
    )
    cite = (
        f"CLAPS provides {cls['name']} {subject['name']} individual tuition online, "
        f"covering CBSE, Kerala State, and ICSE syllabuses with one teacher per student."
    )
    sections = [
        {
            "heading": f"{subject['name']} tuition for {cls['name']}",
            "body": (
                f"<p>{cls['blurb']}</p>"
                f"<p>{subject['blurb']}</p>"
                f"<p>CLAPS pairs {cls['name']} students with a dedicated {subject['name']} teacher "
                f"for private online sessions — board-aligned and paced to your child's needs.</p>"
            ),
        },
        {
            "heading": "What is covered",
            "body": (
                f"<ul>"
                f"<li><strong>CBSE:</strong> Full NCERT {subject['name']} chapter coverage for {cls['name']}</li>"
                f"<li><strong>Kerala State:</strong> SCERT {subject['name']} syllabus for {cls['name']}</li>"
                f"<li><strong>ICSE / ISC:</strong> Detailed {subject['name']} for {cls['name']}</li>"
                f"<li>Past paper practice, mock tests, and exam technique</li>"
                "</ul>"
            ),
        },
        {
            "heading": "Why individual tuition for " + subject['name'],
            "body": (
                f"<p>{subject['blurb']} At {cls['level']} level, focused one-to-one sessions mean "
                f"every doubt is resolved immediately and exam preparation is targeted precisely.</p>"
                f"<p><a href=\"../research-individual-tuition/index.html\">See the research on one-to-one tutoring →</a></p>"
            ),
        },
    ]
    related = [
        {"slug": f"{subject['key']}-individual-tuition", "label": f"{subject['name']} Tuition", "sub": "All classes"},
        {"slug": f"{cls['key']}-individual-tuition", "label": f"{cls['name']} Tuition", "sub": "All subjects"},
        {"slug": "individual-tuition-online", "label": "Online Tuition", "sub": "How it works"},
        {"slug": "research-individual-tuition", "label": "Research", "sub": "Evidence base"},
    ]
    return dict(slug=slug, title=title, description=desc, h1=h1, lede=lede,
                cite=cite, sections=sections, related=related, breadcrumb_name=h1, city_key='', city_display='India')


def city_subject_class_page(city, subject, cls):
    """e.g. maths-individual-tuition-class-10-kochi"""
    slug = f"{subject['key']}-individual-tuition-{cls['key']}-{city['key']}"
    h1   = f"{subject['name']} Individual Tuition — {cls['name']} in {city['name']}"
    title = f"{subject['name']} {cls['name']} Individual Tuition {city['name']} | CLAPS"
    desc  = (
        f"Individual {subject['name'].lower()} tuition for {cls['name']} in {city['name']} — "
        f"one-to-one online, all boards. Expert teacher. WhatsApp to join CLAPS."
    )
    lede = (
        f"One dedicated {subject['name']} teacher for your {cls['name']} child in {city['name']} — "
        f"online, flexible timings, all syllabuses covered."
    )
    cite = (
        f"CLAPS provides {cls['name']} {subject['name']} individual tuition online to students "
        f"in {city['name']} ({city['also']}) with board-aligned one-to-one sessions."
    )
    sections = [
        {
            "heading": f"{subject['name']} tuition for {cls['name']} in {city['name']}",
            "body": (
                f"<p>{city['blurb']}</p>"
                f"<p>{cls['blurb']}</p>"
                f"<p>{subject['blurb']}</p>"
                f"<p>CLAPS connects {city['name']} students in {cls['name']} with a dedicated "
                f"{subject['name']} teacher for focused online one-to-one sessions.</p>"
            ),
        },
        {
            "heading": "Syllabuses available",
            "body": (
                "<ul>"
                f"<li><strong>CBSE:</strong> NCERT {subject['name']} for {cls['name']}</li>"
                f"<li><strong>Kerala State:</strong> SCERT {subject['name']} chapter flow</li>"
                f"<li><strong>ICSE / ISC:</strong> Detailed {subject['name']} coverage</li>"
                "</ul>"
            ),
        },
        {
            "heading": "How to start",
            "body": (
                "<p>WhatsApp CLAPS, share your child's class and subject requirement. "
                "A coordinator confirms the teacher and timeslot — classes begin within days. "
                "Coordinator support available 10 AM – 10 PM IST.</p>"
            ),
        },
    ]
    related = [
        {"slug": f"{subject['key']}-individual-tuition-{city['key']}", "label": f"{subject['name']} Tuition {city['name']}", "sub": "All classes"},
        {"slug": f"{cls['key']}-individual-tuition-{city['key']}", "label": f"{cls['name']} Tuition {city['name']}", "sub": "All subjects"},
        {"slug": f"{subject['key']}-individual-tuition-{cls['key']}", "label": f"{subject['name']} Tuition {cls['name']}", "sub": "All cities"},
        {"slug": "individual-tuition-online", "label": "Online Tuition", "sub": "How it works"},
    ]
    return dict(slug=slug, title=title, description=desc, h1=h1, lede=lede,
                cite=cite, sections=sections, related=related, breadcrumb_name=h1, city_key=city['key'], city_display=city['name'])


# ── RUNNER ────────────────────────────────────────────────────────────────────

# City×subject×class triples: only high-value combos to avoid thin content explosion.
# Use key secondary/board classes and highest-demand subjects.
PSEO_CITIES    = [c for c in CITIES if c["key"] in {
    "kochi","trivandrum","kozhikode","thrissur","kannur","kollam",
    "bangalore","chennai","hyderabad","dubai","mumbai","delhi"
}]
PSEO_SUBJECTS  = [s for s in SUBJECTS if s["key"] in {
    "maths","physics","chemistry","biology","english","science","accountancy"
}]
PSEO_CLASSES   = [c for c in CLASSES if c["key"] in {
    "class-8","class-9","class-10","class-11","class-12"
}]


def collect_pages():
    seen = set()
    pages = []

    def add(page):
        if page["slug"] not in seen:
            seen.add(page["slug"])
            pages.append(page)

    # 1. city × subject  (25 × 14 = 350)
    for city in CITIES:
        for subject in SUBJECTS:
            add(city_subject_page(city, subject))

    # 2. city × class  (25 × 13 = 325)
    for city in CITIES:
        for cls in CLASSES:
            add(city_class_page(city, cls))

    # 3. subject × syllabus  (14 × 4 = 56)
    for subject in SUBJECTS:
        for syllabus in SYLLABUSES:
            add(subject_syllabus_page(subject, syllabus))

    # 4. class × syllabus  (13 × 4 = 52)
    for cls in CLASSES:
        for syllabus in SYLLABUSES:
            add(class_syllabus_page(cls, syllabus))

    # 5. city × syllabus  (25 × 4 = 100)
    for city in CITIES:
        for syllabus in SYLLABUSES:
            add(city_syllabus_page(city, syllabus))

    # 6. subject × class  (14 × 13 = 182)
    for subject in SUBJECTS:
        for cls in CLASSES:
            add(subject_class_page(subject, cls))

    # 7. city × subject × class  (12 × 7 × 5 = 420, curated high-value combos)
    for city in PSEO_CITIES:
        for subject in PSEO_SUBJECTS:
            for cls in PSEO_CLASSES:
                add(city_subject_class_page(city, subject, cls))

    return pages


def write_page(page):
    out_dir = ROOT / page["slug"]
    out_dir.mkdir(parents=True, exist_ok=True)
    html = build_page(**page)
    (out_dir / "index.html").write_text(html, encoding="utf-8")


def main():
    pages = collect_pages()
    total = len(pages)
    print(f"Generating {total} pSEO pages...")
    for i, page in enumerate(pages, 1):
        write_page(page)
        if i % 50 == 0 or i == total:
            print(f"  [{i}/{total}] /{page['slug']}/")
    print(f"\nDone. {total} pages written to {ROOT}")
    # Emit slugs for sitemap pipeline
    slug_file = ROOT.parent / "scripts" / "_pseo_slugs.txt"
    slug_file.write_text("\n".join(p["slug"] for p in pages), encoding="utf-8")
    print(f"Slugs written to {slug_file}")


if __name__ == "__main__":
    main()
