import re
import sys

header_pattern = re.compile(r'(?P<hashes>#{1,3})\s+(?P<header_text>.+)')
ordered_item_pattern = re.compile(r'\d+\.\s+(?P<item_text>.+)')
image_pattern = re.compile(r'!\[(?P<alt_text>[^\]]*)\]\((?P<image_path>[^)\s]+)\)')
link_pattern = re.compile(r'\[(?P<link_text>[^\]]+)\]\((?P<link_url>[^)\s]+)\)')
bold_pattern = re.compile(r'\*\*(?=\S)(?P<bold_text>.+?)(?<=\S)\*\*')
italic_pattern = re.compile(r'\*(?=\S)(?P<italic_text>.+?)(?<=\S)\*')


def convert_inline_elements(text):
    text = image_pattern.sub(r'<img src="\g<image_path>" alt="\g<alt_text>"/>', text)
    text = link_pattern.sub(r'<a href="\g<link_url>">\g<link_text></a>', text)
    text = bold_pattern.sub(r'<b>\g<bold_text></b>', text)
    text = italic_pattern.sub(r'<i>\g<italic_text></i>', text)
    return text


def convert_markdown_to_html(markdown_text):
    html_lines = []
    inside_ordered_list = False

    for markdown_line in markdown_text.splitlines():
        stripped_line = markdown_line.strip()

        ordered_item_match = ordered_item_pattern.fullmatch(stripped_line)
        if ordered_item_match:
            if not inside_ordered_list:
                html_lines.append('<ol>')
                inside_ordered_list = True
            item_html = convert_inline_elements(ordered_item_match.group('item_text'))
            html_lines.append(f'<li>{item_html}</li>')
            continue

        if inside_ordered_list:
            html_lines.append('</ol>')
            inside_ordered_list = False

        header_match = header_pattern.fullmatch(stripped_line)
        if header_match:
            header_level = len(header_match.group('hashes'))
            header_html = convert_inline_elements(header_match.group('header_text'))
            html_lines.append(f'<h{header_level}>{header_html}</h{header_level}>')
        else:
            html_lines.append(convert_inline_elements(markdown_line))

    if inside_ordered_list:
        html_lines.append('</ol>')

    return '\n'.join(html_lines)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as markdown_file:
            markdown_text = markdown_file.read()
    else:
        markdown_text = sys.stdin.read()

    html_text = convert_markdown_to_html(markdown_text)

    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w', encoding='utf-8') as html_file:
            html_file.write(html_text + '\n')
    else:
        print(html_text)


if __name__ == '__main__':
    main()
