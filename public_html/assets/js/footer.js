/**
 * CLAPS site footer — scroll reveal & newsletter form
 */
(() => {
  "use strict";

  const footer = document.getElementById("site-footer");
  if (!footer) return;

  const cols = footer.querySelectorAll(".site-footer__block");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reducedMotion) {
    cols.forEach((col) => col.classList.add("is-visible"));
  } else {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { root: null, rootMargin: "0px 0px -40px 0px", threshold: 0.12 }
    );
    cols.forEach((col) => observer.observe(col));
  }

  const form = document.getElementById("footer-newsletter");
  const emailInput = document.getElementById("footer-email");
  const msgEl = document.getElementById("footer-newsletter-msg");
  const waBase = "https://wa.me/918610416147?text=";

  if (form && emailInput && msgEl) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const email = emailInput.value.trim();

      if (!email || !emailInput.checkValidity()) {
        emailInput.focus();
        msgEl.textContent = "Please enter a valid email address.";
        msgEl.className = "site-footer__newsletter-msg is-error";
        return;
      }

      const text = encodeURIComponent(
        `Hi, I'd like to receive CLAPS individual tuition updates. My email: ${email}`
      );
      msgEl.textContent = "Opening WhatsApp to confirm your subscription…";
      msgEl.className = "site-footer__newsletter-msg is-success";
      window.open(`${waBase}${text}`, "_blank", "noopener,noreferrer");
      form.reset();
    });
  }
})();
