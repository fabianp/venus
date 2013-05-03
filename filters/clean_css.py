import sys

data = sys.stdin.read()

# remove "clear: both" from html
# f = open('tmp.txt', 'r+w')
# f.write(f.read() + data)
# f.close()
if data.find('clear: both;'):
    data = data.replace('clear: both;', '')
sys.stdout.write(data)

