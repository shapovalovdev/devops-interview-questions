---
title: Configure TLS for Kubernetes Ingress safely
theme: kubernetes
difficulty: middle
type: scenario
tags: [kubernetes, security, tls, networking, cks]
sources:
  - url: https://kubernetes.io/docs/concepts/services-networking/ingress/
    source_type: official-docs
    verified_on: 2026-08-06
---

# Configure TLS for Kubernetes Ingress safely

How would you expose `api.example.com` through an Ingress with TLS while preventing accidental plaintext or wrong-host routing?

## Answer guide

- Create a TLS Secret containing the certificate and private key, reference it from the Ingress `tls` section with the exact host, and configure the paths and backend according to the installed Ingress controller. Kubernetes defines the Ingress API; controller-specific TLS redirects and cipher settings are not portable.
- Obtain and renew certificates through an approved issuer or automation path, constrain who can read or replace the Secret, and monitor both certificate expiry and the actual endpoint handshake. Test the expected hostname, chain, protocol policy, and backend route from outside the cluster.
- Redirect or reject HTTP at the controller or edge according to the service policy, and make the intended host explicit so a default virtual host cannot accidentally serve the API. Keep separate certificates and ownership boundaries where tenant isolation requires them.
- TLS termination does not secure traffic after the proxy, authorize callers, or prevent a misrouted backend. A controller may continue serving an old certificate after a bad Secret update, and an over-broad default route can expose a service even when TLS is valid.

## References

- [Kubernetes: Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Kubernetes: TLS Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets)
- Further reading (blog): [cert-manager: Securing Ingress resources](https://cert-manager.io/docs/usage/ingress/)
