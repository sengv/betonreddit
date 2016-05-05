# betonreddit

[![Coverage Status](https://coveralls.io/repos/github/betonreddit/betonreddit/badge.svg?branch=master)](https://coveralls.io/github/betonreddit/betonreddit?branch=master)



This is a website where users can place bets on when/how often certain things happen on Reddit. Users will win (and lose) very valuable imaginary points.


Everyone is welcomed to help on this project. Fork it, and do your thing!

I am using Python3.4. 

I recommend working in a virtual environment. 


Here is one way to start working on this:

1. Using a Terminal or Command Prompt, navigate to the directory where the project will be stored.
2. Enter in `git init`. If you don't have it, here is the download page: https://git-scm.com/download/ 
3. Go to your 'betonreddit' repository that you just forked and copy the HTTPS url. It should be something like `https://github.com/<your_username>/betonreddit.git.`
4. In your Terminal, enter in `git remote add origin https://github.com/<your_username>/betonreddit.git`
5. Enter in `git pull origin master`. 
6. To install the necessary tools, `pip install -r requirements.txt`. 
7. The SECRET_KEY is saved in a file called `secret.py` in the same directory as `settings.py`. Go to http://www.miniwebtool.com/django-secret-key-generator/ to generate your own secret key. `secret.py` should be ignored via the .gitignore file. There are better ways to hide the secret key, but this way is simple and it works.


7. Once you implemented some features and you want to add to the project, you create a Pull Request. 
