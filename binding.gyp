{
    "includes": [ "deps/common.gypi" ],
    "targets": [
        {
          "target_name": "node_libtorrent",
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
              '<@(default_defines)'
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
          ]
        }
    ]
}
