import os
import glob
import re

base_dir = "d:/Krystalaligners"
files = glob.glob(os.path.join(base_dir, "*.html"))

logo_img = "benyamin-bohlouli-e7MJLM5VGjY-unsplash.jpg"
logo_html = f'<img src="{logo_img}" alt="Krystal Aligners Logo" style="height: 65px; border-radius: 50%;">'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Navbar Brand
    # Find all instances of navbar brand that look like text and replace with image
    pattern_nav = r'<a class="navbar-brand[^>]*>[\s\n]*<i class="fa-solid fa-tooth[^>]*></i>[\s\n]*Krystal Aligners[\s\n]*</a>'
    replacement_nav = f'<a class="navbar-brand" href="index.html">\n                {logo_html}\n            </a>'
    content = re.sub(pattern_nav, replacement_nav, content)
    
    # 2. Update Footer Brand
    # Find instances in footer (it might still say Pristine Aligner or Krystal Aligners)
    pattern_footer = r'<a class="navbar-brand[^>]*>[\s\n]*<i class="fa-solid fa-tooth[^>]*></i>[\s\n]*(Pristine Aligner|Krystal Aligners)[\s\n]*</a>'
    replacement_footer = f'<a class="navbar-brand mb-4 d-inline-block" href="index.html">\n                        {logo_html}\n                    </a>'
    content = re.sub(pattern_footer, replacement_footer, content)
    
    # 3. Fix inline background images for page headers (about, treatments, testimonials)
    # The broken unsplash link
    pattern_bg = r"url\('https://images.unsplash.com/photo-1606811841689-23dfddce3e95.*?'\)"
    replacement_bg = r"url('photo_2026-03-08_11-19-49.jpg')"
    content = re.sub(pattern_bg, replacement_bg, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 4. Update style.css for the main hero section background
css_path = os.path.join(base_dir, "style.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace broken unsplash link in hero section with one of the local shots
pattern_css = r"url\('https://images.unsplash.com/photo-1606265863640-.*?'\)"
replacement_css = r"url('photo_2026-03-08_11-20-20.jpg')"
css = re.sub(pattern_css, replacement_css, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Logos and backgrounds updated across all files.")
