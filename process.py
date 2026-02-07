import re
import logging

logger = logging.getLogger(__name__)

def determine_header_size(line):
    level = 0
    for x in line:
        if x == '#':
            level += 1
        else:
            break
    return level

if __name__ == "__main__":
    in_file = "FPF-Spec.md"
    out_file = "out.md"
    logging.basicConfig(filename="out.log", level=logging.INFO)
    with open(in_file) as f:
        with open(out_file, "w") as out:
            last_header_level = 0
            for (i, line) in enumerate(f):
                header_size = determine_header_size(line.lstrip())
                if header_size != 0:
                    rest_header = line[header_size:].lstrip()
                    # Part header level 1
                    matched_part_text = re.match(r"^(\*{2,2}\s?)?Part\s+([A-Z])", rest_header)
                    if matched_part_text:
                        logger.info(f"Found part {matched_part_text.group(2)}".strip())
                        last_header_level = 1
                        out.write(f"# {rest_header}")
                    else:
                        matched_h2 = re.match(r"^(\*{2,2}\s?)?([A-Z]{1}\.[0-9]+)(?!\.)", rest_header)
                        if matched_h2:
                            logger.info(f"Found h2 {matched_h2.group(2)} -- {rest_header}".strip())
                            last_header_level = 2
                            out.write(f"## {rest_header}")
                        else:
                            matched_h3 = re.match(r"^(\*{2,2}\s?)?([A-Z]{1}\.[0-9]+\.[0-9A-Z]+)(?!\.)", rest_header)
                            if matched_h3:
                                logger.info(f"Found h3 {matched_h3.group(2)} -- {rest_header}".strip())
                                last_header_level = 3
                                out.write(f"### {rest_header}")
                            else:
                                matched_h4 = re.match(r"^(\*{2,2}\s?)?([A-Z]{1}\.[0-9]+\.[0-9]+\.[0-9]+)(?!\.)", rest_header)
                                if matched_h4:
                                    logger.info(f"Found h4 {matched_h4.group(2)} -- {rest_header}".strip())
                                    last_header_level = 4
                                    out.write(f"#### {rest_header}")
                                else:
                                    matched_sublist = re.match(r"^[0-9]+\.[0-9]+", rest_header)
                                    if matched_sublist:
                                        logger.info(f"Found sublist -- {rest_header}".strip())
                                        out.write('#' * (last_header_level + 2) + ' ' + rest_header)
                                    else:
                                        matched_list = re.match(r"^[0-9]+(\)\s?)?", rest_header)
                                        if matched_list:
                                            logger.info(f"Found list -- {rest_header}".strip())
                                            out.write('#' * (last_header_level + 1) + ' ' + rest_header)
                                        else:
                                            logger.info(f"HEADER -- {rest_header.strip()}")
                                            out.write(f'#' * (last_header_level + 1) + ' ' + f"{rest_header}")
                else:
                    out.write(f"{line}")
