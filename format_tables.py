#!/usr/bin/env python3
"""
FPF Specification - Table Formatter

Formats all markdown tables in spec/ files for consistent appearance.
Ensures:
  1. All rows in the column have the SAME width within each table
  2. Rows with dashes contain ONLY ':' and '-' (no whitespaces)
  3. NO whitespaces between '|' and ':' or '|' and '-' in separator rows
  4. Whitespace at first/last position of every cell (except separator row)
"""

import os

SPEC_DIR = "spec"


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def is_table_separator(line):
    """Check if a line is a markdown table separator (contains only -, :, |)."""
    stripped = line.strip()
    if not stripped.startswith('|') or not stripped.endswith('|'):
        return False
    content = stripped[1:-1]
    parts = content.split('|')
    for part in parts:
        cleaned = part.strip()
        if cleaned and not all(c in '-:' for c in cleaned):
            return False
    return len(parts) >= 2


def parse_table_row(line):
    """Parse a table row line into cells (stripped of pipe delimiters)."""
    stripped = line.strip()
    if stripped.startswith('|'):
        stripped = stripped[1:]
    if stripped.endswith('|'):
        stripped = stripped[:-1]
    cells = [cell.strip() for cell in stripped.split('|')]
    return cells


def get_alignment(sep_cell):
    """Determine alignment from separator cell content."""
    text = sep_cell.strip()
    starts_colon = text.startswith(':')
    ends_colon = text.endswith(':')

    if starts_colon and ends_colon:
        return 'center'
    elif starts_colon:
        return 'left'
    elif ends_colon:
        return 'right'
    else:
        return 'left'


def format_table_block(table_lines):
    """Format a table block with uniform column width."""
    if len(table_lines) < 3:
        return table_lines

    rows = []
    for line in table_lines:
        cells = parse_table_row(line)
        if cells:
            rows.append(cells)

    if len(rows) < 3:
        return table_lines

    header = rows[0]
    sep_cells = rows[1]
    data_rows = rows[2:]
    num_cols = len(header)

    # Calculate max width for EACH column independently
    # Width = content width + 2 (for leading/trailing spaces)
    col_widths = []
    for col_idx in range(num_cols):
        max_w = 0
        # Header cell
        if col_idx < len(header):
            max_w = max(max_w, len(header[col_idx]))
        # Data cells
        for row in data_rows:
            if col_idx < len(row):
                max_w = max(max_w, len(row[col_idx]))
        # Add 2 for leading/trailing spaces, minimum width of 3 (1 char + 2 spaces)
        col_widths.append(max(3, max_w + 2))

    formatted = []

    # Header row: "| cell | cell |" format - spaces at first/last position
    header_parts = []
    for i in range(num_cols):
        cell = header[i] if i < len(header) else ''
        # Content width = col_width - 2 (for spaces)
        content_width = col_widths[i] - 2
        header_parts.append(' ' + cell.ljust(content_width) + ' ')
    formatted.append('|' + '|'.join(header_parts) + '|')

    # Separator row: "|:---|:---:|---:|---|" NO spaces around pipes
    # Contains ONLY ':' and '-' characters, no whitespaces
    sep_parts = []
    for i in range(num_cols):
        sep_cell = sep_cells[i] if i < len(sep_cells) else ''
        align = get_alignment(sep_cell)
        # Width for dash row = col_width - 2 (to match content width, no spaces)
        dash_width = col_widths[i] - 2

        if align == 'center':
            # :------: (colon + dashes + colon)
            dash_count = max(0, dash_width - 2)
            sep_parts.append(':' + '-' * dash_count + ':')
        elif align == 'left':
            # :------- (colon + dashes)
            dash_count = max(0, dash_width - 1)
            sep_parts.append(':' + '-' * dash_count)
        elif align == 'right':
            # -------: (dashes + colon)
            dash_count = max(0, dash_width - 1)
            sep_parts.append('-' * dash_count + ':')
        else:
            # -------- (dashes only)
            sep_parts.append('-' * dash_width)

    formatted.append('|' + '|'.join(sep_parts) + '|')

    # Data rows: "| cell | cell |" format - spaces at first/last position
    for row in data_rows:
        row_parts = []
        for i in range(num_cols):
            cell = row[i] if i < len(row) else ''
            # Content width = col_width - 2 (for spaces)
            content_width = col_widths[i] - 2
            row_parts.append(' ' + cell.ljust(content_width) + ' ')
        formatted.append('|' + '|'.join(row_parts) + '|')

    return formatted


def find_and_format_tables(content):
    """Find and format all tables in content."""
    lines = content.split('\n')
    result_lines = []
    table_count = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check if this line starts a table
        if stripped.startswith('|') and '|' in stripped[1:]:
            table_lines = [line]
            j = i + 1

            # Next line should be separator
            if j < len(lines) and is_table_separator(lines[j]):
                table_lines.append(lines[j])
                j += 1

                # Collect data rows (non-separator lines starting with |)
                while j < len(lines):
                    data_line = lines[j].strip()
                    if data_line.startswith('|') and '|' in data_line[1:]:
                        if not is_table_separator(lines[j]):
                            table_lines.append(lines[j])
                            j += 1
                        else:
                            break
                    else:
                        break

                # Format the table if valid
                if len(table_lines) >= 3:
                    formatted_lines = format_table_block(table_lines)
                    result_lines.extend(formatted_lines)
                    table_count += 1
                    i = j
                    continue

        result_lines.append(line)
        i += 1

    return '\n'.join(result_lines), table_count


def format_all_tables():
    """Format tables in all spec files."""
    print("=" * 80)
    print("FPF Specification - Table Formatter")
    print("=" * 80)
    print()

    total_files = 0
    total_tables = 0
    files_with_tables = 0

    for root, dirs, filenames in os.walk(SPEC_DIR):
        for filename in filenames:
            if filename.endswith('.md') and filename != 'README.md':
                filepath = os.path.join(root, filename)
                content = read_file(filepath)

                new_content, table_count = find_and_format_tables(content)

                if table_count > 0:
                    write_file(filepath, new_content)
                    rel_path = filepath.replace(SPEC_DIR + '/', '')
                    print(f"✅ {rel_path}: {table_count} table(s) formatted")
                    files_with_tables += 1
                    total_tables += table_count

                total_files += 1

    print()
    print("=" * 80)
    print(f"Summary:")
    print(f"  Total files checked: {total_files}")
    print(f"  Files with tables: {files_with_tables}")
    print(f"  Total tables formatted: {total_tables}")
    print("=" * 80)
    print()

    return total_tables


if __name__ == '__main__':
    format_all_tables()
