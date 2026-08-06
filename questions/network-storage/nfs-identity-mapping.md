---
title: Diagnose NFS ownership and identity mapping
theme: network-storage
difficulty: middle
type: troubleshooting
tags: [storage, networking, security, filesystem]
sources:
  - url: https://www.rfc-editor.org/rfc/rfc8881.html
    source_type: standard
    verified_on: 2026-08-06
---

# Diagnose NFS ownership and identity mapping

Why can a user authenticate successfully yet see wrong ownership or permission denied on NFS?

## Answer guide

- Separate transport authentication from filesystem authorization. NFS servers and clients must agree on identities, domains, numeric IDs or name mapping, export policy, and the filesystem’s ownership and mode or ACL model.
- Capture the effective application UID/GID, `stat` output on both ends, mount version and options, name-service lookup results, and server logs. Test with a disposable file and the precise user rather than changing ownership recursively without evidence.
- Root squashing and ID mapping can intentionally prevent a client root account from becoming server root. A mismatch may expose files as nobody, deny writes, or—if “fixed” by broad permissions—turn into cross-tenant data access.

## References

- [RFC 8881: NFS identity and access control](https://www.rfc-editor.org/rfc/rfc8881.html)
- Further reading (blog): [Linux NFS project resources](https://wiki.linux-nfs.org/wiki/index.php/Main_Page)

## What to learn next

- Official documentation: [Linux NFS client guide](https://docs.kernel.org/admin-guide/nfs/index.html)
- Manual or specification: [RFC 8881: NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881.html)
- Maintainer or personal blog: [Linux NFS project resources](https://wiki.linux-nfs.org/wiki/index.php/Main_Page)
- Technical blog: [Red Hat Blog: NFS](https://www.redhat.com/en/blog/channel/red-hat-enterprise-linux)
- Hands-on guide: [Ubuntu Server: NFS](https://ubuntu.com/server/docs/how-to/networking/install-nfs/)
