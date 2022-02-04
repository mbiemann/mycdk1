import aws_cdk as core
import aws_cdk.assertions as assertions

from mycdk1.mycdk1_stack import Mycdk1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in mycdk1/mycdk1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Mycdk1Stack(app, "mycdk1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
