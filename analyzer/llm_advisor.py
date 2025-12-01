"""
LLM Advisor module for generating DNSSEC recommendations using Google Gemini.
"""
import os
import json
import google.generativeai as genai
from typing import Dict, Any, Optional


class LLMAdvisor:
    """Generates AI-powered recommendations based on DNSSEC analysis results."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the LLM advisor with Gemini API.

        Args:
            api_key: Gemini API key. If not provided, reads from GEMINI_API_KEY env var.
        """
        self.api_key = api_key or os.environ.get('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY environment variable.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.cache = {}

    def get_recommendations(self, analysis: Dict[str, Any], mode: str = 'executive') -> str:
        """
        Generate recommendations based on DNSSEC analysis.

        Args:
            analysis: The full analysis result from the DNSSEC analyzer
            mode: 'executive' or 'technical'

        Returns:
            Markdown-formatted recommendations string
        """
        domain = analysis.get('domain', 'unknown')
        cache_key = f"{domain}:{mode}"

        # Check cache
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Build prompt
        prompt = self._build_prompt(analysis, mode)

        try:
            response = self.model.generate_content(prompt)
            result = response.text
            self.cache[cache_key] = result
            return result
        except Exception as e:
            raise RuntimeError(f"Failed to generate recommendations: {str(e)}")

    def _build_prompt(self, analysis: Dict[str, Any], mode: str) -> str:
        """Build the prompt for the LLM based on analysis data and mode."""
        domain = analysis.get('domain', 'unknown')
        dnssec = analysis.get('analysis', {}).get('dnssec', {})
        rfc_compliance = analysis.get('rfc_compliance', {})

        # Extract key information
        summary = dnssec.get('summary', {})
        dnssec_enabled = summary.get('dnssec_enabled', False)
        chain_complete = summary.get('chain_complete', False)
        has_signatures = summary.get('has_signatures', False)
        has_ds_record = summary.get('has_ds_record', False)
        nsec_type = summary.get('nsec_type', 'none')

        # RFC compliance info
        rfc_score = rfc_compliance.get('score', '0/0')
        rfc_percentage = rfc_compliance.get('percentage', 0)
        failed_checks = [
            check for check in rfc_compliance.get('checks', [])
            if check.get('passed') is False
        ]

        # DNSKEY info
        dnskey = dnssec.get('dnskey', {})
        keys = dnskey.get('keys', [])

        # Chain of trust info
        chain = dnssec.get('chain_of_trust', {})
        broken_at = chain.get('broken_at')

        # Build analysis summary for context
        analysis_summary = f"""
## Domain Analysis Summary for {domain}

### DNSSEC Status
- **DNSSEC Enabled:** {dnssec_enabled}
- **Chain of Trust Complete:** {chain_complete}
- **Has Valid Signatures:** {has_signatures}
- **Has DS Record in Parent Zone:** {has_ds_record}
- **NSEC Type:** {nsec_type}
{f'- **Chain Broken At:** {broken_at}' if broken_at else ''}

### RFC Compliance
- **Score:** {rfc_score} ({rfc_percentage}%)
- **Failed Checks:** {len(failed_checks)}

### DNSKEY Information
- **Number of Keys:** {len(keys)}
"""

        if keys:
            for i, key in enumerate(keys, 1):
                key_type = "KSK" if key.get('is_sep') else "ZSK"
                analysis_summary += f"- Key {i}: {key_type}, Algorithm {key.get('algorithm')} ({key.get('algorithm_name')}), {key.get('key_size_bits')} bits\n"

        if failed_checks:
            analysis_summary += "\n### Failed RFC Checks\n"
            for check in failed_checks[:10]:  # Limit to 10 for brevity
                analysis_summary += f"- **{check.get('check_id')}:** {check.get('description')} - {check.get('details', 'No details')}\n"

        # Mode-specific prompts
        if mode == 'executive':
            prompt = f"""You are a cybersecurity advisor providing a brief executive summary for non-technical stakeholders.

Based on the following DNSSEC analysis for the domain **{domain}**, provide a concise executive summary.

{analysis_summary}

Please provide your response in the following format (use Markdown):

## Security Posture
[1-2 sentences describing the overall security state]

## Risk Level
[One of: **Low**, **Medium**, **High**, or **Critical** with a brief explanation]

## Key Findings
[3-4 bullet points of the most important findings]

## Recommended Actions
[3-4 prioritized action items for management, written in business terms]

## Business Impact
[Brief explanation of what this means for the organization]

Keep the response concise and avoid technical jargon. Focus on business impact and actionable recommendations.
"""
        else:  # technical mode
            prompt = f"""You are a DNS/DNSSEC expert providing detailed technical recommendations.

Based on the following DNSSEC analysis for the domain **{domain}**, provide comprehensive technical guidance.

{analysis_summary}

Please provide your response in the following format (use Markdown):

## Technical Assessment
[Detailed assessment of the current DNSSEC configuration]

## Issues Identified
[List all identified issues with technical details]

## Configuration Recommendations

### Immediate Actions (Critical)
[Steps that should be taken immediately]

### Short-term Improvements
[Improvements to implement within 30 days]

### Long-term Best Practices
[Ongoing maintenance and best practices]

## Implementation Guide
[Specific DNS records to add or modify, with examples where applicable]

## RFC References
[Relevant RFC citations for compliance]

## Monitoring Recommendations
[What to monitor and how to maintain DNSSEC health]

Be specific and technical. Include command examples or DNS record formats where helpful.
"""

        return prompt

    def clear_cache(self):
        """Clear the recommendations cache."""
        self.cache = {}
