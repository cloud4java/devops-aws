aws ec2 create-security-group --group-name lamp --description "Secutiry group for lamp env"  >> aws-commands.cmd
aws ec2 delete-security-group --group-name lamp
aws ec2 authorize-security-group-ingress --group-name lamp2 --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name lamp2 --protocol tcp --port 80 --cidr 0.0.0.0/0
aws ec2 describe-security-groups --group-name lamp2 --output table | more 
aws ec2 create-key-pair --key-name lamp2Key --output text 
chmod 600 /home/dorival/.ssh/lamp2Key.pem
aws ec2 run-instances --image-id --instance-type t2-micro --key-name lamp2Key --security-group-ids sg-0a58c5622bcaa02cb
aws ec2 describe-instance-status --instance-id i-123
Sessao 3 aula 10
aws ec2 run-instances --image-id ami-0799ad445b5727125 --instance-type t2.micro --key-name lamp2Key --security-group-ids sg-0a58c5622bcaa02cb
aws ec2 describe-instance-status --instance-id i-0551450c19accdd6a --output text
aws ec2 describe-instances  --instance-id i-0551450c19accdd6a --query "Reservations[].Instances[].PublicDnsName"


aws ec2 describe-instances --instance-id i-0551450c19accdd6a --output table
ssh -i /home/dorival/.ssh/lamp2Key.pem ec2-user@ec2-54-183-148-69.us-west-1.compute.amazonaws.com
chmod 400 /home/dorival/.ssh/lamp2Key.pem
aws ec2 describe-instances --instance-ids i-0551450c19accdd6a --output text
aws ec2 terminate-instances --instance-ids i-0551450c19accdd6a
