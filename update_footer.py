import codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

html = html.replace('2024</p>', '2026</p>')
html = html.replace('Open to opportunities 🚀', 'Open to opportunities')

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Footer updated!")
