from troposphere import Ref, Template, Parameter, Output, Join, GetAtt, Base64
import troposphere.ec2 as ec2

t = Template() #Securi group sg = ec2.SecurityGroup("LampSg")
sg = ec2.SecurityGroup("LampSg")
sg.GroupDescription = "Allow access throught ports 80 and 22"
sg.SecurityGroupIngress = [
ec2.SecurityGroupRule(IpProtocol = "tcp", FromPort="80", ToPort="80", CidrIp="0.0.0.0/0"),
ec2.SecurityGroupRule(IpProtocol = "tcp", FromPort="22", ToPort="22", CidrIp="0.0.0.0/0")
]
t.add_resource(sg)

keypair = t.add_parameter(Parameter(
"KeyName",
Description = "Name of the ssh keky pair that will be used to access the instance",
Type = "String"
	))

instance = ec2.Instance("Webserver")
instance.ImageId = "ami-0cc848dfaa82172af"
instance.InstanceType = "t2.micro"
instance.SecurityGroups = [Ref(sg)]
instance.KeyName = Ref(keypair)
ud = Base64(Join('\n',
	[
		"#!/bin/bash",
		"sudo yum -y update",
		"sudo yum install httpd",
		"sudo echo  '<html><body><h1>Welcome to devos on AWS</h1></body></html>' > /var/www/html/test.html",
		"sudo service httpd start",
		"sudo chkconfig httpd on"
	]))

#instance.UserData = ud
t.add_resource(instance)

t.add_output(Output(
	"InstanceAccess",
	Description = "Command to use to access the instance using SSH",
	Value = Join("", ["ssh -i ~/.ssh/lamp2Key.pem ec2-user@", GetAtt(instance, "PublicDnsName")])
	))

t.add_output(Output(
	"WebUrl",
	Description = "The url of the server",
	Value = Join("",["http://",GetAtt(instance, "PublicDnsName")]) )
)


print(t.to_json())
#AmiID=ami-0cc848dfaa82172af
#AmiID
