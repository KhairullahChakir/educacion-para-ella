// Education for Her — main JavaScript

let currentSlideIndex = 0;
let autoSlideTimer = null;
let classSliderTimer = null;

// ==========================================
// Class Programs Horizontal Slider Function
// ==========================================
function scrollClassSlider(direction) {
    const container = document.getElementById('class-slider-container');
    if (!container) return;

    // Calculate actual card width including gap
    const firstCard = container.querySelector('div');
    const scrollAmount = firstCard ? (firstCard.offsetWidth + 24) : 360;
    const maxScroll = container.scrollWidth - container.clientWidth;

    if (direction > 0) {
        // Scrolling right (Next)
        if (container.scrollLeft >= maxScroll - 15) {
            container.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
            container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
        }
    } else {
        // Scrolling left (Prev)
        if (container.scrollLeft <= 15) {
            container.scrollTo({ left: maxScroll, behavior: 'smooth' });
        } else {
            container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
        }
    }
}

// Make globally accessible immediately
window.scrollClassSlider = scrollClassSlider;

document.addEventListener('DOMContentLoaded', function () {
    // Mobile menu toggle
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Language Dropdown Toggle
    const langBtn = document.getElementById('language-dropdown-btn');
    const langMenu = document.getElementById('language-dropdown-menu');

    if (langBtn && langMenu) {
        langBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            langMenu.classList.toggle('hidden');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function (e) {
            if (!langBtn.contains(e.target) && !langMenu.contains(e.target)) {
                langMenu.classList.add('hidden');
            }
        });
    }

    // Load saved language preference if any
    const savedLang = localStorage.getItem('maktab_language_label');
    if (savedLang) {
        const langText = document.getElementById('current-lang-text');
        if (langText) langText.textContent = savedLang;
    }

    // Initialize Hero Carousel Auto-play
    startAutoSlide();

    // Initialize Classes Horizontal Slider
    initClassSlider();

    // Attach direct click listeners for Class Slider Arrow Buttons
    const prevBtn = document.getElementById('class-slider-prev');
    const nextBtn = document.getElementById('class-slider-next');

    if (prevBtn) {
        prevBtn.addEventListener('click', function (e) {
            e.preventDefault();
            scrollClassSlider(-1);
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function (e) {
            e.preventDefault();
            scrollClassSlider(1);
        });
    }
});

// ==========================================
// Hero News Carousel Functions
// ==========================================
function goToSlide(index) {
    const slides = document.querySelectorAll('.hero-slide');
    if (!slides.length) return;

    currentSlideIndex = (index + slides.length) % slides.length;
    const dots = document.querySelectorAll('.slide-dot');

    slides.forEach((slide, idx) => {
        if (idx === currentSlideIndex) {
            slide.classList.remove('hidden', 'opacity-0', 'translate-x-8');
            slide.classList.add('active-slide', 'opacity-100', 'translate-x-0');
        } else {
            slide.classList.add('hidden', 'opacity-0', 'translate-x-8');
            slide.classList.remove('active-slide', 'opacity-100', 'translate-x-0');
        }
    });

    dots.forEach((dot, idx) => {
        if (idx === currentSlideIndex) {
            dot.className = "slide-dot w-8 h-2 rounded-full bg-white transition-all duration-300";
        } else {
            dot.className = "slide-dot w-2.5 h-2 rounded-full bg-white/40 hover:bg-white/70 transition-all duration-300";
        }
    });
}

function nextSlide() {
    const slides = document.querySelectorAll('.hero-slide');
    const total = slides.length || 1;
    goToSlide((currentSlideIndex + 1) % total);
}

function prevSlide() {
    const slides = document.querySelectorAll('.hero-slide');
    const total = slides.length || 1;
    goToSlide((currentSlideIndex - 1 + total) % total);
}

function startAutoSlide() {
    stopAutoSlide();
    autoSlideTimer = setInterval(function () {
        nextSlide();
    }, 3000);
}

function stopAutoSlide() {
    if (autoSlideTimer) {
        clearInterval(autoSlideTimer);
        autoSlideTimer = null;
    }
}

// ==========================================
// Class Slider Auto-Glide & Drag Handler
// ==========================================
function initClassSlider() {
    const container = document.getElementById('class-slider-container');
    if (!container) return;

    function startGlider() {
        stopGlider();
        classSliderTimer = setInterval(function () {
            scrollClassSlider(1);
        }, 3500);
    }

    function stopGlider() {
        if (classSliderTimer) {
            clearInterval(classSliderTimer);
            classSliderTimer = null;
        }
    }

    // Start auto glide
    startGlider();

    // Pause on mouse / touch interaction
    container.addEventListener('mouseenter', stopGlider);
    container.addEventListener('mouseleave', startGlider);
    container.addEventListener('touchstart', stopGlider, { passive: true });
    container.addEventListener('touchend', startGlider, { passive: true });

    // Enable smooth mouse dragging
    let isDown = false;
    let startX;
    let scrollLeft;

    container.addEventListener('mousedown', (e) => {
        isDown = true;
        container.classList.add('cursor-grabbing');
        container.classList.remove('cursor-grab');
        startX = e.pageX - container.offsetLeft;
        scrollLeft = container.scrollLeft;
        stopGlider();
    });

    container.addEventListener('mouseleave', () => {
        isDown = false;
        container.classList.remove('cursor-grabbing');
        container.classList.add('cursor-grab');
    });

    container.addEventListener('mouseup', () => {
        isDown = false;
        container.classList.remove('cursor-grabbing');
        container.classList.add('cursor-grab');
        startGlider();
    });

    container.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - container.offsetLeft;
        const walk = (x - startX) * 1.5;
        container.scrollLeft = scrollLeft - walk;
    });
}

// ==========================================
// Language Selector Function
// ==========================================
function selectLanguage(langCode, label) {
    localStorage.setItem('maktab_language', langCode);
    localStorage.setItem('maktab_language_label', label);
    
    const langText = document.getElementById('current-lang-text');
    if (langText) {
        langText.textContent = label;
    }

    const langMenu = document.getElementById('language-dropdown-menu');
    if (langMenu) {
        langMenu.classList.add('hidden');
    }
}
