# SEDataDumpTools
Python scripts for processing XML data from Stack Exchange data dumps


user_content.py accepts a site-specific Stack Exchange user ID as an argument and reads in Posts.xml, then creates user_Posts.xml
containing only the posts created by the specified user ID and any associated posts (parent questions,
answers to the user questions).
