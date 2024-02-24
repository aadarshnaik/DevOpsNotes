#! /bin/bash

URL='https://www.tooplate.com/zip-templates/2126_antique_cafe.zip'
ART_NAME='2126_antique_cafe'
TEMPDIR="/tmp/webfiles"

yum --help &> /dev/null

if [ $? -eq 0 ]
then
	PACKAGE="httpd wget unzip"
	SVC="httpd"
	echo "Running centOS setup"
	sudo yum install $PACKAGE -y
	sudo systemctl start $SVC
	sudo systemctl enable $SVC
	mkdir -p $TEMPDIR
	cd $TEMPDIR
	echo
	
	wget $URL
	unzip $ART_NAME.zip 
	sudo cp -r $ART_NAME/* /var/www/html/
	systemctl restart $SVC
	rm -rf $TEMPDIR
	sudo systemctl status $SVC
	ls /var/www/html/
else
	PACKAGE="apache2 wget unzip"
	SVC="apache2"
	echo "Running Ubunty setup"
	sudo apt install $PACKAGE -y
	sudo systemctl start $SVC
	sudo systemctl enable $SVC
	mkdir -p $TEMPDIR
	cd $TEMPDIR
	echo
	wget $URL
	unzip $ART_NAME.zip 
	sudo cp -r $ART_NAME/* /var/www/html/
	systemctl restart $SVC
	rm -rf $TEMPDIR
	sudo systemctl status $SVC
	ls /var/www/html/
fi