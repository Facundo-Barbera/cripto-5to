// i18n.js - Internationalization module for DNSSEC Visualizer

let translations = {};
let currentLang = 'en';

const SUPPORTED_LANGS = ['en', 'es'];
const DEFAULT_LANG = 'en';

/**
 * Detect user's preferred language
 */
function detectLanguage() {
    // 1. Check localStorage for user preference (highest priority)
    const stored = localStorage.getItem('preferred-language');
    if (stored && SUPPORTED_LANGS.includes(stored)) {
        return stored;
    }

    // 2. Check browser language
    const browserLang = (navigator.language || navigator.userLanguage || '').split('-')[0].toLowerCase();

    // 3. Return if supported, otherwise default to English
    if (SUPPORTED_LANGS.includes(browserLang)) {
        return browserLang;
    }

    return DEFAULT_LANG;
}

/**
 * Load translations from JSON file
 */
async function loadTranslations(lang) {
    try {
        // Determine base path based on deployment
        const isFlask = document.querySelector('script[src*="/static/"]') !== null;
        const basePath = isFlask ? '/static/locales' : '/locales';

        const response = await fetch(`${basePath}/${lang}.json`);

        if (!response.ok) {
            throw new Error(`Failed to load translations for ${lang}`);
        }

        translations = await response.json();
        currentLang = lang;

        return true;
    } catch (error) {
        console.error('Translation load error:', error);

        // Fallback to English if loading failed
        if (lang !== DEFAULT_LANG) {
            return loadTranslations(DEFAULT_LANG);
        }

        return false;
    }
}

/**
 * Get nested value from object using dot notation
 */
function getNestedValue(obj, path) {
    return path.split('.').reduce((current, key) => {
        return current && current[key] !== undefined ? current[key] : undefined;
    }, obj);
}

/**
 * Get translation for a key
 */
function t(key) {
    const value = getNestedValue(translations, key);

    if (value === undefined) {
        console.warn(`Missing translation key: ${key}`);
        return key;
    }

    return value;
}

/**
 * Update all DOM elements with data-i18n attributes
 */
function updateAllTranslations() {
    // Update text content
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const translation = t(key);
        el.textContent = translation;
    });

    // Update page title
    const titleKey = document.querySelector('title')?.getAttribute('data-i18n');
    if (titleKey) {
        document.title = t(titleKey);
    }

    // Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        el.placeholder = t(key);
    });

    // Update HTML lang attribute
    document.documentElement.lang = currentLang;

    // Update language switcher UI
    updateLanguageSwitcherUI();
}

/**
 * Update language switcher UI state
 */
function updateLanguageSwitcherUI() {
    document.querySelectorAll('.lang-current').forEach(el => {
        el.textContent = currentLang.toUpperCase();
    });

    document.querySelectorAll('.lang-option').forEach(option => {
        const isActive = option.dataset.lang === currentLang;
        option.classList.toggle('active', isActive);
    });
}

/**
 * Set language and update UI
 */
async function setLanguage(lang) {
    if (!SUPPORTED_LANGS.includes(lang)) {
        console.warn(`Unsupported language: ${lang}`);
        return false;
    }

    localStorage.setItem('preferred-language', lang);

    await loadTranslations(lang);
    updateAllTranslations();

    // Re-render dynamic content if data exists
    if (typeof currentData !== 'undefined' && currentData) {
        renderResults(currentData);
    }

    // Close dropdowns
    document.querySelectorAll('.language-switcher').forEach(s => {
        s.classList.remove('open');
    });

    return true;
}

/**
 * Get current language
 */
function getCurrentLanguage() {
    return currentLang;
}

/**
 * Initialize language switcher event listeners
 */
function initLanguageSwitcher() {
    document.querySelectorAll('.lang-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            const switcher = toggle.closest('.language-switcher');

            // Close other switchers
            document.querySelectorAll('.language-switcher').forEach(s => {
                if (s !== switcher) s.classList.remove('open');
            });

            switcher.classList.toggle('open');
        });
    });

    document.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', () => {
            const lang = option.dataset.lang;
            setLanguage(lang);
        });
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.language-switcher')) {
            document.querySelectorAll('.language-switcher').forEach(s => {
                s.classList.remove('open');
            });
        }
    });
}

/**
 * Initialize i18n system
 */
async function initI18n() {
    const lang = detectLanguage();
    await loadTranslations(lang);
    updateAllTranslations();
    initLanguageSwitcher();
}

// Export globally
window.t = t;
window.setLanguage = setLanguage;
window.getCurrentLanguage = getCurrentLanguage;
window.initI18n = initI18n;
window.updateAllTranslations = updateAllTranslations;
