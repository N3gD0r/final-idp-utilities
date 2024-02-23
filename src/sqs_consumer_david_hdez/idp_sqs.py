from collections.abc import Callable
from deploy_args_david_hdez.idp_args import ProgramArgs

import boto3
import json


class SqsSettings:
    def __init__(self,
                 queue_url: str = None,
                 region: str = None):
        self.queue_url = queue_url
        self.region = region


class SqsConsumer:
    def __init__(self,
                 settings: SqsSettings = None,
                 args: ProgramArgs = None,
                 program: Callable[[ProgramArgs], None] = None):
        self.settings = settings
        self.args = args
        self.program = program

    def get_workloads(self):
        region = self.settings.region
        url = self.settings.queue_url
        sqs = boto3.client('sqs', region_name=region)

        while True:
            response: dict = sqs.receive_message(
                QueueUrl=url,
                WaitTimeSeconds=20,
                VisibilityTimeout=5
            )

            if 'Messages' not in response:
                return 'No messages available'

            for message in response['Messages']:
                receipt: str = message.get('ReceiptHandle')
                message_id: str = message.get('MessageId')
                body: str = message.get('Body')

                workload: dict = json.loads(body)
                service: dict = workload.get('Service')

                self.args.region = workload.get('awsRegion')
                self.args.team = workload.get('TeamName')
                self.args.project = workload.get('ProjectName')
                self.args.owner = workload.get('OwnerName')
                self.args.process_payload(service)

                self.program(self.args)

                sqs.delete_message(
                    QueueUrl=url,
                    ReceiptHandle=receipt
                )
