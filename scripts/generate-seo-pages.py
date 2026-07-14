#!/usr/bin/env python3
"""Generate SEO subpages for individualtuition.in"""

import json
import os
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from seo_pages_extra import EXTRA_PAGES
from seo_content_enrichment import EXTRA_PAGES_BATCH2, enrich_page
from footer_template import footer_html
from seo_meta import BASE as SEO_BASE, robots_txt, seo_head

ROOT = Path(__file__).resolve().parent.parent / "public_html"
BASE = "https://individualtuition.in"
WA = "https://wa.me/918610416147?text=Hi%20%2C%20how%20can%20we%20join%20CLAPS%3F"
GA = "G-0WRLE4YHZW"

WA_SVG = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

NAV_ITEMS = [
    ("Home", "/"),
    ("Online Tuition", "/individual-tuition-online/"),
    ("Research", "/research-individual-tuition/"),
    ("Syllabuses", "/syllabuses/"),
    ("Classes", "/classes/"),
    ("FAQ", "/faq/"),
    ("About", "/about/"),
]

PAGES = [
    {
        "slug": "individual-tuition-online",
        "title": "Online Individual Tuition | One-to-One Classes KG to +2 | CLAPS",
        "description": "Online individual tuition with one teacher per student. KG to +2, all syllabuses, flexible timings, expert teachers. Part of ClapsLearn — chat on WhatsApp to join.",
        "h1": "Online Individual Tuition",
        "lede": "One teacher, one student — live online classes for KG to +2 across CBSE, Kerala State, ICSE and more. Flexible timings that fit your family schedule.",
        "cite": "CLAPS Individual Tuition (individualtuition.in) is the dedicated one-to-one tuition brand of ClapsLearn, offering online individual classes from kindergarten through Plus Two with subject-expert teachers and academic coordinator support from 10 AM to 10 PM.",
        "sections": [
            ("What is online individual tuition?", "<p>Online individual tuition means your child learns with a dedicated teacher in a private live session — not a crowded batch. At CLAPS, every class is personalised: the teacher adapts pace, language, and examples to your child's syllabus and learning gaps.</p><p>Classes run on video with interactive whiteboard tools. Parents can choose subjects individually, schedule preferred time slots, and get coordinator support throughout the day.</p>"),
            ("Who is it for?", "<ul><li>Students from KG to Plus Two (+2)</li><li>CBSE, Kerala State, ICSE, ISC and other boards</li><li>Families in Kerala, other Indian states, and NRI students abroad</li><li>Learners who need focused help in specific subjects or exam preparation</li></ul>"),
            ("Why choose CLAPS over group tuition?", "<ul><li><strong>Personal attention</strong> — doubts cleared in real time, no waiting</li><li><strong>Flexible timing</strong> — morning, evening, or weekend slots</li><li><strong>Pick your subjects</strong> — pay only for what you need</li><li><strong>Expert teachers</strong> — 3,000+ teachers across subjects</li><li><strong>Research-backed model</strong> — one-to-one tuition consistently outperforms group instruction in studies worldwide (<a href=\"../research-individual-tuition/index.html\">see research</a>)</li></ul>"),
            ("What research says about individual tuition", "<p>Decades of education research show that tutoring — especially one-to-one instruction — produces among the largest learning gains in schooling. A 2020 meta-analysis of 96 randomised tutoring studies found an average improvement of <strong>0.37 standard deviations</strong> (about 14 percentile points). The UK Education Endowment Foundation estimates roughly <strong>five additional months of progress</strong> from one-to-one tuition.</p><p><a href=\"../research-individual-tuition/index.html\">Read the full research summary →</a></p>"),
        ],
        "related": [
            ("Research on Individual Tuition", "/research-individual-tuition/", "Studies & evidence"),
            ("Benefits of Individual Tuition", "/benefits-of-individual-tuition/", "Why one-to-one works"),
            ("Individual Tuition Kerala", "/individual-tuition-kerala/", "Online classes for Kerala families"),
            ("How It Works", "/how-it-works/", "Join in 3 simple steps"),
        ],
        "schema_type": "Course",
        "schema_extra": {"name": "Online Individual Tuition", "description": "One-to-one online tuition KG to +2", "provider": {"@type": "Organization", "name": "CLAPS Individual Tuition", "url": BASE}, "educationalLevel": "KG to Plus Two"},
    },
    {
        "slug": "individual-tuition-kerala",
        "title": "Individual Tuition Kerala | Online One-to-One Classes | CLAPS",
        "description": "Best individual tuition in Kerala — online one-to-one classes for Kerala State, CBSE & ICSE. Malayalam-friendly teaching. ClapsLearn brand. WhatsApp to join.",
        "h1": "Individual Tuition in Kerala",
        "lede": "Trusted online individual tuition for Kerala students — Kerala State syllabus, CBSE, ICSE from KG to +2. Teachers who understand Malayalam-medium and English-medium learners.",
        "cite": "CLAPS provides individual tuition for Kerala students online, covering Kerala State syllabus and national boards with flexible scheduling for families across Kerala and Malayali diaspora worldwide.",
        "sections": [
            ("Individual tuition for Kerala students", "<p>Kerala has one of India's highest literacy rates — and parents expect quality, personalised learning. CLAPS Individual Tuition delivers one teacher per student online, so your child gets full attention whether they follow Kerala State syllabus or CBSE/ICSE.</p>"),
            ("Syllabuses we cover for Kerala", "<ul><li><strong>Kerala State syllabus</strong> — SCERT-aligned teaching from primary to +2</li><li><strong>CBSE</strong> — popular in urban Kerala schools</li><li><strong>ICSE / ISC</strong> — structured curriculum support</li></ul>"),
            ("Malayalam & English medium", "<p>Many Kerala families prefer teachers who can explain concepts in Malayalam when needed, while building English fluency for exams. CLAPS matches students with teachers suited to their medium and comfort level.</p>"),
        ],
        "related": [
            ("Kerala cities", "/locations/", "Kochi, Trivandrum & more"),
            ("Malayalam Tuition", "/individual-tuition-malayalam/", "Classes in Malayalam"),
            ("Kerala State Syllabus", "/kerala-state-syllabus-tuition/", "SCERT-aligned coaching"),
            ("SSLC tuition", "/sslc-individual-tuition/", "Class 10 Kerala"),
        ],
    },
    {
        "slug": "individual-tuition-malayalam",
        "title": "Individual Tuition in Malayalam | Online Classes KG to +2 | CLAPS",
        "description": "Individual tuition in Malayalam for Kerala State, CBSE & ICSE students. One-to-one online classes with patient teachers. From ClapsLearn — join via WhatsApp.",
        "h1": "Individual Tuition in Malayalam",
        "lede": "Concepts explained clearly in Malayalam — with exam-ready English support. One-to-one online tuition for students who learn best in their mother tongue.",
        "cite": "CLAPS Individual Tuition offers Malayalam-medium and bilingual one-to-one online classes for Kerala syllabus and national boards, helping students understand fundamentals before exam-focused practice.",
        "malayalam_block": True,
        "sections": [
            ("മലയാളത്തിൽ Individual Tuition", "<p class=\"page-hero__lede--ml\">മലയാളത്തിൽ concept clear ആക്കി, exam-ന് English-ലും confident ആകാൻ CLAPS one-to-one online tuition നൽകുന്നു. KG മുതൽ +2 വരെ, Kerala State, CBSE, ICSE syllabus-കൾ support ചെയ്യുന്നു.</p>"),
            ("Why Malayalam-medium tuition works", "<ul><li>Hard topics become clear when explained in the child's first language</li><li>Builds confidence before switching to English exam answers</li><li>Ideal for primary students and Kerala State syllabus learners</li><li>Parents can communicate easily with coordinators (10 AM – 10 PM)</li></ul>"),
        ],
        "related": [
            ("Kerala Tuition", "/individual-tuition-kerala/", "For Kerala families"),
            ("Kerala State Syllabus", "/kerala-state-syllabus-tuition/", "SCERT coaching"),
            ("Primary Tuition", "/primary-individual-tuition/", "Classes 1–5"),
        ],
    },
    {
        "slug": "cbse-individual-tuition",
        "title": "CBSE Individual Tuition Online | One-to-One KG to Class 12 | CLAPS",
        "description": "CBSE individual tuition online — one teacher per student, NCERT-aligned, Class 1 to 12. Maths, Science, English & more. ClapsLearn. Enrol via WhatsApp.",
        "h1": "CBSE Individual Tuition",
        "lede": "NCERT-aligned one-to-one CBSE tuition from primary to Class 12. Board exam preparation, concept building, and homework support with expert subject teachers.",
        "cite": "CLAPS Individual Tuition provides CBSE one-to-one online coaching aligned with NCERT textbooks, covering foundation years through Class 10 board exams and Class 11–12 senior secondary subjects.",
        "sections": [
            ("CBSE one-to-one coaching", "<p>CBSE students benefit from structured syllabus coverage and exam-pattern practice. Individual tuition lets the teacher focus entirely on your child's weak chapters — whether that's Class 10 Maths or Class 12 Physics.</p>"),
            ("Subjects & classes", "<ul><li><strong>Primary (1–5):</strong> Maths, EVS, English, Hindi/Malayalam</li><li><strong>Middle (6–8):</strong> Maths, Science, Social Science, Languages</li><li><strong>Secondary (9–10):</strong> Board exam prep — Maths, Science, Social, English</li><li><strong>Senior (11–12):</strong> PCM, PCB, Commerce streams</li></ul>"),
        ],
        "related": [
            ("Class 10 CBSE", "/class-10-individual-tuition/", "Board exam focus"),
            ("Plus Two", "/plus-two-individual-tuition/", "Class 11–12"),
            ("Maths Tuition", "/maths-individual-tuition/", "One-to-one Maths"),
        ],
    },
    {
        "slug": "kerala-state-syllabus-tuition",
        "title": "Kerala State Syllabus Individual Tuition | SCERT Online Classes | CLAPS",
        "description": "Kerala State syllabus individual tuition online — SCERT-aligned one-to-one classes KG to +2. Malayalam & English medium. ClapsLearn brand.",
        "h1": "Kerala State Syllabus Individual Tuition",
        "lede": "SCERT-aligned individual tuition for Kerala State board students — from primary through Plus Two, with teachers who know the Kerala textbook sequence and exam pattern.",
        "cite": "CLAPS offers Kerala State syllabus individual tuition online following SCERT curriculum structure for primary, secondary, and higher secondary levels with optional Malayalam-medium instruction.",
        "sections": [
            ("SCERT-aligned teaching", "<p>Kerala State syllabus has its own textbook flow and evaluation style. CLAPS teachers follow SCERT chapter order, help with Onam/Christmas exam prep, and build up to SSLC and Plus Two board exams.</p>"),
            ("Levels covered", "<ul><li>Lower primary & upper primary (Classes 1–7)</li><li>High school (Classes 8–10) — SSLC preparation</li><li>Higher secondary (Plus One & Plus Two)</li></ul>"),
        ],
        "related": [
            ("Malayalam Tuition", "/individual-tuition-malayalam/", "Learn in Malayalam"),
            ("Class 10", "/class-10-individual-tuition/", "SSLC prep"),
            ("Plus Two", "/plus-two-individual-tuition/", "Higher secondary"),
        ],
    },
    {
        "slug": "icse-individual-tuition",
        "title": "ICSE Individual Tuition Online | One-to-One Classes | CLAPS",
        "description": "ICSE & ISC individual tuition online — detailed syllabus coverage, one teacher per student. KG to Class 12. Part of ClapsLearn. WhatsApp to enrol.",
        "h1": "ICSE Individual Tuition",
        "lede": "ICSE's in-depth curriculum needs focused teaching time. CLAPS individual tuition gives your child a dedicated expert for each subject — from primary through ISC Class 12.",
        "cite": "CLAPS Individual Tuition supports ICSE and ISC students with one-to-one online classes covering the board's comprehensive syllabus including literature, applications-based Science, and structured exam practice.",
        "sections": [
            ("Why ICSE students choose individual tuition", "<p>ICSE covers more ground per subject than many boards. One-to-one sessions let teachers spend extra time on literature analysis, detailed Science diagrams, and the writing practice ICSE exams demand.</p>"),
            ("Classes covered", "<ul><li>Primary & middle school ICSE foundations</li><li>ICSE Class 10 board preparation</li><li>ISC Class 11–12 — Science, Commerce, Humanities</li></ul>"),
        ],
        "related": [
            ("English Tuition", "/english-individual-tuition/", "Literature & language"),
            ("Class 10", "/class-10-individual-tuition/", "Board exams"),
            ("CBSE Tuition", "/cbse-individual-tuition/", "Alternative board"),
        ],
    },
    {
        "slug": "kg-individual-tuition",
        "title": "KG Individual Tuition Online | Early Learning One-to-One | CLAPS",
        "description": "KG & preschool individual tuition online — playful one-to-one learning, letters, numbers & English basics. ClapsLearn. WhatsApp to start.",
        "h1": "KG Individual Tuition",
        "lede": "Gentle one-to-one online classes for LKG & UKG — building curiosity, reading readiness, and number sense with patient teachers who make learning fun.",
        "cite": "CLAPS Individual Tuition offers kindergarten-level one-to-one online sessions focused on early literacy, numeracy, and school readiness for ages 3–6.",
        "sections": [
            ("Early learning, one child at a time", "<p>Young children learn best with attention and encouragement. Individual KG tuition avoids the distraction of group classes — the teacher follows your child's pace through alphabets, phonics, counting, shapes, and simple English.</p>"),
            ("What parents can expect", "<ul><li>Short, engaging sessions suited to attention span</li><li>Progress updates from academic coordinators</li><li>Flexible timing around nap and school schedules</li><li>Smooth transition to Class 1 primary tuition</li></ul>"),
        ],
        "related": [
            ("Primary Tuition", "/primary-individual-tuition/", "Classes 1–5"),
            ("Malayalam Tuition", "/individual-tuition-malayalam/", "Mother-tongue support"),
            ("How It Works", "/how-it-works/", "Getting started"),
        ],
    },
    {
        "slug": "primary-individual-tuition",
        "title": "Primary Individual Tuition | Classes 1–5 Online | CLAPS",
        "description": "Primary school individual tuition online for Classes 1–5 — Maths, English, EVS & languages. One-to-one, all syllabuses. ClapsLearn.",
        "h1": "Primary Individual Tuition (Classes 1–5)",
        "lede": "Strong foundations in Classes 1–5 with one-to-one tuition — Maths, languages, EVS, and homework help across CBSE, Kerala State, and ICSE.",
        "cite": "CLAPS provides primary-level individual tuition online for Classes 1 through 5 with subject-specialist teachers and syllabus-aligned lesson plans.",
        "sections": [
            ("Building foundations early", "<p>Primary years set the tone for every exam ahead. Individual tuition catches gaps early — whether your child struggles with multiplication tables or reading comprehension — before they compound in middle school.</p>"),
            ("Subjects", "<ul><li>Mathematics & mental maths</li><li>English reading, grammar & writing</li><li>Malayalam / Hindi (as per syllabus)</li><li>EVS / Science & Social basics</li></ul>"),
        ],
        "related": [
            ("KG Tuition", "/kg-individual-tuition/", "Ages 3–6"),
            ("Maths Tuition", "/maths-individual-tuition/", "Primary to +2"),
            ("Kerala State", "/kerala-state-syllabus-tuition/", "SCERT primary"),
        ],
    },
    {
        "slug": "class-10-individual-tuition",
        "title": "Class 10 Individual Tuition | SSLC & CBSE Board Prep | CLAPS",
        "description": "Class 10 individual tuition for SSLC, CBSE & ICSE board exams — one-to-one Maths, Science, Social & English. Exam-focused. ClapsLearn.",
        "h1": "Class 10 Individual Tuition",
        "lede": "Board exam year made manageable — intensive one-to-one Class 10 tuition for SSLC (Kerala), CBSE, and ICSE with past-paper practice and chapter-wise revision.",
        "cite": "CLAPS Individual Tuition offers Class 10 board exam preparation through one-to-one online sessions covering Kerala SSLC, CBSE, and ICSE syllabuses with exam-oriented practice.",
        "sections": [
            ("Board exam preparation", "<p>Class 10 is a milestone. CLAPS pairs your child with teachers who know the exact board pattern — SSLC scoring schemes, CBSE NCERT weightage, or ICSE structured questions — and builds a revision plan around mock tests and weak-area drills.</p>"),
            ("Typically covered", "<ul><li>Mathematics — full syllabus + problem speed</li><li>Science (Physics, Chemistry, Biology combined or split)</li><li>Social Science / Humanities</li><li>English & second language papers</li></ul>"),
        ],
        "related": [
            ("Plus Two", "/plus-two-individual-tuition/", "After Class 10"),
            ("CBSE Tuition", "/cbse-individual-tuition/", "NCERT aligned"),
            ("Science Tuition", "/science-individual-tuition/", "PCB & general Science"),
        ],
    },
    {
        "slug": "plus-two-individual-tuition",
        "title": "Plus Two Individual Tuition | Class 11 & 12 Online | CLAPS",
        "description": "Plus Two (+2) individual tuition online — Science, Commerce & Humanities. PCM, PCB, Accountancy & more. One-to-one. ClapsLearn.",
        "h1": "Plus Two Individual Tuition",
        "lede": "Class 11 & 12 one-to-one tuition for Kerala Higher Secondary, CBSE, and ISC — Physics, Chemistry, Maths, Biology, Commerce, and core languages.",
        "cite": "CLAPS Individual Tuition delivers Plus Two (+2) coaching through individual online classes for Science (PCM/PCB), Commerce, and selected Humanities subjects with board and entrance exam orientation.",
        "sections": [
            ("Higher secondary, individually taught", "<p>Plus Two subjects are demanding — individual tuition lets students master derivations, numericals, and long-form answers without falling behind a batch pace. Ideal for NEET/JEE foundation alongside board prep.</p>"),
            ("Streams & subjects", "<ul><li><strong>Science:</strong> Physics, Chemistry, Maths, Biology</li><li><strong>Commerce:</strong> Accountancy, Business Studies, Economics</li><li><strong>Languages & optional subjects</strong> as per syllabus</li></ul>"),
        ],
        "related": [
            ("Maths Tuition", "/maths-individual-tuition/", "Calculus & algebra"),
            ("Science Tuition", "/science-individual-tuition/", "PCB focus"),
            ("Class 10", "/class-10-individual-tuition/", "SSLC foundation"),
        ],
    },
    {
        "slug": "maths-individual-tuition",
        "title": "Maths Individual Tuition Online | One-to-One KG to +2 | CLAPS",
        "description": "Maths individual tuition online — algebra, geometry, calculus & board exam prep. One teacher per student, all syllabuses. ClapsLearn.",
        "h1": "Maths Individual Tuition",
        "lede": "From basic arithmetic to Plus Two calculus — dedicated Maths teachers who diagnose gaps, teach step-by-step, and build exam speed in one-to-one sessions.",
        "cite": "CLAPS Individual Tuition provides mathematics coaching from primary level through Plus Two with one-to-one online instruction across CBSE, Kerala State, ICSE, and ISC syllabuses.",
        "sections": [
            ("Why Maths needs individual attention", "<p>Maths is cumulative — a missed concept in Class 8 fractions causes struggles in Class 10 trigonometry. Individual tuition identifies the exact gap and fixes it before moving forward.</p>"),
            ("Levels", "<ul><li>Primary & middle school numeracy</li><li>Class 10 board Maths (standard & basic where applicable)</li><li>Plus Two Maths — calculus, probability, vectors</li><li>Competitive exam foundations (where requested)</li></ul>"),
        ],
        "related": [
            ("Science Tuition", "/science-individual-tuition/", "Physics & Chemistry too"),
            ("Class 10", "/class-10-individual-tuition/", "Board year"),
            ("Plus Two", "/plus-two-individual-tuition/", "Senior secondary"),
        ],
    },
    {
        "slug": "science-individual-tuition",
        "title": "Science Individual Tuition | Physics, Chemistry, Biology | CLAPS",
        "description": "Science individual tuition online — Physics, Chemistry, Biology one-to-one. Class 6 to +2, all boards. ClapsLearn. Join on WhatsApp.",
        "h1": "Science Individual Tuition",
        "lede": "Physics, Chemistry, and Biology taught one-to-one — diagrams, numericals, and theory explained at your child's pace from middle school through Plus Two.",
        "cite": "CLAPS offers individual Science tuition online covering general Science for middle grades and specialised Physics, Chemistry, and Biology for secondary and Plus Two levels.",
        "sections": [
            ("Science subjects, individually", "<p>Science splits into distinct skills — Physics numericals, Chemistry equations, Biology diagrams. CLAPS assigns subject specialists so your child learns from a teacher who masters that discipline.</p>"),
            ("Coverage", "<ul><li>Integrated Science (Classes 6–10)</li><li>Separate PCM / PCB at Plus Two</li><li>Practical & viva preparation support</li><li>NEET/JEE basics (on request)</li></ul>"),
        ],
        "related": [
            ("Maths Tuition", "/maths-individual-tuition/", "Numerical skills"),
            ("Plus Two", "/plus-two-individual-tuition/", "Higher secondary"),
            ("Class 10", "/class-10-individual-tuition/", "Board Science"),
        ],
    },
    {
        "slug": "english-individual-tuition",
        "title": "English Individual Tuition Online | Grammar & Literature | CLAPS",
        "description": "English individual tuition — grammar, writing, literature & exam answers one-to-one. KG to +2, CBSE & ICSE. ClapsLearn.",
        "h1": "English Individual Tuition",
        "lede": "Reading, writing, grammar, and literature — one-to-one English tuition that builds fluency for exams and confidence for life.",
        "cite": "CLAPS Individual Tuition provides English language and literature coaching through private online sessions for school syllabus and board exam requirements.",
        "sections": [
            ("English skills, personalised", "<p>English tuition at CLAPS covers comprehension, essay writing, grammar drills, and ICSE/CBSE literature texts — paced for your child's current level, whether they're in Class 3 phonics or Class 12 poetry analysis.</p>"),
        ],
        "related": [
            ("ICSE Tuition", "/icse-individual-tuition/", "Literature-heavy board"),
            ("Primary Tuition", "/primary-individual-tuition/", "Early English"),
            ("Malayalam Tuition", "/individual-tuition-malayalam/", "Bilingual support"),
        ],
    },
    {
        "slug": "nri-individual-tuition",
        "title": "NRI Individual Tuition | Gulf & Abroad Online Classes | CLAPS",
        "description": "Individual tuition for NRI students in UAE, Saudi, Qatar & worldwide — CBSE, Kerala & ICSE online. Indian time zones. ClapsLearn.",
        "h1": "NRI Individual Tuition",
        "lede": "Keep your child connected to the Indian syllabus abroad — flexible one-to-one online tuition for NRI families in the Gulf, Europe, Americas, and beyond.",
        "cite": "CLAPS Individual Tuition serves NRI and expatriate Indian students in 12+ countries with online one-to-one classes scheduled across time zones for CBSE, Kerala State, and ICSE curricula.",
        "sections": [
            ("Schooling abroad, syllabus at home", "<p>NRI children often follow Indian boards through embassy schools or distance learning. CLAPS fills the gap with live individual tuition — same syllabus, same exam patterns, scheduled around your local evening or weekend.</p>"),
            ("Popular with families in", "<ul><li>UAE, Saudi Arabia, Qatar, Kuwait, Oman, Bahrain</li><li>USA, UK, Canada, Australia</li><li>Singapore, Malaysia, and other diaspora hubs</li></ul>"),
        ],
        "related": [
            ("Online Tuition", "/individual-tuition-online/", "How classes work"),
            ("CBSE Tuition", "/cbse-individual-tuition/", "Most common NRI board"),
            ("Kerala Tuition", "/individual-tuition-kerala/", "Malayali families"),
        ],
    },
    {
        "slug": "about",
        "title": "About CLAPS Individual Tuition | A ClapsLearn Brand",
        "description": "CLAPS Individual Tuition is the one-to-one online tuition brand of ClapsLearn — 10,000+ students, 3,000+ teachers, KG to +2. Learn our story.",
        "h1": "About CLAPS Individual Tuition",
        "lede": "CLAPS is the dedicated individual (one-to-one) tuition division of ClapsLearn — built for parents who want personal attention, flexible timing, and expert teachers for every subject.",
        "cite": "CLAPS Individual Tuition (individualtuition.in) operates as a focused sub-brand of ClapsLearn (clapslearn.com), specialising exclusively in one teacher–one student online classes from KG through Plus Two.",
        "sections": [
            ("Part of ClapsLearn", "<p><a href=\"https://clapslearn.com\" rel=\"noopener\">ClapsLearn</a> is a leading online education platform serving students across India and 12+ countries. CLAPS Individual Tuition was created as a dedicated destination for families specifically looking for <strong>individual tuition</strong> — not group batches.</p>"),
            ("Our numbers", "<ul><li><strong>4+ years</strong> of online teaching experience</li><li><strong>10,000+ students</strong> taught</li><li><strong>3,000+ expert teachers</strong></li><li><strong>4.9/5</strong> Google rating from 1,000+ reviews</li><li><strong>12+ countries</strong> — including NRI families worldwide</li></ul>"),
            ("Built on what research recommends", "<p>Education research consistently ranks tutoring among the most effective learning interventions. CLAPS applies that evidence in practice: every session is one-to-one, syllabus-aligned, and led by a subject expert — the model studies from Bloom to the Education Endowment Foundation identify as high-impact. <a href=\"../research-individual-tuition/index.html\">Explore the research →</a></p>"),
        ],
        "related": [
            ("Research & Evidence", "/research-individual-tuition/", "Studies on tutoring"),
            ("How It Works", "/how-it-works/", "Enrolment process"),
            ("FAQ", "/faq/", "Common questions"),
        ],
    },
    {
        "slug": "how-it-works",
        "title": "How Individual Tuition Works | Join CLAPS in 3 Steps",
        "description": "How to start individual tuition with CLAPS — WhatsApp enquiry, teacher matching, flexible online classes. Part of ClapsLearn.",
        "h1": "How Individual Tuition Works",
        "lede": "Starting one-to-one tuition with CLAPS is simple — message us on WhatsApp, tell us your child's class and subjects, and we match an expert teacher at your preferred time.",
        "cite": "CLAPS Individual Tuition enrolment begins with a WhatsApp consultation, followed by teacher assignment and scheduled one-to-one online classes with ongoing academic coordinator support.",
        "sections": [
            ("Step 1: Chat on WhatsApp", "<p>Tap the WhatsApp button on any page or message <strong>+91 86104 16147</strong>. Share your child's class, syllabus (CBSE / Kerala / ICSE), subjects needed, and preferred timing.</p>"),
            ("Step 2: Teacher matching", "<p>Our team assigns a subject-expert teacher suited to your syllabus and language preference. You'll receive class schedule details and how to join online sessions.</p>"),
            ("Step 3: Start learning", "<p>Attend live one-to-one classes. Pick only the subjects you need. Adjust timing when possible. Reach coordinators 10 AM – 10 PM for any support.</p>"),
        ],
        "related": [
            ("FAQ", "/faq/", "Fees & technical questions"),
            ("About CLAPS", "/about/", "Our story"),
            ("Online Tuition", "/individual-tuition-online/", "Full overview"),
        ],
    },
    {
        "slug": "faq",
        "title": "Individual Tuition FAQ | CLAPS & ClapsLearn",
        "description": "Frequently asked questions about CLAPS individual tuition — fees, timings, syllabuses, online setup & NRI students. Answers from ClapsLearn.",
        "h1": "Individual Tuition FAQ",
        "lede": "Answers to common questions about CLAPS one-to-one online tuition — syllabuses, classes, timings, and how we're connected to ClapsLearn.",
        "faqs": [
            ("What is individual tuition?", "Individual tuition (also called one-to-one tuition) means one dedicated teacher teaches one student in a private session. At CLAPS, all classes are individual — never group batches."),
            ("Is CLAPS the same as ClapsLearn?", "CLAPS Individual Tuition is a focused sub-brand of ClapsLearn (clapslearn.com). ClapsLearn is the parent online education platform; individualtuition.in is dedicated to one-to-one tuition enquiries and enrolment."),
            ("Which classes and syllabuses do you cover?", "KG through Plus Two (+2). Syllabuses include CBSE, Kerala State (SCERT), ICSE, ISC, and other boards on request."),
            ("Are classes fully online?", "Yes. All CLAPS individual tuition classes are live online sessions with interactive teaching tools. You need a device with internet — phone, tablet, or laptop."),
            ("Can I choose only specific subjects?", "Yes. Unlike all-subject packages, you select only the subjects your child needs — for example, just Class 10 Maths and Science."),
            ("Can we pick class timings?", "Yes. CLAPS arranges classes at your preferred time slots where teacher availability allows — including evenings and weekends."),
            ("Do you teach in Malayalam?", "Yes. Many teachers support Malayalam-medium or bilingual explanation, especially for Kerala State syllabus and primary students."),
            ("Do you serve NRI students abroad?", "Yes. We teach students in the Gulf, Europe, Americas, and 12+ countries with scheduling adapted to local time zones."),
            ("What support do parents get?", "Academic coordinators are available 10 AM to 10 PM daily via WhatsApp for scheduling, teacher queries, and progress follow-up."),
            ("How do I enrol?", "Message us on WhatsApp at +91 86104 16147 or use the green WhatsApp button on this site. There is no lengthy form — we guide you personally."),
            ("Does research support individual tuition?", "Yes. Multiple meta-analyses and government evidence reviews find that one-to-one tuition produces substantial learning gains — larger than typical classroom interventions. See our research page for citations from Bloom (1984), Cohen et al. (1982), Nickow et al. (2020), the Education Endowment Foundation, and ASER-based studies in India."),
            ("Is individual tuition better than group tuition?", "Research comparing one-to-one and small-group tuition is mixed on effect sizes, but one-to-one always maximises individual attention, pacing, and doubt-clearing. CLAPS focuses exclusively on individual tuition because parents choose us specifically for that personal model — not batch classes."),
        ],
        "related": [
            ("Research & Evidence", "/research-individual-tuition/", "Studies worldwide & India"),
            ("Benefits", "/benefits-of-individual-tuition/", "Why one-to-one works"),
            ("How It Works", "/how-it-works/", "3-step enrolment"),
        ],
    },
    {
        "slug": "research-individual-tuition",
        "title": "Research on Individual Tuition | Evidence & Studies | CLAPS",
        "description": "What research says about individual tuition — Bloom, Cohen, Nickow NBER meta-analysis, EEF 5 months progress, ASER India studies. Evidence for one-to-one tutoring.",
        "h1": "Research on Individual Tuition",
        "lede": "Education researchers worldwide agree: one-to-one tuition is among the most powerful tools for improving student learning. Here is what the evidence says — with sources you can verify.",
        "cite": "Peer-reviewed meta-analyses and government evidence reviews consistently find that individual and small-group tutoring produces larger learning gains than typical whole-class instruction, with pooled effect sizes around 0.33–0.37 standard deviations in rigorous experimental studies.",
        "sections": [
            ("Summary: why individual tuition works", "<p>Individual tuition works because it removes the constraints of the average classroom: the teacher can match the student's pace, diagnose gaps immediately, give instant feedback, and adapt explanations until the concept clicks. Researchers call this <strong>adaptive instruction</strong> — and it is far easier to deliver with one student than with thirty.</p><ul class=\"benefit-list\"><li><strong>Immediate feedback</strong> — mistakes corrected in the moment, not weeks later in an exam</li><li><strong>Custom pacing</strong> — slow down on hard topics, accelerate where the child is strong</li><li><strong>Targeted practice</strong> — focus only on weak chapters or subjects</li><li><strong>Higher engagement</strong> — shy students ask questions they would never raise in a batch</li><li><strong>Exam alignment</strong> — syllabus and board pattern taught to the individual's timeline</li></ul>"),
            ("International meta-analyses", "<ul class=\"research-grid\"><li class=\"research-card\"><span class=\"research-card__stat\">0.37 SD</span><p class=\"research-card__title\">Nickow, Oreopoulos & Quan (2020)</p><p>A systematic review and meta-analysis of <strong>96 randomised controlled trials</strong> on preK–12 tutoring found consistent, substantial positive impacts on learning, with a pooled effect size of <strong>0.37 standard deviations</strong> — roughly 14 percentile points. Effects were stronger when tutoring was led by teachers or trained tutors, and in earlier grades.</p><span class=\"research-card__source\">Source: <a href=\"https://www.nber.org/papers/w27476\" rel=\"noopener noreferrer\">NBER Working Paper 27476</a></span></li><li class=\"research-card\"><span class=\"research-card__stat\">0.33 SD</span><p class=\"research-card__title\">Cohen, Kulik & Kulik (1982)</p><p>An earlier meta-analysis of <strong>65 tutoring studies</strong> reported an average effect of about <strong>0.33 standard deviations</strong> (13 percentile points) — one of the largest effects in education research at the time, and a finding that has held up in later reviews.</p><span class=\"research-card__source\">Source: Cohen, P. A., Kulik, J. A., & Kulik, C. L. C. (1982). Educational outcomes of tutoring: A meta-analysis of findings. <em>American Educational Research Journal</em>.</span></li><li class=\"research-card\"><span class=\"research-card__stat\">~5 months</span><p class=\"research-card__title\">Education Endowment Foundation (EEF)</p><p>The UK's EEF Teaching & Learning Toolkit — synthesising <strong>123 studies</strong> — rates one-to-one tuition as high impact, providing approximately <strong>five additional months of progress</strong> on average. Primary pupils tend to gain more (+6 months) than secondary (+4 months). Short, regular sessions (about 30 minutes, several times per week) show optimum results.</p><span class=\"research-card__source\">Source: <a href=\"https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/one-to-one-tuition\" rel=\"noopener noreferrer\">EEF One to One Tuition Toolkit</a></span></li><li class=\"research-card\"><span class=\"research-card__stat\">2σ (ideal)</span><p class=\"research-card__title\">Bloom's \"Two Sigma Problem\" (1984)</p><p>Educational psychologist Benjamin Bloom argued that one-to-one tutoring offered <strong>\"the best learning conditions we can devise.\"</strong> Small controlled experiments in his review showed gains of up to two standard deviations above conventional classroom instruction. Later large-scale meta-analyses find smaller but still impressive average effects — the key takeaway is that individual instruction consistently outperforms business-as-usual schooling.</p><span class=\"research-card__source\">Source: Bloom, B. S. (1984). The 2 Sigma Problem. <em>Educational Researcher</em>. See also <a href=\"https://www.educationnext.org/two-sigma-tutoring-separating-science-fiction-from-science-fact/\" rel=\"noopener noreferrer\">Education Next summary</a>.</span></li></ul>"),
            ("Research in India", "<ul class=\"research-grid\"><li class=\"research-card\"><span class=\"research-card__stat\">0.14 SD</span><p class=\"research-card__title\">Private tutoring & learning levels (ASER data)</p><p>Using large-scale ASER household survey data from rural India with fixed-effect methods to control for background factors, researchers found a <strong>positive, statistically significant effect of private tutoring</strong> on reading and maths for Classes 1–8. The estimated gain is about <strong>0.14 standard deviations</strong> — comparable to an additional year of schooling. Effects were <strong>stronger for disadvantaged students</strong>: children in government schools, from lower-income households, and with less-educated parents benefited most.</p><span class=\"research-card__source\">Source: Dongre, A., & Tewary, V. — Accountability Initiative / ASER-based working paper. <a href=\"https://accountabilityindia.in/sites/default/files/pdf_files/Impact_of_Private_Tutoring_on_Learning_Levels.pdf\" rel=\"noopener noreferrer\">PDF</a></span></li><li class=\"research-card\"><span class=\"research-card__stat\">60% gap closed</span><p class=\"research-card__title\">ASER analysis on tuition & reading (Wadhwa, 2013)</p><p>Analysis of ASER data on Std 5 reading levels found that <strong>private tuition helped government-school children substantially</strong> — additional tutoring bridged roughly <strong>60% of the learning gap</strong> between government and private school students. Tuition also helped private-school pupils, but the relative gain was largest for those starting from weaker baselines.</p><span class=\"research-card__source\">Source: Wadhwa, W. (2013). ASER Centre analysis — <a href=\"https://img.asercentre.org/docs/Publications/ASER%20Reports/ASER_2013/ASER2013_report%20sections/willimawadhwaarticle.pdf\" rel=\"noopener noreferrer\">ASER 2013 report section</a></span></li></ul><p>India has one of the world's highest rates of private supplementary tutoring — often called \"shadow education.\" Research confirms what millions of Indian parents already observe: structured extra teaching, especially when targeted to a child's gaps, measurably improves outcomes.</p>"),
            ("One-to-one vs group tuition", "<p>Studies comparing one-to-one and small-group tutoring (2–3 students) show mixed results — sometimes group tutoring matches one-to-one when teaching quality is high. What is consistent across research is that <strong>smaller instructional groups dramatically outperform large batches</strong>, and that the personalised elements — feedback, pacing, diagnostic teaching — matter more than group size alone.</p><p>CLAPS chooses strict one-to-one tuition because:</p><ul><li>Every child gets 100% of the teacher's attention for the full session</li><li>No peer pressure or embarrassment when asking basic doubts</li><li>Schedule and subject selection fit each family individually</li><li>Parents of KG to +2 students consistently report that personal attention is the reason they chose individual over group classes</li></ul>"),
            ("How CLAPS applies the evidence", "<p>CLAPS Individual Tuition is designed around principles that research identifies as effective:</p><ul class=\"benefit-list\"><li><strong>One teacher, one student</strong> — never batch classes</li><li><strong>Syllabus-aligned content</strong> — linked to school curriculum (CBSE, Kerala State, ICSE)</li><li><strong>Subject experts</strong> — specialist teachers, not generalists covering every subject poorly</li><li><strong>Flexible regular sessions</strong> — parents schedule ongoing classes at preferred times</li><li><strong>Coordinator monitoring</strong> — academic support team available 10 AM – 10 PM</li><li><strong>Pick subjects individually</strong> — target weak areas rather than generic packages</li></ul><p>CLAPS is part of <a href=\"https://clapslearn.com\" rel=\"noopener\">ClapsLearn</a>, which has taught 10,000+ students with a 4.9 Google rating — real-world outcomes alongside research-backed methods.</p>"),
            ("Full reference list", "<ol class=\"sources-list\"><li>Bloom, B. S. (1984). The 2 Sigma Problem: The Search for Methods of Group Instruction as Effective as One-to-One Tutoring. <em>Educational Researcher</em>, 13(6), 4–16.</li><li>Cohen, P. A., Kulik, J. A., & Kulik, C. L. C. (1982). Educational outcomes of tutoring: A meta-analysis of findings. <em>American Educational Research Journal</em>, 19(2), 237–248.</li><li>Nickow, A. J., Oreopoulos, P., & Quan, V. (2020). The Impressive Effects of Tutoring on PreK-12 Learning: A Systematic Review and Meta-Analysis of the Experimental Evidence. <a href=\"https://www.nber.org/papers/w27476\" rel=\"noopener noreferrer\">NBER Working Paper 27476</a>.</li><li>Education Endowment Foundation (2024). One to one tuition — Teaching & Learning Toolkit. <a href=\"https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/one-to-one-tuition\" rel=\"noopener noreferrer\">educationendowmentfoundation.org.uk</a></li><li>Dongre, A., & Tewary, V. Impact of Private Tutoring on Learning Levels (ASER-based study). <a href=\"https://accountabilityindia.in/sites/default/files/pdf_files/Impact_of_Private_Tutoring_on_Learning_Levels.pdf\" rel=\"noopener noreferrer\">Accountability Initiative PDF</a></li><li>Wadhwa, W. (2013). Private inputs into schooling — ASER Centre analysis. <a href=\"https://img.asercentre.org/docs/Publications/ASER%20Reports/ASER_2013/ASER2013_report%20sections/willimawadhwaarticle.pdf\" rel=\"noopener noreferrer\">ASER 2013 PDF</a></li><li>VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. <em>Educational Psychologist</em>, 46(4), 197–221.</li><li>Kraft, M. A. (2015). How to Make Tutoring More Effective. <em>Education Next</em>. — Practical synthesis of tutoring evidence.</li></ol><p><em>Note: Effect sizes vary by study design, tutor quality, and context. Research summarises averages — individual results depend on student effort, teacher quality, and consistency of attendance. CLAPS does not claim specific grade guarantees; we provide the one-to-one model that evidence identifies as high-impact.</em></p>"),
        ],
        "related": [
            ("Benefits of Individual Tuition", "/benefits-of-individual-tuition/", "Parent-friendly summary"),
            ("Online Tuition", "/individual-tuition-online/", "CLAPS programme"),
            ("FAQ", "/faq/", "Common questions"),
        ],
    },
    {
        "slug": "benefits-of-individual-tuition",
        "title": "Benefits of Individual Tuition | Why One-to-One Works | CLAPS",
        "description": "Benefits of individual tuition for students & parents — personal attention, flexible timing, better exam results. Backed by education research. CLAPS online KG to +2.",
        "h1": "Benefits of Individual Tuition",
        "lede": "Why do parents choose one-to-one tuition over group classes? Because individual tuition delivers benefits that batch teaching structurally cannot — and decades of research back that up.",
        "cite": "Individual tuition benefits include personalised pacing, immediate feedback, targeted gap-filling, and higher student engagement — mechanisms identified in tutoring research as drivers of the large average learning gains reported in meta-analyses.",
        "sections": [
            ("10 benefits for your child", "<ul class=\"benefit-list\"><li><strong>Undivided teacher attention</strong> — the full session belongs to one student</li><li><strong>Learn at the right pace</strong> — never rushed or held back by a batch median</li><li><strong>Doubts cleared instantly</strong> — no waiting until the teacher finishes with 30 others</li><li><strong>Weak subjects targeted</strong> — choose only Maths, only Science, or any combination</li><li><strong>Confident participation</strong> — shy children speak up in a safe one-to-one setting</li><li><strong>Syllabus & exam focus</strong> — SSLC, CBSE, ICSE patterns taught to your timeline</li><li><strong>Malayalam or English</strong> — explanations in the language your child understands best</li><li><strong>Flexible scheduling</strong> — evening, weekend, or NRI-friendly time zones</li><li><strong>Progress you can see</strong> — coordinators support parents 10 AM – 10 PM</li><li><strong>Research-backed model</strong> — tutoring ranks among the highest-impact education interventions studied</li></ul>"),
            ("What the numbers say", "<p>You do not have to take our word for it:</p><ul class=\"research-grid\"><li class=\"research-card\"><span class=\"research-card__stat\">+5 months</span><p>Average extra progress from one-to-one tuition (Education Endowment Foundation, 123 studies)</p></li><li class=\"research-card\"><span class=\"research-card__stat\">0.37 SD</span><p>Average learning gain across 96 randomised tutoring trials (Nickow et al., 2020, NBER)</p></li><li class=\"research-card\"><span class=\"research-card__stat\">0.14 SD</span><p>Learning improvement from private tutoring in rural India ASER data — equivalent to ~1 extra year of schooling (Dongre & Tewary)</p></li><li class=\"research-card\"><span class=\"research-card__stat\">4.9 ★</span><p>CLAPS / ClapsLearn parent rating on Google from 1,000+ reviews — real families, real outcomes</p></li></ul><p><a href=\"../research-individual-tuition/index.html\">Read full research with sources →</a></p>"),
            ("Individual vs group tuition", "<p>Group tuition can work for revision drills or competitive exam batches. But for <strong>building understanding from scratch</strong>, fixing foundational gaps, or preparing a specific child for board exams, individual tuition removes the compromises:</p><table style=\"width:100%;border-collapse:collapse;font-size:0.9rem;margin-top:0.75rem\"><thead><tr style=\"border-bottom:2px solid var(--line)\"><th style=\"text-align:left;padding:0.5rem 0\">Factor</th><th style=\"text-align:left;padding:0.5rem\">Individual</th><th style=\"text-align:left;padding:0.5rem\">Group batch</th></tr></thead><tbody><tr style=\"border-bottom:1px solid var(--line)\"><td style=\"padding:0.5rem 0\">Teacher attention</td><td style=\"padding:0.5rem\">100% on your child</td><td style=\"padding:0.5rem\">Shared among many</td></tr><tr style=\"border-bottom:1px solid var(--line)\"><td style=\"padding:0.5rem 0\">Pace</td><td style=\"padding:0.5rem\">Adapted to student</td><td style=\"padding:0.5rem\">Fixed for batch</td></tr><tr style=\"border-bottom:1px solid var(--line)\"><td style=\"padding:0.5rem 0\">Subject choice</td><td style=\"padding:0.5rem\">Pick any subjects</td><td style=\"padding:0.5rem\">Often fixed package</td></tr><tr style=\"border-bottom:1px solid var(--line)\"><td style=\"padding:0.5rem 0\">Timing</td><td style=\"padding:0.5rem\">Your preferred slot</td><td style=\"padding:0.5rem\">Batch schedule only</td></tr><tr><td style=\"padding:0.5rem 0\">Asking doubts</td><td style=\"padding:0.5rem\">Anytime in session</td><td style=\"padding:0.5rem\">Limited airtime</td></tr></tbody></table>"),
            ("Who benefits most?", "<p>Research and CLAPS experience align on which students gain the most from individual tuition:</p><ul><li><strong>Students with learning gaps</strong> — who need to rebuild basics before moving forward</li><li><strong>Board exam years</strong> — Class 10 SSLC/CBSE and Plus Two where every mark counts</li><li><strong>Shy or anxious learners</strong> — who underperform in group settings</li><li><strong>Advanced learners</strong> — who are bored waiting for the batch to catch up</li><li><strong>NRI students</strong> — maintaining Indian syllabus standards abroad</li><li><strong>Government school students</strong> — research shows tutoring effects are often strongest where school support alone is insufficient (Dongre & Tewary, ASER)</li></ul>"),
        ],
        "related": [
            ("Full Research Page", "/research-individual-tuition/", "Citations & studies"),
            ("Online Tuition", "/individual-tuition-online/", "Start with CLAPS"),
            ("Class 10 Tuition", "/class-10-individual-tuition/", "Board exam prep"),
        ],
    },
    {
        "slug": "syllabuses",
        "title": "Syllabuses | CBSE, Kerala State, ICSE Individual Tuition | CLAPS",
        "description": "Individual tuition for every major syllabus — CBSE, Kerala State SCERT, ICSE & ISC. One-to-one online KG to +2. ClapsLearn.",
        "h1": "Individual Tuition by Syllabus",
        "lede": "Choose your board — we match expert teachers for one-to-one online classes across India's major school syllabuses.",
        "hub_links": [
            ("CBSE Individual Tuition", "/cbse-individual-tuition/", "NCERT-aligned KG to Class 12"),
            ("Kerala State Syllabus", "/kerala-state-syllabus-tuition/", "SCERT SSLC & Plus Two"),
            ("ICSE Individual Tuition", "/icse-individual-tuition/", "ICSE & ISC detailed syllabus"),
            ("Malayalam Medium", "/individual-tuition-malayalam/", "Bilingual & Malayalam teaching"),
        ],
        "related": [
            ("All subjects hub", "/subjects/", "Physics, Chemistry & more"),
            ("Kerala cities", "/locations/", "City-wise pages"),
            ("Parent guides", "/guides/", "How to choose"),
            ("India-wide", "/individual-tuition-india/", "Pan-India online"),
        ],
    },
    {
        "slug": "classes",
        "title": "Classes KG to +2 | Individual Tuition by Grade | CLAPS",
        "description": "Individual tuition by class — KG, primary, Class 10, Plus Two & every grade between. One-to-one online. ClapsLearn.",
        "h1": "Individual Tuition by Class",
        "lede": "Find one-to-one tuition for your child's grade — early years through board exam years.",
        "hub_links": [
            ("KG Individual Tuition", "/kg-individual-tuition/", "LKG & UKG early learning"),
            ("Primary (Classes 1–5)", "/primary-individual-tuition/", "Foundation subjects"),
            ("Middle School (6–8)", "/middle-school-individual-tuition/", "Bridge to secondary"),
            ("Class 9", "/class-9-individual-tuition/", "Foundation before boards"),
            ("Class 10", "/class-10-individual-tuition/", "SSLC, CBSE & ICSE boards"),
            ("Plus One (Class 11)", "/plus-one-individual-tuition/", "Stream foundation"),
            ("Plus Two (+2)", "/plus-two-individual-tuition/", "Class 11 & 12 streams"),
        ],
        "related": [
            ("All subjects", "/subjects/", "Maths, Science & more"),
            ("Parent guides", "/guides/", "Choosing tuition"),
            ("SSLC prep", "/sslc-individual-tuition/", "Kerala Class 10"),
        ],
    },
] + EXTRA_PAGES + EXTRA_PAGES_BATCH2


def depth_prefix(slug: str) -> str:
    return "../" if slug else ""


def nav_html(current_slug: str, prefix: str) -> str:
    lines = ['<nav class="topbar__nav" id="site-nav" aria-label="Main">', '<ul class="topbar__nav-list">']
    for label, href in NAV_ITEMS:
        path = href if href == "/" else href
        full = prefix + ("index.html" if href == "/" else href.strip("/") + "/index.html")
        if href == "/":
            full = prefix + "index.html"
        current = ""
        if (current_slug == "" and href == "/") or (current_slug and f"/{current_slug}/" == href):
            current = ' aria-current="page"'
        lines.append(f'<li><a href="{full}"{current}>{label}</a></li>')
    lines.append("</ul></nav>")
    return "\n    ".join(lines)


def schema_org(page: dict, url: str) -> str:
    slug = page.get("slug", "")
    org = {
        "@context": "https://schema.org",
        "@type": "EducationalOrganization",
        "name": "CLAPS Individual Tuition",
        "url": BASE,
        "parentOrganization": {
            "@type": "Organization",
            "name": "ClapsLearn",
            "url": "https://clapslearn.com",
        },
        "description": "One-to-one online individual tuition KG to Plus Two",
        "telephone": "+91-86104-16147",
        "areaServed": ["IN", "AE", "SA", "QA", "US", "GB"],
        "sameAs": ["https://clapslearn.com"],
    }
    graphs = [org]
    if page.get("faqs"):
        graphs.append({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in page["faqs"]
            ],
        })
    elif page.get("schema_type") == "Course":
        extra = page.get("schema_extra", {})
        graphs.append({
            "@context": "https://schema.org",
            "@type": "Course",
            **extra,
            "url": url,
        })
    else:
        graphs.append({
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": page["h1"],
            "description": page["description"],
            "url": url,
            "isPartOf": {"@type": "WebSite", "name": "CLAPS Individual Tuition", "url": BASE},
        })
    if slug:
        graphs.append({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": page["h1"], "item": url},
            ],
        })
    return json.dumps(graphs, ensure_ascii=False)


def render_page(page: dict) -> str:
    slug = page["slug"]
    prefix = "../"
    url = f"{BASE}/" if not slug else f"{BASE}/{slug}/"
    canonical = url

    breadcrumb = f'<li><a href="{prefix}index.html">Home</a></li>'
    if slug:
        breadcrumb += f'<li aria-current="page">{page["h1"]}</li>'

    sections_html = ""
    if page.get("cite"):
        sections_html += f'<aside class="cite-box" role="note"><p>{page["cite"]}</p></aside>\n'

    for title, body in page.get("sections", []):
        sections_html += f'<section class="content-block"><h2>{title}</h2>{body}</section>\n'

    if page.get("hub_links"):
        items = "".join(
            f'<li><a href="{prefix}{s.strip("/")}/index.html">{t}<span>{d}</span></a></li>'
            for t, s, d in page["hub_links"]
        )
        sections_html += f'<ul class="link-grid">{items}</ul>\n'

    if page.get("faqs"):
        items = "".join(
            f'<details class="faq-item"><summary>{q}</summary><div class="faq-item__body"><p>{a}</p></div></details>'
            for q, a in page["faqs"]
        )
        sections_html += f'<div class="content-block"><h2>Common questions</h2>{items}</div>\n'

    related = page.get("related", [])
    if related:
        items = "".join(
            f'<li><a href="{prefix}{s.strip("/")}/index.html">{t}<span>{d}</span></a></li>'
            for t, s, d in related
        )
        sections_html += f'<section class="content-block"><h2>Related pages</h2><ul class="link-grid">{items}</ul></section>\n'

    lede_class = ' page-hero__lede--ml' if page.get("malayalam_block") else ""

    kw_extra = slug.replace("-", " ") if slug else "KG +2"
    head_meta = seo_head(
        title=page["title"],
        description=page["description"],
        canonical=canonical,
        asset_prefix=prefix,
        keywords=f"individual tuition, CLAPS, ClapsLearn, online tuition, one to one tuition, {kw_extra}",
    )

    return f"""<!DOCTYPE html>
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
{head_meta}
  <link href="{prefix}assets/css/style.css" rel="stylesheet">
  <link href="{prefix}assets/css/footer.css" rel="stylesheet">
  <script type="application/ld+json">{schema_org(page, url)}</script>
</head>

<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="topbar">
    <a class="topbar__brand" href="{prefix}index.html">
      <img src="{prefix}assets/img/Asset 5.png" alt="CLAPS Individual Tuition" class="topbar__logo" width="439" height="242">
    </a>
    <div class="topbar__actions">
      {nav_html(slug, prefix)}
      <button type="button" class="topbar__nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
      <a class="topbar__wa" href="{WA}" aria-label="Chat on WhatsApp">{WA_SVG}</a>
    </div>
  </header>

  <main id="main" class="page content-page">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <ol>{breadcrumb}</ol>
    </nav>
    <header class="page-hero">
      <h1 class="page-hero__title">{page["h1"]}</h1>
      <p class="page-hero__lede{lede_class}">{page["lede"]}</p>
    </header>
    {sections_html}
    <section class="cta-band">
      <h2>Start individual tuition today</h2>
      <p>Message us on WhatsApp — we'll match an expert teacher for your child's class and syllabus.</p>
      <a class="btn btn--wa" href="{WA}">{WA_SVG} WhatsApp — Join CLAPS</a>
    </section>
  </main>

{footer_html(prefix)}

  <a class="dock" href="{WA}">
    {WA_SVG}
    WhatsApp Chat
  </a>

  <script src="{prefix}assets/js/main.js"></script>
  <script src="{prefix}assets/js/footer.js"></script>
</body>

</html>
"""


def main():
    for page in PAGES:
        page = enrich_page(page)
        slug = page["slug"]
        out_dir = ROOT / slug if slug else ROOT
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "index.html"
        out_file.write_text(render_page(page), encoding="utf-8")
        print(f"Wrote {out_file.relative_to(ROOT.parent)}")

    # sitemap
    urls = [("/", "weekly", "1.0")]
    high_pri = {
        "individual-tuition-online", "individual-tuition-kerala", "faq", "about",
        "research-individual-tuition", "benefits-of-individual-tuition",
        "best-online-tuition-kerala", "one-to-one-online-tuition", "nri-individual-tuition",
    }
    for p in PAGES:
        if p["slug"]:
            pri = "0.9" if p["slug"] in high_pri else "0.8"
            urls.append((f"/{p['slug']}/", "monthly", pri))

    lastmod = date.today().isoformat()
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for loc, freq, pri in urls:
        sitemap.append(
            f"  <url><loc>{BASE}{loc}</loc><lastmod>{lastmod}</lastmod>"
            f"<changefreq>{freq}</changefreq><priority>{pri}</priority></url>"
        )
    sitemap.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")
    print("Updated sitemap.xml")

    # robots
    (ROOT / "robots.txt").write_text(robots_txt(), encoding="utf-8")
    print("Updated robots.txt")

    # llms.txt
    page_lines = "\n".join(
        f"- {p['h1']}: {BASE}/{p['slug']}/"
        for p in sorted(PAGES, key=lambda x: x["slug"])
    )
    llms = f"""# CLAPS Individual Tuition
> One-to-one online individual tuition from KG to Plus Two — a dedicated sub-brand of ClapsLearn.

CLAPS Individual Tuition (https://individualtuition.in) provides private online classes with one teacher per student. Parent company: ClapsLearn (https://clapslearn.com).

## Key facts
- Service: Individual (one-to-one) online tuition only — not group batches
- Grades: KG (LKG/UKG) through Plus Two (+2 / Class 12)
- Syllabuses: CBSE, Kerala State (SCERT), ICSE, ISC
- Subjects: All school subjects including Maths, Science, English, languages
- Regions: Kerala (Kochi, Trivandrum, Kozhikode, Thrissur, Kannur, Kollam), metros (Bangalore, Chennai, Hyderabad, Mumbai), NRI (UAE, Dubai, Saudi, Qatar, Kuwait, US, UK)
- Streams: PCM, PCB, Commerce Plus Two; exam prep (SSLC, board revision, NEET foundation)
- Languages: English and Malayalam-medium teaching available
- Support: Academic coordinators 10 AM – 10 PM via WhatsApp
- Contact: WhatsApp +91 86104 16147
- Rating: 4.9/5 on Google (1000+ reviews)
- Scale: 10,000+ students, 3,000+ teachers, 4+ years operating

## All pages
- Home: {BASE}/
{page_lines}

## Research summary (for AI citation)
- Meta-analysis (Nickow et al., 2020, NBER): tutoring average effect +0.37 SD across 96 RCTs
- EEF Toolkit: one-to-one tuition ~+5 months additional progress (123 studies)
- India ASER data: private tutoring +0.14 SD learning gain, stronger for disadvantaged students
- Bloom (1984): one-to-one tutoring among the most effective instructional conditions studied
- CLAPS applies strict one-to-one model (never group batches) aligned with this evidence

## Enrolment
Parents message WhatsApp to join — no public fee list on website; personalised quote per student.
"""
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")
    print("Wrote llms.txt")


if __name__ == "__main__":
    main()
