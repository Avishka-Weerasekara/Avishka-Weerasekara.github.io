import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# Replace project github links
old_link = '<a href="#" target="_blank" aria-label="GitHub" class="project-link">'
new_link = '<a href="https://github.com/Avishka-Weerasekara?tab=repositories" target="_blank" aria-label="GitHub" class="project-link">'
html = html.replace(old_link, new_link)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Links updated!")
