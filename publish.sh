# active python
echo $(pwd)
echo "1"
cd /home/yoon/blog/1yoouoo.github.io
echo $(pwd)
#/usr/bin/python3 main.py
echo "2"

# git push after python file
#if test $? -eq 0; then
echo "3"
git pull
echo "4"
git config --local user.name "blanc"
git config --local user.email "1yoouoo@gmail.com" 
git add -A
git commit -m "publish blog"
echo "5"
git push origin HEAD
echo "6"
#fi
 #>> /var/log/syslog 2>&1
