# active python
echo "started"
cd /home/yoon/blog/1yoouoo.github.io
/usr/bin/python3 main.py

git pull
git config --local user.name "blanc"
git config --local user.email "1yoouoo@gmail.com" 
git add -A
git commit -m "publish blog"
git push origin HEAD
