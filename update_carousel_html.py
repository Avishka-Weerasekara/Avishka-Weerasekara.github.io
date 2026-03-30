import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:    html = f.read()

html = html.replace('<div class="projects-grid">', '''<div class="carousel-wrapper">
        <button class="carousel-btn prev-btn" aria-label="Previous project">❮</button>
        <button class="carousel-btn next-btn" aria-label="Next project">❯</button>
        <div class="projects-grid">''')

html = html.replace('      </div>\n    </div>\n  </section>', '      </div>\n      </div>\n    </div>\n  </section>')

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("HTML structure updated for carousel buttons!")
