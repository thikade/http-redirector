# http-redirector
A minimal HTTP redirect service that issues 301 redirects to a configurable target URL, preserving the request path.

## Configuration

| Variable | Default | Description |
|---|---|---|
| `REDIRECT_URL` | `https://www.google.com` | Base URL to redirect to |
| `PORT` | `8080` | Port to listen on |

All incoming GET and POST requests are redirected to `REDIRECT_URL + <original path>`.

## Run

```sh
# Docker
docker build -t redirector .
docker run -p 8080:8080 -e REDIRECT_URL=https://example.com redirector

# Local
PORT=8080 REDIRECT_URL=https://example.com python redirect.py
```

## Kubernetes

Apply the manifests in [k8s/](k8s/), setting `REDIRECT_URL` in [k8s/deployment.yaml](k8s/deployment.yaml).
