# This file is part asset_internetdomain module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import asset

def register():
    Pool.register(
        asset.Asset,
        asset.AssetInternetdomainLine,
        module='asset_internetdomain', type_='model')
