from aws_cdk.aws_cloudfront import (
    CloudFrontWebDistribution,
    SourceConfiguration,
    Behavior,
    S3OriginConfig
)
from services.route53_service import Route53Service
from services.bucket_service import BucketService


class StackService:
    def create_stack(stack):
        domain = "radiant-lounge.com"

        website_bucket = BucketService.create_deployment_bucket(
            stack,
            domain,
            "Website"
        )

        BucketService.create_redirect_bucket(
            stack,
            domain,
            "Website"
        )

        distribution = CloudFrontWebDistribution(
            stack,
            "RadiantLoungeDistribution",
            origin_configs=[SourceConfiguration(
                s3_origin_source=S3OriginConfig(
                    s3_bucket_source=website_bucket
                ),
                behaviors=[Behavior(is_default_behavior=True)]
            )
            ]
        )

        Route53Service.create_route53(stack, domain, distribution)
