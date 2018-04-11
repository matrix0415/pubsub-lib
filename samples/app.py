#!/usr/bin/env python
# coding=utf-8
#
import os
import logging

from soocii_pubsub_lib import pubsub_client, sub_service

# ========== Initial Logger ==========
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)-15s][%(levelname)-5s][%(filename)s][%(funcName)s#%(lineno)d] %(message)s')
logger = logging.getLogger(__name__)
# ====================================


def callback(payload):
    logger.info(payload)
    # ack message
    return True


if __name__ == '__main__':
    project = os.environ['PUBSUB_PROJECT_ID'] if 'PUBSUB_PROJECT_ID' in os.environ else 'pubsub-trial-198610'
    cred = os.environ['GOOGLE_APPLICATION_CREDENTIALS'] if 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ else './pubsub-trial.json'
    logger.info('project: {}, cred: {}'.format(project, cred))

    # prepare subscriber
    subscriber = pubsub_client.SubscribeClient(project, cred)
    subscription = subscriber.create_subscription('test-topic', 'test-sub2')

    service = sub_service.SubscriptionService(subscription)
    service.run(callback)
