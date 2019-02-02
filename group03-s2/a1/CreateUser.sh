echo "Name of the user you want to create:"
read NAME
sudo adduser $NAME --no-create-home
