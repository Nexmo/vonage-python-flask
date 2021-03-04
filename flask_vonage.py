import vonage
from flask import current_app, _app_ctx_stack

class Vonage(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('VONAGE_API_KEY', None)
        app.config.setdefault('VONAGE_API_SECRET', None)
        app.config.setdefault('VONAGE_API_SIGNATURE_SECRET', None)
        app.config.setdefault('VONAGE_API_SIGNATURE_METHOD', None)
        app.config.setdefault('VONAGE_APPLICATION_ID', None)
        app.config.setdefault('VONAGE_PRIVATE_KEY', None)

    def build(self):
        client_params = {
            'key': 'VONAGE_API_KEY',
            'secret': 'VONAGE_API_SECRET',
            'signature_secret': 'VONAGE_API_SIGNATURE_SECRET',
            'signature_method': 'VONAGE_API_SIGNATURE_METHOD',
            'application_id': 'VONAGE_APPLICATION_ID',
            'private_key': 'VONAGE_PRIVATE_KEY',
        }

        auth = {}
        for key in client_params:
            if current_app.config[client_params[key]] is not None:
                auth[key] = current_app.config[client_params[key]]

        return vonage.Client(**auth)

    @property
    def client(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'vonage'):
                ctx.vonage = self.build()
            return ctx.vonage

    @property
    def sms(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'vonage_sms'):
                ctx.vonage_sms = vonage.Sms(self.client)
            return ctx.vonage_sms

    @property
    def voice(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'vonage_voice'):
                ctx.vonage_voice = vonage.Voice(self.client)
            return ctx.vonage_voice

    @property
    def verify(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'vonage_verify'):
                ctx.vonage_verify = vonage.Verify(self.client)
            return ctx.vonage_verify
