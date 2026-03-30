import re, codecs

with codecs.open('index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Remove Featured
html = html.replace('<div class="project-badge">⭐ Featured</div>', '')
html = html.replace('class="project-card featured"', 'class="project-card"')
html = html.replace('<h2 class="section-title">Featured <span class="gradient-text">Projects</span></h2>', '<h2 class="section-title">My <span class="gradient-text">Projects</span></h2>')

# 2. Add real icons to 'Get In Touch' replacing emojis
# 📧 -> email svg
email_svg = '<svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/></svg>'
html = html.replace('<div class="contact-icon">📧</div>', f'<div class="contact-icon">{email_svg}</div>')

# 📱 -> phone svg
phone_svg = '<svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M17 1H7c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-2-2-2zm0 18H7V5h10v14z"/></svg>'
html = html.replace('<div class="contact-icon">📱</div>', f'<div class="contact-icon">{phone_svg}</div>')

# 🐙 -> github devicon or svg
github_svg = '<i class="devicon-github-original" style="font-size: 24px;"></i>'
html = html.replace('<div class="contact-icon">🐙</div>', f'<div class="contact-icon">{github_svg}</div>')

# 💼 -> linkedin svg
linkedin_svg = '<svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.13 1.44-2.13 2.94v5.67H9.38V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.59 0 4.25 2.36 4.25 5.44v6.3zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45C23.21 24 24 23.23 24 22.27V1.73C24 .77 23.21 0 22.22 0z"/></svg>'
html = html.replace('<div class="contact-icon">💼</div>', f'<div class="contact-icon">{linkedin_svg}</div>')

# 3. Update the form to FormSubmit
old_form = '<form class="contact-form" id="contact-form">'
new_form = '<form action="https://formsubmit.co/avish20weerasekara@gmail.com" method="POST" class="contact-form" id="contact-form">\n          <input type="hidden" name="_captcha" value="false">'
html = html.replace(old_form, new_form)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)

print("HTML modified!")
