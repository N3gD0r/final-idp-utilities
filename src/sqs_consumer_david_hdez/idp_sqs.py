from collections.abc import Callable
from deploy_args_david_hdez.idp_args import ProgramArgs

import boto3
import json


class SqsSettings:
    def __init__(self,
                 queue_url: str = None,
                 region: str = None,
                 wait_time: int = 20,
                 vis_timout: int = 60 * 2):
        self.queue_url = queue_url
        self.region = region
        self.wait_time = wait_time
        self.visibility_timeout = vis_timout


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
        wait_time = self.settings.wait_time
        vis_timout = self.settings.visibility_timeout
        sqs = boto3.client('sqs', region_name=region)

        while True:
            response: dict = sqs.receive_message(
                QueueUrl=url,
                WaitTimeSeconds=wait_time,
                VisibilityTimeout=vis_timout
            )

            if 'Messages' in response:
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
                    self.args.service_name = service.get('service_name')
                    self.args.process_payload(service)

                    self.program(self.args)

                    sqs.delete_message(
                        QueueUrl=url,
                        ReceiptHandle=receipt
                    )
