import os
import boto3

def create_key_pair():
	ec2_client = boto3.client("ec2", region_name="us-east-1")
	
	key_pair = ec2_client.create_key_pair(KeyName="pair5")
	private_key = key_pair["KeyMaterial"]
	with os.fdopen(os.open("pair5.pem", os.O_WRONLY |
	os.O_CREAT, 0o400), "w+") as handle:
		handle.write(private_key)

# create_key_pair()

# function to get public ip automatically
def get_public_ip(instance_id):
	ec2_client = boto3.client("ec2", region_name="us-east-1")

	reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

	for reservation in reservations:
		for instance in reservation["Instances"]:
			return instance.get("PublicIpAddress")

def create_instance():
	ec2_client = boto3.client("ec2", region_name="us-east-1")
	instances = ec2_client.run_instances(
		ImageId="ami-0c4f7023847b90238",
		MinCount=1,
		MaxCount=1,
		InstanceType="t2.micro",
		KeyName = "pair5",
		# very important to notice a Security Group Id!
		SecurityGroupIds=[
        	'sg-0aac868bd8c68435c',
    	],
	)

	# get instance_id
	instance_id = instances["Instances"][0]["InstanceId"]

	# a command to copy commands.sh file to a new instance
	copy = "pscp -i pair5.ppk commands.sh ubuntu@" + get_public_ip(instance_id) + ":/home/ubuntu/"
	os.system(copy)

	# connect to a new instance using public_ip
	connect = "ssh -t -i pair5.pem ubuntu@" + get_public_ip(instance_id) + " 'bash commands.sh; bash'"

	# run bash commands
	os.system(connect)

create_instance()