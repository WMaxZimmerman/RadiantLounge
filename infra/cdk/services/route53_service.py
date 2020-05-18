from aws_cdk.aws_route53 import (
    HostedZone,
    ARecord,
    AaaaRecord,
    RecordTarget
)
from aws_cdk.aws_route53_targets import CloudFrontTarget


class Route53Service:
    def create_route53(stack, domain, distrubution):
        hosted_zone = HostedZone.from_lookup(
            stack,
            'RadiantLoungeZone',
            domain_name=domain
        )

        ARecord(
            stack,
            f'RadiantLoungeARecord',
            zone=hosted_zone,
            target=RecordTarget.from_alias(CloudFrontTarget(distrubution))
        )

        AaaaRecord(
            stack,
            f'RadiantLoungeAaaaRecord',
            zone=hosted_zone,
            target=RecordTarget.from_alias(CloudFrontTarget(distrubution))
        )
