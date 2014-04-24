# -*- coding: utf-8 -*-

#
#
#  Copyright 2014 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#

"""
aminator.plugins.volume.docker
=============================
docker volume allocator
"""
import logging

from aminator.plugins.volume.base import BaseVolumePlugin

__all__ = ('DockerVolumePlugin',)
log = logging.getLogger(__name__)


class DockerVolumePlugin(BaseVolumePlugin):
    _name = 'docker'

    def __enter__(self):
        container = self._config.context.cloud["container"]
        # FIXME this path should be configurable
        mountpoint = "/var/lib/docker/containers/{}/root".format(container)
        self._config.context.volume["mountpoint"] = mountpoint
        return mountpoint
