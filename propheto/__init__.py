# Copyright 2021 Propheto Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

SUPPORTED_VERSIONS = [(3, 8), ]

if sys.version_info[:2] not in SUPPORTED_VERSIONS:
    formatted_supported_versions = [
        "{}.{}".format(*version) for version in SUPPORTED_VERSIONS
    ]
    err_msg = "This version of Python ({}.{}) is not supported!\n".format(
        *sys.version_info
    ) + "Propheto supports the following versions of Python: {}".format(
        formatted_supported_versions
    )
    raise RuntimeError(err_msg)

__version__ = '0.1.3'

from .app import Propheto