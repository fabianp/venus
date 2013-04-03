import sys

data = sys.stdin.read()

# remove clear: both from html
data = data.replace('clear: both', '')
sys.stdout.write(data)
