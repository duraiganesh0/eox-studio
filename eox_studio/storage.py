#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
eox-studio storages
"""
from eox_studio.edxapp_wrapper.storages import (
    get_edxapp_development_staticfiles_storage,
    get_edxapp_production_staticfiles_storage,
)

EdxappProductionStorage = get_edxapp_production_staticfiles_storage()  # pylint: disable=invalid-name
EdxappDevelopmentStorage = get_edxapp_development_staticfiles_storage()  # pylint: disable=invalid-name


class AbsoluteUrlAssetsMixin:
    """
    Mixin that overrides the url method on storages
    """
    def url(self, name):
        """
        Return url of the asset.
        If the asset name is an absolute url, just return the asset name
        """
        if name.startswith("https://") or name.startswith("http://"):
            return name

        return super(AbsoluteUrlAssetsMixin, self).url(name)


class ProductionStorage(AbsoluteUrlAssetsMixin, EdxappProductionStorage):
    """
    eox-studio production extended static files storage
    """


class DevelopmentStorage(AbsoluteUrlAssetsMixin, EdxappDevelopmentStorage):
    """
    eox-studio development extended static files storage
    """
