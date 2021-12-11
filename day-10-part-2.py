import sys
from statistics import median

def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]

    brack_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
    brack_points = {')': 1, ']': 2, '}': 3, '>': 4}

    print(lines)

    bad_lines = set()
    inc_scores = []
    for i in range(len(lines)):
        brack_stack = []
        bad_line = False
        for c in lines[i]:
            if c in brack_map:
                brack_stack.append(c)
            elif len(brack_stack) > 0 and c == brack_map[brack_stack[-1]]:
                brack_stack.pop()
            else:
                bad_line = True
                break

        if not bad_line:
            ext = [brack_map[c] for c in reversed(brack_stack)]
            score = 0
            for c in ext:
                score *= 5
                score += brack_points[c]
            inc_scores.append(score)

    print(median(inc_scores))

main()
