var lt, main, s, th, ti;

try {
	lt = require("../build/Debug/node_libtorrent");
} catch(e) {
	lt = require("../build/Release/node_libtorrent");
}

s = new lt.session();

s.listen_on([6881, 6889]);

ti = new lt.torrent_info("./test.torrent");

th = s.add_torrent({
  ti: ti,
  save_path: "./test_torrent"
});

main = function() {
  var st;
  st = th.status();
  console.log("" + (st.progress * 100) + " complete (down: " + (st.download_rate / 1000) + " kb/s | up: " + (st.upload_rate / 1000) + " kB/s | peers: " + st.num_peers + ")");
  return setTimeout(main, 2500);
};

main();
