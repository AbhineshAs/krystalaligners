import os
import glob

base_dir = "d:/Krystalaligners"
files = glob.glob(os.path.join(base_dir, "*.html"))

# 1. Replace logo image in HTML files
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replaced it with benyamin-bohlouli earlier, now let's use the real extracted logo
    content = content.replace('src="benyamin-bohlouli-e7MJLM5VGjY-unsplash.jpg"', 'src="logo.png"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update CSS for hero background
css_path = os.path.join(base_dir, "style.css")
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the previous hero background with benyamin-bohlouli
css = css.replace("url('photo_2026-03-08_11-20-20.jpg')", "url('benyamin-bohlouli-e7MJLM5VGjY-unsplash.jpg')")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("HTML and CSS successfully updated with the proper logo and hero background!")
