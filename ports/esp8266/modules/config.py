import json

defconfig = {
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

def config(name, value=None):
  try:
    with open('config.json', 'r') as c:
      conf = json.loads(c.read())
  except:
    conf = defconfig

  if value:
    conf.update({name: value})
    with open('config.json', 'w') as c:
      c.write(json.dumps(conf))
  else:
    return conf.get(name, None)
