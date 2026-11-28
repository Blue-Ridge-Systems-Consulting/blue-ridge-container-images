#!/usr/bin/env bash
# Call the account's restricted image-publishing gateway, keeping stdin open for login.
set -euo pipefail
[[ $# -gt 0 ]]
printf -v command ' %q' "$@"
exec ssh -i "$REO_IMAGE_HOST_KEY_FILE" -o BatchMode=yes -o IdentitiesOnly=yes \
  -o ClearAllForwardings=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=12 \
  -o UserKnownHostsFile="$GITHUB_WORKSPACE/config/reo-laptop-ssh-known-hosts" \
  ray@host.containers.internal "podman$command"
