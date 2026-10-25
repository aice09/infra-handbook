# Staging environment

Staging is the pre-production environment for checking handbook changes before they are released to the production site.

## Deployment flow

1. Make and review changes on a feature branch.
2. Merge or push the changes to the persistent `staging` branch.
3. GitHub Actions builds the Sphinx site and deploys it to Vercel Preview.
4. Review the preview deployment for broken pages, navigation, and content.
5. Merge the verified changes into `main` to deploy to production.

The deployment workflow treats `main` as production and deploys other branches as Vercel Preview deployments. The staging branch is therefore a branch-based preview environment, not a separate Vercel custom environment.

## Checking a staging deployment

- Open the **Build and Deploy Infrastructure Handbook** workflow in GitHub Actions and select the run for the `staging` branch.
- Confirm the documentation build and Vercel preview deployment both succeed.
- Open the Preview URL from the deployment step and check the rendered handbook.
- If Vercel Deployment Protection is enabled, sign in with an authorized account.

For a stable staging URL, assign a domain to the Vercel Preview environment and configure its Git branch as `staging`.
