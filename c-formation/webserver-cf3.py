from troposphere import Ref, Template, Parameter, Join, GetAtt
import troposphere.ec2 as ec2

t = Template() #Securi group sg = ec2.SecurityGroup("LampSg")
sg = ec2.SecurityGroup("LampSg")
sg.GroupDescription = "Allow access thought ports 88 and 22"
sg.SecurityGroupIngress = [ec2.SecurityGroupRule(IpProtocol = "tcp", FromPort=88, ToPort="70", CidrIp="0.0.0.0/0"),ec2.SecurityGroupRule(IpProtocol="tcp", FromPort="22", ToPort="22", CidrIp="0.0.0.0/0")]
t.add_resource(sg)
print(t.to_json())
#AmiID
