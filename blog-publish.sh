# set git
git config --global core.sharedRepository group
git config --global --add safe.directory /home/yoon/blog/1yoouoo.github.io

# set Auth
chmod -R g+rwX /home/yoon/blog/1yoouoo.github.io

# PATH
export PYTHONPATH=${PYTHONPATH}:/home/yoon/.local/lib/python3.10/site-packages

# active python
/usr/bin/python3 /home/yoon/blog/1yoouoo.github.io/main.py >> /var/log/syslog 2>&1

# git push after python file
if test $? -eq 0; then
    cd /home/yoon/blog/1yoouoo.github.io && \
    git config --local user.name "blanc" && \
    git config --local user.email "1yoouoo@gmail.com" && \
    git add . && \
    git commit -m "publish blog" && \
    git push origin HEAD >> /var/log/syslog 2>&1
fi
