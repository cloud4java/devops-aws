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
