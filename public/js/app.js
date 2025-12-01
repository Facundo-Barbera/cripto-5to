let currentData = null;
let isNavbarMode = false;
let currentBatchJob = null;
let batchPollInterval = null;
let batchResults = [];
let currentRecommendationMode = 'executive';
let recommendationsCache = {};
let isViewingBatchDetail = false;

// Initialize app after i18n is loaded
document.addEventListener('DOMContentLoaded', async function() {
    await initI18n();

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
    const batchResultsEl = document.getElementById('batch-results');

    const domain = input.value.trim();
    if (!domain) {
        showError(t('errors.emptyDomain'));
        return;
    }

    btn.classList.add('loading');
    btn.disabled = true;
    errorEl.classList.remove('visible');
    resultsEl.classList.add('hidden');
    // Hide batch results when analyzing a single domain
    batchResultsEl.classList.add('hidden');
    isViewingBatchDetail = false;

    try {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ domain })
        });

        const data = await response.json();

        if (!response.ok) {
            // Check if we have domain status info for better error messages
            if (data.domain_status && data.domain_status.status) {
                const statusKey = `domainStatus.${data.domain_status.status}`;
                const translatedMessage = t(statusKey);
                // Use translated message if available, otherwise fall back to server message
                throw new Error(translatedMessage !== statusKey ? translatedMessage : (data.error || t('errors.analysisFailed')));
            }
            throw new Error(data.error || t('errors.analysisFailed'));
        }

        currentData = data;

        // Show sanitized domain info if the input was cleaned
        const sanitizedInfoEl = document.getElementById('sanitized-info');
        if (data.sanitized_from) {
            sanitizedInfoEl.innerHTML = `<span class="sanitized-icon">ℹ️</span> ${t('sanitized.message')} <strong>${data.domain}</strong> ${t('sanitized.from')} "${data.sanitized_from}"`;
            sanitizedInfoEl.classList.remove('hidden');
        } else {
            sanitizedInfoEl.classList.add('hidden');
        }

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
        document.getElementById('current-domain-display').textContent = data.domain;

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
    renderDomainDetails(data);
    renderRFCCompliance(data);
    // Reset AI recommendations UI for new domain
    resetRecommendationsUI();
    // Clear recommendations cache for fresh start
    recommendationsCache = {};
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

        // Better font scaling for long domains
        let fontSize;
        if (displayName.length <= 6) {
            fontSize = 14;
        } else if (displayName.length <= 10) {
            fontSize = 12;
        } else if (displayName.length <= 14) {
            fontSize = 10;
        } else {
            fontSize = 9;
        }

        // Truncate very long domains with ellipsis
        const truncatedName = displayName.length > 18
            ? displayName.substring(0, 15) + '...'
            : displayName;

        const text = bubble.append('text')
            .attr('y', 5)
            .attr('font-size', fontSize)
            .style('opacity', 0)
            .text(truncatedName);

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
        statusEl.innerHTML = `✓ ${t('results.chainComplete')}`;
    } else {
        statusEl.className = 'chain-status broken';
        statusEl.innerHTML = `✗ ${t('results.chainBroken')} <strong>${chainData.broken_at}</strong>`;
    }
}

function showDetailPanel(zone, data) {
    const panel = document.getElementById('detail-panel');
    const zoneEl = document.getElementById('detail-zone');
    const contentEl = document.getElementById('detail-content');

    zoneEl.textContent = zone.zone === '.' ? t('detail.rootZone') : zone.zone;

    let html = `
        <div class="detail-item">
            <div class="label">${t('detail.dnskey')}</div>
            <div class="value ${zone.has_dnskey ? 'yes' : 'no'}">
                ${zone.has_dnskey ? `✓ ${t('detail.present')}` : `✗ ${t('detail.missing')}`}
            </div>
        </div>
        <div class="detail-item">
            <div class="label">${t('detail.dsRecord')}</div>
            <div class="value ${zone.has_ds ? 'yes' : 'no'}">
                ${zone.zone === '.' ? t('detail.naRoot') : (zone.has_ds ? `✓ ${t('detail.present')}` : `✗ ${t('detail.missing')}`)}
            </div>
        </div>
        <div class="detail-item">
            <div class="label">${t('detail.rrsig')}</div>
            <div class="value ${zone.has_rrsig ? 'yes' : 'no'}">
                ${zone.has_rrsig ? `✓ ${t('detail.present')}` : `✗ ${t('detail.missing')}`}
            </div>
        </div>
        <div class="detail-item">
            <div class="label">${t('detail.status')}</div>
            <div class="value ${zone.is_signed ? 'yes' : 'no'}">
                ${zone.is_signed ? `✓ ${t('detail.signed')}` : `✗ ${t('detail.unsigned')}`}
            </div>
        </div>
    `;

    if (zone.algorithms && zone.algorithms.length > 0) {
        html += `
            <div class="detail-item">
                <div class="label">${t('detail.algorithms')}</div>
                <div class="value">${zone.algorithms.join(', ')}</div>
            </div>
        `;
    }

    if (zone.zone === data.domain) {
        const compliance = data.rfc_compliance;
        html += `
            <div class="detail-item">
                <div class="label">${t('detail.rfcCompliance')}</div>
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
            <div class="label">${t('rfc.passed')}</div>
        </div>
        <div class="summary-card">
            <div class="number failed">${compliance.failed}</div>
            <div class="label">${t('rfc.failed')}</div>
        </div>
        <div class="summary-card">
            <div class="number percentage">${compliance.percentage}%</div>
            <div class="label">${t('rfc.score')}</div>
        </div>
    `;

    const checksEl = document.getElementById('rfc-checks');
    checksEl.innerHTML = '';

    const rfcNames = {
        'RFC4034': t('rfc.names.RFC4034'),
        'RFC4035': t('rfc.names.RFC4035'),
        'RFC6840': t('rfc.names.RFC6840'),
        'RFC9364': t('rfc.names.RFC9364')
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
                    <span class="passed-count">${passed} ${t('rfc.passedCount')}</span>
                    <span class="failed-count">${failed} ${t('rfc.failedCount')}</span>
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

function toggleNavMenu() {
    document.getElementById('navbar').classList.toggle('menu-open');
}

// ==================== DOMAIN DETAILS FUNCTIONS ====================

function toggleDomainDetails() {
    const content = document.getElementById('domain-details-content');
    const section = document.querySelector('.domain-details-section');
    content.classList.toggle('hidden');
    section.classList.toggle('expanded');
}

function toggleDetailsGroup(header) {
    const group = header.parentElement;
    group.classList.toggle('expanded');
}

function renderDomainDetails(data) {
    const body = document.getElementById('domain-details-body');
    if (!body || !data) return;

    let html = '';

    // Basic DNS Section
    html += renderBasicDNSSection(data);

    // DNSKEY Section
    html += renderDNSKEYSection(data);

    // RRSIG Section
    html += renderRRSIGSection(data);

    // DS Records Section
    html += renderDSSection(data);

    // NSEC/NSEC3 Section
    html += renderNSECSection(data);

    body.innerHTML = html;
}

function renderBasicDNSSection(data) {
    const dnsBasic = data.analysis?.dns_basic || {};

    let content = '';

    // SOA Records
    if (dnsBasic.SOA && dnsBasic.SOA.length > 0) {
        const soa = dnsBasic.SOA[0];
        content += `
            <div class="details-subsection">
                <div class="subsection-title">${t('domainDetails.soa')}</div>
                <div class="details-grid">
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.primaryServer')}</span>
                        <span class="detail-value">${soa.mname}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.adminEmail')}</span>
                        <span class="detail-value">${soa.rname.replace('.', '@')}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.serial')}</span>
                        <span class="detail-value">${soa.serial}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.refresh')}</span>
                        <span class="detail-value">${formatSeconds(soa.refresh)}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.retry')}</span>
                        <span class="detail-value">${formatSeconds(soa.retry)}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.expire')}</span>
                        <span class="detail-value">${formatSeconds(soa.expire)}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.ttl')}</span>
                        <span class="detail-value">${formatSeconds(soa.ttl)}</span>
                    </div>
                </div>
            </div>
        `;
    }

    // NS Records
    if (dnsBasic.NS && dnsBasic.NS.length > 0) {
        content += `
            <div class="details-subsection">
                <div class="subsection-title">${t('domainDetails.nameservers')} (${dnsBasic.NS.length})</div>
                <div class="details-list">
                    ${dnsBasic.NS.map(ns => `
                        <div class="detail-row">
                            <span class="detail-value">${ns.nameserver}</span>
                            <span class="detail-ttl">TTL: ${formatSeconds(ns.ttl)}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    // A Records
    if (dnsBasic.A && dnsBasic.A.length > 0) {
        content += `
            <div class="details-subsection">
                <div class="subsection-title">${t('domainDetails.ipv4')} (${dnsBasic.A.length})</div>
                <div class="details-list">
                    ${dnsBasic.A.map(a => `
                        <div class="detail-row">
                            <span class="detail-value mono">${a.address}</span>
                            <span class="detail-ttl">TTL: ${formatSeconds(a.ttl)}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    // AAAA Records
    if (dnsBasic.AAAA && dnsBasic.AAAA.length > 0) {
        content += `
            <div class="details-subsection">
                <div class="subsection-title">${t('domainDetails.ipv6')} (${dnsBasic.AAAA.length})</div>
                <div class="details-list">
                    ${dnsBasic.AAAA.map(aaaa => `
                        <div class="detail-row">
                            <span class="detail-value mono">${aaaa.address}</span>
                            <span class="detail-ttl">TTL: ${formatSeconds(aaaa.ttl)}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    // MX Records
    if (dnsBasic.MX && dnsBasic.MX.length > 0) {
        content += `
            <div class="details-subsection">
                <div class="subsection-title">${t('domainDetails.mailServers')} (${dnsBasic.MX.length})</div>
                <div class="details-list">
                    ${dnsBasic.MX.map(mx => `
                        <div class="detail-row">
                            <span class="detail-value">${mx.exchange}</span>
                            <span class="detail-priority">${t('domainDetails.priority')}: ${mx.preference}</span>
                            <span class="detail-ttl">TTL: ${formatSeconds(mx.ttl)}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    if (!content) {
        content = `<div class="no-data">${t('domainDetails.noData')}</div>`;
    }

    return `
        <div class="details-group">
            <div class="details-group-header" onclick="toggleDetailsGroup(this)">
                <div class="details-group-title">${t('domainDetails.basicDns')}</div>
                <span class="expand-icon">▼</span>
            </div>
            <div class="details-group-content">
                ${content}
            </div>
        </div>
    `;
}

function renderDNSKEYSection(data) {
    const dnskey = data.analysis?.dnssec?.dnskey || {};

    let content = '';

    if (dnskey.present && dnskey.keys && dnskey.keys.length > 0) {
        content = `
            <div class="details-subsection">
                <div class="subsection-info">
                    <span>${t('domainDetails.totalKeys')}: ${dnskey.count}</span>
                    <span>TTL: ${formatSeconds(dnskey.ttl)}</span>
                </div>
                ${dnskey.keys.map((key, i) => `
                    <div class="key-card">
                        <div class="key-header">
                            <span class="key-type ${key.is_sep ? 'ksk' : 'zsk'}">${key.is_sep ? 'KSK' : 'ZSK'}</span>
                            <span class="key-algo">${key.algorithm_name}</span>
                        </div>
                        <div class="details-grid">
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.algorithm')}</span>
                                <span class="detail-value">${key.algorithm_name} (${key.algorithm})</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.keySize')}</span>
                                <span class="detail-value">${key.key_size_bits} bits</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.flags')}</span>
                                <span class="detail-value">${key.flags}</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.protocol')}</span>
                                <span class="detail-value">${key.protocol}</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.zoneKey')}</span>
                                <span class="detail-value">${key.is_zone_key ? t('domainDetails.yes') : t('domainDetails.no')}</span>
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    } else {
        content = `<div class="no-data">${t('domainDetails.noDnskey')}</div>`;
    }

    return `
        <div class="details-group">
            <div class="details-group-header" onclick="toggleDetailsGroup(this)">
                <div class="details-group-title">${t('domainDetails.dnskeyRecords')}</div>
                <span class="details-group-status ${dnskey.present ? 'present' : 'absent'}">${dnskey.present ? t('domainDetails.present') : t('domainDetails.absent')}</span>
                <span class="expand-icon">▼</span>
            </div>
            <div class="details-group-content">
                ${content}
            </div>
        </div>
    `;
}

function renderRRSIGSection(data) {
    const rrsig = data.analysis?.dnssec?.rrsig || {};

    let content = '';

    if (rrsig.present && rrsig.signatures && rrsig.signatures.length > 0) {
        const byType = rrsig.signatures_by_type || {};

        content = `
            <div class="details-subsection">
                <div class="subsection-info">
                    <span>${t('domainDetails.totalSignatures')}: ${rrsig.count}</span>
                    ${rrsig.ttl ? `<span>TTL: ${formatSeconds(rrsig.ttl)}</span>` : ''}
                </div>
                ${Object.entries(byType).map(([type, sigs]) => `
                    <div class="sig-type-group">
                        <div class="sig-type-header">${type} ${t('domainDetails.signatures')} (${sigs.length})</div>
                        ${sigs.map(sig => `
                            <div class="sig-card ${sig.is_expired ? 'expired' : 'valid'}">
                                <div class="sig-status ${sig.is_expired ? 'expired' : 'valid'}">
                                    ${sig.is_expired ? t('domainDetails.expired') : t('domainDetails.valid')}
                                </div>
                                <div class="details-grid">
                                    <div class="detail-row">
                                        <span class="detail-label">${t('domainDetails.algorithm')}</span>
                                        <span class="detail-value">${sig.algorithm_name}</span>
                                    </div>
                                    <div class="detail-row">
                                        <span class="detail-label">${t('domainDetails.keyTag')}</span>
                                        <span class="detail-value">${sig.key_tag}</span>
                                    </div>
                                    <div class="detail-row">
                                        <span class="detail-label">${t('domainDetails.signer')}</span>
                                        <span class="detail-value">${sig.signer}</span>
                                    </div>
                                    <div class="detail-row">
                                        <span class="detail-label">${t('domainDetails.inception')}</span>
                                        <span class="detail-value">${formatDate(sig.inception)}</span>
                                    </div>
                                    <div class="detail-row">
                                        <span class="detail-label">${t('domainDetails.expiration')}</span>
                                        <span class="detail-value">${formatDate(sig.expiration)}</span>
                                    </div>
                                    <div class="detail-row">
                                        <span class="detail-label">${t('domainDetails.daysUntilExpiration')}</span>
                                        <span class="detail-value ${sig.days_until_expiration < 7 ? 'warning' : ''}">${sig.days_until_expiration} ${t('domainDetails.days')}</span>
                                    </div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                `).join('')}
            </div>
        `;
    } else {
        content = `<div class="no-data">${t('domainDetails.noRrsig')}</div>`;
    }

    return `
        <div class="details-group">
            <div class="details-group-header" onclick="toggleDetailsGroup(this)">
                <div class="details-group-title">${t('domainDetails.rrsigRecords')}</div>
                <span class="details-group-status ${rrsig.present ? 'present' : 'absent'}">${rrsig.present ? t('domainDetails.present') : t('domainDetails.absent')}</span>
                <span class="expand-icon">▼</span>
            </div>
            <div class="details-group-content">
                ${content}
            </div>
        </div>
    `;
}

function renderDSSection(data) {
    const ds = data.analysis?.dnssec?.ds || {};

    let content = '';

    if (ds.present && ds.records && ds.records.length > 0) {
        content = `
            <div class="details-subsection">
                <div class="subsection-info">
                    <span>${t('domainDetails.totalRecords')}: ${ds.count}</span>
                    <span>TTL: ${formatSeconds(ds.ttl)}</span>
                </div>
                ${ds.records.map((record, i) => `
                    <div class="ds-card">
                        <div class="details-grid">
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.keyTag')}</span>
                                <span class="detail-value">${record.key_tag}</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.algorithm')}</span>
                                <span class="detail-value">${record.algorithm_name} (${record.algorithm})</span>
                            </div>
                            <div class="detail-row">
                                <span class="detail-label">${t('domainDetails.digestType')}</span>
                                <span class="detail-value">${record.digest_type_name} (${record.digest_type})</span>
                            </div>
                            <div class="detail-row digest-row">
                                <span class="detail-label">${t('domainDetails.digest')}</span>
                                <span class="detail-value mono digest">${record.digest}</span>
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    } else {
        content = `<div class="no-data">${t('domainDetails.noDs')}</div>`;
    }

    return `
        <div class="details-group">
            <div class="details-group-header" onclick="toggleDetailsGroup(this)">
                <div class="details-group-title">${t('domainDetails.dsRecords')}</div>
                <span class="details-group-status ${ds.present ? 'present' : 'absent'}">${ds.present ? t('domainDetails.present') : t('domainDetails.absent')}</span>
                <span class="expand-icon">▼</span>
            </div>
            <div class="details-group-content">
                ${content}
            </div>
        </div>
    `;
}

function renderNSECSection(data) {
    const nsec = data.analysis?.dnssec?.nsec || {};

    let content = '';
    const hasNSEC = nsec.nsec_present || nsec.nsec3_present;

    if (hasNSEC) {
        content = `
            <div class="details-subsection">
                <div class="nsec-type-badge ${nsec.nsec_type?.toLowerCase()}">${nsec.nsec_type || 'NONE'}</div>
                <div class="details-grid">
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.nsecType')}</span>
                        <span class="detail-value">${nsec.nsec_type || t('domainDetails.none')}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.nsecPresent')}</span>
                        <span class="detail-value">${nsec.nsec_present ? t('domainDetails.yes') : t('domainDetails.no')}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.nsec3Present')}</span>
                        <span class="detail-value">${nsec.nsec3_present ? t('domainDetails.yes') : t('domainDetails.no')}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.nsec3paramPresent')}</span>
                        <span class="detail-value">${nsec.nsec3param_present ? t('domainDetails.yes') : t('domainDetails.no')}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.optOut')}</span>
                        <span class="detail-value">${nsec.opt_out ? t('domainDetails.yes') : t('domainDetails.no')}</span>
                    </div>
                    ${nsec.detection_source ? `
                    <div class="detail-row">
                        <span class="detail-label">${t('domainDetails.detectionSource')}</span>
                        <span class="detail-value">${nsec.detection_source}</span>
                    </div>
                    ` : ''}
                </div>
                ${renderNSECDetails(nsec.details)}
            </div>
        `;
    } else {
        content = `<div class="no-data">${t('domainDetails.noNsec')}</div>`;
    }

    return `
        <div class="details-group">
            <div class="details-group-header" onclick="toggleDetailsGroup(this)">
                <div class="details-group-title">${t('domainDetails.nsecConfig')}</div>
                <span class="details-group-status ${hasNSEC ? 'present' : 'absent'}">${hasNSEC ? nsec.nsec_type : t('domainDetails.none')}</span>
                <span class="expand-icon">▼</span>
            </div>
            <div class="details-group-content">
                ${content}
            </div>
        </div>
    `;
}

function renderNSECDetails(details) {
    if (!details) return '';

    let html = '';

    if (details.nsec3param && details.nsec3param.records && details.nsec3param.records.length > 0) {
        html += `
            <div class="nsec-details-section">
                <div class="subsection-title">${t('domainDetails.nsec3param')}</div>
                ${details.nsec3param.records.map(record => `
                    <div class="details-grid">
                        <div class="detail-row">
                            <span class="detail-label">${t('domainDetails.hashAlgorithm')}</span>
                            <span class="detail-value">${record.hash_algorithm}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">${t('domainDetails.iterations')}</span>
                            <span class="detail-value">${record.iterations}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">${t('domainDetails.salt')}</span>
                            <span class="detail-value mono">${record.salt || t('domainDetails.none')}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">${t('domainDetails.flags')}</span>
                            <span class="detail-value">${record.flags}</span>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    if (details.nsec3 && details.nsec3.records && details.nsec3.records.length > 0) {
        html += `
            <div class="nsec-details-section">
                <div class="subsection-title">${t('domainDetails.nsec3Records')} (${details.nsec3.count})</div>
                ${details.nsec3.records.slice(0, 3).map(record => `
                    <div class="details-grid">
                        <div class="detail-row">
                            <span class="detail-label">${t('domainDetails.hashAlgorithm')}</span>
                            <span class="detail-value">${record.hash_algorithm}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">${t('domainDetails.iterations')}</span>
                            <span class="detail-value">${record.iterations}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">${t('domainDetails.optOut')}</span>
                            <span class="detail-value">${record.opt_out ? t('domainDetails.yes') : t('domainDetails.no')}</span>
                        </div>
                    </div>
                `).join('')}
                ${details.nsec3.records.length > 3 ? `<div class="more-records">+ ${details.nsec3.records.length - 3} ${t('domainDetails.moreRecords')}</div>` : ''}
            </div>
        `;
    }

    return html;
}

function formatSeconds(seconds) {
    if (seconds === null || seconds === undefined) return 'N/A';
    if (seconds < 60) return `${seconds}s`;
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m`;
    if (seconds < 86400) return `${Math.floor(seconds / 3600)}h`;
    return `${Math.floor(seconds / 86400)}d`;
}

function formatDate(isoString) {
    if (!isoString) return 'N/A';
    const date = new Date(isoString);
    return date.toLocaleDateString(getCurrentLanguage(), {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// ==================== BATCH MODE FUNCTIONS ====================

function setAnalysisMode(mode) {
    const singleMode = document.getElementById('single-mode');
    const batchMode = document.getElementById('batch-mode');
    const batchResultsEl = document.getElementById('batch-results');
    const modeButtons = document.querySelectorAll('.mode-btn');

    modeButtons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.mode === mode);
    });

    if (mode === 'single') {
        singleMode.classList.remove('hidden');
        batchMode.classList.add('hidden');
        // Hide batch results and reset batch state when switching to single mode
        batchResultsEl.classList.add('hidden');
        batchResults = [];
        isViewingBatchDetail = false;
    } else {
        singleMode.classList.add('hidden');
        batchMode.classList.remove('hidden');
    }
}

async function loadDefaultDomains() {
    try {
        const response = await fetch('/api/domains/default');
        const data = await response.json();

        if (data.domains) {
            document.getElementById('batch-domains-input').value = data.domains.join('\n');
        }
    } catch (error) {
        showError('Failed to load default domains');
    }
}

async function startBatchAnalysis() {
    const textarea = document.getElementById('batch-domains-input');
    const btn = document.getElementById('batch-analyze-btn');
    const errorEl = document.getElementById('error-message');
    const batchResultsEl = document.getElementById('batch-results');
    const resultsEl = document.getElementById('results');

    const domainsText = textarea.value.trim();
    if (!domainsText) {
        showError(t('errors.emptyDomain'));
        return;
    }

    const domains = domainsText.split('\n')
        .map(d => d.trim())
        .filter(d => d && !d.startsWith('#'));

    if (domains.length === 0) {
        showError(t('errors.emptyDomain'));
        return;
    }

    btn.classList.add('loading');
    btn.disabled = true;
    errorEl.classList.remove('visible');
    resultsEl.classList.add('hidden');
    batchResultsEl.classList.remove('hidden');

    // Reset progress
    document.getElementById('batch-progress-bar').style.width = '0%';
    document.getElementById('batch-progress-text').textContent = `0 / ${domains.length}`;
    document.getElementById('batch-summary').classList.add('hidden');
    document.getElementById('batch-results-body').innerHTML = '';
    batchResults = [];

    // Process domains sequentially (Vercel-compatible approach)
    let completed = 0;
    let dnssecEnabledCount = 0;
    let chainCompleteCount = 0;
    let errorsCount = 0;
    let totalScore = 0;

    for (const domain of domains) {
        try {
            const response = await fetch('/api/batch', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ domain })
            });

            const data = await response.json();

            const result = {
                domain: data.domain,
                dnssec_enabled: data.dnssec_enabled || false,
                chain_complete: data.chain_complete || false,
                rfc_score: parseInt((data.rfc_score || '0/0').split('/')[0]) || 0,
                rfc_total: parseInt((data.rfc_score || '0/0').split('/')[1]) || 0,
                rfc_percentage: data.rfc_percentage || 0,
                status: data.status === 'OK' ? 'success' : 'error',
                error: data.error || null,
                full_result: data.full_result || null
            };

            batchResults.push(result);

            // Update counters
            if (result.dnssec_enabled) dnssecEnabledCount++;
            if (result.chain_complete) chainCompleteCount++;
            if (result.status === 'error') errorsCount++;
            totalScore += result.rfc_percentage;

        } catch (error) {
            batchResults.push({
                domain: domain,
                dnssec_enabled: false,
                chain_complete: false,
                rfc_score: 0,
                rfc_total: 0,
                rfc_percentage: 0,
                status: 'error',
                error: error.message
            });
            errorsCount++;
        }

        completed++;

        // Update progress
        const progress = (completed / domains.length) * 100;
        document.getElementById('batch-progress-bar').style.width = `${progress}%`;
        document.getElementById('batch-progress-text').textContent = `${completed} / ${domains.length}`;

        // Update table
        updateBatchResultsTable(batchResults);
    }

    // Show summary
    const avgScore = batchResults.length > 0 ? totalScore / batchResults.length : 0;
    document.getElementById('summary-dnssec').textContent = dnssecEnabledCount;
    document.getElementById('summary-chain').textContent = chainCompleteCount;
    document.getElementById('summary-errors').textContent = errorsCount;
    document.getElementById('summary-avg-score').textContent = `${avgScore.toFixed(1)}%`;
    document.getElementById('batch-summary').classList.remove('hidden');

    // Re-enable button
    btn.classList.remove('loading');
    btn.disabled = false;
}

function updateBatchResultsTable(results) {
    const tbody = document.getElementById('batch-results-body');
    tbody.innerHTML = '';

    results.forEach((result, index) => {
        const row = document.createElement('tr');
        row.className = result.status === 'error' ? 'row-error' : '';

        const dnssecClass = result.dnssec_enabled ? 'status-yes' : 'status-no';
        const chainClass = result.chain_complete ? 'status-yes' : 'status-no';
        const statusClass = result.status === 'success' ? 'status-success' : 'status-error';

        // Make domain clickable if we have full results
        const domainCell = result.full_result
            ? `<td class="domain-cell domain-clickable" onclick="viewBatchDomainDetail(${index})">${result.domain}</td>`
            : `<td class="domain-cell">${result.domain}</td>`;

        row.innerHTML = `
            ${domainCell}
            <td class="${dnssecClass}">${result.dnssec_enabled ? t('batch.yes') : t('batch.no')}</td>
            <td class="${chainClass}">${result.chain_complete ? t('batch.yes') : t('batch.no')}</td>
            <td>${result.rfc_percentage.toFixed(1)}%</td>
            <td class="${statusClass}">${result.status === 'success' ? '✓' : (result.error || t('batch.error'))}</td>
        `;
        tbody.appendChild(row);
    });
}

function exportBatchCSV() {
    if (batchResults.length === 0) return;

    const headers = ['Domain', 'DNSSEC Enabled', 'Chain Complete', 'RFC Score', 'RFC Percentage', 'Status', 'Error'];
    const rows = batchResults.map(r => [
        r.domain,
        r.dnssec_enabled ? 'Yes' : 'No',
        r.chain_complete ? 'Yes' : 'No',
        `${r.rfc_score}/${r.rfc_total}`,
        `${r.rfc_percentage.toFixed(1)}%`,
        r.status,
        r.error || ''
    ]);

    const csvContent = [headers, ...rows]
        .map(row => row.map(cell => `"${cell}"`).join(','))
        .join('\n');

    downloadFile(csvContent, 'dnssec-batch-results.csv', 'text/csv');
}

function exportBatchJSON() {
    if (batchResults.length === 0) return;

    const jsonContent = JSON.stringify({
        exported_at: new Date().toISOString(),
        total: batchResults.length,
        results: batchResults
    }, null, 2);

    downloadFile(jsonContent, 'dnssec-batch-results.json', 'application/json');
}

function downloadFile(content, filename, mimeType) {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function viewBatchDomainDetail(index) {
    const result = batchResults[index];
    if (!result || !result.full_result) return;

    isViewingBatchDetail = true;
    currentData = result.full_result;

    // Hide batch results, show single domain results
    const batchResultsEl = document.getElementById('batch-results');
    const resultsEl = document.getElementById('results');

    batchResultsEl.classList.add('hidden');
    resultsEl.classList.remove('hidden');

    // Show back button
    showBackToBatchButton();

    // Switch to navbar mode if not already
    if (!isNavbarMode) {
        switchToNavbarMode();
    }

    // Update navbar display
    document.getElementById('current-domain-display').textContent = result.domain;

    // Render the results
    renderResults(result.full_result);
}

function showBackToBatchButton() {
    // Add back button if not already present
    let backBtn = document.getElementById('back-to-batch-btn');
    if (!backBtn) {
        const resultsEl = document.getElementById('results');
        backBtn = document.createElement('button');
        backBtn.id = 'back-to-batch-btn';
        backBtn.className = 'btn-back-to-batch';
        backBtn.innerHTML = `<span class="back-arrow">←</span> <span data-i18n="batch.backToResults">${t('batch.backToResults')}</span>`;
        backBtn.onclick = backToBatchResults;
        resultsEl.insertBefore(backBtn, resultsEl.firstChild);
    } else {
        backBtn.classList.remove('hidden');
    }
}

function backToBatchResults() {
    isViewingBatchDetail = false;
    currentData = null;

    // Hide single results, show batch results
    const batchResultsEl = document.getElementById('batch-results');
    const resultsEl = document.getElementById('results');

    resultsEl.classList.add('hidden');
    batchResultsEl.classList.remove('hidden');

    // Hide back button
    const backBtn = document.getElementById('back-to-batch-btn');
    if (backBtn) {
        backBtn.classList.add('hidden');
    }

    // Update navbar display
    document.getElementById('current-domain-display').textContent = t('batch.batchMode');
}

// ==================== AI RECOMMENDATIONS FUNCTIONS ====================

function toggleRecommendations() {
    const content = document.getElementById('recommendations-content');
    const section = document.querySelector('.recommendations-section');
    content.classList.toggle('hidden');
    section.classList.toggle('expanded');
}

function setRecommendationMode(mode) {
    currentRecommendationMode = mode;
    const buttons = document.querySelectorAll('.rec-mode-btn');
    buttons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.mode === mode);
    });

    // If we have cached recommendations for this mode, domain, and language, show them
    if (currentData) {
        const cacheKey = `${currentData.domain}:${mode}:${getCurrentLanguage()}`;
        if (recommendationsCache[cacheKey]) {
            renderRecommendations(recommendationsCache[cacheKey]);
        } else {
            // Reset to generate button if no cache
            resetRecommendationsUI();
        }
    }
}

async function generateRecommendations() {
    if (!currentData) return;

    const btn = document.getElementById('generate-recommendations-btn');
    const body = document.getElementById('recommendations-body');
    const currentLanguage = getCurrentLanguage();

    btn.classList.add('loading');
    btn.disabled = true;

    try {
        const response = await fetch('/api/recommendations', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                analysis: currentData,
                mode: currentRecommendationMode,
                language: currentLanguage
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || t('recommendations.error'));
        }

        // Cache the result (include language in cache key)
        const cacheKey = `${currentData.domain}:${currentRecommendationMode}:${currentLanguage}`;
        recommendationsCache[cacheKey] = data.recommendations;

        // Render recommendations
        renderRecommendations(data.recommendations);

    } catch (error) {
        body.innerHTML = `
            <div class="recommendations-error">
                <span class="error-icon">⚠️</span>
                <span>${error.message}</span>
            </div>
            <button id="generate-recommendations-btn" class="btn-generate" onclick="generateRecommendations()">
                <span class="btn-text" data-i18n="recommendations.regenerate">${t('recommendations.regenerate')}</span>
                <span class="btn-loader"></span>
            </button>
        `;
    }
}

function renderRecommendations(markdown) {
    const body = document.getElementById('recommendations-body');

    // Simple markdown to HTML conversion
    let html = markdown
        // Headers
        .replace(/^### (.*$)/gim, '<h4>$1</h4>')
        .replace(/^## (.*$)/gim, '<h3>$1</h3>')
        .replace(/^# (.*$)/gim, '<h2>$1</h2>')
        // Bold
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        // Italic
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        // Code blocks
        .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
        // Inline code
        .replace(/`(.*?)`/g, '<code>$1</code>')
        // Unordered lists
        .replace(/^\- (.*$)/gim, '<li>$1</li>')
        // Line breaks
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>');

    // Wrap list items
    html = html.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

    body.innerHTML = `
        <div class="recommendations-text">
            <p>${html}</p>
        </div>
        <button class="btn-regenerate" onclick="generateRecommendations()">
            <span data-i18n="recommendations.regenerate">${t('recommendations.regenerate')}</span>
        </button>
    `;
}

function resetRecommendationsUI() {
    const body = document.getElementById('recommendations-body');
    body.innerHTML = `
        <button id="generate-recommendations-btn" class="btn-generate" onclick="generateRecommendations()">
            <span class="btn-text" data-i18n="recommendations.generate">${t('recommendations.generate')}</span>
            <span class="btn-loader"></span>
        </button>
    `;
}

function areRecommendationsDisplayed() {
    const body = document.getElementById('recommendations-body');
    // Check if recommendations text is displayed (not just the generate button)
    return body && body.querySelector('.recommendations-text') !== null;
}

async function regenerateRecommendationsForLanguage() {
    // Only regenerate if recommendations are currently displayed and we have data
    if (currentData && areRecommendationsDisplayed()) {
        await generateRecommendations();
    }
}

// Export for use by i18n.js
window.areRecommendationsDisplayed = areRecommendationsDisplayed;
window.regenerateRecommendationsForLanguage = regenerateRecommendationsForLanguage;
