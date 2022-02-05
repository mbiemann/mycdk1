#!/usr/bin/env python3

from aws_cdk import (
    App,
    AssetHashType,
    aws_lambda,
    RemovalPolicy,
    Stack
)
from constructs import Construct


class MyStack1(Stack):

    def __init__(self, scope: Construct) -> None:
        
        construct_id: str = "MyStack1"
        super().__init__(scope, construct_id)

        layer1 = aws_lambda.LayerVersion(self, 'MyLayer1',
            layer_version_name="global-my-lambda-layer-1",
            code=aws_lambda.Code.from_asset("code_layer", asset_hash="abc", asset_hash_type=AssetHashType.CUSTOM),
            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_9],
            removal_policy=RemovalPolicy.RETAIN
        )

        aws_lambda.Function(self, "MyFunction1",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=aws_lambda.Code.from_asset("code_lambda"),
            layers=[layer1]
        )


app = App()
MyStack1(app)
app.synth()
