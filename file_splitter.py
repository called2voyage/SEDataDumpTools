import os

with open('Posts.xml', 'r', encoding='utf-8') as f:
    count = 0
    chunk = 1
    if not os.path.exists('chunk%d' % (chunk,)):
        os.makedirs('chunk%d' % (chunk,))
    output = open('chunk%d\\Posts.xml' % (chunk,), 'w', encoding='utf-8')
    output.write('<?xml version="1.0" encoding="utf-8"?>\n')
    output.write('<posts>\n')
    for line in f:
        if '<?xml version="1.0" encoding="utf-8"?>' not in line and '<posts>' not in line and '</posts>' not in line:
            count = count + 1
            if count == 365000:
                count = 1
                chunk = chunk + 1
                output.write('</posts>\n')
                output.close()
                if not os.path.exists('chunk%d' % (chunk,)):
                    os.makedirs('chunk%d' % (chunk,))
                output = open('chunk%d\\Posts.xml' % (chunk,), 'w', encoding='utf-8')
                output.write('<?xml version="1.0" encoding="utf-8"?>\n')
                output.write('<posts>\n')
            output.write(line)
    output.write('</posts>\n')
    output.close()