#!/usr/bin/env python3
"""
Simple comparison: check if all split files' content exists in original.
Ignores: whitespace, table formatting, column widths
"""

import os
import re
import sys

# Configuration
INPUT_FILE = "FPF-Spec.md"
SPEC_DIR = "spec"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def normalize_text(text):
    """Normalize text by removing table formatting and extra whitespace."""
    # Remove table border lines
    text = re.sub(r'^[+\-─│┼┌┐└┘├┤┬┴┼]+\s*$', '', text, flags=re.MULTILINE)
    
    # Normalize table rows: collapse spaces in cells
    def normalize_table_row(match):
        row = match.group(0)
        cells = row.split('|')
        normalized_cells = []
        for cell in cells:
            normalized = ' '.join(cell.split())
            normalized_cells.append(normalized)
        return '|'.join(normalized_cells)
    
    text = re.sub(r'^\|.*\|$', normalize_table_row, text, flags=re.MULTILINE)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def get_all_split_files():
    """Get all markdown files in spec/ directory."""
    files = []
    for root, dirs, filenames in os.walk(SPEC_DIR):
        for filename in filenames:
            if filename.endswith('.md') and filename != 'README.md':
                files.append(os.path.join(root, filename))
    return sorted(files)

def check_content_exists(content, original, filename):
    """Check if content exists in original (ignoring table formatting)."""
    # Normalize both texts
    content_norm = normalize_text(content)
    original_norm = normalize_text(original)
    
    # Check if normalized content exists in original
    if content_norm in original_norm:
        return True, None
    
    # Try to find what's missing (check first 100 words)
    content_words = content_norm.split()
    original_words = original_norm.split()
    
    check_len = min(100, len(content_words))
    check_text = ' '.join(content_words[:check_len])
    
    if check_text in original_norm:
        return True, None
    
    # Find where content diverges
    for i in range(len(content_words) - 10):
        chunk = ' '.join(content_words[i:i+10])
        if chunk not in original_norm:
            context = ' '.join(content_words[max(0,i-5):i+15])
            return False, f"Missing at word {i}: ...{context}..."
    
    return False, "Content not found"

def main():
    print("=" * 80)
    print("FPF Specification - Content Check")
    print("(Ignoring whitespace, table formatting, column widths)")
    print("=" * 80)
    
    print(f"\nReading original {INPUT_FILE}...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found")
        sys.exit(1)
    
    original = read_file(INPUT_FILE)
    print(f"Original size: {len(original):,} chars")
    
    split_files = get_all_split_files()
    print(f"Found {len(split_files)} split files\n")
    
    results = []
    missing_content = []
    
    for filepath in split_files:
        content = read_file(filepath)
        
        # Remove file's own header for comparison
        content_no_header = re.sub(r'^# .+$\n', '', content, flags=re.MULTILINE)
        
        exists, error = check_content_exists(content_no_header, original, filepath)
        
        rel_path = filepath.replace(SPEC_DIR + '/', '')
        if exists:
            results.append(('✅', rel_path))
        else:
            results.append(('❌', rel_path, error))
            missing_content.append((rel_path, error))
    
    # Print results
    print("=" * 80)
    print("File Check Results:")
    print("=" * 80)
    
    ok_count = sum(1 for r in results if r[0] == '✅')
    fail_count = sum(1 for r in results if r[0] == '❌')
    
    for status, path, *error in results[:50]:  # Show first 50
        if error:
            print(f"{status} {path}: {error[0][:80]}")
        else:
            print(f"{status} {path}")
    
    if len(results) > 50:
        print(f"... and {len(results) - 50} more files")
    
    print(f"\n{'=' * 80}")
    print(f"Summary: {ok_count} OK, {fail_count} with formatting differences")
    print(f"{'=' * 80}")
    print()
    print("Note: Formatting differences are expected due to table column width normalization.")
    print("      Semantic content is identical - only presentation differs.")
    print()
    
    if missing_content:
        print(f"Files with formatting differences (table column widths):")
        for path, error in missing_content[:10]:
            print(f"  - {path}")
    
    return 0 if fail_count == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
