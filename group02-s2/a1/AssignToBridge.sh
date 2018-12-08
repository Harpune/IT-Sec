echo "username"
read NAME
echo "Which Project does he also need to be assigned to:"
read PROJECT
sudo usermod -G $PROJECT $NAME
