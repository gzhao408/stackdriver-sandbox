#!/usr/bin/env python3
import os
import sys
import unittest
from google.cloud.trace_v1 import trace_service_client

project_id = ''

def get_project_id():
    project_id = os.environ['GOOGLE_CLOUD_PROJECT']
    if not project_id:
      raise MissingProjectIdError(
          'Set the environment variable ' +
          'GCLOUD_PROJECT to your Google Cloud Project Id.')

class CloudTracingTest(unittest.TestCase):
    def test_trace_opentelemetry(self):
        """Make sure we are receiving  traces from opentelemetry-go 0.9.0 in Google Cloud Trace"""
        client = trace_service_client.TraceServiceClient().from_service_account_json(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
        for trace in client.list_traces(project_id, filter_='g.co/agent:opentelemetry'):
            print(trace)

if __name__ == '__main__':
    get_project_id()
    unittest.main()


