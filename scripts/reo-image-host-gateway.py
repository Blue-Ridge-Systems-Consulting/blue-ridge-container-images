#!/usr/bin/python3
"""Forced SSH command for the Fedora image publisher on reo-laptop."""
import os
from pathlib import Path
import re
import shlex
import socket

source_pattern = r"localhost/(reo-ai|ray-tools|olmoai|apertusai):[A-Za-z0-9._-]+"
target_pattern = r"ghcr\.io/blue-ridge-systems-consulting/(reo-ai|reo-tools|olmoai|apertusai):(blue-ridge-public|reo-laptop-[0-9]+)"


def approve(argv, auth):
    if not argv or argv[0] != "podman":
        raise ValueError("Expected Podman")
    match argv[1:]:
        case ["image", "exists", source] if re.fullmatch(source_pattern, source):
            return ["image", "exists", source]
        case ["image", "inspect", "--format", "{{.Id}}", source] if re.fullmatch(source_pattern, source):
            return ["image", "inspect", "--format", "{{.Id}}", source]
        case ["login", "ghcr.io", "-u", actor, "--password-stdin"] if re.fullmatch(r"[A-Za-z0-9-]+(?:\[bot\])?", actor):
            return ["login", "--authfile", auth, "--username", actor, "--password-stdin", "ghcr.io"]
        case ["tag", source, target] if re.fullmatch(source_pattern, source) and re.fullmatch(target_pattern, target):
            if re.fullmatch(source_pattern, source)[1].replace("ray-tools", "reo-tools") == re.fullmatch(target_pattern, target)[1]:
                return ["tag", source, target]
        case ["push", target] if re.fullmatch(target_pattern, target):
            return ["push", "--authfile", auth, target]
        case ["logout", "ghcr.io"]:
            return ["logout", "--authfile", auth, "ghcr.io"]
        case ["pull", "--quiet", target] if re.fullmatch(target_pattern, target) and target.endswith(":blue-ridge-public"):
            return ["pull", "--quiet", "--authfile", str(Path(auth).with_name("anonymous.json")), target]
    raise ValueError("Image gateway command is not allowed")


def main():
    if socket.gethostname().split(".", 1)[0] != "reo-laptop":
        raise SystemExit("Wrong gateway host")
    os.umask(0o077)
    directory = Path.home() / ".local/state/reo-image-gateway"
    auth = str(directory / "github.json")
    try:
        args = approve(shlex.split(os.environ.get("SSH_ORIGINAL_COMMAND", "")), auth)
    except ValueError:
        raise SystemExit("Image gateway denied the command") from None
    directory.mkdir(parents=True, mode=0o700, exist_ok=True)
    if args[0] == "pull":
        (directory / "anonymous.json").write_text('{"auths":{}}\n')
    os.execv("/usr/bin/podman", ["/usr/bin/podman", *args])


if __name__ == "__main__":
    main()
