# node-libtorrent-rb

node-libtorrent-rb is a fork of [node-libtorrent](https://github.com/fanatid/node-libtorrent) and provides native bindings to [libtorrent rastebar](http://www.rasterbar.com/products/libtorrent/) as a [Node.js addon](http://nodejs.org/docs/latest/api/addons.html).

There is a lot of forks out there. My goal here was to be able to easily use this module everywhere (Mac, Linux *and* Windows).

Libtorrent and it's dependencies (Boost) are bundled and compiled with node-gyp. We then use node-pre-gyp to easily install the module from precompiled .node packages.

If a precompiled package is not available for the user's config, we try to compile the bindings, libtorrent and Boost with node-gyp.

# Getting started
Execute in command line:
```
$ npm install libtorrent-rb
```
or copy repository and build bindings manually
```
$ git clone git://github.com/leeroybrun/node-libtorrent-rb.git
$ cd node-libtorrent-rb
$ npm install -g node-gyp
$ node-gyp configure
$ node-gyp build
```

# TODO
- Configure node-pre-gyp & add to package.json
- Clean tools/bcp_helper
- Update libtorrent to latest version
- Add OpenSSL optional support
- Package deps in a compressed folder (example: https://github.com/mapbox/node-sqlite3/tree/master/deps)
- Use Travis-CI ?
- Add options to node-gyp building