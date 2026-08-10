---
title: Decide whether a function should attach to a private network
theme: serverless
difficulty: middle
type: scenario
tags: [cloud, networking, security, reliability, cost-optimization]
sources:
  - url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html
    source_type: official-docs
    verified_on: 2026-08-10
---

# Decide whether a function should attach to a private network

A team wants every function attached to the private VPC "for security". What do you tell them, and what does the attachment actually change?

## Answer guide

- Start with the requirement, not the default. Attach a function to a private network when it must reach a resource that has no public endpoint or must not be reached over the internet—databases, internal services, on-premises systems over a private link. Do not attach a function whose only dependencies are public managed APIs, because the attachment buys nothing and costs reachability.
- The mechanism: the platform creates network interfaces in your subnets and routes the function's outbound traffic through them. Modern implementations create and share those interfaces per unique subnet-plus-security-group combination rather than per execution environment, which is why the old multi-second attachment penalty largely disappeared. Interface creation still consumes IP addresses in the subnet and is subject to account-level interface quotas.
- The main surprise is that attaching removes default internet access. A function in a private subnet reaches the internet only through a NAT gateway, and reaches provider services privately only through interface or gateway endpoints. That decision has both a cost dimension—NAT charges per gigabyte processed—and a reliability dimension, because NAT becomes a shared dependency for every attached function.
- Size subnets deliberately. A burst of concurrency across many attached functions consumes addresses and interfaces; use several subnets across availability zones, keep security groups narrow, and prefer private endpoints over NAT for provider APIs so that traffic never leaves the private network.
- Failure modes to expect: subnet IP exhaustion that surfaces as invocation failures during a traffic spike, a missing endpoint or NAT route that turns every outbound call into a timeout consuming the full function duration, DNS resolution that differs inside the VPC, and security-group changes that force interface churn during a deploy.

## References

- [Connecting Lambda functions to an Amazon VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
- Further reading (blog): [AWS Compute Blog — serverless networking articles](https://aws.amazon.com/blogs/compute/)

## What to learn next

- Official documentation: [Lambda networking foundations](https://docs.aws.amazon.com/lambda/latest/dg/foundation-networking.html)
- Manual or specification: [AWS Lambda API reference — UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html)
- Maintainer or personal blog: [Yan Cui — theburningmonk on serverless networking trade-offs](https://theburningmonk.com/)
- Technical blog: [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- Hands-on guide: [NAT gateways in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
