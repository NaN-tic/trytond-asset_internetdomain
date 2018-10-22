#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['Asset', 'AssetInternetdomainLine']

_STATES = {
    'invisible': Eval('type') != 'internetdomain',
    }
_DEPENDS = ['type']


class Asset(metaclass=PoolMeta):
    __metaclass__ = PoolMeta
    __name__ = 'asset'
    internetdomain_registration_date = fields.Date('Registration Date',
        states=_STATES, depends=_DEPENDS)
    internetdomain_dns1 = fields.Char('DNS Primary',
        states=_STATES, depends=_DEPENDS)
    internetdomain_dns2 = fields.Char('DNS Secundary',
        states=_STATES, depends=_DEPENDS)
    internetdomain_dns3 = fields.Char('DNS Secundary (2)',
        states=_STATES, depends=_DEPENDS)
    internetdomain_dns4 = fields.Char('DNS Secundary (3)',
        states=_STATES, depends=_DEPENDS)
    internetdomain_comment = fields.Text('Comment',
        states=_STATES, depends=_DEPENDS)
    internetdomain_lines = fields.One2Many('asset.internetdomain.line', 'asset',
        'Lines', states=_STATES, depends=_DEPENDS)

    @classmethod
    def __setup__(cls):
        super(Asset, cls).__setup__()
        elevator = ('internetdomain', 'Internet Domain')
        if not elevator in cls.type.selection:
            cls.type.selection.append(elevator)


class AssetInternetdomainLine(ModelSQL, ModelView):
    'Asset Internet Domain Line'
    __name__ = 'asset.internetdomain.line'
    asset = fields.Many2One('asset', 'Domain',
        ondelete='CASCADE', select=True, required=True)
    date_renewal = fields.Date('Date Renewal', required=True)
    date_expire = fields.Date('Date Expire', required=True)
    registrator = fields.Many2One('party.party', 'Registrator', required=True)
    comment = fields.Text('Comment')

    @classmethod
    def __setup__(cls):
        super(AssetInternetdomainLine, cls).__setup__()
        cls._order = [
            ('date_renewal', 'DESC'),
            ('id', 'DESC'),
            ]
