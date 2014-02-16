try {
	var lt = require('../build/Debug/node_libtorrent');
} catch(e) {
	var lt = require('../build/Release/node_libtorrent');
}

var s = new lt.session();