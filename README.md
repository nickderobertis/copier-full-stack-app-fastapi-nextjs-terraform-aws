# Copier Full Stack App Fastapi Nextjs Terraform Aws

A Copier template to create a full-stack app with a FastAPI backend, NextJS frontend, and deployed on AWS with Terraform

See the [example generated repo here](https://github.com/nickderobertis/copier-full-stack-app-fastapi-nextjs-terraform-aws-example).

## First-Time Setup

After creating the application from the template, you will need to complete the following
steps to get everything deployed correctly:

1. Create a Vercel account if you don't have one already and generate an API key
2. Create a [Google Cloud account](https://console.developers.google.com/) if you don't have one already and generate a client id,
   client secret, and JWT secret
   - Create a project for the application, if one does not exist
   - Go to Credentials -> Create Credentials -> OAuth Client ID
   - Select Web Application
   - Add `http://localhost:3000`, `https://<insert main domain>`, and
     `https://staging.<insert main domain>` as authorized JavaScript origins
   - Add the same domains but with `/auth/google` as authorized redirect URIs,
     e.g. `https://staging.<insert main domain>/auth/google`
   - Go to "OAuth consent screen" in the navigation menu
   - Select "External" and add the main domain as an authorized domain. Fill
     out the rest of the form as desired
   - On the Scopes page, add any additional scopes you would like to gain access to during the OAuth flow. If you only want Google login, you can skip this step.
3. Create a Google account for the e2e user
4. Create a Google account for the system email user and enable
   "less secure access"
5. Create an AWS root account and an IAM user for the application, with the following permissions:

- AmazonRoute53FullAccess
- AmazonEC2ContainerRegistryFullAccess
- AmazonSSMFullAccess
- AmazonEC2FullAccess
- AWSCertificateManagerFullAccess
- IAMFullAccess
- AmazonECS_FullAccess
- CloudWatchFullAccess
- AmazonVPCFullAccess
- AWSCloudFormationFullAccess
- AmazonDynamoDBFullAccess
- AmazonS3FullAccess
- AmazonRDSFullAccess
- AmazonSNSFullAccess
- AmazonPrometheusFullAccess
- AWSLambda_FullAccess

6. Create a Slack user token starting with `xoxp`, and a Slack webhook URL

- See the README.md in the `infra` directory for more details on setting up Slack alerts

7. Createa RapidAPI account and go to [Temp Mail's page](https://rapidapi.com/Privatix/api/temp-mail). Subscribe to a plan and the API key will be available from the playground.
8. Install and set up `direnv` if not already installed
9. `cd` into the repo directory and run `direnv allow`, then `cd` into the `infra` directory, then `cd` back into the root directory and into the `e2e` directory, running `direnv allow` each time prompted.
10. Fill out `.env`, `infra/.env`, and `e2e/.env`
11. Add secrets to the Github repo:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `GH_TOKEN`: Personal access token
- `E2E_RAPID_API_KEY`: RapidAPI key

12. Create the `global` environment in AWS. `cd` into the `infra` folder, and follow instructions in the README.md Setup section.
13. Once the `global` environment is created, make a change to
    the `infra` README.md and create a PR to trigger a preview build. Ensure that the "Deploy Previews for PR" workflow
    runs successfully and inspect the preview build to ensure that it is working correctly.
14. Once all checks are passing, merge the PR. Ensure that the destroy preview workflow runs successfully. It will also trigger a
    job to deploy to staging and production.
15. The deploy to staging and production will not work on the first run. If only e2e tests are failing, re-run the workflow from the
    beginning. Re-run until it can pass.

## Development Status

This project uses [semantic-release](https://github.com/semantic-release/semantic-release) for versioning.
Any time the major version changes, there may be breaking changes. If it is working well for you, consider
pegging to the current major version, e.g. `copier-full-stack-app-fastapi-nextjs-terraform-aws@v1`, to avoid breaking changes. Alternatively,
you can always point to the most recent stable release with the `copier-full-stack-app-fastapi-nextjs-terraform-aws@latest`.

## Developing

Clone the repo and then run `npm install` to set up the pre-commit hooks.

## Author

Created by Nick DeRobertis. MIT License.
