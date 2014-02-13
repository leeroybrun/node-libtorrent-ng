# Really messy and big file, can be good to seperate in other files for boost and libtorrent
{
  "includes": [ "deps/common.gypi" ],
  "targets": [
    {
      "target_name": "node_libtorrent",
      'type': 'executable',
      "sources": [
        # Node.js libtorrent bindings sources
      	"src/module.cpp",

        "src/add_torrent_params.cpp",
        "src/alert.cpp",
        "src/bencode.cpp",
        "src/create_torrent.cpp",
        "src/entry.cpp",
        "src/file_storage.cpp",
        "src/fingerprint.cpp",
        "src/ip_filter.cpp",
        "src/peer_info.cpp",
        "src/rss.cpp",
        "src/session.cpp",
        "src/session_settings.cpp",
        "src/session_status.cpp",
        "src/storage.cpp",
        "src/torrent_handle.cpp",
        "src/torrent_info.cpp",
        "src/torrent_status.cpp",
      ],
      'defines': [
        '_LIB',
        'UNICODE',
        'BOOST_ASIO_HASH_MAP_BUCKETS=1021',
        'BOOST_FILESYSTEM_VERSION=2'
      ], 
      'dependencies': [
        'deps/libtorrent/libtorrent.gyp:libtorrent'
      ],
      'include_dirs': [
        'deps/libtorrent',
        'deps/libtorrent/include',
        'deps/libtorrent/include/libtorrent',
        'deps/boost',
        'deps/boost/boost'
      ],
      "ldflags": []
    }
  ]
}
