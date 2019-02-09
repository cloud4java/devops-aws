from troposphere import Ref, Template, Parameter, Join, GetAtt
import troposphere.ec2 as ec2

t = template()
#Securi group
sg = ec2.SecurityGroup("LampSg")
sg.GroupDescription = "Allou access thought ports 88 and 22"
sg.securityGroupIngress = [
	ec2.SecurityGroupRule(IpProtocol = "tcp", fromPort = "22", toPort = "22", CidrIp = "0.0.0.0/0")
	,ec2.SecurityGroupRule(IpProtocol = "tcp", fromPort = "88", toPort = "70", CidrIp = "0.0.0.0/0")

]
t.add_resource(sg);
print(t.to_json)
#AmiID