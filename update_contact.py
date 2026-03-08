import os
import glob

base_dir = "d:/Krystalaligners"
files = glob.glob(os.path.join(base_dir, "*.html"))

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Floating Whatsapp
    content = content.replace('href="https://wa.me/1234567890"', 'href="https://wa.me/919656058125"')
    
    # Update Floating Phone
    content = content.replace('href="tel:+1234567890"', 'href="tel:+918139815081"')
    
    # Update Map Card Phone
    content = content.replace('+1 (555) 123-4567', '+91 8139815081<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+91 9656058125')

    # Update Map Card Email
    content = content.replace('hello@pristinealigner.com', 'krystalaligners@gmail.com')

    # Update Footer Copyright Name
    content = content.replace('Pristine Aligner', 'Krystal Aligners')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated contact info in {len(files)} files.")
