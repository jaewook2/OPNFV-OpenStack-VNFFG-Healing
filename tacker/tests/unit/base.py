# Copyright 2016 Brocade Communications System, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
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

import mock
from oslo_config import cfg
from oslo_config import fixture as config_fixture
from requests_mock.contrib import fixture as requests_mock_fixture

from tacker.tests import base

CONF = cfg.CONF


class TestCase(base.BaseTestCase):

    def setUp(self):
        super(TestCase, self).setUp()
        self.config_fixture = self.useFixture(config_fixture.Config(CONF))
        CONF([], default_config_files=[])

    def _mock(self, target, new=mock.DEFAULT):
        patcher = mock.patch(target, new)
        return patcher.start()


class FixturedTestCase(TestCase):
    client_fixture_class = None

    def setUp(self):
        super(FixturedTestCase, self).setUp()
        if self.client_fixture_class:
            self.requests_mock = self.useFixture(requests_mock_fixture.
                                                 Fixture())
            fix = self.client_fixture_class(self.requests_mock)
            self.cs = self.useFixture(fix).client
