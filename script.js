/* ============================================================
   PORTFOLIO JAVASCRIPT
   ============================================================ */

// ---- NAVBAR SCROLL ----
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
  highlightActiveNav();
});

// ---- HAMBURGER MENU ----
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('nav-links');

hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  const spans = hamburger.querySelectorAll('span');
  if (navLinks.classList.contains('open')) {
    spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
    spans[1].style.opacity   = '0';
    spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
  } else {
    spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  }
});

navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.querySelectorAll('span').forEach(s => {
      s.style.transform = ''; s.style.opacity = '';
    });
  });
});

// ---- ACTIVE NAV HIGHLIGHT ----
function highlightActiveNav() {
  const sections = document.querySelectorAll('section[id]');
  const scrollY  = window.scrollY + 100;
  sections.forEach(sec => {
    const top    = sec.offsetTop;
    const height = sec.offsetHeight;
    const id     = sec.getAttribute('id');
    const link   = document.querySelector(`.nav-links a[href="#${id}"]`);
    if (link) {
      link.classList.toggle('active', scrollY >= top && scrollY < top + height);
    }
  });
}

// ---- TYPED TEXT EFFECT ----
const phrases = [
  'Computer Engineering Undergraduate',
  'Problem Solver',
  'Tech Enthusiast',
  'Continuous Learner'
];
let phraseIdx = 0, charIdx = 0, deleting = false;
const typedEl = document.getElementById('typed-text');

function type() {
  const current = phrases[phraseIdx];
  if (deleting) {
    typedEl.innerHTML = current.slice(0, charIdx - 1) + '<span class="cursor">|</span>';
    charIdx--;
    if (charIdx === 0) {
      deleting = false;
      phraseIdx = (phraseIdx + 1) % phrases.length;
      setTimeout(type, 400);
      return;
    }
    setTimeout(type, 50);
  } else {
    typedEl.innerHTML = current.slice(0, charIdx + 1) + '<span class="cursor">|</span>';
    charIdx++;
    if (charIdx === current.length) {
      deleting = true;
      setTimeout(type, 2000);
      return;
    }
    setTimeout(type, 90);
  }
}
type();

// ---- PARTICLE CANVAS ----
const canvas  = document.getElementById('particles-canvas');
const ctx     = canvas.getContext('2d');
let particles = [];

function resizeCanvas() {
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

class Particle {
  constructor() { this.reset(); }
  reset() {
    this.x     = Math.random() * canvas.width;
    this.y     = Math.random() * canvas.height;
    this.size  = Math.random() * 2 + 0.5;
    this.speedX = (Math.random() - 0.5) * 0.4;
    this.speedY = (Math.random() - 0.5) * 0.4;
    this.opacity = Math.random() * 0.5 + 0.2;
    const colors = ['#6c63ff','#a855f7','#06b6d4'];
    this.color  = colors[Math.floor(Math.random() * colors.length)];
  }
  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    if (this.x < 0 || this.x > canvas.width ||
        this.y < 0 || this.y > canvas.height) this.reset();
  }
  draw() {
    ctx.save();
    ctx.globalAlpha = this.opacity;
    ctx.fillStyle   = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

for (let i = 0; i < 80; i++) particles.push(new Particle());

// draw connections
function drawConnections() {
  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      const dx   = particles[i].x - particles[j].x;
      const dy   = particles[i].y - particles[j].y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 120) {
        ctx.save();
        ctx.globalAlpha = (1 - dist / 120) * 0.12;
        ctx.strokeStyle = '#6c63ff';
        ctx.lineWidth   = 0.5;
        ctx.beginPath();
        ctx.moveTo(particles[i].x, particles[i].y);
        ctx.lineTo(particles[j].x, particles[j].y);
        ctx.stroke();
        ctx.restore();
      }
    }
  }
}

function animateParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => { p.update(); p.draw(); });
  drawConnections();
  requestAnimationFrame(animateParticles);
}
animateParticles();

// ---- SCROLL REVEAL ----
const revealEls = document.querySelectorAll(
  '.about-grid, .skill-category, .project-card, .contact-grid, .section-header'
);
revealEls.forEach(el => el.classList.add('reveal'));

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

revealEls.forEach(el => observer.observe(el));

// ---- CONTACT FORM ----
const form      = document.getElementById('contact-form');
const submitBtn = document.getElementById('submit-btn');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  submitBtn.textContent = 'Sending…';
  submitBtn.disabled    = true;

  fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: {
          'Accept': 'application/json'
      }
  })
  .then(response => {
    if (response.ok) {
        form.reset();
        submitBtn.textContent = 'Message Sent! ✅';
        showToast('✅ Message sent successfully!');
    } else {
        submitBtn.textContent = 'Error ❌';
        showToast('❌ Failed to send message.');
    }
  })
  .catch(error => {
    submitBtn.textContent = 'Error ❌';
    showToast('❌ Failed to send message.');
  })
  .finally(() => {
    setTimeout(() => {
        submitBtn.textContent = 'Send Message ✉️';
        submitBtn.disabled    = false;
    }, 3000);
  });
});

// ---- TOAST ----
function showToast(msg) {
  let toast = document.querySelector('.toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3500);
}

// ---- SKILL CARD RIPPLE ----
document.querySelectorAll('.skill-card').forEach(card => {
  card.addEventListener('mouseenter', () => {
    card.style.transition = 'transform 0.2s, box-shadow 0.2s, border-color 0.2s, background 0.2s';
  });
});

// Resume download functions automatically via HTML element

// ---- SMOOTH CURSOR TRAIL (subtle) ----
let mouseX = 0, mouseY = 0;
const trail = document.createElement('div');
trail.style.cssText = `
  position: fixed; pointer-events: none; z-index: 9998;
  width: 200px; height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(108,99,255,0.06) 0%, transparent 70%);
  transform: translate(-50%, -50%);
  transition: left 0.15s ease, top 0.15s ease;
  left: -200px; top: -200px;
`;
document.body.appendChild(trail);

document.addEventListener('mousemove', (e) => {
  trail.style.left = e.clientX + 'px';
  trail.style.top  = e.clientY + 'px';
});


// Auto-scroll projects with custom ultra-smooth easing
const projectsGrid = document.querySelector('.projects-grid');
if (projectsGrid) {
  function smoothScrollTo(element, target, duration) {
    target = Math.round(target);
    const start = element.scrollLeft;
    const change = target - start;
    const startTime = performance.now();

    function easeInOutQuad(t, b, c, d) {
      t /= d / 2;
      if (t < 1) return c / 2 * t * t + b;
      t--;
      return -c / 2 * (t * (t - 2) - 1) + b;
    }

    function animateScroll(currentTime) {
      const timeElapsed = currentTime - startTime;
      const amount = easeInOutQuad(timeElapsed, start, change, duration);
      element.scrollLeft = amount;
      if (timeElapsed < duration) {
        requestAnimationFrame(animateScroll);
      } else {
        element.scrollLeft = target;
      }
    }
    requestAnimationFrame(animateScroll);
  }

  const cards = Array.from(projectsGrid.children);
  cards.forEach(card => {
    const clone = card.cloneNode(true);
    clone.classList.remove('reveal');
    clone.classList.add('visible');
    clone.style.opacity = '1';
    clone.style.transform = 'none';
    projectsGrid.appendChild(clone);
  });

  const startScroll = () => {
    return setInterval(() => {
      const card = projectsGrid.querySelector('.project-card');
      const shift = card ? card.offsetWidth + 24 : 344;
      const originalLengthPx = shift * cards.length;
      
      if (projectsGrid.scrollLeft >= originalLengthPx) {
         projectsGrid.scrollLeft -= originalLengthPx;
      }
      smoothScrollTo(projectsGrid, projectsGrid.scrollLeft + shift, 1200);
    }, 5000);
  };
  
  let scrollInterval = startScroll();

  projectsGrid.addEventListener('mouseenter', () => clearInterval(scrollInterval));
  projectsGrid.addEventListener('mouseleave', () => scrollInterval = startScroll());
  projectsGrid.addEventListener('touchstart', () => clearInterval(scrollInterval));
  projectsGrid.addEventListener('touchend', () => scrollInterval = startScroll());

  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');

  if (prevBtn && nextBtn) {
      prevBtn.addEventListener('click', () => {
          clearInterval(scrollInterval);
          const card = projectsGrid.querySelector('.project-card');
          const shift = card ? card.offsetWidth + 24 : 344;
          const originalLengthPx = shift * cards.length;
          
          if (projectsGrid.scrollLeft <= 5) { // 5px buffer
              projectsGrid.scrollLeft += originalLengthPx;
          }
          smoothScrollTo(projectsGrid, projectsGrid.scrollLeft - shift, 800);
          scrollInterval = startScroll();
      });

      nextBtn.addEventListener('click', () => {
          clearInterval(scrollInterval);
          const card = projectsGrid.querySelector('.project-card');
          const shift = card ? card.offsetWidth + 24 : 344;
          const originalLengthPx = shift * cards.length;
          
          if (projectsGrid.scrollLeft >= originalLengthPx - 5) { // 5px buffer
              projectsGrid.scrollLeft -= originalLengthPx;
          }
          smoothScrollTo(projectsGrid, projectsGrid.scrollLeft + shift, 800);
          scrollInterval = startScroll();
      });
  }
}
