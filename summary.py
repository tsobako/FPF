#!/usr/bin/env python3
"""
FPF Specification - Split Summary

Shows the final state of the split specification with pretty table formatting.
"""

import os
import re

SPEC_DIR = "spec"

def count_files():
    """Count files in spec directory."""
    stats = {
        'total': 0,
        'patterns': 0,
        'intro': 0,
        'readme': 0,
        'by_part': {}
    }
    
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
                elif part == '0-Intro' or re.match(r'\d{2}-', f):
                    stats['intro'] += 1
                    stats['by_part'][part]['intro'] += 1
                else:
                    stats['patterns'] += 1
                    stats['by_part'][part]['patterns'] += 1
    
    return stats

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
    stats = count_files()
    
    print()
    print_separator()
    print(' ' * 25 + 'FPF Specification - Split Summary')
    print_separator()
    print()
    
    # Overview Table
    print('📊 Overview:')
    print()
    headers = ['Component', 'Count', 'Percentage']
    widths = [25, 10, 15]
    
    print_table_header(widths, headers)
    print_table_row(widths, ['Total Markdown Files', stats['total'], f"{100.0:.1f}%"])
    print_table_row(widths, ['Pattern Files', stats['patterns'], f"{100*stats['patterns']/stats['total']:.1f}%"])
    print_table_row(widths, ['Intro Chapters', stats['intro'], f"{100*stats['intro']/stats['total']:.1f}%"])
    print_table_row(widths, ['README Indexes', stats['readme'], f"{100*stats['readme']/stats['total']:.1f}%"])
    print_table_footer(widths)
    print()
    
    # Detailed By Part Table
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
                dir_name = part
                print_table_row(widths, [
                    part_display,
                    dir_name,
                    p['patterns'],
                    p['intro'] if p['intro'] > 0 else '-',
                    p['readme'],
                    total
                ], align='left')
                grand_total['patterns'] += p['patterns']
                grand_total['intro'] += p['intro']
                grand_total['readme'] += p['readme']
                grand_total['total'] += total
    
    # Total row with emphasis
    print_table_row(widths, ['TOTAL', '', grand_total['patterns'], grand_total['intro'], grand_total['readme'], grand_total['total']], align='center')
    print_table_footer(widths)
    print()
    
    # Part Details
    print('📋 Part Details:')
    print()
    
    details_headers = ['Part', 'Description', 'Files']
    details_widths = [8, 50, 8]
    
    part_descriptions = {
        '0-Intro': 'Preface & Introduction (non-normative orientation)',
        'A-Kernel': 'Kernel Architecture Cluster (core ontology)',
        'B-Reasoning': 'Trans-disciplinary Reasoning Cluster',
        'C-Calculi': 'Calculi and Characteristic Spaces',
        'D-Discipline': 'Discipline-Specific Patterns',
        'E-Publication': 'Editorial and Publication Patterns',
        'F-Coordination': 'Coordination and Bridge Patterns',
        'G-SoTA': 'Discipline SoTA Patterns Kit',
        'H-Glossary': 'Glossary & Definitional Pattern Index',
        'I-Annexes': 'Annexes & Extended Tutorials',
        'J-Indexes': 'Indexes & Navigation Aids',
        'K-LexicalDebt': 'Lexical Debt',
    }
    
    print_table_header(details_widths, details_headers)
    
    for part in part_order:
        if part in stats['by_part']:
            p = stats['by_part'][part]
            total = p['patterns'] + p['readme'] + p['intro']
            if total > 0:
                part_display = part.split('-')[0] if '-' in part else part
                desc = part_descriptions.get(part, 'N/A')
                # Truncate description if too long
                if len(desc) > details_widths[1]:
                    desc = desc[:details_widths[1]-3] + '...'
                print_table_row(details_widths, [part_display, desc, total])
    
    print_table_footer(details_widths)
    print()
    
    # Summary
    print_separator()
    print('✅ Split Complete!')
    print(f'   Original: FPF-Spec.md (74,359 lines)')
    print(f'   Split:    spec/ directory ({stats["total"]} files)')
    print(f'   Coverage: {grand_total["patterns"]} patterns across {len([p for p in part_order if p in stats["by_part"]])} parts')
    print_separator()
    print()

if __name__ == '__main__':
    main()
