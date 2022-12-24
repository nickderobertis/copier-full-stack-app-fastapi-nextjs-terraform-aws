# Copier Full Stack App Fastapi Nextjs Terraform Aws

A Copier template to create a full-stack app with a FastAPI backend, NextJS frontend, and deployed on AWS with Terraform

See the [example generated repo here](https://github.com/nickderobertis/copier-full-stack-app-fastapi-nextjs-terraform-aws-example).

## First-Time Setup

After creating the application from the template, you will need to complete the following
steps to get everything deployed correctly:

1. Create a Vercel account if you don't have one already and generate an API key
2. Create a Google Cloud account if you don't have one already and generate a client id,
   client secret, and JWT secret
3. Create a Google account for the e2e user
4. Create a Google account for the system email user
5. Create an AWS root account and an IAM user for the application
6. Fill out `.env` and `infra/.env`

## Development Status

This project uses [semantic-release](https://github.com/semantic-release/semantic-release) for versioning.
Any time the major version changes, there may be breaking changes. If it is working well for you, consider
pegging to the current major version, e.g. `copier-full-stack-app-fastapi-nextjs-terraform-aws@v1`, to avoid breaking changes. Alternatively,
you can always point to the most recent stable release with the `copier-full-stack-app-fastapi-nextjs-terraform-aws@latest`.

## Developing

Clone the repo and then run `npm install` to set up the pre-commit hooks.

## Author

Created by Nick DeRobertis. MIT License.
