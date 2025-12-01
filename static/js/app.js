let currentData = null;
let isNavbarMode = false;

document.getElementById('domain-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        analyzeDomain();
    }
});

document.getElementById('nav-domain-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        analyzeDomain();
    }
});

function getActiveInput() {
    if (isNavbarMode) {
        return document.getElementById('nav-domain-input');
    }
    return document.getElementById('domain-input');
}

function getActiveButton() {
    if (isNavbarMode) {
        return document.getElementById('nav-analyze-btn');
    }
    return document.getElementById('analyze-btn');
}

function switchToNavbarMode() {
    if (isNavbarMode) return;
    isNavbarMode = true;

    const navbar = document.getElementById('navbar');
    const heroHeader = document.getElementById('hero-header');
    const heroSearch = document.getElementById('hero-search');
    const container = document.getElementById('main-container');

    heroHeader.classList.add('hidden');
    heroSearch.classList.add('hidden');
    container.classList.add('with-navbar');

    setTimeout(() => {
        navbar.classList.add('visible');
    }, 200);
}

function resetToHome() {
    isNavbarMode = false;

    const navbar = document.getElementById('navbar');
    const heroHeader = document.getElementById('hero-header');
    const heroSearch = document.getElementById('hero-search');
    const container = document.getElementById('main-container');
    const resultsEl = document.getElementById('results');

    navbar.classList.remove('visible');

    setTimeout(() => {
        heroHeader.classList.remove('hidden');
        heroSearch.classList.remove('hidden');
        container.classList.remove('with-navbar');
        resultsEl.classList.add('hidden');
        document.getElementById('domain-input').value = '';
        document.getElementById('nav-domain-input').value = '';
    }, 300);
}

async function analyzeDomain() {
    const input = getActiveInput();
    const btn = getActiveButton();
    const errorEl = document.getElementById('error-message');
    const resultsEl = document.getElementById('results');

    const domain = input.value.trim();
    if (!domain) {
        showError('Please enter a domain name');
        return;
    }

    btn.classList.add('loading');
    btn.disabled = true;
    errorEl.classList.remove('visible');
    resultsEl.classList.add('hidden');

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ domain })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Analysis failed');
        }

        currentData = data;

        if (!isNavbarMode) {
            switchToNavbarMode();
            setTimeout(() => {
                renderResults(data);
                resultsEl.classList.remove('hidden');
            }, 500);
        } else {
            renderResults(data);
            resultsEl.classList.remove('hidden');
        }

        document.getElementById('nav-domain-input').value = '';
        document.getElementById('current-domain-display').textContent = domain;

    } catch (error) {
        showError(error.message);
    } finally {
        btn.classList.remove('loading');
        btn.disabled = false;
    }
}

function showError(message) {
    const errorEl = document.getElementById('error-message');
    errorEl.textContent = message;
    errorEl.classList.add('visible');
}

function renderResults(data) {
    renderChainGraph(data);
    renderChainStatus(data);
    renderRFCCompliance(data);
}

function renderChainGraph(data) {
    const container = document.getElementById('chain-graph');
    container.innerHTML = '';

    const chain = data.analysis.dnssec.chain_of_trust.chain;
    const reversedChain = [...chain].reverse();

    const width = Math.max(600, reversedChain.length * 200);
    const height = 200;
    const bubbleRadius = 45;
    const spacing = width / (reversedChain.length + 1);

    const svg = d3.select(container)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .attr('viewBox', `0 0 ${width} ${height}`);

    const defs = svg.append('defs');

    const gradientSigned = defs.append('linearGradient')
        .attr('id', 'gradient-signed')
        .attr('x1', '0%').attr('y1', '0%')
        .attr('x2', '100%').attr('y2', '100%');
    gradientSigned.append('stop').attr('offset', '0%').attr('stop-color', '#00d4aa');
    gradientSigned.append('stop').attr('offset', '100%').attr('stop-color', '#00a080');

    const gradientUnsigned = defs.append('linearGradient')
        .attr('id', 'gradient-unsigned')
        .attr('x1', '0%').attr('y1', '0%')
        .attr('x2', '100%').attr('y2', '100%');
    gradientUnsigned.append('stop').attr('offset', '0%').attr('stop-color', '#ff6b6b');
    gradientUnsigned.append('stop').attr('offset', '100%').attr('stop-color', '#cc5555');

    const glowFilter = defs.append('filter')
        .attr('id', 'glow')
        .attr('x', '-50%').attr('y', '-50%')
        .attr('width', '200%').attr('height', '200%');
    glowFilter.append('feGaussianBlur').attr('stdDeviation', '3').attr('result', 'coloredBlur');
    const feMerge = glowFilter.append('feMerge');
    feMerge.append('feMergeNode').attr('in', 'coloredBlur');
    feMerge.append('feMergeNode').attr('in', 'SourceGraphic');

    for (let i = 0; i < reversedChain.length - 1; i++) {
        const x1 = spacing * (i + 1);
        const x2 = spacing * (i + 2);
        const y = height / 2;

        const currentZone = reversedChain[i];
        const nextZone = reversedChain[i + 1];
        const isValid = currentZone.is_signed && nextZone.is_signed && nextZone.has_ds;

        const lineGroup = svg.append('g')
            .attr('class', 'connection')
            .style('opacity', 0);

        lineGroup.append('line')
            .attr('x1', x1 + bubbleRadius)
            .attr('y1', y)
            .attr('x2', x2 - bubbleRadius)
            .attr('y2', y)
            .attr('class', `connection-line ${isValid ? 'connection-valid' : 'connection-broken'}`);

        const midX = (x1 + x2) / 2;
        lineGroup.append('text')
            .attr('x', midX)
            .attr('y', y - 15)
            .attr('text-anchor', 'middle')
            .attr('class', `connection-icon ${isValid ? 'valid' : 'broken'}`)
            .text(isValid ? '✓' : '✗');

        lineGroup.transition()
            .delay(i * 150 + 300)
            .duration(400)
            .style('opacity', 1);
    }

    reversedChain.forEach((zone, i) => {
        const x = spacing * (i + 1);
        const y = height / 2;

        const bubble = svg.append('g')
            .attr('class', `bubble ${zone.is_signed ? 'bubble-signed' : 'bubble-unsigned'}`)
            .attr('transform', `translate(${x}, ${y})`)
            .style('opacity', 1)
            .on('click', () => showDetailPanel(zone, data));

        const circle = bubble.append('circle')
            .attr('r', 0)
            .attr('filter', 'url(#glow)');

        circle.transition()
            .delay(i * 150)
            .duration(600)
            .ease(d3.easeElastic.amplitude(1).period(0.4))
            .attr('r', bubbleRadius);

        const displayName = zone.zone === '.' ? 'ROOT' : zone.zone;
        const fontSize = displayName.length > 10 ? 11 : 14;

        const text = bubble.append('text')
            .attr('y', 5)
            .attr('font-size', fontSize)
            .style('opacity', 0)
            .text(displayName);

        text.transition()
            .delay(i * 150 + 200)
            .duration(300)
            .style('opacity', 1);
    });
}

function renderChainStatus(data) {
    const statusEl = document.getElementById('chain-status');
    const chainData = data.analysis.dnssec.chain_of_trust;

    if (chainData.is_complete) {
        statusEl.className = 'chain-status complete';
        statusEl.innerHTML = '✓ Chain of Trust Complete - Full validation path to root';
    } else {
        statusEl.className = 'chain-status broken';
        statusEl.innerHTML = `✗ Chain Broken at <strong>${chainData.broken_at}</strong>`;
    }
}

function showDetailPanel(zone, data) {
    const panel = document.getElementById('detail-panel');
    const zoneEl = document.getElementById('detail-zone');
    const contentEl = document.getElementById('detail-content');

    zoneEl.textContent = zone.zone === '.' ? 'Root Zone (.)' : zone.zone;

    let html = `
        <div class="detail-item">
            <div class="label">DNSKEY</div>
            <div class="value ${zone.has_dnskey ? 'yes' : 'no'}">
                ${zone.has_dnskey ? '✓ Present' : '✗ Missing'}
            </div>
        </div>
        <div class="detail-item">
            <div class="label">DS Record</div>
            <div class="value ${zone.has_ds ? 'yes' : 'no'}">
                ${zone.zone === '.' ? 'N/A (Root)' : (zone.has_ds ? '✓ Present' : '✗ Missing')}
            </div>
        </div>
        <div class="detail-item">
            <div class="label">RRSIG</div>
            <div class="value ${zone.has_rrsig ? 'yes' : 'no'}">
                ${zone.has_rrsig ? '✓ Present' : '✗ Missing'}
            </div>
        </div>
        <div class="detail-item">
            <div class="label">Status</div>
            <div class="value ${zone.is_signed ? 'yes' : 'no'}">
                ${zone.is_signed ? '✓ Signed' : '✗ Unsigned'}
            </div>
        </div>
    `;

    if (zone.algorithms && zone.algorithms.length > 0) {
        html += `
            <div class="detail-item">
                <div class="label">Algorithms</div>
                <div class="value">${zone.algorithms.join(', ')}</div>
            </div>
        `;
    }

    if (zone.zone === data.domain) {
        const compliance = data.rfc_compliance;
        html += `
            <div class="detail-item">
                <div class="label">RFC Compliance</div>
                <div class="value">${compliance.score} (${compliance.percentage}%)</div>
            </div>
        `;
    }

    contentEl.innerHTML = html;
    panel.classList.remove('hidden');
}

function closeDetailPanel() {
    document.getElementById('detail-panel').classList.add('hidden');
}

function renderRFCCompliance(data) {
    const compliance = data.rfc_compliance;

    const summaryEl = document.getElementById('rfc-summary');
    summaryEl.innerHTML = `
        <div class="summary-card">
            <div class="number passed">${compliance.passed}</div>
            <div class="label">Passed</div>
        </div>
        <div class="summary-card">
            <div class="number failed">${compliance.failed}</div>
            <div class="label">Failed</div>
        </div>
        <div class="summary-card">
            <div class="number percentage">${compliance.percentage}%</div>
            <div class="label">Score</div>
        </div>
    `;

    const checksEl = document.getElementById('rfc-checks');
    checksEl.innerHTML = '';

    const rfcNames = {
        'RFC4034': 'RFC 4034 - Resource Records',
        'RFC4035': 'RFC 4035 - Protocol Modifications',
        'RFC6840': 'RFC 6840 - Clarifications',
        'RFC9364': 'RFC 9364 - Operational Practices'
    };

    const rfcOrder = ['RFC4034', 'RFC4035', 'RFC6840', 'RFC9364'];

    rfcOrder.forEach(rfc => {
        const checks = compliance.by_rfc[rfc];
        if (!checks || checks.length === 0) return;

        const passed = checks.filter(c => c.passed === true).length;
        const failed = checks.filter(c => c.passed === false).length;
        const total = checks.filter(c => c.passed !== null).length;

        const group = document.createElement('div');
        group.className = 'rfc-group';
        group.innerHTML = `
            <div class="rfc-group-header" onclick="toggleRFCGroup(this)">
                <div class="rfc-group-title">
                    <span>${rfcNames[rfc] || rfc}</span>
                </div>
                <div class="rfc-group-stats">
                    <span class="passed-count">${passed} passed</span>
                    <span class="failed-count">${failed} failed</span>
                    <span class="expand-icon">▼</span>
                </div>
            </div>
            <div class="rfc-group-content">
                ${checks.map(check => renderCheck(check)).join('')}
            </div>
        `;

        checksEl.appendChild(group);
    });
}

function renderCheck(check) {
    let iconClass, iconText;
    if (check.passed === true) {
        iconClass = 'pass';
        iconText = '✓';
    } else if (check.passed === false) {
        iconClass = 'fail';
        iconText = '✗';
    } else {
        iconClass = 'na';
        iconText = '—';
    }

    return `
        <div class="rfc-check">
            <div class="check-icon ${iconClass}">${iconText}</div>
            <div class="check-content">
                <div class="check-id">${check.check_id}</div>
                <div class="check-description">${check.description}</div>
                ${check.details ? `<div class="check-details">${check.details}</div>` : ''}
            </div>
        </div>
    `;
}

function toggleRFCGroup(header) {
    const group = header.parentElement;
    group.classList.toggle('expanded');
}
