aws ec2 create-security-group --group-name lamp --description "Secutiry group for lamp env"
aws ec2 delete-security-group --group-name lamp
aws ec2 authorize-security-group-ingress --group-name lamp2 --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name lamp2 --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 describe-security-groups --group-name lamp2 --output table | more 
aws ec2 create-key-pair --key-name lamp2Key --output text 
chmod 600 /home/dorival/.ssh/lamp2Key.pem
aws ec2 run-instances --image-id --instance-type t2-micro --key-name lamp2Key --security-group-ids sg-0a58c5622bcaa02cb

aws ec2 run-instances --image-id ami-02da3a138888ced85 --count 1 --instance-type t2.micro --key-name lamp2Key 

#created:aws ec2 run-instances --image-id ami-09bfcadb25ee95bec --count 1 --instance-type t2.micro --key-name lamp2Key 
#i-0d61ec6448901b336


aws ec2 describe-instance-status --instance-id i-123
echo "Sessao 3 class 10 "
aws ec2 run-instances --image-id ami-0799ad445b5727125 --instance-type t2.micro --key-name lamp2Key --security-group-ids sg-0a58c5622bcaa02cb
aws ec2 describe-instance-status --instance-id i-0551450c19accdd6a --output text
aws ec2 describe-instances  --instance-id i-0551450c19accdd6a --query "Reservations[].Instances[].PublicDnsName"


aws ec2 describe-instances --instance-id i-0551450c19accdd6a --output table
chmod 400 /home/dorival/.ssh/lamp2Key.pem
ssh -i /home/dorival/.ssh/lamp2Key.pem ec2-user@ec2-54-183-148-69.us-west-1.compute.amazonaws.com
aws ec2 describe-instances --instance-ids i-0551450c19accdd6a --output text
aws ec2 terminate-instances --instance-ids i-0551450c19accdd6a

#Begin create stack
aws cloudformation create-stack --stack-name lamp-stack --template-body file://cf1.json --parameters file://params.json

[
{"ParameterKey": "KeyName",
"ParameterValue":"lamp2Key"
},
{"ParameterKey": "t2.micro",
"ParameterValue":"instances"
}
]
#End create stack

############ Ansible commands #####################
ansible --private-key=~/.ssh/lamp2Key.pem --user=ec2-user -m ping all

#Add ssh configuration 
sublime-text.subl ~/.ssh/config

#Same ping command - no need to type key path
ansible -m ping all

ansible all -a "df -h"

ansible all -a "bash --version"

#cd lamp/
ansible-playbook lamp.yml 


