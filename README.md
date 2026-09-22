# Blue Ridge Systems Container Images

General-use OCI container images for AI experimentation, exploration, local prototyping, and learning.

These images are intended as starting points for hands-on evaluation. They are not a managed service, a promise of long-term API compatibility, or a replacement for reviewing the software and upstream licenses that apply to your use case.

## Available images

Each image uses the `blue-ridge-public` tag.

| Image | Pull command |
| --- | --- |
| `reo-ai` | `podman pull ghcr.io/blue-ridge-systems-consulting/reo-ai:blue-ridge-public` |
| `reo-tools` | `podman pull ghcr.io/blue-ridge-systems-consulting/reo-tools:blue-ridge-public` |
| `olmoai` | `podman pull ghcr.io/blue-ridge-systems-consulting/olmoai:blue-ridge-public` |

The packages must be publicly visible on GitHub before anonymous pulls will succeed.

## Use responsibly

- Review image metadata, included software, and applicable upstream licenses before use.
- Pin a digest rather than a moving tag when you need a reproducible environment.
- Start containers with least privilege and keep credentials, private data, and host mounts out of experimental workloads.
- Obtain and use any AI models or weights under their own terms. A runtime image does not grant rights to a model.
- Validate behavior, security, performance, and output quality for your own environment before relying on an image.

## Scope

These images are published for general experimentation and exploration. They may change as the underlying tools evolve, and are provided as-is without operational guarantees or support commitments.
