from troposphere import Ref, Template, Parameter, Output, Join, GetAtt, Base64, FindInMap
from troposphere.iam import InstanceProfile, PolicyType as IAMPolicy, Role
from awacs.aws import Action, Allow, Policy, Principal, Statement 
from awacs.sts import  AssumeRole
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
	"LampStage",
	ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
	InstanceType="t2.micro",
	KeyName=Ref(keypair),
	SecurityGroups=[Ref(sg)],
	UserData=Base64("80")
	)
principal = Principal("Service", ["ec2.amazonaws.com"])
statement = Statement(Effect=Allow,Action=[AssumeRole],Principal=principal)
#statement = Statement(Effect=Allow,Action=[AssumeRole],Principal=principal)
policy = Policy(Statement=[statement])
role = Role("Role", AssumeRolePolicyDocument=policy)
t.add_resource(role)

t.add_resource(InstanceProfile("InstanceProfile",Path="/",Roles=[Ref("Role")]))

t.add_resource(IAMPolicy("Policy",PolicyName="AllowS3",PolicyDocument=Policy(Statement=[Statement(Effect=Allow, Action=[Action("s3","*")],Resource=["*"])]),Roles=[Ref("Role")]))
#t.add_resource(IAMPolicy("Policy",PolicyName="AllowS3",PolicyDocument=Policy(Statement=[Statement(Effect=Allow, Action=[Action("s3","*")],Resource=["*"])]),Roles=[Ref("Role")]))
instance.IamInstanceProfile = Ref("InstanceProfile")

t.add_resource(instance)

print(t.to_json())