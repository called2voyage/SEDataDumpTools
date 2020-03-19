# Copyright 2020 called2voyage
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
