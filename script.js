document.addEventListener('DOMContentLoaded', () => {

    // 1. Initial Setup
    const navbar = document.getElementById('mainNavbar');


    // Set initial navbar state (transparent if at top, solid if scrolled)
    // Add navbar-dark initially so text is white on hero image
    if (window.scrollY < 50) {
        navbar.classList.add('navbar-dark');
    }

    // 2. Scroll Events (Navbar + Scroll to Top)
    window.addEventListener('scroll', () => {
        // Navbar styling on scroll
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
            navbar.classList.remove('navbar-dark');
            navbar.classList.add('navbar-light');
        } else {
            navbar.classList.remove('scrolled');
            navbar.classList.add('navbar-dark');
            navbar.classList.remove('navbar-light');
        }


    });

    // 3. Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Offset for fixed navbar
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const offsetTop = targetElement.getBoundingClientRect().top + window.scrollY - navbarHeight;

                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                const navbarCollapse = document.getElementById('navbarNav');
                if (navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                }
            }
        });
    });



    // 4. Scroll Reveal Animation Setup using IntersectionObserver
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-scale, .reveal-right, .reveal-left');

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // 4.5 Trending Interactions
    // Magnetic Buttons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translate(0px, 0px)';
        });
    });

    // Parallax Images
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;

        document.querySelectorAll('.parallax-img').forEach(img => {
            const speed = img.getAttribute('data-speed') || 0.1;
            const yPos = -(scrolled * speed);
            img.style.transform = `translateY(${yPos}px)`;
        });
    });

    // 5. Animated Number Counters
    const counters = document.querySelectorAll('.counter');
    let countersAnimated = false;

    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !countersAnimated) {
                counters.forEach(counter => {
                    const updateCount = () => {
                        const target = +counter.getAttribute('data-target');
                        const count = +counter.innerText;

                        // Calculate increment speed based on target
                        const inc = target / 50;

                        if (count < target) {
                            counter.innerText = Math.ceil(count + inc);
                            setTimeout(updateCount, 40);
                        } else {
                            counter.innerText = target;
                        }
                    };
                    updateCount();
                });
                countersAnimated = true;
                observer.disconnect(); // Only animate once
            }
        });
    }, { threshold: 0.5 });

    // Observe the about section for counters
    const aboutSection = document.getElementById('about');
    if (aboutSection) {
        counterObserver.observe(aboutSection);
    }

    // 6. Premium Split Text Letter Hover Effects
    const splitElements = document.querySelectorAll('.display-3, .display-5, .nav-link');
    splitElements.forEach(el => {
        if (el.children.length > 0) return;

        const text = el.textContent.trim();
        if (!text) return;

        try {
            const fragment = document.createDocumentFragment();
            const words = text.split(' ');
            let charIndex = 0;

            words.forEach((word, wordIdx) => {
                const wordSpan = document.createElement('span');
                wordSpan.style.display = 'inline-block';
                wordSpan.style.whiteSpace = 'nowrap';

                [...word].forEach((char) => {
                    const charSpan = document.createElement('span');
                    charSpan.textContent = char;
                    charSpan.className = 'split-char';
                    charSpan.style.transitionDelay = `${charIndex * 15}ms`;
                    wordSpan.appendChild(charSpan);
                    charIndex++;
                });

                fragment.appendChild(wordSpan);

                if (wordIdx < words.length - 1) {
                    const space = document.createElement('span');
                    space.innerHTML = '&nbsp;';
                    fragment.appendChild(space);
                    charIndex++;
                }
            });

            el.textContent = '';
            el.appendChild(fragment);
            el.classList.add('split-hover-container');
        } catch (err) {
            console.error('Error splitting text:', err);
            // If it fails, the original text remains untouched
        }
    });

    // 7. Contact Form WhatsApp Redirect
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const message = document.getElementById('message').value;

            const whatsappNumber = '919656058125';
            const text = `Hello Krystal Aligners! I would like to book a Free Scan.\n\n*Details:*\n- Name: ${name}\n- Email: ${email}\n- Phone: ${phone}\n- Message: ${message}`;

            const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(text)}`;
            window.open(whatsappUrl, '_blank');

            // Optional: reset form after redirect
            contactForm.reset();
        });
    }
});
