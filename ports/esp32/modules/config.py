import json

_defconfig = {
  'debug': False,
  'wifi': {
    'ssid': '',
    'psk':  '',
    'ip':   '',
    'mask': '',
    'gw':   '',
    'dns':  '',
  },
  'webrepl': {
    'enabled':  False,
    'password': '',
  },
  'ntp': {
    'enabled': False,
    'srv':     '',
    'freq':    5*60,
  },
}

def _writeconfig(conf):
  with open('config.json', 'w') as c:
    c.write(json.dumps(conf))

def _readconfig():
  with open('config.json', 'r') as c:
    return json.loads(c.read())

def config(name, value=None):
  try:
    conf = _readconfig()
  except:
    try:
      from defconfig import defconfig
      conf = _defconfig.copy()
      conf.update(defconfig)
      _writeconfig(conf)
    except:
      conf = _defconfig.copy()

  if value is not None:
    conf.update({name: value})
    _writeconfig(conf)
  else:
    return conf.get(name, None)
