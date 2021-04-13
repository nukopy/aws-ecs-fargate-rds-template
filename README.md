# aws-alb-vpc-ecs-fargate-rds

## Environment Variables

- `.env`

```sh

```

## Deploy with AWS CloudFormation

1. Create AWS account
2. Setup aws-cli in local environment
3. Create stack with CloudFormation
   1. Create registry
   2. TODO

## Execute App in local

- start up containers
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
