# In this project, you need to install instaloader library. 
# "pip install instaloader"

import instaloader
# Here A is the variable and Instaloader is a Library.
A = instaloader.Instaloader()
dp = input("Enter any Instagram Username = ")
# Using Instaloader library download profile picture.
A.download_profile(dp, profile_pic_only = True)