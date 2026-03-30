import codecs

with codecs.open('script.js', 'r', 'utf-8') as f:
    js = f.read()

import re
pattern = r'const startScroll = \(\) => \{.+?(?=\n\s*\})'
# We will just replace everything from const startScroll = () => { to the end of the projectsGrid if block.
# Actually, it's easier to just split by const startScroll = () => {
parts = js.split('const startScroll = () => {')
prefix = parts[0]

new_logic = '''const cards = Array.from(projectsGrid.children);
  cards.forEach(card => projectsGrid.appendChild(card.cloneNode(true)));

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
'''

new_js = prefix + new_logic

with codecs.open('script.js', 'w', 'utf-8') as f:
    f.write(new_js)

print("Infinite loop logic injected!")
