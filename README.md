# AWS ECS Fargate, RDS Template

## Set Environment Variables

You MUST set environment variables for deploying.

### Local Environment Variables

These are used in the sections [Execute deploy commands with aws-cli](#execute-deploy-commands-with-aws-cli)

```sh
# CloudFormation
export PROFILE_NAME="test-metheus-cfn"  # aws-cli の profile
export CFN_STACK_NAME="metheus-dev-cfn"
export CFN_TEMPLATE="./templates/stack.yml"

# CloudFormation params
export ProjectName="metheus"
export ENV="dev"
```

### GitHub repository Secrets

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
  - AWS region to deploy to
- `DISCORD_WEBHOOK_URL`
  - to notify workflow results

## Deploy with AWS CloudFormation

In this repository, 2 ways are provided to deploy with AWS CloudFormation.

- Execute deploy commands with aws-cli
- Deploy via GitHub Actions

### Execute deploy commands with aws-cli

1. Create AWS account & Get AWS Access Key / Secret Access Key
2. Setup aws-cli in local environment using keys obtained in step 1
3. Set local environment variables mentioned in the section [Local Environment Variables](#local-environment-variables)
4. Create stack with CloudFormation
   1. Create registry
   2. TODO

### Deploy via GitHub Actions

1. Create AWS account & Get AWS Access Key / Secret Access Key
2. Set GitHub secrets for GitHub Actions mentioned in the section [GitHub repository Secrets](#github-repository-secrets)

## Execute App in local with Docker Compose

Run sample app in local with Docker Compose.

### Create `.env`

You MUST create 2 `.env` files to run containers for app.

- `./app/.env`
  - the file format is in `./app/.env.sample`)

```sh
DB_USER="myuser"
DB_PASSWORD="mypass"
DB_HOST="db"  # コンテナ名
DB_NAME="mydb"  # db/mariadb/init.d/init.sql の DB の名前と合わせる
DB_URL="mariadb://${DB_USER}:${DB_PASSWORD}@${DB_HOST}/${DB_NAME}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS=""  # false を表す
SQLALCHEMY_ECHO=""  # false を表す
```

- `./db/.env`
  - the file format is in `./db/.env.sample`)

```sh
MYSQL_DATABASE="mydb"
MYSQL_USER="myuser"
MYSQL_PASSWORD="mypass"
MYSQL_ROOT_PASSWORD="password"
```

### Run containers

- Run containers
  - access to http://localhost:8000/healthcheck in your browser for checking whether API server is running

```sh
make up
```

- operation in the Python/FastAPI container

```sh
make app
```

- check the MariaDB container

```sh
make db
```

Execute SQL query below in DB container:

```sh
# in DB container
show tables;
# +----------------+
# | Tables_in_mydb |
# +----------------+
# | test_table     |
# +----------------+
select * from test_table;
# output records in table 'test_table' below
# ...
```
