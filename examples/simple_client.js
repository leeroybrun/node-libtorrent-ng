var lt, main, s, th, ti;

try {
	lt = require("../build/Debug/node_libtorrent");
} catch(e) {
	lt = require("../build/Release/node_libtorrent");
}

var torrentFile = process.argv[2];
var savePath = process.argv[3];

s = new lt.session();

s.listen_on([6881, 6889]);

s.start_dht();
s.start_lsd();
//s.start_upnp();
//s.start_natpmp();

s.add_extension('ut_metadata');
s.add_extension('ut_pex');
s.add_extension('lt_trackers');
s.add_extension('metadata_transfer');
s.add_extension('smart_ban');

ti = new lt.torrent_info(torrentFile);

th = s.add_torrent({
  ti: ti,
  save_path: savePath
});

th.force_recheck();
th.force_reannounce();

main = function() {
  var st;
  st = th.status();

  console.log(s);
  console.log(s.get_torrents());
  console.log(st);
  console.log('error : '+ st.error);
  console.log('paused ? '+ st.paused);
  console.log('seeders -> '+ st.list_seeds);
  console.log("" + (st.progress * 100) + " complete (down: " + (st.download_rate / 1000) + " kb/s | up: " + (st.upload_rate / 1000) + " kB/s | peers: " + st.num_peers + ")");
  return setTimeout(main, 2500);
};

main();
