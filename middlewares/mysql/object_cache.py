# Simple object caching engine

import md5
import pickle
import time
import os

class object_cache:

  _ttl = 10
  _filename = None
  _cache_folder = './tmp/cache/'
  _content = None
  
  def __init__(self, TTL = _ttl):
    self._ttl = TTL

  def setTTL(self, TTL):
    self._ttl = TTL
    return

  def setCacheFolder(self, folder):
    self._cache_folder = folder
    return
    
  def read(self, name, id = ''):
    self._filename = self.cacheFileName(name, id)
    if os.path.isfile(self._filename):
      if os.stat(self._filename).st_mtime > (time.time() - self._ttl):
        with open(self._filename,'r') as f:
          p = f.read()
        self._content = pickle.loads(p)
        return self._content
      else:
        return False
    else:
      return False
    return

  def content(self):
    return self._content
    
  def write(self, object):
    p = pickle.dumps(object)
    with open(self._filename,'w') as cachefile:
      cachefile.write(p)
    return
  
  def cacheFileName(self, name, id):
    self._filename = self._cache_folder + name.replace('-','_').replace(' ','_') + '_' + str(md5.new(id).hexdigest()) + '.cache'
    return self._filename
    
  def __repr__(self):
    return '<objectCache %s>' % self._filename