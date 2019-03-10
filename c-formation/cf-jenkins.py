from troposphere import Ref, Template, Parameter, Output, Join, GetAtt, Base64, FindInMap
import troposphere.ec2 as ec2

t = Template() #Securi group sg = ec2.SecurityGroup("LampSg")
sg = ec2.SecurityGroup("LampSg")
sg.GroupDescription = "Allow access through ports 80 and 22"
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

t.add_mapping('RegionMap', {
    "us-east-1":      {"AMI": "ami-09bfcadb25ee95bec"},
    "us-west-1":      {"AMI": "ami-09bfcadb25ee95bec"},
    "us-west-2":      {"AMI": "ami-16fd7026"},
    "eu-west-1":      {"AMI": "ami-24506250"},
    "sa-east-1":      {"AMI": "ami-3e3be423"},
    "ap-southeast-1": {"AMI": "ami-74dda626"},
    "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
})

instance =  ec2.Instance(
	"Ec2Instance",
	ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
	InstanceType="t2.micro",
	KeyName=Ref(keypair),
	SecurityGroups=[Ref(sg)],
	UserData=Base64("80")
	)

t.add_resource(instance)

print(t.to_json())