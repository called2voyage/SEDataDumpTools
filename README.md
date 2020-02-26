# SEDataDumpTools
Python scripts for processing XML data from Stack Exchange data dumps


**user_content.py** accepts a site-specific Stack Exchange user ID as an argument and reads in *Posts.xml*, then creates *user_Posts.xml* containing only the posts created by the specified user ID and any associated posts (parent questions,
answers to the user questions).

**file_splitter.py** reads in *Posts.xml* and splits it out into chunks (each chunk saved as *Posts.xml* in a numbered chunk folder). This is useful for breaking down large *Posts.xml* files, like Stack Overflow's, so that they can be processed by user_content.py.
