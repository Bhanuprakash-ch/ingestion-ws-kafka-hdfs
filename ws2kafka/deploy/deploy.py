#
# Copyright (c) 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
This scripts automates deployment of ws2kafka application
(creates required service instances, pushes to TAP instance).
"""

from app_deployment_helpers import cf_cli
from app_deployment_helpers import cf_helpers

APP_NAME = "ws2kafka"

PARSER = cf_helpers.get_parser(APP_NAME)

ARGS = PARSER.parse_args()

CF_INFO = cf_helpers.get_info(ARGS)
cf_cli.login(CF_INFO)

cf_cli.create_service('kafka', 'shared', 'kafka-inst')

PROJECT_DIR = ARGS.project_dir if ARGS.project_dir else \
    cf_helpers.get_project_dir()

cf_helpers.push(work_dir=PROJECT_DIR, options=ARGS.app_name)