import os
import re

def main(filepath):
    pattern = re.compile("##.*")
    out = []
    with open(filepath,"r",encoding="utf-8")as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                out.append(match.group(0))
    print(out)

if __name__ == "__main__":
    filepath = os.path.join(os.path.dirname(__file__), "README.md")
    main(filepath)