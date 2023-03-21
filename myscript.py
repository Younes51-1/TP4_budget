import os

BAD_HASH            = 'c1a4be04b972b6c17db242fc37752ad517c29402'
GOOD_HASH           = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'
BISECT_START_CMD    = 'git bisect start'
BISECT_RUN_CMD      = 'git bisect run python manage.py test'
BISECT_RESET_CMD    = 'git bisect reset'

os.system(f'{BISECT_START_CMD} {BAD_HASH} {GOOD_HASH}')
os.system(BISECT_RUN_CMD)
os.system(BISECT_RESET_CMD)