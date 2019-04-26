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

# Wifi setup
wificfg = config('wifi')
if wificfg.get('ssid'):
    import network, time
    sta_if = network.WLAN(network.STA_IF)
    try:
        sta_if.disconnect()
    except:
        pass
    sta_if.active(True)
    if wificfg.get('ip'):
        sta_if.ifconfig((
            wificfg.get('ip',   ''),
            wificfg.get('mask', ''),
            wificfg.get('gw', ''),
            wificfg.get('dns', ''),
        ))
    sta_if.connect(wificfg['ssid'], wificfg['psk'])
    for i in range(0,10):
        time.sleep(1)
        if sta_if.isconnected():
            break
    if not sta_if.isconnected():
        import machine
        machine.reset()

# Set NTP host and set up ntp update cronjob
ntpcfg = config('ntp')
if ntpcfg.get('enabled'):
    import ntptime, machine
    ntptime.host = ntpcfg.get('srv')
    _ntptimer = machine.Timer(-1)
    _ntptimer.init(period=ntpcfg.get('freq')*1000,
                   callback=lambda t: ntptime.settime())
    ntptime.settime()

# Start webrepl
wrcfg = config('webrepl')
if wrcfg.get('enabled'):
    import webrepl
    webrepl.start()

gc.collect()
