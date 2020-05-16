#======================================
#import libraries
#======================================
import boto3
import click
#import sys

#======================================
#visao para todo s cript
#======================================
session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

#======================================
#define funcoes
#======================================
@click.command()
def list_instances():
	"List EC2 instances"
	for i in ec2.instances.all():
	    print(', '.join((
	    	i.id,
	    	i.instance_type,
	    	i.placement['AvailabilityZone'],
	    	i.state['Name'],
	    	i.public_dns_name)))

	return
	    	

#======================================
#bloco de execucao
#======================================
if __name__ == '__main__':
	#print(sys.argv)
	list_instances()

