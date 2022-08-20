
from fileinput import filename


def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:  # sig 會去除 \ufeff
        for line in f:
            lines.append(line.strip())  # strip() 去除string前後的東西
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()