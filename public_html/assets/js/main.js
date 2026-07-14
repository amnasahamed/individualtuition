document.getElementById("year").textContent = new Date().getFullYear();

const navToggle = document.querySelector(".topbar__nav-toggle");
const nav = document.querySelector(".topbar__nav");

if (navToggle && nav) {
  navToggle.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const heroMarquee = document.querySelector(".hero__cards-marquee");
const heroTrack = document.querySelector(".hero__cards-track");
const heroCardsSet = heroTrack?.querySelector(".hero__cards");

if (heroMarquee && heroTrack && heroCardsSet) {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!reducedMotion) {
    heroCardsSet.querySelectorAll(".hero-card").forEach((card) => {
      const copy = card.cloneNode(true);
      copy.setAttribute("aria-hidden", "true");
      heroCardsSet.appendChild(copy);
    });
    heroMarquee.classList.add("is-active");
  }
}
