# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval, If, In
from trytond.pool import PoolMeta


class BankAccount(metaclass=PoolMeta):
    __name__ = 'bank.account'
    pyafipws_cbu = fields.Boolean('CBU del Emisor')
