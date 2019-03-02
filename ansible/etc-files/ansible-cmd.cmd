 export AWS_ACCES_KEY_ID='xxxxx'
 export AWS_SECRET_ACCESS_KEY='asxxxsa'
 cd /etc/ansible/
 cat hosts 
 sudo pip install boto
 sudo pip2 install boto

 #Class 19- Senting up dynamic inventory
 ./ec2.py --list
 export EC2_INI_PATH=/etc/ansible/ec2.ini
 export ANSIBLE_HOSTS=/etc/ansible/ec2.py 
 #class 20 - running first ansible command
 
