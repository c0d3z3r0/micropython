import gc

gc.threshold((gc.mem_free() + gc.mem_alloc()) // 4)
import uos
from flashbdev import bdev

if bdev:
    try:
        uos.mount(bdev, "/")
    except:
        import inisetup

        inisetup.setup()

# Import config
from config import config

# Debug
import esp
if config('debug'):
    esp.osdebug(0)
else:
    esp.osdebug(None)

gc.collect()
