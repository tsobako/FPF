#!/usr/bin/env python3
"""
Split FPF-Spec.md into organized directory structure:
- spec/0-Intro/ for Preface and Introduction chapters
- spec/A-Kernel/ for Part A patterns
- spec/B-Reasoning/ for Part B patterns
- spec/C-Calculi/ for Part C patterns
- spec/D-Discipline/ for Part D patterns
- spec/E-Publication/ for Part E patterns
- spec/F-Coordination/ for Part F patterns

Patterns are split at the [A-F].Y.Z level into individual files.
Intro chapters are split by ## headers into individual files.
"""

import re
import os
from pathlib import Path

# Configuration
INPUT_FILE = "FPF-Spec.md"
OUTPUT_BASE = "spec"

# Part name mapping
PART_NAMES = {
    'A': 'A-Kernel',
    'B': 'B-Reasoning',
    'C': 'C-Calculi',
    'D': 'D-Discipline',
    'E': 'E-Publication',
    'F': 'F-Coordination',
    'G': 'G-SoTA',
    'H': 'H-Glossary',
    'I': 'I-Annexes',
    'J': 'J-Indexes',
    'K': 'K-LexicalDebt',
}

# Intro folder name
INTRO_FOLDER = '0-Intro'

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

def get_part_folder(pattern_id):
    """Extract part letter from pattern ID and return folder name."""
    part_letter = pattern_id.split('.')[0]
    return PART_NAMES.get(part_letter, f'{part_letter}-Unknown')

def parse_intro_chapters(filepath):
    """Parse the intro/preface section and extract chapters."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of Part A (supports both "# Part A" and "# **Part A...**" formats)
    part_a_match = re.search(r'^#\s+\*\*Part A|^\s*# Part A', content, re.MULTILINE)
    if not part_a_match:
        print("Warning: Could not find Part A start, skipping intro extraction")
        return [], None, None

    # Extract intro content (from start to Part A)
    intro_content = content[:part_a_match.start()]

    # Extract Table of Contents (between "# Table of Content" and "**Part A" or "## Preface")
    # New format: # Table of Content followed by tables until **Part A
    toc_match = re.search(r'^# Table of Content\s*\n\n(.*?)(?=\*\*Part A|\Z)', intro_content, re.MULTILINE | re.DOTALL)
    toc_content = None
    if toc_match:
        toc_content = "# Table of Content\n\n" + toc_match.group(1).strip()

    # Keywords section is no longer separate in new FPF-Spec.md format
    # Keywords are now part of pattern tables, not a separate intro chapter
    keywords_content = None

    # Remove the "# Table of Content" section from intro_content for chapter parsing
    intro_content = re.sub(r'^# Table of Content\s*\n\n.*?(?=\*\*Part A|\Z)', '', intro_content, flags=re.MULTILINE | re.DOTALL)

    # Remove the "# **Preface** (non-normative)" header as it's just a section divider
    # Match with 1-3 # symbols and optional trailing whitespace
    intro_content = re.sub(r'^#{1,3}\s+\*\*Preface\*\*\s+\(non-normative\)\s*$', '', intro_content, flags=re.MULTILINE)

    # Find all chapter headers (## Chapter Title)
    chapter_header_re = re.compile(r'^## (.+)$', re.MULTILINE)
    matches = list(chapter_header_re.finditer(intro_content))

    chapters = []
    chapter_index = 0

    for i, match in enumerate(matches):
        title = match.group(1).strip()

        # Skip "Table of Content" as it's extracted separately
        if 'Table of Content' in title:
            continue

        # Get start position of this chapter
        start_pos = match.start()

        # Get end position (start of next chapter or end of intro content)
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(intro_content)

        # Extract chapter content
        chapter_content = intro_content[start_pos:end_pos]

        # Remove End markers if any (### Chapter:End)
        chapter_content = re.sub(r'\n###?\s+[^:]+:End\s*\n', '\n', chapter_content)

        # Create a slug from title for filename with index (shifted by 1 for ToC only)
        slug = create_slug(title, chapter_index + 1)

        chapters.append({
            'index': chapter_index,
            'title': title,
            'slug': slug,
            'content': chapter_content,
        })

        chapter_index += 1

    return chapters, toc_content, keywords_content

def create_slug(title, index=None):
    """Create a filename-safe slug from a title with optional index prefix."""
    # Remove special characters and convert to lowercase
    slug = title.lower()
    # Remove asterisks and other special chars but keep hyphens
    slug = re.sub(r'[^a-z0-9\s\-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    # Truncate if too long (leave room for index)
    max_len = 80
    if index is not None:
        max_len -= 3  # Leave room for "00-" or "000-"
    if len(slug) > max_len:
        slug = slug[:max_len]
    
    # Add index prefix if provided
    if index is not None:
        slug = f"{index:02d}-{slug}"
    
    return slug + '.md'

def parse_patterns(filepath):
    """Parse the spec file and extract patterns with their content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all pattern headers (## [A-K].Y.Z or ## [A-K].Y)
    # Pattern header format: ^## [A-K]\.[\d\w]+(\.[\d\w]+)* [-—] Title
    # Support both hyphen (-) and em-dash (—), and alphanumeric segment IDs (e.g., A.6.B, A.19.SURF-SPACE)
    pattern_header_re = re.compile(r'^(## ([A-K]\.[\d\w]+(?:\.[\d\w-]+)*))\s+[-—]\s+(.+)$', re.MULTILINE)
    
    matches = list(pattern_header_re.finditer(content))
    
    patterns = []
    for i, match in enumerate(matches):
        header_line = match.group(1)  # Full header line (## A.1.1 - Title)
        pattern_id = match.group(2)    # Pattern ID (A.1.1)
        title = match.group(3).strip() # Title
        
        # Get start position of this pattern
        start_pos = match.start()
        
        # Get end position (start of next pattern or end of file)
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)
        
        # Extract pattern content
        pattern_content = content[start_pos:end_pos]
        
        # Remove End markers (### A.Y.Z:End or ## A.Y.Z:End)
        pattern_content = re.sub(r'\n###?\s+[A-K]\.[\d\w]+(?:\.[\d\w-]+)*:End\s*\n', '\n', pattern_content)
        
        patterns.append({
            'id': pattern_id,
            'title': title,
            'content': pattern_content,
            'header': header_line
        })
    
    return patterns

def sanitize_filename(pattern_id):
    """Convert pattern ID to safe filename."""
    # Replace dots with underscores for filesystem
    return f"{pattern_id}.md"

def create_pattern_file(pattern, output_dir):
    """Write pattern to individual file."""
    filename = sanitize_filename(pattern['id'])
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(pattern['content'])
    
    return filepath

def create_part_index(part_letter, patterns, output_dir):
    """Create index file for each part."""
    index_path = os.path.join(output_dir, 'README.md')

    part_name = PART_NAMES.get(part_letter, f'Part {part_letter}')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(f"# {part_name}\n\n")
        f.write(f"Patterns from Part {part_letter} of FPF Specification.\n\n")
        f.write("## Patterns\n\n")

        # Group by major section (A.1, A.2, etc.)
        sections = {}
        for p in patterns:
            parts = p['id'].split('.')
            if len(parts) >= 2:
                section = f"{parts[0]}.{parts[1]}"
            else:
                section = parts[0]

            if section not in sections:
                sections[section] = []
            sections[section].append(p)

        for section_id in sorted(sections.keys()):
            section_patterns = sections[section_id]
            f.write(f"### {section_id}\n\n")

            for p in section_patterns:
                filename = sanitize_filename(p['id']).replace('.md', '')
                f.write(f"- [[{filename}|{p['id']} - {p['title']}]]\n")

            f.write("\n")

    return index_path

def create_intro_chapter_file(chapter, output_dir):
    """Write intro chapter to individual file with corrected header levels."""
    filepath = os.path.join(output_dir, chapter['slug'])
    
    # Promote all headers by one level (## -> #, ### -> ##, etc.)
    content = chapter['content']
    
    # Promote headers: ## becomes #, ### becomes ##, etc.
    # But only for the chapter content (not the Table of Content which is level 1)
    def promote_header(match):
        hashes = match.group(1)
        rest = match.group(2)
        # Remove one hash to promote the header
        if len(hashes) > 1:
            return '#' * (len(hashes) - 1) + ' ' + rest
        return match.group(0)  # Don't promote level 1 headers
    
    content = re.sub(r'^(#+)\s+(.+)$', promote_header, content, flags=re.MULTILINE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath

def create_intro_index(chapters, toc_content, keywords_content, output_dir):
    """Create index file for intro chapters."""
    index_path = os.path.join(output_dir, 'README.md')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# FPF Specification — Preface & Introduction\n\n")
        f.write("Introductory chapters from the FPF Core Conceptual Specification (non-normative orientation).\n\n")
        f.write("## Chapters\n\n")

        # Add Keywords & Search Queries Discipline first if present
        if keywords_content:
            f.write(f"- [[00-keywords-search-queries-discipline|00. Keywords & Search Queries Discipline]]\n")

        # Add Table of Contents if present
        if toc_content:
            toc_index = 0 if not keywords_content else 1
            f.write(f"- [[{toc_index:02d}-table-of-content|{toc_index:02d}. Table of Contents]]\n")

        for chapter in chapters:
            # Show index number in the link text
            chapter_index = chapter['index'] + (1 if toc_content else 0) + (1 if keywords_content else 0)
            slug_without_ext = chapter['slug'].replace('.md', '')
            f.write(f"- [[{slug_without_ext}|{chapter_index:02d}. {chapter['title']}]]\n")

        f.write("\n")

    return index_path

def main():
    print(f"Reading {INPUT_FILE}...")

    # Parse and split intro chapters first
    print("\n=== Processing Introduction Chapters ===")
    intro_chapters, toc_content, keywords_content = parse_intro_chapters(INPUT_FILE)

    if intro_chapters or toc_content or keywords_content:
        intro_dir = os.path.join(OUTPUT_BASE, INTRO_FOLDER)
        os.makedirs(intro_dir, exist_ok=True)

        # Save Keywords & Search Queries Discipline if found
        if keywords_content:
            keywords_path = os.path.join(intro_dir, '00-keywords-search-queries-discipline.md')
            with open(keywords_path, 'w', encoding='utf-8') as f:
                f.write("# Keywords & Search Queries Discipline\n\n" + keywords_content.strip())
            print(f"  Created: Keywords & Search Queries Discipline")

        # Save Table of Contents if found
        if toc_content:
            toc_index = 0 if not keywords_content else 1
            toc_path = os.path.join(intro_dir, f'{toc_index:02d}-table-of-content.md')
            with open(toc_path, 'w', encoding='utf-8') as f:
                f.write(toc_content)
            print(f"  Created: Table of Contents")

        print(f"Found {len(intro_chapters)} intro chapters")

        # Create individual chapter files
        for chapter in intro_chapters:
            filepath = create_intro_chapter_file(chapter, intro_dir)
            print(f"  Created: {chapter['title']}")

        # Create intro index
        index_path = create_intro_index(intro_chapters, toc_content, keywords_content, intro_dir)
        print(f"Created index: {index_path}")
    
    # Parse and split patterns
    print("\n=== Processing Patterns ===")
    patterns = parse_patterns(INPUT_FILE)
    print(f"Found {len(patterns)} patterns")
    
    # Group patterns by part
    patterns_by_part = {}
    for pattern in patterns:
        part_letter = pattern['id'].split('.')[0]
        if part_letter not in patterns_by_part:
            patterns_by_part[part_letter] = []
        patterns_by_part[part_letter].append(pattern)
    
    # Create files for each part
    part_stats = {}
    for part_letter, part_patterns in sorted(patterns_by_part.items()):
        if part_letter not in PART_NAMES:
            print(f"Skipping Part {part_letter} (not in A-K)")
            continue

        part_folder = PART_NAMES[part_letter]
        output_dir = os.path.join(OUTPUT_BASE, part_folder)

        # Ensure directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Create individual pattern files
        for pattern in part_patterns:
            filepath = create_pattern_file(pattern, output_dir)

        # Create part index
        index_path = create_part_index(part_letter, part_patterns, output_dir)
        
        part_stats[part_letter] = {
            'folder': part_folder,
            'patterns': len(part_patterns)
        }

    # Print summary with tables
    print()
    print_separator()
    print(' ' * 30 + '✓ Split Complete!')
    print_separator()
    print()
    
    # Summary table
    print('📊 Summary:')
    print()
    headers = ['Component', 'Count']
    widths = [30, 10]
    
    total_files = len(intro_chapters) + len(patterns) + len(part_stats) + 1  # +1 for root README
    
    print_table_header(widths, headers)
    print_table_row(widths, ['Intro Chapters', len(intro_chapters)])
    print_table_row(widths, ['Pattern Files', len(patterns)])
    print_table_row(widths, ['Part Indexes', len(part_stats)])
    print_table_row(widths, ['Root README', 1])
    print_table_row(widths, ['TOTAL FILES', total_files], align='center')
    print_table_footer(widths)
    print()
    
    # By Part table
    print('📂 By Part:')
    print()
    part_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    headers = ['Part', 'Directory', 'Patterns']
    widths = [8, 20, 10]
    
    print_table_header(widths, headers)
    
    for part_letter in part_order:
        if part_letter in part_stats:
            stats = part_stats[part_letter]
            print_table_row(widths, [part_letter, stats['folder'], stats['patterns']])
    
    print_table_row(widths, ['TOTAL', '', len(patterns)], align='center')
    print_table_footer(widths)
    print()
    
    print_separator()
    print(f'Output directory: {OUTPUT_BASE}')
    print_separator()
    print()

if __name__ == '__main__':
    main()
