echo "What's the name of the project"
read PROJECT
mkdir $PROJECT
sudo chmod 770 $PROJECT
sudo groupadd $PROJECT
sudo chown -Rf $USER:$PROJECT $PROJECT
