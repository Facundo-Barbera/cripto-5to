// Presentation Mode JavaScript
// Navigation, keyboard controls, D3.js charts, and interactivity

let currentSlide = 1;
const totalSlides = 13;
let chartsRendered = false;

// Initialize presentation when DOM is ready
document.addEventListener('DOMContentLoaded', async function() {
    await initI18n();
    initPresentation();
    initKeyboardNavigation();
    initProgressDots();
    updateProgress();
});

function initPresentation() {
    // Set total slides display
    document.getElementById('total-slides').textContent = totalSlides;

    // Check for slide parameter in URL
    const urlParams = new URLSearchParams(window.location.search);
    const slideParam = urlParams.get('slide');
    if (slideParam) {
        const slideNum = parseInt(slideParam);
        if (slideNum >= 1 && slideNum <= totalSlides) {
            goToSlide(slideNum, false);
        }
    }
}

function initProgressDots() {
    const dotsContainer = document.getElementById('progress-dots');
    dotsContainer.innerHTML = '';

    for (let i = 1; i <= totalSlides; i++) {
        const dot = document.createElement('button');
        dot.className = 'progress-dot' + (i === 1 ? ' active' : '');
        dot.setAttribute('data-slide', i);
        dot.setAttribute('aria-label', `Go to slide ${i}`);
        dot.onclick = () => goToSlide(i);
        dotsContainer.appendChild(dot);
    }
}

function initKeyboardNavigation() {
    document.addEventListener('keydown', function(e) {
        // Don't trigger navigation if typing in an input
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
            return;
        }

        switch(e.key) {
            case 'ArrowRight':
            case ' ':
            case 'Enter':
                e.preventDefault();
                nextSlide();
                break;
            case 'ArrowLeft':
                e.preventDefault();
                prevSlide();
                break;
            case 'Escape':
                exitPresentation();
                break;
            case 'f':
            case 'F':
                toggleFullscreen();
                break;
            case 'Home':
                e.preventDefault();
                goToSlide(1);
                break;
            case 'End':
                e.preventDefault();
                goToSlide(totalSlides);
                break;
        }
    });
}

function goToSlide(n, animate = true) {
    if (n < 1 || n > totalSlides) return;

    const slides = document.querySelectorAll('.slide');
    const currentSlideEl = document.querySelector('.slide.active');
    const targetSlideEl = document.querySelector(`.slide[data-slide="${n}"]`);

    if (currentSlideEl && targetSlideEl && currentSlideEl !== targetSlideEl) {
        // Remove active class with animation
        currentSlideEl.classList.remove('active');
        if (animate) {
            currentSlideEl.classList.add('slide-exit');
            setTimeout(() => {
                currentSlideEl.classList.remove('slide-exit');
            }, 500);
        }

        // Add active class to new slide
        targetSlideEl.classList.add('active');
    } else if (targetSlideEl && !currentSlideEl) {
        targetSlideEl.classList.add('active');
    }

    currentSlide = n;
    updateProgress();

    // Render charts when arriving at slide 9
    if (n === 9 && !chartsRendered) {
        setTimeout(() => renderMetricsCharts(), 300);
        chartsRendered = true;
    }

    // Update URL without reload
    const url = new URL(window.location);
    url.searchParams.set('slide', n);
    window.history.replaceState({}, '', url);
}

function nextSlide() {
    if (currentSlide < totalSlides) {
        goToSlide(currentSlide + 1);
    }
}

function prevSlide() {
    if (currentSlide > 1) {
        goToSlide(currentSlide - 1);
    }
}

function updateProgress() {
    // Update slide counter
    document.getElementById('current-slide-num').textContent = currentSlide;

    // Update progress dots
    const dots = document.querySelectorAll('.progress-dot');
    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index + 1 === currentSlide);
        dot.classList.toggle('visited', index + 1 < currentSlide);
    });

    // Update navigation arrow visibility
    const prevBtn = document.querySelector('.nav-prev');
    const nextBtn = document.querySelector('.nav-next');

    if (prevBtn) prevBtn.style.opacity = currentSlide === 1 ? '0.3' : '1';
    if (nextBtn) nextBtn.style.opacity = currentSlide === totalSlides ? '0.3' : '1';
}

function exitPresentation() {
    window.location.href = '/';
}

function toggleFullscreen() {
    const icon = document.getElementById('fullscreen-icon');

    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().then(() => {
            icon.textContent = '⛶';
        }).catch(err => {
            console.log('Fullscreen not available');
        });
    } else {
        document.exitFullscreen().then(() => {
            icon.textContent = '⛶';
        });
    }
}

// Handle fullscreen change events
document.addEventListener('fullscreenchange', () => {
    const icon = document.getElementById('fullscreen-icon');
    if (document.fullscreenElement) {
        icon.textContent = '⛶';
    } else {
        icon.textContent = '⛶';
    }
});

// Domain analysis from presentation
function analyzeDomainFromPresentation(domain) {
    // Navigate to main app with demo parameter (shows return banner)
    window.location.href = `/?demo=${encodeURIComponent(domain)}`;
}

// Transition to demo mode
function transitionToDemo() {
    const container = document.querySelector('.presentation-container');
    container.classList.add('fade-out');

    setTimeout(() => {
        window.location.href = '/?demo=gob.mx';
    }, 500);
}

// Render D3.js pie charts for slide 9
function renderMetricsCharts() {
    // Chart data
    const chainCompleteData = [
        { label: 'Yes', value: 3, percentage: 6.25 },
        { label: 'No', value: 45, percentage: 93.75 }
    ];

    const dnssecEnabledData = [
        { label: 'Yes', value: 6, percentage: 12.5 },
        { label: 'No', value: 42, percentage: 87.5 }
    ];

    renderPieChart('#chart-chain-complete', chainCompleteData, 0);
    renderPieChart('#chart-dnssec-enabled', dnssecEnabledData, 300);
}

function renderPieChart(selector, data, delay) {
    const container = document.querySelector(selector);
    if (!container) return;

    // Clear any existing content
    container.innerHTML = '';

    const width = 200;
    const height = 200;
    const radius = Math.min(width, height) / 2;

    const svg = d3.select(selector)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', `translate(${width / 2}, ${height / 2})`);

    // Define gradients
    const defs = svg.append('defs');

    // Yes gradient (green)
    const gradientYes = defs.append('linearGradient')
        .attr('id', `gradient-yes-${selector.replace('#', '')}`)
        .attr('x1', '0%').attr('y1', '0%')
        .attr('x2', '100%').attr('y2', '100%');
    gradientYes.append('stop').attr('offset', '0%').attr('stop-color', '#00d4aa');
    gradientYes.append('stop').attr('offset', '100%').attr('stop-color', '#00a080');

    // No gradient (red)
    const gradientNo = defs.append('linearGradient')
        .attr('id', `gradient-no-${selector.replace('#', '')}`)
        .attr('x1', '0%').attr('y1', '0%')
        .attr('x2', '100%').attr('y2', '100%');
    gradientNo.append('stop').attr('offset', '0%').attr('stop-color', '#ff6b6b');
    gradientNo.append('stop').attr('offset', '100%').attr('stop-color', '#cc5555');

    // Pie generator
    const pie = d3.pie()
        .value(d => d.value)
        .sort(null)
        .startAngle(-Math.PI / 2)
        .endAngle(Math.PI * 1.5);

    // Arc generator
    const arc = d3.arc()
        .innerRadius(radius * 0.5)
        .outerRadius(radius * 0.9);

    // Create arcs with animation
    const arcs = svg.selectAll('.arc')
        .data(pie(data))
        .enter()
        .append('g')
        .attr('class', 'arc');

    arcs.append('path')
        .attr('fill', (d, i) => {
            const gradientId = i === 0
                ? `gradient-yes-${selector.replace('#', '')}`
                : `gradient-no-${selector.replace('#', '')}`;
            return `url(#${gradientId})`;
        })
        .style('opacity', 0)
        .transition()
        .delay(delay)
        .duration(800)
        .ease(d3.easeElastic.amplitude(1).period(0.5))
        .style('opacity', 1)
        .attrTween('d', function(d) {
            const interpolate = d3.interpolate({ startAngle: d.startAngle, endAngle: d.startAngle }, d);
            return function(t) {
                return arc(interpolate(t));
            };
        });

    // Add percentage text in center after animation
    setTimeout(() => {
        const yesData = data.find(d => d.label === 'Yes');
        svg.append('text')
            .attr('text-anchor', 'middle')
            .attr('dy', '-0.2em')
            .attr('class', 'chart-percentage')
            .style('fill', '#00d4aa')
            .style('font-size', '1.5rem')
            .style('font-weight', 'bold')
            .style('opacity', 0)
            .text(`${yesData.percentage}%`)
            .transition()
            .duration(500)
            .style('opacity', 1);

        svg.append('text')
            .attr('text-anchor', 'middle')
            .attr('dy', '1.2em')
            .style('fill', '#a0a0b0')
            .style('font-size', '0.75rem')
            .style('opacity', 0)
            .text('firmados')
            .transition()
            .duration(500)
            .style('opacity', 1);
    }, delay + 800);
}

// Language switcher for presentation
document.addEventListener('DOMContentLoaded', function() {
    const langSwitcher = document.getElementById('presentation-lang-switcher');
    if (!langSwitcher) return;

    const toggle = langSwitcher.querySelector('.lang-toggle');
    const dropdown = langSwitcher.querySelector('.lang-dropdown');
    const options = langSwitcher.querySelectorAll('.lang-option');

    toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        dropdown.classList.toggle('open');
    });

    options.forEach(option => {
        option.addEventListener('click', () => {
            const lang = option.dataset.lang;
            setLanguage(lang);

            // Update active state
            options.forEach(opt => opt.classList.remove('active'));
            option.classList.add('active');

            // Update current display
            const currentDisplay = toggle.querySelector('.lang-current');
            currentDisplay.textContent = lang.toUpperCase();

            dropdown.classList.remove('open');

            // Re-render charts if on slide 9
            if (currentSlide === 9) {
                chartsRendered = false;
                renderMetricsCharts();
            }
        });
    });

    // Close dropdown on outside click
    document.addEventListener('click', () => {
        dropdown.classList.remove('open');
    });

    // Set initial language display
    const currentLang = getCurrentLanguage();
    const currentDisplay = toggle.querySelector('.lang-current');
    currentDisplay.textContent = currentLang.toUpperCase();

    options.forEach(opt => {
        opt.classList.toggle('active', opt.dataset.lang === currentLang);
    });
});

// Touch support for mobile
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
}, false);

document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
}, false);

function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartX - touchEndX;

    if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
            // Swipe left - next slide
            nextSlide();
        } else {
            // Swipe right - prev slide
            prevSlide();
        }
    }
}
