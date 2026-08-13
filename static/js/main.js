// Maktab — main JavaScript

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
});

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

    // Smooth feedback or page language adaptation can be wired here
    console.log('Language changed to:', langCode);
}
