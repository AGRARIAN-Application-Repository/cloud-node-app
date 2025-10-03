# Cloud Node App

Agrarian Cloud Node Application for the Agrarian ecosystem.

## Description

This application provides cloud node functionality for the Agrarian farming ecosystem.

## Development

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

### Docker

```bash
# Build the image
docker build -t cloud-node-app .

# Run the container
docker run -p 80:80 cloud-node-app
```

## CI/CD

This repository uses GitHub Actions for CI/CD:

- **Build**: Multi-arch Docker images (AMD64/ARM64)
- **Security**: Trivy vulnerability scanning
- **SBOM**: Software Bill of Materials generation
- **Registry**: GitHub Container Registry (GHCR)

## Deployment

The application is deployed to the Agrarian k3s cluster using FluxCD GitOps.
