from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class SemanticVersioningValidator(RegexValidator):
    # Semantiv Versioning regex
    # Plucked from https://github.com/semver/semver/issues/232
    regex = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*)?(\+[0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*)?$'
    message = 'Enter a valid (semantic) version'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
