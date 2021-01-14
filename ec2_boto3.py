import boto3
ec2 = boto3.resource('ec2')

security_group = ec2.create_security_group(
    Description='http',
    GroupName='gigi'
)
security_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=80,
    ToPort=80
)

key_pair = ec2.create_key_pair( KeyName='kobe')


instance = ec2.create_instances(
    ImageId='ami-0a36eb8fadc976275',
    InstanceType='t2.micro',
    KeyName='kobe',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=['gigi']
)

