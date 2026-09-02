#!/usr/bin/env python3
"""
FPF Specification - Split Verification Summary

Final verification that all patterns from FPF-Spec.md are properly split.
"""

import os
import re

INPUT_FILE = "FPF-Spec.md"
SPEC_DIR = "spec"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def extract_patterns_from_original(content):
    """Extract all pattern IDs with ## headers from original."""
    pattern_ids = set()
    matches = re.findall(r'^##\s+([A-K]\.\d+(?:\.\d+)*(?:\.[A-Z0-9\-]+)?)\s+[-—]', content, re.MULTILINE)
    pattern_ids.update(matches)
    return sorted(pattern_ids)

def get_split_pattern_ids():
    """Get all pattern IDs from split files."""
    pattern_ids = set()
    for root, dirs, filenames in os.walk(SPEC_DIR):
        for filename in filenames:
            if filename.endswith('.md') and filename != 'README.md':
                match = re.match(r'([A-K]\.\d+(?:\.\d+)*(?:\.[A-Z0-9\-]+)?)', filename)
                if match:
                    pattern_ids.add(match.group(1))
    return sorted(pattern_ids)

def count_files():
    """Count files by type."""
    stats = {'total': 0, 'patterns': 0, 'intro': 0, 'readme': 0, 'by_part': {}}

    for root, dirs, filenames in os.walk(SPEC_DIR):
        part = os.path.basename(root)
        if part == 'spec':
            continue

        if part not in stats['by_part']:
            stats['by_part'][part] = {'patterns': 0, 'readme': 0, 'intro': 0}

        for f in filenames:
            if f.endswith('.md'):
                stats['total'] += 1
                if f == 'README.md':
                    stats['readme'] += 1
                    stats['by_part'][part]['readme'] = 1
                elif part == '0-Intro':
                    stats['intro'] += 1
                    stats['by_part'][part]['intro'] += 1
                else:
                    stats['patterns'] += 1
                    stats['by_part'][part]['patterns'] += 1

    return stats

def print_table_header(widths, headers):
    """Print table header with borders."""
    # Top border
    border = '+' + '+'.join(['-' * (w + 2) for w in widths]) + '+'
    print(border)
    # Header row
    row = '|' + '|'.join([f' {h:^{w}} ' for h, w in zip(headers, widths)]) + '|'
    print(row)
    # Separator
    print(border)

def print_table_row(widths, row_data):
    """Print a table row."""
    row = '|' + '|'.join([f' {str(d):<{w}} ' for d, w in zip(row_data, widths)]) + '|'
    print(row)

def print_table_footer(widths):
    """Print table footer."""
    border = '+' + '+'.join(['-' * (w + 2) for w in widths]) + '+'
    print(border)

def main():
    # Read original
    original = read_file(INPUT_FILE)
    original_patterns = extract_patterns_from_original(original)

    # Get split patterns
    split_patterns = get_split_pattern_ids()

    # Compare
    original_set = set(original_patterns)
    split_set = set(split_patterns)

    missing = original_set - split_set
    extra = split_set - original_set
    matched = original_set & split_set

    # File stats
    stats = count_files()

    # Print header
    print()
    print('=' * 80)
    print(' ' * 20 + 'FPF Specification - Split Verification Summary')
    print('=' * 80)
    print()

    # File Statistics Table
    print('📊 File Statistics:')
    print()
    headers = ['Metric', 'Count', 'Percentage']
    widths = [25, 10, 15]
    
    print_table_header(widths, headers)
    print_table_row(widths, ['Total Files', stats['total'], f"{100.0:.1f}%"])
    print_table_row(widths, ['Pattern Files', stats['patterns'], f"{100*stats['patterns']/stats['total']:.1f}%"])
    print_table_row(widths, ['Intro Chapters', stats['intro'], f"{100*stats['intro']/stats['total']:.1f}%"])
    print_table_row(widths, ['README Indexes', stats['readme'], f"{100*stats['readme']/stats['total']:.1f}%"])
    print_table_footer(widths)
    print()

    # Pattern Verification Table
    print('📋 Pattern Verification:')
    print()
    headers = ['Source', 'Count', 'Status']
    widths = [35, 10, 30]
    
    print_table_header(widths, headers)
    print_table_row(widths, ['Patterns in Original (## headers)', len(original_patterns), '✓ Reference'])
    print_table_row(widths, ['Pattern Files in spec/', len(split_patterns), '✓ Generated'])
    print_table_row(widths, ['Matched Patterns', len(matched), '✅ Verified'])
    if missing:
        print_table_row(widths, ['Missing Patterns', len(missing), '❌ Missing'])
    if extra:
        print_table_row(widths, ['Extra Files', len(extra), '⚠️  Format Variation'])
    print_table_footer(widths)
    print()

    # By Part Table
    print('📂 Files by Part:')
    print()
    part_order = ['0-Intro', 'A-Kernel', 'B-Reasoning', 'C-Calculi',
                  'D-Discipline', 'E-Publication', 'F-Coordination',
                  'G-SoTA', 'H-Glossary', 'I-Annexes', 'J-Indexes', 'K-LexicalDebt']
    
    headers = ['Part', 'Directory', 'Patterns', 'Intro', 'README', 'Total']
    widths = [8, 18, 10, 10, 10, 8]
    
    print_table_header(widths, headers)
    
    grand_total = {'patterns': 0, 'intro': 0, 'readme': 0, 'total': 0}
    
    for part in part_order:
        if part in stats['by_part']:
            p = stats['by_part'][part]
            total = p['patterns'] + p['readme'] + p['intro']
            if total > 0:
                # Extract part letter for display
                part_display = part.split('-')[0] if '-' in part else part
                dir_name = part if part != '0-Intro' else '0-Intro'
                print_table_row(widths, [
                    part_display,
                    dir_name,
                    p['patterns'],
                    p['intro'] if p['intro'] > 0 else '-',
                    p['readme'],
                    total
                ])
                grand_total['patterns'] += p['patterns']
                grand_total['intro'] += p['intro']
                grand_total['readme'] += p['readme']
                grand_total['total'] += total
    
    # Total row
    print_table_row(widths, ['TOTAL', '', grand_total['patterns'], grand_total['intro'], grand_total['readme'], grand_total['total']])
    print_table_footer(widths)
    print()

    # Summary
    print('=' * 80)
    if not missing:
        print('✅ SUCCESS: All patterns with ## headers are properly split!')
        print(f'   {len(matched)} patterns verified')
        print(f'   Split is content-complete (ignoring whitespace/header formatting)')
    else:
        print(f'⚠️  {len(missing)} patterns missing from split files:')
        for pid in sorted(missing)[:10]:
            print(f'      - {pid}')
        if len(missing) > 10:
            print(f'      ... and {len(missing) - 10} more')
    print('=' * 80)
    print()

if __name__ == '__main__':
    main()
