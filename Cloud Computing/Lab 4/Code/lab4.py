import boto3
import botocore
import os

def create_key_pair():
	ec2_client = boto3.client("ec2", region_name="us-east-1")
	key_pair = ec2_client.create_key_pair(KeyName="ec2-key-pair2")
	private_key = key_pair["KeyMaterial"]
	with os.fdopen(os.open("aws_lab4.pem", os.O_WRONLY |
	os.O_CREAT, 0o400), "w+") as handle:
		handle.write(private_key)

create_key_pair()

def create_instance():
	ec2_client = boto3.client("ec2", region_name="us-east-1")
	instances = ec2_client.run_instances(
		ImageId="ami-08895422b5f3aa64a",
		MinCount=1,
		MaxCount=1,
		InstanceType="t2.micro",
		KeyName="ec2-key-pair2"
	)

	print(instances["Instances"][0]["InstanceId"])
	
create_instance()

def get_running_instances():
	ec2_client = boto3.client("ec2", region_name="us-east-1")
	reservations = ec2_client.describe_instances(Filters=[
		{
			"Name": "instance-state-name",
			"Values": ["running"],
		},
		{
			"Name": "instance-type",
			"Values": ["t2.micro"]
		}]).get("Reservations")
	
	for reservation in reservations:
		for instance in reservation["Instances"]:
			instance_id = instance["InstanceId"]
			instance_type = instance["InstanceType"]
			public_ip = instance["PublicIpAddress"]
			private_ip = instance["PrivateIpAddress"]
			print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")
	
get_running_instances()

def stop_instance(instance_id):
	ec2_client = boto3.client("ec2", region_name="us-east-1")
	response = ec2_client.stop_instances(InstanceIds=[instance_id])
	print(response)
	
stop_instance("i-009bcccd7094269e8")

def terminate_instance(instance_id):
	ec2_client = boto3.client("ec2", region_name="us-east-1")
	response = ec2_client.terminate_instances(InstanceIds=[instance_id])
	print(response)

terminate_instance("i-009bcccd7094269e8")

def create_bucket(bucket_name, region):
	s3_client = boto3.client("s3", region_name=region)

	try:
		response = s3_client.create_bucket(Bucket=bucket_name)
		print(response)
	except botocore.exceptions.ClientError:
		print("Wrong name!")
	except s3_client.exceptions.BucketAlreadyExists:
		print("Such bucket already exists!")

create_bucket("bucket02my", "us-east-1")

def printing_buckets():
	s3_client = boto3.client("s3")
	response = s3_client.list_buckets()

	print("Existing buckets:")
	for bucket in response["Buckets"]:
		print(f" {bucket['Name']}")

printing_buckets()

def upload(file_name, bucket_name, s3_obj_name):
	s3_client = boto3.client("s3")
	responce = s3_client.upload_file(Filename=file_name, Bucket=bucket_name, Key=s3_obj_name)
	print(responce)

upload("request.csv", "bucket02my", "data.csv")

def destroy_bucket(bucket_name):
	s3_client = boto3.client("s3")
	
	# First of all delete an existing file
	s3_client.delete_object(Bucket = bucket_name, Key = "data.csv")

	response = s3_client.delete_bucket(Bucket=bucket_name)
	print(response)

destroy_bucket("bucket02my")

import pandas

def printing_data_from_s3(file_name, bucket_name):
	s3_client = boto3.client("s3")

	try:
		obj = s3_client.get_object(Bucket = bucket_name, Key = file_name)
		data = pandas.read_csv(obj["Body"])
		print("Printing the data frame...")
		print(data.head())
	except s3_client.exceptions.NoSuchBucket:
		print("Проблемка. з. іменем. бакету")
	except s3_client.exceptions.NoSuchKey:
  		print("Проблемка. з. іменем. файлу")

printing_data_from_s3("data.csv", "bucket02my")

























