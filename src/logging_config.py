import logging as log

# Configuración para crear logs
log.basicConfig(level=log.INFO,
                filename='debug.log',
                filemode= 'w',
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                )