# Fedora 45 laptop image publisher

The Fedora 45 organization runner is online in the laptop's existing `runner-reo-fedora45` migration pod. This proposal routes the existing publisher through pinned SSH and a forced host command that accepts only its supported image operations and the existing repository and tag allowlists. The gateway does not mount the host Podman socket in the runner, grant a general shell, or reuse the fleet SSH key.

Before merging, install the reviewed gateway on reo-laptop and authorize its dedicated public key with a forced command and forwarding disabled. Store the corresponding private credential in the repository's `REO_IMAGE_HOST_SSH_KEY` secret. Test the credential with a read-only inventory dispatch and leave the old runner available until the replacement is verified. The gateway and credential were not installed as part of this PR. No images were pushed for validation.
