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