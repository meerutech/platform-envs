# SSM Parameter generation

## Why

We need to generate parameters for pipelines that run in other accounts. In order to do this, we need a central location to store them for deployment.

## What does this do

This code will look at the config.ini file, and based on each environment, build and deploy ssm parameters to that account.

## Real world example

- We add the following to the config.ini:

```
[test]
account_number = 12345678910
cross_account_role_arn = arn:aws:iam::12345678910:role/cross-acount-example
region = us-east-1
example_item_1 = item1
example_item_2 = item2
```

- The automation will create everything for the "test" environment, based off of the top level name.

- Using the `account_number` and `cross_account_role_arn`, the automation will generate temporary credentials for the cdk to deploy the SSM parameters.

- Next, it will iterate through every key/value in the config under "test" and generate an SSM parameter in the account that is noted in the config.

- Here is an example of what an SSM parameter will look like:

```
parameter name: /test/example_item_1
paremeter value: item1
```

## Requirements to have this generate parameters for a new account

1) A cross account role with permissions to deploy to Cloudformation and SSM are required. (TODO: Example IAM policy will need to be added to onboard)
2) Account number, region, and the role arn from the deploy to account need to be added to the config file (example below).

```
[test]
account_number = 12345678910
cross_account_role_arn = arn:aws:iam::12345678910:role/cross-acount-example
region = us-east-1
example_item_1 = item1
example_item_2 = item2
```

3) Once changes are added to the config file and merged, (TODO) a pipeline will trigger to update/delete/add values to the accounts listed in the config.