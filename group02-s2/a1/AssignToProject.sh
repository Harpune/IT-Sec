echo "username:"
read $NAME
echo "Projectname:"
read $PROJECT
sudo usermod -g $PROJECT $NAME
