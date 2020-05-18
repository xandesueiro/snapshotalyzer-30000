# snapshotalyzer-30000

Demo project to manage AWS EC2 instance snapshots

## Abount

This project is a demo, and uses boto3 to manage AWS EC2 instances snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli, e.g.

'aws configure --profile shotty'

## Running

'pipenv run python "shotty/shotty.py <command> <--project=PROJECT>"'

*command* is list, stop or start
*project* is optional. It's a tag in EC2 instance  (e.g. --project=Valkyrie)

pipenv run python shotty/shotty.py list --project=Valkyrie
pipenv run python shotty/shotty.py stop --project=Valkyrie
pipenv run python shotty/shotty.py start --project=Valkyrie
pipenv run python shotty/shotty.py --help
pipenv run python shotty/shotty.py list --help
pipenv run python shotty/shotty.py stop --help
pipenv run python shotty/shotty.py start --help



