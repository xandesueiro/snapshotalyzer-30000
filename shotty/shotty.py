#======================================
#import libraries
#======================================
import boto3
import botocore
import click
#import sys

#======================================
#visao para todo s cript
#======================================
session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

#======================================
#define functions
#======================================
def filter_instances(project):
	instances = []
	tags = {}

	if project:
		filters = [{'Name':'tag:Project', 'Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
	else:
		instances = ec2.instances.all()

	return instances

#Group by commands: cli
@click.group()
def cli():
	"""cli - Command Line Interface: Shotty manages snapshots"""

#=====================
#SNAPSHOTS  commands
#=====================
@cli.group('snapshots')
def snapshot():
	"""Commands for snapshots"""

@snapshot.command('list')
@click.option('--project', default=None,
		help="Only snapshots for project _tag Project:<name>)")
def list_snapshots(project):
	"List EC2 snapshots"

	instances = filter_instances(project)

	for i in instances:
		for v in i.volumes.all():
			for s in v.snapshots.all():
				print(', '.join((
					s.id,
					v.id,
					i.id,
					s.state,
					s.progress,
					s.start_time.strftime("%c")
				)))

	return


#=====================
#END SNAPSHOTS commands
#=====================


#=====================
#Group VOLUMES commands
#=====================
@cli.group('volumes')
def volumes():
	"""Commands for volumes"""

@volumes.command('list')
@click.option('--project', default=None,
		help="Only volumes for project _tag Project:<name>)")
def list_volumes(project):
	"List EC2 volumes"

	instances = filter_instances(project)

	for i in instances:
		for v in i.volumes.all():
			print(', '.join((
				v.id,
				i.id,
				v.state,
				str(v.size) + "GiB",
				v.encrypted and "Encrypted" or "Not Encrypted"
			)))

	return


#=====================
#END Group VOLUMES commands
#=====================

#=====================
#Group INSTANCES commands
#=====================
@cli.group('instances')
def instances():
	"""Commands for instances"""

@instances.command('snapshot-vol',
	help="Create snapshots of all volumes")
@click.option('--project', default=None,
		help="Only instances for project _tag Project:<name>)")
def create_snapshots(project):
	"Create snapshots for EC2 instances"

	print("Start creating snapshots...")

	instances = filter_instances(project)

	for i in instances:
		print("Stopping {0}...".format(i.id))
		
		i.stop()
		i.wait_until_stopped()
		
		for v in i.volumes.all():
			print("    Creating snapshot of {0}".format(v.id))
			v.create_snapshot(Description="Created by SnapshotAlyzer 30000")

		print("Starting {0}...".format(i.id))

		i.start()
		i.wait_until_running()

	print("Job is done!")

	return

@instances.command('list')
@click.option('--project', default=None,
		help="Only instances for project _tag Project:<name>)")
def list_instances(project):
	"List EC2 instances"

	instances = filter_instances(project)

	for i in instances:
		tags = { t['Key']: t['Value'] for t in i.tags or [] }
		print(', '.join((
			i.id,
			i.instance_type,
			i.placement['AvailabilityZone'],
			i.state['Name'],
			i.public_dns_name,
			tags.get('Project', '<no project>')
		)))

	return
			
@instances.command('stop')
@click.option('--project', default=None,
	help='Only instances for project')
def stop_instances(project):
	"Stop EC2 instances"
	
	instances = filter_instances(project)

	for i in instances:

		print("Stopping {0}...".format(i.id))
		try:
			i.stop()
		except botocore.exceptions.ClientError as e:
			print("Could not stop {0}. ".format(i.id) + str(e))
			continue

	return

@instances.command('start')
@click.option('--project', default=None,
	help='Only instances for project')
def start_instances(project):
	"Start EC2 instances"
	
	instances = filter_instances(project)

	for i in instances:
		print("Starting {0}...".format(i.id))

		try:
			i.start()
		except botocore.exceptions.ClientError as e:
			print("Could not start {0}. ".format(i.id) + str(e))
			continue

	return
#=====================
#END Group INSTANCES commands
#=====================

#======================================
#bloco de execucao
#======================================
if __name__ == '__main__':
	#print(sys.argv)
	cli()

