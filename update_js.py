import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_logic = "projectsGrid.scrollBy({ left: 344, behavior: 'smooth' });"
new_logic = '''const card = projectsGrid.querySelector('.project-card');
        const shift = card ? card.offsetWidth + 24 : 344;
        projectsGrid.scrollBy({ left: shift, behavior: 'smooth' });'''

js = js.replace(old_logic, new_logic)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS updated successfully!")
