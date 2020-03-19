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

import sys
import re
from shutil import move
from xml.dom.minidom import parse

posts = parse('Posts.xml')
user_posts = [f for f in posts.getElementsByTagName('row') if f.getAttribute('OwnerUserId') == sys.argv[1]]
parent_questions = [f for f in posts.getElementsByTagName('row') if f.getAttribute('Id') in [f.getAttribute('ParentId') for f in user_posts]]
linked_answers = [f for f in posts.getElementsByTagName('row') if f.getAttribute('ParentId') in [f.getAttribute('Id') for f in user_posts]]

for child in posts.getElementsByTagName('row'):
    if child not in user_posts and child not in parent_questions and child not in linked_answers:
        _ = posts.getElementsByTagName('posts')[0].removeChild(child)

file = open('user_Posts.xml', 'w', encoding='utf-8')
posts.writexml(file)
file.close()

file = open('user_Posts.xml', 'r', encoding='utf-8')
new_file = open('pretty_user_Posts.xml', 'w', encoding='utf-8')

empty = re.compile(r'^\s*$')

for line in file.readlines():
    if empty.match(line):
        continue
    else:
        new_file.write(line)

file.close()
new_file.close()

move('pretty_user_Posts.xml', 'user_Posts.xml')
