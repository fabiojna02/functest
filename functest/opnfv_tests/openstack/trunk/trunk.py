#!/usr/bin/env python

# Copyright (c) 2018 Orange and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0

# pylint: disable=missing-docstring

from six.moves import configparser

from functest.opnfv_tests.openstack.tempest import tempest


class TempestNeutronTrunk(tempest.TempestCommon):
    """Tempest neutron trunk testcase implementation."""

    def configure(self, **kwargs):
        super(TempestNeutronTrunk, self).configure(**kwargs)
        rconfig = configparser.RawConfigParser()
        rconfig.read(self.conf_file)
        rconfig.set('network-feature-enabled', 'api_extensions', 'all')
        with open(self.conf_file, 'wb') as config_file:
            rconfig.write(config_file)
        self.backup_tempest_config(self.conf_file, self.res_dir)