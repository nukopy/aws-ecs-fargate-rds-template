# AWS ECS Fargate, RDS Template

## Set Environment Variables / Secrets

You MUST set environment variables or GitHub repository Secrets to deploy app.

### Local Environment Variables

Environment variables below are used in the section [Deploy with AWS CLI](#deploy-with-aws-cli).

```sh
# CloudFormation
export PROFILE_NAME="profile-name-for-aws-cli"  # aws-cli の profile
export CFN_TEMPLATE="./templates/stack.yml"

# CloudFormation params
export ProjectName="test-project"
export Env="dev"
export CFN_STACK_NAME="${ProjectName}-${ENV}-cfn"
```

### GitHub repository Secrets

Secrets below are used in the section [Deploy with GitHub Actions](#deploy-with-github-actions)

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
  - AWS region to deploy to
- `DISCORD_WEBHOOK_URL`
  - to notify workflow results

## Deploy with AWS CloudFormation

In this repository, 2 ways are provided to deploy with AWS CloudFormation.

- Deploy with AWS CLI
- Deploy with GitHub Actions

### Deploy with AWS CLI

1. Create AWS account & Get AWS Access Key / Secret Access Key
2. Setup aws-cli in local environment using keys obtained in step 1
3. Set local environment variables mentioned in the section [Local Environment Variables](#local-environment-variables)
4. Create stack with CloudFormation
   1. Create registry
   2. TODO

### Deploy with GitHub Actions

1. Create AWS account & Get AWS Access Key / Secret Access Key
2. Set GitHub secrets for GitHub Actions mentioned in the section [GitHub repository Secrets](#github-repository-secrets)

## Run App in local with Docker Compose

Run sample app in local environment with Docker Compose.

Please follow the steps below:

1. Create `.env`
2. Run containers with Docker Compose

### Create `.env`

You MUST create 2 `.env` files to run containers for app.

- `app/.env`
  - file sample: [`app/.env.sample`](https://github.com/nukopy/aws-ecs-fargate-rds-template/blob/develop/app/.env.sample)

```sh
DB_USER="myuser"
DB_PASSWORD="mypass"
DB_HOST="db"  # コンテナ名
DB_NAME="mydb"  # db/mariadb/init.d/init.sql の DB の名前と合わせる
DB_URL="mariadb://${DB_USER}:${DB_PASSWORD}@${DB_HOST}/${DB_NAME}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS=""  # false を表す
SQLALCHEMY_ECHO=""  # false を表す
```

- `db/.env`
  - file sample: [`db/.env.sample`](https://github.com/nukopy/aws-ecs-fargate-rds-template/blob/develop/db/.env.sample)

```sh
MYSQL_DATABASE="mydb"
MYSQL_USER="myuser"
MYSQL_PASSWORD="mypass"
MYSQL_ROOT_PASSWORD="password"
```

### Run containers with Docker Compose

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
