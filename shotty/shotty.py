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
@click.option('--project', default=None,
		help="Only instances for project _tag Project:<name>)")
def list_instances(project):
	"List EC2 instances"
	instances = []
	tags = {}

	if project:
		filters = [{'Name':'tag:Project', 'Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
	else:
		instances = ec2.instances.all()

	for i in instances:
		tags = { t['Key']: t['Value'] for t in i.tags or [] }
		print(', '.join((
			i.id,
			i.instance_type,
			i.placement['AvailabilityZone'],
			i.state['Name'],
			i.public_dns_name
		)))

	return
			

#======================================
#bloco de execucao
#======================================
if __name__ == '__main__':
	#print(sys.argv)
	list_instances()

