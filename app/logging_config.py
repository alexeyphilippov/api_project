from config import Config

StreamHandler = 'logging.StreamHandler'
RotatingFileHandler = 'logging.handlers.RotatingFileHandler'

level = Config.LOG_LEVEL


loggingConfig = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'root': {
            'level': level,
            'handlers': ['console']
        },
        'audit': {
            'level': level,
            'propagate': False,
            'handlers': ['consoleAudit']
        },
        'checks': {
            'level': level,
            'propagate': False,
            'handlers': ['console']
        },
        'file_writer': {
            'level': level,
            'propagate': False,
            'handlers': ['console']
        },
        'authentication': {
            'level': level,
            'propagate': False,
            'handlers': ['console']
        },
        'scheduler': {
            'level': level,
            'propagate': False,
            'handlers': ['console']
        }
    },
    'handlers': {
        'console': {
            'class': StreamHandler,
            'level': level,
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'consoleAudit': {
            'class': StreamHandler,
            'level': level,
            'formatter': 'audit',
            'stream': 'ext://sys.stdout'
        },
    },
    'formatters': {
        'default': {
            'format': '[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s'
        },
        'audit': {
            'format': '[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(request_time)s | %(ip)s | %(user)s '
                      '| %(method)s | %(url)s | %(status)s | %(message)s',
        },
    }
}
