# Copyright (c) 2016 Intel, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from flask_restful import abort
from flask_restful import Resource
import logging

LOG = logging.getLogger(__name__)


class StoragesList(Resource):

    def get(self):
        LOG.debug("GET /storages")
        return abort(501)


class Storages(Resource):

    def get(self, storageid):
        LOG.debug("GET /storages" + storageid)
        return abort(501)