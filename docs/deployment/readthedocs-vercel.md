# Hosting Sphinx documentation on Vercel

This handbook uses **Sphinx** to build its documentation and **Vercel** to host
the generated static HTML. It uses the Sphinx Read the Docs theme
(`sphinx_rtd_theme`), but it is not currently hosted by the Read the Docs
service. A Read the Docs account is not needed for this deployment.

## Prerequisites

- A GitHub repository containing the Sphinx documentation.
- A Vercel project linked to that repository.
- A Vercel token, team or account ID, and project ID.
- Permission to add GitHub Actions repository secrets.
- A DNS-managed domain if you want custom production or staging URLs.
- Python 3.12 for the automated build. Local builds also require the packages
  in `requirements.txt`.

## What is already configured

- `docs/conf.py` configures Sphinx, MyST Markdown support, and the Read the Docs
  theme.
- `requirements.txt` lists Sphinx and its documentation dependencies.
- `.github/workflows/deploy.yml` installs dependencies, builds the HTML, and
  deploys it to Vercel.
- `vercel.json` leaves Sphinx's generated `.html` URLs available. Do not enable
  `cleanUrls` without updating and testing the Sphinx links.
- Pushes to `main` deploy to Vercel Production; pushes to other branches,
  including `staging`, deploy to Vercel Preview.
- `docs.phlopentech.org` is the production domain. The `staging` branch is
  assigned the Preview domain `staging.docs.phlopentech.org`.

## Configure the GitHub-to-Vercel deployment

1. Create or select a Vercel project and link it to the GitHub repository.
2. In the GitHub repository, open **Settings → Secrets and variables →
   Actions** and add these repository secrets:

   | Secret | Value |
   | --- | --- |
   | `VERCEL_TOKEN` | A Vercel access token with permission to deploy the project |
   | `VERCEL_ORG_ID` | The Vercel team ID, or account ID for a personal project |
   | `VERCEL_PROJECT_ID` | The ID of the Vercel project |

   Keep these values in GitHub Secrets; do not commit them to the repository.
3. Confirm the GitHub Actions workflow is enabled. It uses the secrets to deploy
   a prebuilt static output to Vercel.
4. Push to a non-`main` branch to create a Preview deployment. Push to `main`
   only when ready to update Production.

## Configure custom domains

1. In the Vercel project, open **Settings → Domains** and add the hostname.
2. Assign `docs.phlopentech.org` to **Production**.
3. Assign `staging.docs.phlopentech.org` to **Preview**, with the Git branch set
   to `staging`.
4. In the DNS provider, create the record using the exact type and target Vercel
   displays for each hostname. DNS targets can differ; do not copy an old target
   from another domain.
5. For the staging CNAME, use **DNS only** while verifying with Vercel if a
   DNS proxy is enabled. Wait for Vercel to show **Valid Configuration** and
   finish issuing the TLS certificate.

Vercel Deployment Protection may require users to sign in to view Preview
deployments. Adjust Preview protection in Vercel only if the staging site is
intended to be publicly accessible. Do not change Production domain settings
when configuring staging.

## Build and check the site

Build locally from the repository root:

```console
python -m pip install -r requirements.txt
sphinx-build -W --keep-going -b html docs _build/html
```

Open `_build/html/index.html` in a browser and check the navigation and pages.
The CI workflow performs the same Sphinx build with warnings treated as errors.

After pushing a change:

1. In GitHub, open **Actions → Build and Deploy Infrastructure Handbook**.
2. Select the run for the branch you pushed. Confirm the build and deploy steps
   succeeded.
3. Open the Preview URL shown in the deployment details or test the staging
   domain. Check representative nested pages, including their `.html` URLs.
4. Merge the reviewed change into `main` to deploy Production.

## Troubleshooting

- **Build fails:** inspect the Sphinx build step in GitHub Actions. It runs with
  `-W`, so warnings such as broken toctree references fail the build.
- **Vercel credential validation fails:** confirm all three GitHub Actions
  secrets are set and that the token can access the selected project.
- **Custom domain is invalid:** compare the DNS record with the exact values
  shown in Vercel. Check for conflicting records or an enabled DNS proxy.
- **A generated page returns 404:** verify that the matching HTML file exists
  in the build output and that Vercel is not rewriting `.html` URLs.
- **Preview redirects to Vercel sign-in:** check Deployment Protection and use
  an account authorized to view the deployment.

## References

- [Vercel environments and staging](https://vercel.com/docs/deployments/environments)
- [Vercel domains](https://vercel.com/docs/domains)
- [Sphinx documentation](https://www.sphinx-doc.org/)
