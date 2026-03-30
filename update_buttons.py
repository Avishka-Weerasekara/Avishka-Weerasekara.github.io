import re, codecs

with codecs.open('script.js', 'r', 'utf-8') as f:
    js = f.read()

append_logic = '''  
  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');

  if (prevBtn && nextBtn) {
      prevBtn.addEventListener('click', () => {
          clearInterval(scrollInterval);
          const card = projectsGrid.querySelector('.project-card');
          const shift = card ? card.offsetWidth + 24 : 344;
          let target = projectsGrid.scrollLeft - shift;
          if (target < 0) target = projectsGrid.scrollWidth - projectsGrid.clientWidth;
          smoothScrollTo(projectsGrid, target, 800);
          scrollInterval = startScroll();
      });

      nextBtn.addEventListener('click', () => {
          clearInterval(scrollInterval);
          const card = projectsGrid.querySelector('.project-card');
          const shift = card ? card.offsetWidth + 24 : 344;
          let target = projectsGrid.scrollLeft + shift;
          if (target + projectsGrid.clientWidth >= projectsGrid.scrollWidth - 10) target = 0;
          smoothScrollTo(projectsGrid, target, 800);
          scrollInterval = startScroll();
      });
  }
}'''

js = js.replace('  projectsGrid.addEventListener(\'touchend\', () => scrollInterval = startScroll());\n}', '  projectsGrid.addEventListener(\'touchend\', () => scrollInterval = startScroll());\n' + append_logic)

with codecs.open('script.js', 'w', 'utf-8') as f:
    f.write(js)

print("JS added manually slider functionality!")
