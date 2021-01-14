import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-0a36eb8fadc976275',
    InstanceType='t2.micro',
    KeyName='bibek',
    MinCount=1,
    MaxCount=1
)    