import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')

volume = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Size=4,
    VolumeType='gp3',
    Iops=3000
)



 

