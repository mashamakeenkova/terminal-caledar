import sys

def extract_lines(day, filename):
    result = []
    current_day = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == day:
                current_day = day
            elif line == ";;;":
                current_day = None
            elif current_day == day and line:
                print(line)

if len(sys.argv) != 3:
    print("Usage: python extract_lines.py <day> <filename>")
    sys.exit(1)

day = sys.argv[1]
filename = sys.argv[2]

result = extract_lines(day, filename)
#print(result)