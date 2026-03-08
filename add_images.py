import os

base_dir = "d:/Krystalaligners"
index_path = os.path.join(base_dir, "index.html")
about_path = os.path.join(base_dir, "about.html")

new_gallery = """
    <!-- Product Showcase Section -->
    <section id="showcase" class="py-6 bg-white">
        <div class="container py-5">
            <div class="text-center mb-5 reveal-up">
                <span class="text-teal font-monospace text-uppercase small fw-bold tracking-wide">Premium Quality</span>
                <h2 class="display-5 fw-bold mt-2 text-dark">Krystal Clear Aligners</h2>
            </div>
            
            <div class="row g-4 justify-content-center">
                <div class="col-md-4 reveal-up">
                    <div class="rounded-4 overflow-hidden shadow-sm h-100 group-hover-zoom">
                        <img src="photo_2026-03-08_11-19-34.jpg" class="img-fluid w-100 h-100 object-fit-cover hover-zoom-img" alt="Krystal Aligners Target">
                    </div>
                </div>
                <div class="col-md-4 reveal-up" style="transition-delay: 100ms;">
                    <div class="rounded-4 overflow-hidden shadow-sm h-100 group-hover-zoom">
                        <img src="photo_2026-03-08_11-20-08.jpg" class="img-fluid w-100 h-100 object-fit-cover hover-zoom-img" alt="Krystal Aligners Case">
                    </div>
                </div>
                <div class="col-md-4 reveal-up" style="transition-delay: 200ms;">
                    <div class="rounded-4 overflow-hidden shadow-sm h-100 group-hover-zoom">
                        <img src="photo_2026-03-08_11-19-49.jpg" class="img-fluid w-100 h-100 object-fit-cover hover-zoom-img" alt="Krystal Aligners Details">
                    </div>
                </div>
                <div class="col-md-6 reveal-up">
                    <div class="rounded-4 overflow-hidden shadow-sm h-100 group-hover-zoom">
                        <img src="photo_2026-03-08_11-20-02.jpg" class="img-fluid w-100 h-100 object-fit-cover hover-zoom-img" alt="Krystal Aligners Clear" style="max-height: 500px;">
                    </div>
                </div>
                <div class="col-md-6 reveal-up" style="transition-delay: 100ms;">
                    <div class="rounded-4 overflow-hidden shadow-sm h-100 group-hover-zoom">
                        <img src="photo_2026-03-08_11-20-20.jpg" class="img-fluid w-100 h-100 object-fit-cover hover-zoom-img" alt="The invisible way to a krystal clear smile" style="max-height: 500px;">
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

# Replace About Image
old_about_img = 'img src="https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&q=80&w=800"\n                            alt="Clinic Interior"'
new_about_img = 'img src="photo_2026-03-08_11-19-57.jpg"\n                            alt="Krystal Aligners Case with Mirror"'
idx_content = idx_content.replace(old_about_img, new_about_img)

# Replace Before image placeholder with an empty placeholder since they provided real aligner photos, 
# But let's leave Before/After placeholders as they are because they are for teeth.

# Insert Gallery before Before & After
idx_content = idx_content.replace('    <!-- Before & After Section -->', new_gallery + '\n    <!-- Before & After Section -->')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

with open(about_path, "r", encoding="utf-8") as f:
    abt_content = f.read()

abt_content = abt_content.replace(old_about_img, new_about_img)
with open(about_path, "w", encoding="utf-8") as f:
    f.write(abt_content)

print("Images integrated successfully!")
