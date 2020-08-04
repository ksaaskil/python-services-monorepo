# Python service monorepo

Example how to share Python packages between multiple services.

Shared Python package is in [`shared/`](./shared) folder.

Two example services using code from `shared/` are [`helloer/`](./helloer) and [`goodbyer/`](./goodbyer). Their `requirements.txt` include `../shared` so that the shared package is installed (if it's in context).

Dockerfiles are in [`docker/`](./docker) folder. They could just as well be in `helloer/Dockerfile` or `goodbyer/Dockerfile` as long as `dockerfile` in [`docker-compose.yml`](./docker-compose.yml) is pointing to the correct file.

### Docker

Start services with `docker-compose`:

```bash
$ docker-compose up
```

Navigate to [`http://localhost:8088`](http://localhost:8088) for `helloer` and [`http://localhost:8089`](http://localhost:8089) for `goodbyer`.

To build a Docker image for service `helloer/`, run this in the repository root:

```bash
$ docker build -f docker/Dockerfile.helloer -t example-helloer .
```
