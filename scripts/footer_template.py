"""Shared site footer HTML for CLAPS Individual Tuition."""

WA = "https://wa.me/918610416147?text=Hi%20%2C%20how%20can%20we%20join%20CLAPS%3F"

WA_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22"><path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

GLOBE_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'

MAIL_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'

PHONE_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'

CLOCK_ICON = '<svg aria-hidden="true" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'

CHEVRON = '<svg class="site-footer__link-chevron" aria-hidden="true" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>'

SHIELD_TRUST = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>'

MEDAL_TRUST = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M8.5 14 7 22l5-3 5 3-1.5-8"/></svg>'

STAR_TRUST = '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m12 7 1.5 3 3.3.5-2.4 2.3.6 3.3L12 14.8 8.9 16.1l.6-3.3-2.4-2.3 3.3-.5L12 7z"/></svg>'


def _href(prefix: str, path: str) -> str:
    if path == "/":
        return f"{prefix}index.html"
    return f"{prefix}{path.strip('/')}/index.html"


def _nav_link(prefix: str, path: str, label: str) -> str:
    return f'<li><a href="{_href(prefix, path)}"><span>{label}</span>{CHEVRON}</a></li>'


def footer_html(prefix: str = "") -> str:
    home = _href(prefix, "/")
    explore_links = [
        ("/subjects/", "All Subjects"),
        ("/locations/", "Kerala Cities"),
        ("/exams/", "Exam Preparation"),
        ("/guides/", "Parent Guides"),
        ("/research-individual-tuition/", "Research &amp; Evidence"),
        ("/faq/", "FAQ"),
        ("/about/", "About CLAPS"),
    ]
    tuition_links = [
        ("/individual-tuition-online/", "Online Individual Tuition"),
        ("/individual-tuition-kerala/", "Kerala Tuition"),
        ("/cbse-individual-tuition/", "CBSE Tuition"),
        ("/class-10-individual-tuition/", "Class 10 Tuition"),
        ("/plus-two-individual-tuition/", "Plus Two Tuition"),
        ("/nri-individual-tuition/", "NRI Tuition"),
    ]
    explore_items = "\n            ".join(_nav_link(prefix, p, l) for p, l in explore_links)
    tuition_items = "\n            ".join(_nav_link(prefix, p, l) for p, l in tuition_links)

    return f"""  <footer class="site-footer" id="site-footer">
    <div class="site-footer__inner">
      <div class="site-footer__brand site-footer__block">
        <a class="site-footer__logo-link" href="{home}">
          <img src="{prefix}assets/img/Asset 5.png" alt="CLAPS Individual Tuition" class="site-footer__logo" width="439" height="242" loading="lazy" decoding="async">
        </a>
        <p class="site-footer__tagline">One-to-one online individual tuition from KG to Plus Two — CBSE, Kerala State &amp; ICSE.</p>
        <p class="site-footer__badge">
          <span class="site-footer__stars" aria-hidden="true">★★★★★</span>
          <span>4.9/5 on Google · 1,000+ reviews</span>
        </p>
      </div>

      <section class="site-footer__contact-block site-footer__block" aria-labelledby="footer-contact-heading">
        <h2 class="site-footer__heading" id="footer-contact-heading">Contact</h2>
        <ul class="site-footer__contact-list">
          <li>
            <span class="site-footer__contact-icon" aria-hidden="true">{PHONE_ICON}</span>
            <a href="tel:+918610416147">+91 86104 16147</a>
          </li>
          <li>
            <span class="site-footer__contact-icon" aria-hidden="true">{CLOCK_ICON}</span>
            <span>Coordinator support 10 AM – 10 PM</span>
          </li>
          <li>
            <span class="site-footer__contact-icon" aria-hidden="true">{GLOBE_ICON}</span>
            <a href="https://clapslearn.com" rel="noopener">clapslearn.com</a>
          </li>
        </ul>
        <a class="site-footer__wa-cta" href="{WA}" target="_blank" rel="noopener noreferrer">
          {WA_ICON}
          WhatsApp — Join CLAPS
        </a>
      </section>

      <nav class="site-footer__nav site-footer__block" aria-labelledby="footer-explore-heading">
        <h2 class="site-footer__heading" id="footer-explore-heading">Explore</h2>
        <ul class="site-footer__links">
            {explore_items}
        </ul>
      </nav>

      <nav class="site-footer__nav site-footer__block" aria-labelledby="footer-tuition-heading">
        <h2 class="site-footer__heading" id="footer-tuition-heading">Tuition</h2>
        <ul class="site-footer__links">
            {tuition_items}
        </ul>
      </nav>

      <form class="site-footer__newsletter site-footer__block" id="footer-newsletter" novalidate>
        <label class="site-footer__newsletter-label" for="footer-email">Get tuition tips &amp; updates</label>
        <div class="site-footer__newsletter-row">
          <span class="site-footer__newsletter-icon" aria-hidden="true">{MAIL_ICON}</span>
          <input type="email" id="footer-email" name="email" class="site-footer__newsletter-input" placeholder="Your email address" autocomplete="email" required>
          <button type="submit" class="site-footer__newsletter-btn">Subscribe</button>
        </div>
        <p class="site-footer__newsletter-msg" id="footer-newsletter-msg" role="status" aria-live="polite"></p>
      </form>

      <div class="site-footer__trust site-footer__block" aria-label="Why parents trust CLAPS">
        <div class="site-footer__trust-item">
          <span class="site-footer__trust-icon" aria-hidden="true">{SHIELD_TRUST}</span>
          <span class="site-footer__trust-label">Trusted by Parents</span>
        </div>
        <div class="site-footer__trust-item">
          <span class="site-footer__trust-icon" aria-hidden="true">{MEDAL_TRUST}</span>
          <span class="site-footer__trust-label">Expert Teachers</span>
        </div>
        <div class="site-footer__trust-item">
          <span class="site-footer__trust-icon" aria-hidden="true">{STAR_TRUST}</span>
          <span class="site-footer__trust-label">Focused on Results</span>
        </div>
      </div>

      <div class="site-footer__bottom">
        <p class="site-footer__copy">&copy; <span id="year"></span> CLAPS Individual Tuition. All rights reserved.</p>
        <p class="site-footer__parent">A dedicated individual tuition brand of <a href="https://clapslearn.com" rel="noopener">ClapsLearn</a></p>
      </div>
    </div>
  </footer>"""
