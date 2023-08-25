# region			  -----Supporting Variables-----
gettext = lambda s: s
# endregion

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    (LANGUAGE_CODE, gettext(LANGUAGE_CODE)),
)

LANGUAGE_CODES = [language[0] for language in LANGUAGES]
