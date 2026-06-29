// Hamburger nav toggle
const toggle = document.querySelector('.nav-toggle');
const nav = document.getElementById('main-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen);
  });

  // Close nav when a link is tapped on mobile
  nav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// Touch-friendly hover on project cards (toggle on tap for mobile)
if ('ontouchstart' in window) {
  document.querySelectorAll('.project-card:not(.placeholder)').forEach(card => {
    card.addEventListener('click', () => {
      card.classList.toggle('touch-active');
    });
  });
}
