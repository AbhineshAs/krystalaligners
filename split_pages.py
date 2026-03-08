import os
import re

base_dir = "d:/Krystalaligners"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

nav_old = """                <ul class="navbar-nav ms-auto fw-medium">
                    <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="#treatments">Treatments</a></li>

                    <li class="nav-item"><a class="nav-link" href="#testimonials">Testimonials</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                </ul>"""
nav_new = """                <ul class="navbar-nav ms-auto fw-medium">
                    <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="treatments.html">Treatments</a></li>
                    <li class="nav-item"><a class="nav-link" href="testimonials.html">Testimonials</a></li>
                    <li class="nav-item"><a class="nav-link" href="index.html#contact">Contact</a></li>
                </ul>"""
html = html.replace(nav_old, nav_new)

foot_old = """                    <ul class="list-unstyled footer-links text-white-50 small d-flex flex-column gap-2">
                        <li><a href="#home">Home</a></li>
                        <li><a href="#about">About</a></li>
                        <li><a href="#how-it-works">Process</a></li>
                        <li><a href="#testimonials">Reviews</a></li>
                        <li><a href="#contact">Contact</a></li>
                    </ul>"""
foot_new = """                    <ul class="list-unstyled footer-links text-white-50 small d-flex flex-column gap-2">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About</a></li>
                        <li><a href="treatments.html">Treatments</a></li>
                        <li><a href="testimonials.html">Reviews</a></li>
                        <li><a href="index.html#contact">Contact</a></li>
                    </ul>"""
html = html.replace(foot_old, foot_new)

scroll_old = """    <!-- Scroll To Top Button -->
    <a href="#" id="scrollTop"
        class="bg-teal text-white rounded-circle shadow d-flex align-items-center justify-content-center position-fixed bottom-0 end-0 mb-4 me-4"
        style="width: 50px; height: 50px; opacity: 0; pointer-events: none; transition: 0.3s z-index: 1000; text-decoration: none;">
        <i class="fa-solid fa-arrow-up"></i>
    </a>"""
scroll_new = """    <!-- Floating Contact & Scroll To Top -->
    <div class="position-fixed bottom-0 end-0 mb-4 me-4 d-flex flex-column gap-2" style="z-index: 1000;">
        <a href="https://wa.me/1234567890" target="_blank" class="bg-success text-white rounded-circle shadow d-flex align-items-center justify-content-center hover-scale" style="width: 55px; height: 55px; text-decoration: none;" aria-label="WhatsApp">
            <i class="fa-brands fa-whatsapp fs-3"></i>
        </a>
        <a href="tel:+1234567890" class="btn-teal text-white rounded-circle shadow d-flex align-items-center justify-content-center hover-scale" style="width: 55px; height: 55px; text-decoration: none;" aria-label="Call Us">
            <i class="fa-solid fa-phone fs-4"></i>
        </a>
        <a href="#" id="scrollTop"
            class="bg-dark text-white rounded-circle shadow d-flex align-items-center justify-content-center hover-scale"
            style="width: 55px; height: 55px; opacity: 0; pointer-events: none; transition: 0.3s; text-decoration: none;" aria-label="Scroll to Top">
            <i class="fa-solid fa-arrow-up border-0"></i>
        </a>
    </div>"""

html = html.replace(scroll_old, scroll_new)

html = html.replace('<a href="#about" class="btn btn-outline-light btn-lg rounded-pill px-5">Learn More</a>', '<a href="about.html" class="btn btn-outline-light btn-lg rounded-pill px-5">Learn More</a>')
html = html.replace('<a href="#about" class="scroll-down-btn text-white">', '<a href="#how-it-works" class="scroll-down-btn text-white">')

def extract_section(section_name):
    pattern = r'<!-- ' + section_name + r' -->[\s\S]*?</section>\n'
    match = re.search(pattern, html)
    if match:
        return match.group(0)
    return ""

about_sec = extract_section("About Section")
treatment_sec = extract_section("Treatments Section")
testimonials_sec = extract_section("Testimonials Section")
doctors_sec = extract_section("Doctors Section")

print(f"Extracted Sections length: About: {len(about_sec)}, Treat: {len(treatment_sec)}, Test: {len(testimonials_sec)}, Doc: {len(doctors_sec)}")

html_index = html.replace(about_sec, "").replace(treatment_sec, "").replace(testimonials_sec, "").replace(doctors_sec, "")

head_nav = html.split('<!-- Hero Section -->')[0]
footer_only = "    <!-- Footer -->" + html.split('<!-- Footer -->')[1]

def generate_page(title, body_content):
    page_head = head_nav.replace('<title>Krystal Aligners</title>', f'<title>{title} - Krystal Aligners</title>')
    page_header = f'''    <!-- Page Header -->
    <section class="page-header d-flex align-items-center justify-content-center position-relative" style="height: 350px; background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&q=80&w=2000') center/cover;">
        <h1 class="display-3 fw-bold text-white mt-5 reveal-up position-relative z-1 text-shadow">{title}</h1>
    </section>\n\n'''
    return page_head + page_header + body_content + footer_only

about_html = generate_page("About Us", about_sec + doctors_sec)
treatments_html = generate_page("Treatments", treatment_sec)
testimonials_html = generate_page("Patient Testimonials", testimonials_sec)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_index)

with open(os.path.join(base_dir, 'about.html'), 'w', encoding='utf-8') as f:
    f.write(about_html)

with open(os.path.join(base_dir, 'treatments.html'), 'w', encoding='utf-8') as f:
    f.write(treatments_html)

with open(os.path.join(base_dir, 'testimonials.html'), 'w', encoding='utf-8') as f:
    f.write(testimonials_html)

print("Pages separated successfully.")
