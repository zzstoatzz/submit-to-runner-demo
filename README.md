## using `submit_to_runner` for concurrent subflows w/ `prefect`

#### run the example
```bash
docker compose up
```

![timeline](https://github.com/zzstoatzz/submit-to-runner-demo/assets/31014960/da191276-3ec1-43dc-aff7-7d3f937cd343)

```markdown
       │ File: /Users/nate/.prefect/profiles.toml
───────┼────────────────────────────────────────────────────────
   1   │ active = "submit-to-runner"
   2   │
   3   │ [profiles.submit-to-runner]
   4   │ PREFECT_EXPERIMENTAL_ENABLE_EXTRA_RUNNER_ENDPOINTS = "True"
   6   │ PREFECT_API_URL = "http://127.0.0.1:4200/api"
```