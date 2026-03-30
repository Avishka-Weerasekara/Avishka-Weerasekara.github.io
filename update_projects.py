import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

projects_data = [
    {
        "title": "Loom – Online Clothing Store",
        "desc": "Designed and developed a full-stack e-commerce application integrating Stripe payment for secure online transactions. Implemented RESTful APIs and user authentication.",
        "tags": ["React", "JavaScript", "Tailwind CSS", "MongoDB", "Vercel"],
        "featured": True
    },
    {
        "title": "Bliss & Bite – RMS",
        "desc": "Developed a MERN stack web application deployed on Vercel, and a .NET-based desktop application using Microsoft SQL Server for order, inventory, and customer management.",
        "tags": ["MERN", ".NET", "C#", "MS SQL", "Vercel"],
        "featured": True
    },
    {
        "title": "DevOps Automation Pipeline",
        "desc": "Designed a CI/CD pipeline using Jenkins to automate build/deployment processes. Containerized applications using Docker and provisioned AWS infrastructure via Terraform.",
        "tags": ["Jenkins", "Docker", "AWS", "Terraform", "WSL"],
        "featured": True
    },
    {
        "title": "QA Testing Project",
        "desc": "Implemented TDD/BDD practices, developed automated UI tests using Selenium, and API tests with Postman. Conducted load testing with JMeter and integrated into a CI/CD pipeline.",
        "tags": ["Selenium", "JMeter", "Postman", "TDD", "OWASP"],
        "featured": False
    },
    {
        "title": "Multi-User Task Manager",
        "desc": "Developed a client–server application enabling multiple users to manage tasks concurrently utilizing network programming and operating system concepts.",
        "tags": ["Network Programming", "C", "Client-Server"],
        "featured": False
    },
    {
        "title": "AI Dermatology Diagnostics system",
        "desc": "Developed an AI-based skin disease detection system using the U-Net++ model to segment and analyze dermatological images. Showcased at the Rextro Exhibition.",
        "tags": ["AI", "U-Net++", "Image Processing", "Python"],
        "featured": False
    },
    {
        "title": "Bus Stop Electronic Time Table",
        "desc": "Built an ESP32 IoT system integrating GPS and GSM to track real-time bus locations and predict arrival. Includes a Vercel/Firebase web app and admin management dashboard.",
        "tags": ["ESP32", "GPS/GSM", "IoT", "Firebase", "Web App"],
        "featured": True
    },
    {
        "title": "RFID-Based Attendance System",
        "desc": "Designing an Embedded C system using ESP32 and RFID to automate attendance tracking. Features UID verification via cloud-based Google Sheets API and live hardware feedback.",
        "tags": ["Embedded C", "ESP32", "RFID", "Google Sheets"],
        "featured": False
    },
    {
        "title": "Water Quality Monitoring",
        "desc": "Developed an embedded system using sensors (temperature, turbidity, conductivity, pH) and ADC-based data acquisition for real-time environmental monitoring.",
        "tags": ["Embedded", "Sensors", "ADC", "Microcontroller"],
        "featured": False
    },
    {
        "title": "Arduino-Based Robotic Trolley",
        "desc": "Designed and developed a microcontroller-based robotic system incorporating motor drivers, sensor integration, and complete logic control for movement and obstacle handling.",
        "tags": ["Arduino", "Robotics", "Motor Drivers", "Sensors"],
        "featured": False
    }
]

svg_github = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.44 9.8 8.21 11.39.6.11.82-.26.82-.58 0-.28-.01-1.02-.01-2-3.34.73-4.04-1.61-4.04-1.61-.54-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73 1.2.09 1.84 1.24 1.84 1.24 1.07 1.83 2.8 1.3 3.49 1 .11-.78.42-1.3.76-1.6-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 3-.4c1.02 0 2.04.14 3 .4 2.29-1.55 3.3-1.23 3.3-1.23.66 1.66.25 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.61-2.81 5.63-5.48 5.92.43.37.81 1.1.81 2.22 0 1.6-.01 2.9-.01 3.29 0 .32.22.7.83.58z"/></svg>'
svg_folder = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>'

grid_html = '<div class="projects-grid">\n'
for i, p in enumerate(projects_data):
    featured_class = " featured" if p["featured"] else ""
    badge_html = '<div class="project-badge">⭐ Featured</div>' if p["featured"] else ""
    
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in p["tags"]])
    
    card = f'''
        <div class="project-card{featured_class}" id="project-{i+1}">
          {badge_html}
          <div class="project-header">
            <div class="project-icons">{svg_folder}</div>
            <div class="project-links">
              <a href="#" target="_blank" aria-label="GitHub" class="project-link">{svg_github}</a>
            </div>
          </div>
          <h3 class="project-title">{p["title"]}</h3>
          <p class="project-description">{p["desc"]}</p>
          <div class="project-tags">{tags_html}</div>
        </div>'''
    grid_html += card + '\n'
grid_html += '      </div>'

new_html = re.sub(r'<div class="projects-grid">.*?</div>\s*</div>\s*</section>', grid_html + '\n    </div>\n  </section>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML Replaced successfully!")
