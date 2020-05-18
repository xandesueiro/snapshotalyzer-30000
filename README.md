# snapshotalyzer-30000

Demo project to manage AWS EC2 instance snapshots

## Abount

This project is a demo, and uses boto3 to manage AWS EC2 instances snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli, e.g.

'aws configure --profile shotty'

## Running

'pipenv run python "shotty/shotty.py <command> <subcommand> <--project=PROJECT>"'

*command* is instances, volumes and snapshots 
*subcommand* depends on command
*project* is optional. It's a tag in EC2 instance  (e.g. --project=Valkyrie)

*help* commands
pipenv run python shotty/shotty.py instances --help
pipenv run python shotty/shotty.py instances list --help
pipenv run python shotty/shotty.py instances stop --help
pipenv run python shotty/shotty.py instances start --help

pipenv run python shotty/shotty.py volumes --help
pipenv run python shotty/shotty.py volumes list --help

pipenv run python shotty/shotty.py snapshots list --help


*all* instances
pipenv run python shotty/shotty.py instances list
pipenv run python shotty/shotty.py instances stop
pipenv run python shotty/shotty.py instances start

pipenv run python shotty/shotty.py volumes list

pipenv run python shotty/shotty.py snapshots list



*filter* instances, volumes and snapshots by project
pipenv run python shotty/shotty.py instances list --project=Valkyrie
pipenv run python shotty/shotty.py instances stop --project=Valkyrie
pipenv run python shotty/shotty.py instances start --project=Valkyrie

pipenv run python shotty/shotty.py volumes list --project=Valkyrie

pipenv run python shotty/shotty.py snapshots list --project=Valkyrie

pipenv run python shotty/shotty.py instances snapshot-vol --project=Valkyrie







