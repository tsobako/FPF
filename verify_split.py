#!/usr/bin/env python3
"""
FPF Specification Split - Final Verification

Checks that all patterns with actual content (## headers) in FPF-Spec.md
have corresponding files in spec/ directory.
"""

import os
import re
import sys

INPUT_FILE = "FPF-Spec.md"
SPEC_DIR = "spec"

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def extract_patterns_with_content(content):
    """Extract pattern IDs that have actual ## header sections."""
    pattern_ids = set()
    
    # Match ## A.Y.Z or ## A.Y patterns (actual content sections)
    matches = re.findall(r'^##\s+([A-Z]\.\d+(?:\.\d+)*(?:\.[A-Z0-9\-]+)?)\s*[-–:]', content, re.MULTILINE)
    pattern_ids.update(matches)
    
    # Also match ## A.Y.Z without dash (some patterns)
    matches2 = re.findall(r'^##\s+([A-Z]\.\d+(?:\.\d+)*(?:\.[A-Z0-9]+)?)\s*$', content, re.MULTILINE)
    pattern_ids.update(matches2)
    
    return sorted(pattern_ids)

def get_split_pattern_ids():
    """Get all pattern IDs from split files."""
    pattern_ids = set()
    
    for root, dirs, filenames in os.walk(SPEC_DIR):
        for filename in filenames:
            if filename.endswith('.md') and filename != 'README.md':
                # Extract ID from filename
                match = re.match(r'([A-Z]\.\d+(?:\.\d+)*(?:\.[A-Z0-9\-]+)?)', filename)
                if match:
                    pattern_ids.add(match.group(1))
    
    return sorted(pattern_ids)

def main():
    print("=" * 80)
    print("FPF Specification Split - Final Verification")
    print("=" * 80)
    
    # Read original
    print(f"\nReading {INPUT_FILE}...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found")
        return 1
    
    original = read_file(INPUT_FILE)
    print(f"Original size: {len(original):,} chars")
    
    # Extract patterns with actual content
    original_patterns = extract_patterns_with_content(original)
    print(f"Patterns with ## headers in original: {len(original_patterns)}")
    
    # Get split file IDs
    split_patterns = get_split_pattern_ids()
    print(f"Pattern files in {SPEC_DIR}/: {len(split_patterns)}")
    
    # Compare
    original_set = set(original_patterns)
    split_set = set(split_patterns)
    
    missing_in_split = original_set - split_set
    extra_in_split = split_set - original_set
    common = original_set & split_set
    
    print(f"\n{'=' * 80}")
    print("Verification Results:")
    print(f"{'=' * 80}")
    print(f"✅ Matched: {len(common)} patterns")
    
    if missing_in_split:
        print(f"\n❌ Missing in split files: {len(missing_in_split)}")
        for pid in sorted(missing_in_split):
            print(f"   - {pid}")
    else:
        print(f"\n✅ All patterns with content are present in split files!")
    
    if extra_in_split:
        print(f"\n⚠️  Extra files (not in original ## headers): {len(extra_in_split)}")
        for pid in sorted(extra_in_split):
            print(f"   + {pid}")
    
    # File statistics
    total_files = 0
    intro_files = 0
    pattern_files = 0
    
    for root, dirs, filenames in os.walk(SPEC_DIR):
        for f in filenames:
            if f.endswith('.md'):
                total_files += 1
                if f == 'README.md':
                    pass  # index file
                elif re.match(r'\d{2}-', f):
                    intro_files += 1
                else:
                    pattern_files += 1
    
    print(f"\n{'=' * 80}")
    print(f"File Statistics:")
    print(f"{'=' * 80}")
    print(f"Total markdown files: {total_files}")
    print(f"  - Pattern files: {pattern_files}")
    print(f"  - Intro chapters: {intro_files}")
    print(f"  - README indexes: {total_files - pattern_files - intro_files}")
    
    # Summary
    print(f"\n{'=' * 80}")
    if not missing_in_split:
        print("✅ SUCCESS: All patterns with content properly split!")
        print(f"   {len(common)} patterns verified")
    else:
        print("⚠️  Some patterns missing:")
        for pid in list(missing_in_split)[:10]:
            print(f"   - {pid}")
        if len(missing_in_split) > 10:
            print(f"   ... and {len(missing_in_split) - 10} more")
    print(f"{'=' * 80}")
    
    return 0 if not missing_in_split else 1

if __name__ == '__main__':
    sys.exit(main())
