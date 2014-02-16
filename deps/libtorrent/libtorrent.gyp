# Really messy and big file, can be good to seperate in other files for boost and libtorrent
{
  "includes": [ "../common.gypi" ],
  "targets": [
    {
      "target_name": "libtorrent",
      'product_prefix': 'lib',
      'type': 'static_library',
      "sources": [
        # Libtorrent sources
        "src/alert.cpp",
        "src/allocator.cpp",
        "src/asio.cpp",
        #"src/asio_ssl.cpp",
        #"src/assert.cpp",
        "src/bandwidth_limit.cpp",
        "src/bandwidth_manager.cpp",
        "src/bandwidth_queue_entry.cpp",
        "src/bloom_filter.cpp",
        "src/broadcast_socket.cpp",
        "src/bt_peer_connection.cpp",
        "src/chained_buffer.cpp",
        "src/connection_queue.cpp",
        "src/ConvertUTF.cpp",
        "src/create_torrent.cpp",
        "src/disk_buffer_holder.cpp",
        "src/disk_buffer_pool.cpp",
        "src/disk_io_thread.cpp",
        "src/entry.cpp",
        "src/enum_net.cpp",
        "src/error_code.cpp",
        "src/escape_string.cpp",
        "src/file.cpp",
        "src/file_pool.cpp",
        "src/file_storage.cpp",
        "src/gzip.cpp",
        "src/http_connection.cpp",
        "src/http_parser.cpp",
        "src/http_seed_connection.cpp",
        "src/http_stream.cpp",
        "src/http_tracker_connection.cpp",
        "src/i2p_stream.cpp",
        "src/identify_client.cpp",
        "src/instantiate_connection.cpp",
        "src/ip_filter.cpp",
        "src/kademlia/dht_tracker.cpp",
        "src/kademlia/find_data.cpp",
        "src/kademlia/node.cpp",
        "src/kademlia/node_id.cpp",
        "src/kademlia/refresh.cpp",
        "src/kademlia/routing_table.cpp",
        "src/kademlia/rpc_manager.cpp",
        "src/kademlia/traversal_algorithm.cpp",
        "src/lazy_bdecode.cpp",
        "src/logger.cpp",
        "src/lsd.cpp",
        "src/lt_trackers.cpp",
        "src/magnet_uri.cpp",
        "src/metadata_transfer.cpp",
        "src/natpmp.cpp",
        "src/packet_buffer.cpp",
        "src/parse_url.cpp",
        "src/pe_crypto.cpp",
        "src/peer_connection.cpp",
        "src/piece_picker.cpp",
        "src/policy.cpp",
        "src/puff.cpp",
        "src/random.cpp",
        "src/rsa.cpp",
        "src/rss.cpp",
        "src/session.cpp",
        "src/session_impl.cpp",
        "src/settings.cpp",
        "src/sha1.cpp",
        "src/smart_ban.cpp",
        "src/socket_io.cpp",
        "src/socket_type.cpp",
        "src/socks5_stream.cpp",
        "src/stat.cpp",
        "src/storage.cpp",
        "src/string_util.cpp",
        "src/thread.cpp",
        "src/time.cpp",
        "src/timestamp_history.cpp",
        "src/torrent.cpp",
        "src/torrent_handle.cpp",
        "src/torrent_info.cpp",
        "src/tracker_manager.cpp",
        "src/udp_socket.cpp",
        "src/udp_tracker_connection.cpp",
        "src/upnp.cpp",
        "src/ut_metadata.cpp",
        "src/ut_pex.cpp",
        "src/utf8.cpp",
        "src/utp_socket_manager.cpp",
        "src/utp_stream.cpp",
        "src/web_connection_base.cpp",
        "src/web_peer_connection.cpp",

        # Tommath
        "src/mpi.c"
      ],
      'include_dirs': [
        './',
        './include/',
        './include/libtorrent/'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          './',
          './include/',
          './include/libtorrent/'
        ],
      },
      'xcode_settings': {
      "OTHER_CFLAGS": [
        '-fPIC',
        '-Wno-parentheses-equality',
        '-Wno-unused-value',
        '-Wno-unused-private-field',
        '-Wno-sign-compare',
        '-ftemplate-depth-128',
        '-O0',
        '-fno-inline',
        '-g',
        '-gdwarf-2',
        '-fexceptions',
        '-ftrapv'
      ],
      'OTHER_CPLUSPLUSFLAGS':[
        '-fPIC',
        '-Wno-parentheses-equality',
        '-Wno-unused-value',
        '-Wno-unused-private-field',
        '-Wno-sign-compare',
        '-ftemplate-depth-128',
        '-O0',
        '-fno-inline',
        '-g',
        '-gdwarf-2',
        '-fexceptions',
        '-ftrapv'
      ],
      'GCC_ENABLE_CPP_RTTI': 'YES',
      'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
    },
    'defines': [
        '_LIB'
      ],
      'dependencies': [
        '../boost/boost.gyp:boost_atomic',
        '../boost/boost.gyp:boost_date_time',
        '../boost/boost.gyp:boost_exception',
        '../boost/boost.gyp:boost_smart_ptr',
        '../boost/boost.gyp:boost_system',
        '../boost/boost.gyp:boost_thread'
      ],
      "conditions": [
         ["OS == 'win'", {
            'defines': [
              #TORRENT_DISABLE_ENCRYPTION ?
            ]
          }],
         ["OS == 'mac'", {
            
          }],
          ["OS=='linux'", {  
          }]
      ]
    }
  ]
}
