// Education for Her — main JavaScript

let currentSlideIndex = 0;
let autoSlideTimer = null;

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

    // Initialize Hero Carousel Auto-play (Starts immediately)
    startAutoSlide();
});

// Carousel Functions
function goToSlide(index) {
    const slides = document.querySelectorAll('.hero-slide');
    if (!slides.length) return;

    // Normalize index
    currentSlideIndex = (index + slides.length) % slides.length;

    const tabBtns = document.querySelectorAll('.news-tab-btn');
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

    // Update Top News Tab Pill Styles
    tabBtns.forEach((btn, idx) => {
        if (idx === currentSlideIndex) {
            btn.className = "news-tab-btn px-4 py-2 text-xs font-extrabold uppercase tracking-wider rounded-full transition-all bg-white/20 text-white backdrop-blur-md border border-white/30";
        } else {
            btn.className = "news-tab-btn px-4 py-2 text-xs font-bold uppercase tracking-wider rounded-full transition-all bg-white/5 hover:bg-white/15 text-white/80 hover:text-white border border-transparent";
        }
    });

    // Update Progress Dots
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

// Function to select language
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
