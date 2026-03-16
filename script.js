document.addEventListener("DOMContentLoaded", () => {
    // 1. Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 80) {
            navbar.classList.add('nav-scrolled');
            // Force primary color on mobile links if any 
        } else {
            navbar.classList.remove('nav-scrolled');
        }
    });

    // 2. Global GSAP Reveal
    gsap.registerPlugin(ScrollTrigger);

    gsap.utils.toArray('.reveal-up').forEach((elem) => {
        const staggerDelay = elem.classList.contains('stagger-1') ? 0.15 : (elem.classList.contains('stagger-2') ? 0.3 : 0);

        gsap.to(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
                toggleActions: "play none none none"
            },
            y: 0,
            opacity: 1,
            duration: 0.8,
            ease: "power3.out",
            delay: staggerDelay
        });
    });

    // 3. Manifesto / Philosophy Text Reveal
    gsap.fromTo('.manifesto-line-1', {
        y: 30, opacity: 0
    }, {
        scrollTrigger: {
            trigger: '.manifesto-container',
            start: "top 70%",
        },
        y: 0, opacity: 1, duration: 1, ease: "power2.out"
    });

    gsap.fromTo('.manifesto-line-2', {
        y: 40, opacity: 0
    }, {
        scrollTrigger: {
            trigger: '.manifesto-container',
            start: "top 60%",
        },
        y: 0, opacity: 1, duration: 1.2, delay: 0.2, ease: "power3.out"
    });

    // Parallax background
    gsap.to('.parallax-img', {
        scrollTrigger: {
            trigger: "#pourquoi",
            start: "top bottom",
            end: "bottom top",
            scrub: true
        },
        y: 100,
        ease: "none"
    });

    // 7. Interactive Before/After Sliders
    const sliders = document.querySelectorAll('.before-after-wrapper');
    
    sliders.forEach(wrapper => {
        const slider = wrapper.querySelector('.slider-range');
        const beforeWrapper = wrapper.querySelector('.before-wrapper');
        const handle = wrapper.querySelector('.slider-handle');
        const beforeImg = wrapper.querySelector('.before-img');

        if (slider && beforeImg) {
            // Sync before-img width to container width so portrait images don't stretch
            const syncWidth = () => {
                beforeImg.style.width = wrapper.offsetWidth + 'px';
            };
            window.addEventListener('resize', syncWidth);
            syncWidth();

            slider.addEventListener('input', (e) => {
                const val = e.target.value;
                beforeWrapper.style.width = `${val}%`;
                handle.style.left = `${val}%`;
            });
        }
    });

    // Buttons Magnetic Effect
    const magneticBtns = document.querySelectorAll('.btn-magnetic');
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            gsap.to(btn, {
                x: x * 0.2, // Movement ratio
                y: y * 0.2,
                duration: 0.3,
                ease: 'power2.out'
            });
        });

        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, {
                x: 0, y: 0,
                duration: 0.5,
                ease: 'elastic.out(1, 0.3)'
            });
        });
    });

});
