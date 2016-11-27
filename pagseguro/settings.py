# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

PAGSEGURO_EMAIL = getattr(settings, 'PAGSEGURO_EMAIL', '')
PAGSEGURO_TOKEN = getattr(settings, 'PAGSEGURO_TOKEN', '')
PAGSEGURO_SANDBOX = getattr(settings, 'PAGSEGURO_SANDBOX', True)
PAGSEGURO_LOG_IN_MODEL = getattr(settings, 'PAGSEGURO_LOG_IN_MODEL', True)

if PAGSEGURO_SANDBOX:
    CHECKOUT_URL = 'https://ws.sandbox.pagseguro.uol.com.br/v2/checkout'
    PAYMENT_URL = 'https://sandbox.pagseguro.uol.com.br/v2/checkout/payment.html'
    NOTIFICATION_URL = 'https://ws.sandbox.pagseguro.uol.com.br/v2/transactions/notifications'
    TRANSACTION_URL = 'https://ws.sandbox.pagseguro.uol.com.br/v2/transactions'
    SESSION_URL = 'https://ws.sandbox.pagseguro.uol.com.br/v2/sessions/'
    PRE_APPROVALS_URL = 'https://ws.sandbox.pagseguro.uol.com.br/v2/pre-approvals/request'
    PRE_APPROVALS_REDIRECT_URL = 'https://ws.sandbox.pagseguro.uol.com.br/v2/pre-approvals/request.html'
else:
    CHECKOUT_URL = 'https://ws.pagseguro.uol.com.br/v2/checkout'
    PAYMENT_URL = 'https://pagseguro.uol.com.br/v2/checkout/payment.html'
    NOTIFICATION_URL = 'https://ws.pagseguro.uol.com.br/v2/transactions/notifications'
    TRANSACTION_URL = 'https://ws.pagseguro.uol.com.br/v2/transactions'
    SESSION_URL = 'https://ws.pagseguro.uol.com.br/v2/sessions/'
    PRE_APPROVALS_URL = 'https://ws.pagseguro.uol.com.br/v2/pre-approvals/request'
    PRE_APPROVALS_REDIRECT_URL = 'https://ws.pagseguro.uol.com.br/v2/pre-approvals/request.html'

TRANSACTION_STATUS = {
    '1': 'aguardando',
    '2': 'em_analise',
    '3': 'pago',
    '4': 'disponivel',
    '5': 'em_disputa',
    '6': 'devolvido',
    '7': 'cancelado'
}
