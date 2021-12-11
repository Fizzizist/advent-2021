import sys

def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]

    brack_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
    brack_points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    brack_stack = []
    error_score = 0

    print(lines)

    for line in lines:
        for c in line:
            if c in brack_map:
                brack_stack.append(c)
            elif len(brack_stack) > 0 and c == brack_map[brack_stack[-1]]:
                brack_stack.pop()
            else:
                error_score += brack_points[c]
                break

    print(error_score)

main()
