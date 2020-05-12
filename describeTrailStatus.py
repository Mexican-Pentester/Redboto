#!/usr/bin/env python3
# TODO: Better API Key Support?
# API keys currently are loaded from a profile
# TODO: Better error handling
import boto3

#This loads the aws profile called 'default'
session = boto3.session.Session(profile_name='default', region_name='us-east-2b')
#We are just connecting to a random region in order to fetch a list of regions
ec2 = session.client('ec2', 'us-east-2')
#Get the regions
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

#Iterate through each region and check for the prescense of trails
#Probably need to do better error checking
for region in regions:
    cloudtrail = boto3.client('cloudtrail', region)
    if not cloudtrail.describe_trails()['trailList']:
        print("[*] Region " + region + " doesn't appear to have Cloudtrails or you don't have permission")
    else:
        print("[-] Region" + region + " appears to have Cloudtrails")
