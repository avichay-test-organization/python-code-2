import os
from typing import Dict, Union

from jit_utils.jit_event_names import JitEventName

DEPLOYMENT_STAGE = "DEPLOYMENT_STAGE"
SERVICE_NAME = "execution-service"
LOCAL = "local"
TEST = "test"
REGION_NAME = "AWS_REGION_NAME"

MAX_RESOURCES_IN_USE = 10
UNLIMITED_MAX_RESOURCES_IN_USE = 1000000

TENANT_HEADER = 'Tenant'
TENANT_ID = "tenant_id"
JIT_EVENT_ID = "jit_event_id"
EXECUTION_ID = "execution_id"

TENANT_ID_ENV_VAR = "TENANT_ID"
JIT_EVENT_ID_ENV_VAR = "JIT_EVENT_ID"
EXECUTION_ID_ENV_VAR = "EXECUTION_ID"
KMS_KEY_ID_ENV_VAR = "KMS_KEY_ID"
GCP_KMS_KEY_NAME_ENV_VAR = "GCP_KMS_KEY_NAME"

JIT_BASE_API_URL = f"https://{os.getenv('API_HOST', 'api.local.jitdev.io')}"

# GCP BATCH CONSTANTS
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "")
GCP_REGION = os.getenv("GCP_REGION", "")
GCP_BATCH_JOB_SERVICE_ACCOUNT_EMAIL = os.getenv("GCP_BATCH_JOB_SERVICE_ACCOUNT_EMAIL", "")
GCP_KMS_KEY_NAME = os.getenv("GCP_KMS_KEY_NAME", "")
GCP_BATCH_VPC_NETWORK_NAME = os.getenv("GCP_BATCH_VPC_NETWORK_NAME", "")
GCP_BATCH_VPC_SUBNETWORK_NAME = os.getenv("GCP_BATCH_VPC_SUBNETWORK_NAME", "")

ENV_VAR_NAME_TO_FIELD_NAME = {
    TENANT_ID_ENV_VAR: TENANT_ID,
    JIT_EVENT_ID_ENV_VAR: JIT_EVENT_ID,
    EXECUTION_ID_ENV_VAR: EXECUTION_ID,
}

DYNAMODB = "dynamodb"
START_KEY = "start_key"
DYNAMODB_INSERT_EVENT_TYPE = "INSERT"
DYNAMODB_MODIFY_EVENT_TYPE = "MODIFY"

LAUNCH_DARKLY_SDK_KEY = 'LAUNCH_DARKLY_SDK_KEY'

ALLOCATE_RUNNER_RESOURCES_RETRY_COUNT = 10
MAX_BATCH_SIZE = 10
MAX_BATCH_GET_SIZE = 100  # DynamoDB allows a maximum of 100 items per BatchGetItem operation
ITEM_IDENTIFIER = 'itemIdentifier'
BATCH_ITEMS_FAILURE = 'batchItemFailures'
MESSAGE_ID = 'messageId'
SLACK_NOTIFICATIONS_BOT_TOKEN = 'SLACK_NOTIFICATIONS_BOT_TOKEN'
ENV_NAME = 'ENV_NAME'

GITHUB = 'github'

EXECUTION_TABLE_NAME = "Executions"
RESOURCES_TABLE_NAME = "Resources"
TRIGGER_SERVICE_NAME = "trigger-service"

# INDEX NAMES
PK = 'PK'
SK = 'SK'
GSI1 = 'GSI1'
GSI2 = 'GSI2'
GSI3 = 'GSI3'
GSI4 = 'GSI4'
GSI5 = 'GSI5'
GSI6 = 'GSI6'
GSI7 = 'GSI7'  # used for querying by tenant and jit_event_id ordered by created_at
GSI8 = 'GSI8'  # used for querying by tenant and asset_id and status ordered by created_at
GSI9 = 'GSI9'  # used for querying by tenant and jit_event_id and job_name ordered by created_at
GSI6PK_VALUE = 'EXECUTION_TIMEOUT'
GSI1PK = 'GSI1PK'
GSI1SK = 'GSI1SK'
GSI2PK = 'GSI2PK'
GSI2SK = 'GSI2SK'
GSI3PK = 'GSI3PK'
GSI3SK = 'GSI3SK'
GSI4PK = 'GSI4PK'
GSI4SK = 'GSI4SK'
GSI5PK = 'GSI5PK'
GSI5SK = 'GSI5SK'
GSI6PK = 'GSI6PK'
GSI6SK = 'GSI6SK'
GSI7PK_TENANT_JIT_EVENT_ID = 'GSI7PK_TENANT_JIT_EVENT_ID'
GSI7SK_CREATED_AT = 'GSI7SK_CREATED_AT'
GSI8PK_TENANT_ID_STATUS = 'GSI8PK_TENANT_ID_STATUS'
GSI8SK_ASSET_ID_CREATED_AT = 'GSI8SK_ASSET_ID_CREATED_AT'
GSI9PK_TENANT_ID = 'GSI9PK_TENANT_ID'
GSI9SK_JIT_EVENT_ID_JOB_NAME_CREATED_AT = 'GSI9SK_JIT_EVENT_ID_JOB_NAME_CREATED_AT'

EXCLUSIVE_START_KEY = 'ExclusiveStartKey'
RESOURCE_IN_USE = 'resource_in_use'
LAST_EVALUATED_KEY = 'LastEvaluatedKey'
LIMIT = 'Limit'

EXECUTION_EVENT_SOURCE = "execution-service"
EXECUTION_EVENT_BUS_NAME = "executions"
EXECUTION_REGISTER_EVENT_DETAIL_TYPE = "execution-registered"
EXECUTION_COMPLETE_EVENT_DETAIL_TYPE = "execution-completed"
FETCH_LOGS_EVENT_DETAIL_TYPE = "fetch-logs"
EXECUTION_ENRICH_EXECUTION_EVENT_DETAIL_TYPE = "enrich-execution"
EXECUTION_DISPATCH_EXECUTION_EVENT_DETAIL_TYPE = "dispatch-execution"
EXECUTION_DEPROVISIONED_EXECUTION_EVENT_DETAIL_TYPE = "execution-deprovisioned"
EXECUTION_DISPATCH_EXECUTION_STATUS_EVENT_DETAIL_TYPE = "dispatch-execution-status"
EXECUTION_FARGATE_TASK_FINISHED = "fargate-task-finished"

EXECUTION_UPDATES_BUS_NAME = "execution-changes"
EXECUTION_UPDATES_DETAIL_TYPE = "execution-change"
RESOURCE_UPDATES_BUS_NAME = "resource-changes"
RESOURCE_IN_USE_DETAIL_TYPE = "resource-in-use"
RESOURCE_COUNTER_DETAIL_TYPE = "resource-counter"

RESOURCE_ALLOCATION_INVOKED_METRIC_DETAIL_TYPE = "resource-allocation-invoked"
EXECUTION_DISPATCH_METRIC_DETAIL_TYPE = "execution-dispatch-metric"

WATCHDOG_EVENT_QUEUE_NAME = 'WatchdogEventQueue.fifo'
SEND_INTERNAL_NOTIFICATION_QUEUE_NAME = 'SendInternalNotificationQueue'

TERMINATED_BY_WATCHDOG_REASON = "Terminated by Watchdog"

EXCEEDED_TIME_LIMITATION_ERROR = 'Exceeded time limitation'

FAILED_TO_ASSUME_ROLE_ASSET_STATUS_DETAILS = 'Failed to assume role'

AWS = 'aws'
ACTIVE = 'ACTIVE'
ASC = 'ASC'

ENV_NAME_STRING = os.getenv(ENV_NAME, '')
AWS_JIT_ROLE = 'JitRole' + ('' if ENV_NAME_STRING == "prod" else ENV_NAME_STRING.capitalize())
AWS_COMMON_STS_CLIENT_NAME = 'sts'
AWS_COMMON_BATCH_CLIENT_NAME = 'batch'
AWS_COMMON_CREDENTIALS_MAP = {
    'aws_access_key_id': 'AccessKeyId',
    'aws_secret_access_key': 'SecretAccessKey',
    'aws_session_token': 'SessionToken'
}

AWS_COMMON_SESSION_SECONDS_DURATION = 3600  # Default 3600 = 1 hour / Max is 43200 = 12 hours
AWS_COMMON_REGION_NAME_KEY = 'region_name'
AWS_COMMON_ASSUMED_ROLE_CREDENTIALS_KEY = 'Credentials'

TENANT_CREATED_EVENT_SOURCE = "tenant-service"
TENANT_CREATED_EVENT_BUS_NAME = "tenants"
TENANT_CREATED_EVENT_DETAIL_TYPE = "tenant-created"

CANCEL_EXECUTION_EVENT_SOURCE = "execution-service"
CANCEL_EXECUTION_EVENT_BUS_NAME = "executions"
CANCEL_EXECUTION_EVENT_DETAIL_TYPE = "cancel-execution"

INSTALLATION_PARTIAL_UPDATE_EVENT_BUS = 'installations'
INSTALLATION_PARTIAL_UPDATE_EVENT_DETAIL_TYPE = 'partial-update-installation'

SLACK_CHANNEL_NAME_FREE_RESOURCES_ERRORS = "jit-free-resources-errors-{env_name}"
SLACK_CHANNEL_NAME_RESOURCE_EXPIRED_ERRORS = "jit-resources-mgmt-{env_name}"
SLACK_CHANNEL_NAME_USER_MISCONFIG = "jit-users-misconfig-{env_name}"
SLACK_CHANNEL_CONTROL_ERRORS_NAME = "jit-control-errors-{env_name}"

EXECUTION_FAILURE_METRIC_DETAIL_TYPE = "execution-failure-metric"

# time definitions
MINUTE_IN_SECONDS = 60
HOUR_IN_MINUTES = 60
HOUR_IN_SECONDS = HOUR_IN_MINUTES * MINUTE_IN_SECONDS
WATCHDOG_GRACE_PERIOD = 5 * MINUTE_IN_SECONDS

# CI runner timeouts
CI_RUNNER_EXECUTION_TIMEOUT = 15 * MINUTE_IN_SECONDS
CI_RUNNER_DISPATCHED_TIMEOUT = 5 * MINUTE_IN_SECONDS

# fargate runner timeouts
JIT_RUNNER_EXECUTION_TIMEOUT = 2 * HOUR_IN_SECONDS
JIT_RUNNER_DISPATCHED_TIMEOUT = 10 * MINUTE_IN_SECONDS


# JIT EVENTS CONSTANTS

PULL_REQUESTS_RELATED_JIT_EVENTS = [JitEventName.PullRequestCreated, JitEventName.PullRequestUpdated]

env_name = os.getenv(ENV_NAME)
FINDINGS_UPLOAD_S3_BUCKET = f"execution-service-{env_name}-upload-findings-bucket"
FINDINGS_UPLOAD_URL_EXPIRATION_SECONDS = 3 * HOUR_IN_SECONDS  # 3 hours in seconds

EXECUTION_LOGS_S3_BUCKET = f"jit-execution-logs-{env_name}"
EXECUTION_LOG_S3_OBJECT_KEY = "{tenant_id}/{jit_event_id}-{execution_id}.log"
EXECUTION_LOG_GET_SIZE_LIMIT = 10 * 1024  # 10KB
EXECUTION_LOG_PRINT_MAX_CHUNK_SIZE = 1024 * 1024  # 1MB

LOGS_UPLOAD_URL_EXPIRATION_SECONDS = 10800  # 3 hours in seconds

IS_SILENT_INVOCATION_ENV_VAR = 'IS_SILENT_INVOCATION'

SILENT_INVOCATION_UPLOAD_FINDINGS_S3_BUCKET = f"jit-silent-invocation-findings-{env_name}"
SILENT_INVOCATION_UPLOAD_LOGS_S3_BUCKET = f"jit-silent-invocation-logs-{env_name}"
SILENT_INVOCATION_UPLOAD_URL_EXPIRATION_SECONDS = 3 * HOUR_IN_SECONDS  # 3 hours in seconds

LOG_MESSAGE_MASK = "************"
EXECUTION_TTL = 60 * 60 * 24 * 7  # 7 days

ECS_TASK_KMS_ARN = os.getenv("ECS_TASK_KMS_ARN", "")

S3_EXECUTION_OUTPUTS_BUCKET_NAME = os.getenv("S3_EXECUTION_OUTPUTS_BUCKET_NAME", "")
S3_OUTPUTS_UPLOAD_URL_EXPIRATION_SECONDS = 15 * MINUTE_IN_SECONDS
MAX_OUTPUTS_UPLOAD_FILES = 10
JIT_PLAN_SLUG = "jit-plan"
DOWNLOAD_URL_EXPIRATION_SECONDS = 3600
PUBLIC_ARTIFACTS_ARCHIVE_BASE_NAME = 'public'

JIT_GITHUB_JOB_LOGS_BUCKET_NAME = f"jit-github-job-logs-{env_name}"
JIT_GCP_JOB_LOGS_BUCKET_NAME = f"jit-gcp-job-logs-{env_name}"
JIT_EXECUTION_OUTPUTS_BUCKET_NAME = f"jit-execution-outputs-{env_name}"
S3_BUCKET_FORMAT = "https://s3.console.aws.amazon.com/s3/buckets/{bucket_name}?prefix={object_key}"
S3_OBJECT_FORMAT = "https://s3.console.aws.amazon.com/s3/object/{bucket_name}?prefix={object_key}"

# alert types
EXECUTION_DISPATCH_ERROR_ALERT = "Execution Dispatch Error"
EXECUTION_NOT_FOUND_ERROR_ALERT = "Execution Not Found Error"
EXECUTION_MAX_RETRIES_ALERT = "Execution Max Retries"

SlackMessageBlock = Dict[str, Union[str, Dict[str, str]]]


MAX_API_GATEWAY_TIMEOUT_SECONDS = 30

# trigger execution event bus
TRIGGER_EXECUTION_EVENT_BUS_NAME = "trigger-execution"
TRIGGER_EXECUTION_DETAIL_TYPE = "trigger-execution"

EXECUTION_RETRY_LIMIT = 3

# Metrics
EXECUTION_METRIC_NAME = "execution-metric"
