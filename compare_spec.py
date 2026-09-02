#!/usr/bin/env python3
"""
FPF Specification - Difference Checker (Content-Aware)

Shows SEMANTIC differences between original FPF-Spec.md and split files.
Ignores: whitespace, blank lines, header level differences (# vs ##)
"""

import os
import re
import sys
import difflib

INPUT_FILE = "FPF-Spec.md"
SPEC_DIR = "spec"
OUTPUT_DIFF = "spec_diff_report.txt"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def get_pattern_files(part_dir):
    """Get all pattern files sorted by ID."""
    if not os.path.isdir(part_dir):
        return []
    
    files = []
    for f in os.listdir(part_dir):
        if f.endswith('.md') and f != 'README.md':
            files.append(os.path.join(part_dir, f))
    
    def sort_key(filepath):
        filename = os.path.basename(filepath)
        match = re.match(r'([A-Z]?\d*(?:\.\d+)*|[A-Z])', filename)
        if match:
            id_part = match.group(1)
            parts = []
            for p in id_part.split('.'):
                if p.isdigit():
                    parts.append((0, int(p)))
                else:
                    parts.append((1, p))
            return parts
        return [(1, filename)]
    
    return sorted(files, key=sort_key)

def reconstruct_spec():
    """Reconstruct spec from split files."""
    reconstructed = []
    original = read_file(INPUT_FILE)

    # Document header
    header_match = re.search(r'^(.*?)^# Table of Content', original, re.MULTILINE | re.DOTALL)
    if header_match:
        reconstructed.append(header_match.group(1).rstrip())

    # Table of Contents
    toc_path = os.path.join(SPEC_DIR, '0-Intro', '01-table-of-content.md')
    if os.path.exists(toc_path):
        toc_content = read_file(toc_path)
        toc_content = re.sub(r'^# Table of Content\s*\n', '', toc_content).rstrip()
        reconstructed.append(f"\n# Table of Content\n\n{toc_content}")

    # Keywords
    keywords_path = os.path.join(SPEC_DIR, '0-Intro', '00-keywords-search-queries-discipline.md')
    if os.path.exists(keywords_path):
        keywords_content = read_file(keywords_path)
        keywords_content = re.sub(r'^# Keywords & Search Queries Discipline\s*\n', '', keywords_content).rstrip()
        reconstructed.append(f"\n## Keywords & Search Queries Discipline\n\n{keywords_content}")

    # Preface
    reconstructed.append("\n\n# **Preface** (non-normative)\n\n")

    # Intro chapters
    intro_dir = os.path.join(SPEC_DIR, '0-Intro')
    intro_files = sorted([f for f in os.listdir(intro_dir)
                         if f.endswith('.md')
                         and f not in ['README.md', '00-keywords-search-queries-discipline.md', '01-table-of-content.md']])

    for filename in intro_files:
        content = read_file(os.path.join(intro_dir, filename))
        content = re.sub(r'^# (.+)$', r'## \1', content, flags=re.MULTILINE)
        reconstructed.append(content.rstrip())

    # Parts A-K
    parts = [
        ('A-Kernel', 'Part A – Kernel Architecture Cluster'),
        ('B-Reasoning', 'Part B – Trans‑disciplinary Reasoning Cluster'),
        ('C-Calculi', 'Part C — Kernel Extensions Specifications'),
        ('D-Discipline', 'Part D – Discipline-Specific Patterns'),
        ('E-Publication', 'Part E – Editorial and Publication Patterns'),
        ('F-Coordination', 'Part F – Coordination and Bridge Patterns'),
        ('G-SoTA', 'Part G – Discipline SoTA Patterns Kit'),
        ('H-Glossary', 'Part H – Glossary & Definitional Pattern Index'),
        ('I-Annexes', 'Part I – Annexes & Extended Tutorials'),
        ('J-Indexes', 'Part J – Indexes & Navigation Aids'),
        ('K-LexicalDebt', 'Part K – Lexical Debt'),
    ]

    for part_folder, part_header in parts:
        part_path = os.path.join(SPEC_DIR, part_folder)
        if not os.path.isdir(part_path):
            continue

        # Support both bold and non-bold Part headers (FPF-Spec.md uses bold)
        reconstructed.append(f"\n\n# **{part_header}**\n")

        for filepath in get_pattern_files(part_path):
            content = read_file(filepath).rstrip()
            reconstructed.append(content)

    return '\n'.join(reconstructed)

def normalize_for_comparison(text):
    """
    Normalize text for semantic comparison.
    Ignores: whitespace, blank lines, header levels, End markers, table borders, column widths
    """
    # Normalize line endings
    text = text.replace('\r\n', '\n')
    
    # Remove End markers (### A.Y.Z:End or ## A.Y.Z:End or # A.Y.Z:End)
    text = re.sub(r'\n#+\s*[A-K]\.[\d\w]+(?:\.[\d\w-]+)*:End\s*\n', '\n', text)
    
    # Remove table borders (lines with +, ─, │, etc.)
    text = re.sub(r'^[+\-─│┼┌┐└┘├┤┬┴┼]+\s*$', '', text, flags=re.MULTILINE)
    
    # Normalize table rows: collapse multiple spaces in table cells
    # Match lines that look like table rows (start and end with |)
    def normalize_table_row(match):
        row = match.group(0)
        # Split by | and normalize each cell
        cells = row.split('|')
        normalized_cells = []
        for cell in cells:
            # Strip whitespace and collapse internal spaces
            normalized = ' '.join(cell.split())
            normalized_cells.append(normalized)
        return '|'.join(normalized_cells)
    
    text = re.sub(r'^\|.*\|$', normalize_table_row, text, flags=re.MULTILINE)
    
    # Normalize header levels (treat #, ##, ###, etc. as same)
    text = re.sub(r'^#+\s+', '# ', text, flags=re.MULTILINE)
    
    # Normalize dashes (em-dash, en-dash to regular dash)
    text = text.replace('—', '-').replace('–', '-')
    
    # Remove all blank lines
    text = re.sub(r'\n\s*\n', '\n', text)
    
    # Normalize whitespace within lines
    text = re.sub(r'[ \t]+', ' ', text)
    
    # Strip trailing whitespace from each line
    lines = [line.rstrip() for line in text.split('\n')]
    
    # Remove leading/trailing blank lines
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    
    return '\n'.join(lines)

def compare_content(original, reconstructed):
    """Compare normalized content and return semantic differences."""
    orig_norm = normalize_for_comparison(original)
    recon_norm = normalize_for_comparison(reconstructed)
    
    orig_lines = orig_norm.splitlines()
    recon_lines = recon_norm.splitlines()
    
    # Check for exact match after normalization
    if orig_norm == recon_norm:
        return [], 0, 0, True
    
    # Find actual differences
    diff = list(difflib.unified_diff(
        orig_lines, recon_lines,
        fromfile='FPF-Spec.md (normalized)',
        tofile='spec/ (normalized)',
        n=5
    ))
    
    added = sum(1 for line in diff if line.startswith('+') and not line.startswith('+++'))
    removed = sum(1 for line in diff if line.startswith('-') and not line.startswith('---'))
    
    return diff, added, removed, False

def extract_pattern_content(filepath):
    """Extract pattern content without header."""
    content = read_file(filepath)
    # Remove first line (header)
    lines = content.split('\n')
    return '\n'.join(lines[1:]).strip()

def verify_patterns():
    """Verify each pattern file exists and has content."""
    original = read_file(INPUT_FILE)
    
    # Extract all pattern IDs from original
    pattern_ids = set(re.findall(r'^##\s+([A-K]\.\d+(?:\.\d+)*(?:\.[A-Z0-9\-]+)?)\s+[-—]', original, re.MULTILINE))
    
    # Check each pattern
    results = {'found': [], 'missing': [], 'content_match': 0, 'content_diff': []}
    
    for pattern_id in sorted(pattern_ids):
        # Find the pattern file
        found = False
        for root, dirs, filenames in os.walk(SPEC_DIR):
            for filename in filenames:
                if filename.startswith(pattern_id.replace('.', '\\.').replace('-', '[-]')) or \
                   filename.startswith(pattern_id.split('.')[0]) and pattern_id in filename:
                    found = True
                    results['found'].append(pattern_id)
                    break
            if found:
                break
        
        if not found:
            results['missing'].append(pattern_id)
    
    return results

def print_table_header(widths, headers):
    """Print table header with borders."""
    border = '+' + '+'.join(['─' * (w + 2) for w in widths]) + '+'
    print(border)
    row = '|' + '|'.join([f' {h:^{w}} ' for h, w in zip(headers, widths)]) + '|'
    print(row)
    print(border)

def print_table_row(widths, row_data, align='left'):
    """Print a table row."""
    if align == 'right':
        row = '|' + '|'.join([f' {str(d):>{w}} ' for d, w in zip(row_data, widths)]) + '|'
    elif align == 'center':
        row = '|' + '|'.join([f' {str(d):^{w}} ' for d, w in zip(row_data, widths)]) + '|'
    else:
        row = '|' + '|'.join([f' {str(d):<{w}} ' for d, w in zip(row_data, widths)]) + '|'
    print(row)

def print_table_footer(widths):
    """Print table footer."""
    border = '+' + '+'.join(['─' * (w + 2) for w in widths]) + '+'
    print(border)

def print_separator():
    """Print a section separator."""
    print('─' * 80)

def main():
    print("=" * 80)
    print("FPF Specification - Content Comparison")
    print("(Ignoring whitespace, blank lines, header levels)")
    print("=" * 80)

    # Read original
    print(f"\nReading {INPUT_FILE}...")
    original = read_file(INPUT_FILE)
    print(f"Original: {len(original):,} chars")

    # Reconstruct from split
    print(f"\nReconstructing from {SPEC_DIR}/...")
    reconstructed = reconstruct_spec()
    print(f"Reconstructed: {len(reconstructed):,} chars")

    # Normalize and compare
    print(f"\nComparing (content-aware, ignoring whitespace/header levels)...")
    orig_norm = normalize_for_comparison(original)
    recon_norm = normalize_for_comparison(reconstructed)

    print(f"Original (normalized): {len(orig_norm):,} chars")
    print(f"Reconstructed (normalized): {len(recon_norm):,} chars")

    diff, added, removed, is_match = compare_content(original, reconstructed)

    # Verify patterns
    pattern_results = verify_patterns()

    # Generate report
    report = []
    report.append("=" * 80)
    report.append("FPF Specification - Content Comparison Report")
    report.append("(Whitespace, blank lines, and header levels ignored)")
    report.append("=" * 80)

    report.append(f"\n📊 File Statistics:")
    report.append(f"   Original: {len(original):,} chars")
    report.append(f"   Reconstructed: {len(reconstructed):,} chars")
    report.append(f"   Size difference: {len(reconstructed) - len(original):+,} chars ({100*(len(reconstructed)/len(original) - 1):+.2f}%)")

    report.append(f"\n📋 Normalized Comparison:")
    report.append(f"   Original (normalized): {len(orig_norm):,} chars")
    report.append(f"   Reconstructed (normalized): {len(recon_norm):,} chars")
    report.append(f"   Difference: {len(recon_norm) - len(orig_norm):+,} chars ({100*(len(recon_norm)/len(orig_norm) - 1):+.2f}%)")

    report.append(f"\n🔍 Pattern Verification:")
    report.append(f"   Patterns in original: {len(pattern_results['found']) + len(pattern_results['missing'])}")
    report.append(f"   Patterns found in split: {len(pattern_results['found'])}")
    if pattern_results['missing']:
        report.append(f"   Missing patterns: {len(pattern_results['missing'])}")
        for pid in pattern_results['missing'][:10]:
            report.append(f"      - {pid}")
        if len(pattern_results['missing']) > 10:
            report.append(f"      ... and {len(pattern_results['missing']) - 10} more")

    report.append(f"\n{'=' * 80}")
    report.append("RESULT:")
    report.append(f"{'=' * 80}")

    if is_match:
        report.append("\n✅ PERFECT CONTENT MATCH!")
        report.append("   All semantic content is identical.")
        report.append("   Differences are only in:")
        report.append("   - Whitespace and blank lines")
        report.append("   - Header levels (# vs ##)")
        report.append("   - Dash styles (— vs -)")
    else:
        report.append(f"\n⚠️  CONTENT DIFFERENCES FOUND:")
        report.append(f"   +{added} lines added")
        report.append(f"   -{removed} lines removed")
        report.append(f"   See diff details below...")

        if len(diff) > 0:
            report.append(f"\n{'=' * 80}")
            report.append("Sample Differences (first 100 lines):")
            report.append(f"{'=' * 80}\n")
            report.extend(diff[:100])
            if len(diff) > 100:
                report.append(f"\n... ({len(diff) - 100} more lines)")

    # Write report
    report_text = '\n'.join(report)
    with open(OUTPUT_DIFF, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(f"\n{'=' * 80}")
    print(f"Summary:")
    print(f"{'=' * 80}")

    if is_match:
        print(f"\n✅ PERFECT CONTENT MATCH!")
        print(f"   Split files contain identical semantic content.")
        print(f"   Only formatting differences (whitespace, headers, dashes).")
    else:
        print(f"\n⚠️  Content differences: +{added}/-{removed} lines")

    print(f"\nPattern verification: {len(pattern_results['found'])} patterns found")
    if pattern_results['missing']:
        print(f"Missing: {len(pattern_results['missing'])} patterns")

    print(f"\n📄 Full report: {OUTPUT_DIFF}")

    return 0 if is_match else 1

if __name__ == '__main__':
    sys.exit(main())
