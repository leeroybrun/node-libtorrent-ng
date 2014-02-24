{
    "includes": [ "deps/common.gypi" ],
    "targets": [
        # CLIENT_TEST
        {
            "target_name": "libtorrent_client_test",
            'type': 'executable',
            "sources": [
                'deps/libtorrent/examples/client_test.cpp'
            ],
            'include_dirs': [
                'deps/boost/inc-examples',
                'deps/boost/inc-examples/boost',
            ],
            'dependencies': [
                'deps/libtorrent/libtorrent.gyp:libtorrent',
                'deps/boost/boost.gyp:boost_atomic',
                'deps/boost/boost.gyp:boost_date_time',
                'deps/boost/boost.gyp:boost_exception',
                'deps/boost/boost.gyp:boost_smart_ptr',
                'deps/boost/boost.gyp:boost_system',
                'deps/boost/boost.gyp:boost_thread'
            ]
        },

        # CONNECTION_TESTER
        {
            "target_name": "libtorrent_connection_tester",
            'type': 'executable',
            "sources": [
                'deps/libtorrent/examples/connection_tester.cpp'
            ],
            'include_dirs': [
                'deps/boost/inc-examples',
                'deps/boost/inc-examples/boost',
            ],
            'dependencies': [
                'deps/libtorrent/libtorrent.gyp:libtorrent',
                'deps/boost/boost.gyp:boost_atomic',
                'deps/boost/boost.gyp:boost_date_time',
                'deps/boost/boost.gyp:boost_exception',
                'deps/boost/boost.gyp:boost_smart_ptr',
                'deps/boost/boost.gyp:boost_system',
                'deps/boost/boost.gyp:boost_thread'
            ]
        },

        # SIMPLE_CLIENT
        {
            "target_name": "libtorrent_simple_client",
            'type': 'executable',
            "sources": [
                'deps/libtorrent/examples/simple_client.cpp'
            ],
            'include_dirs': [
                'deps/boost/inc-examples',
                'deps/boost/inc-examples/boost',
            ],
            'dependencies': [
                'deps/libtorrent/libtorrent.gyp:libtorrent',
                'deps/boost/boost.gyp:boost_atomic',
                'deps/boost/boost.gyp:boost_date_time',
                'deps/boost/boost.gyp:boost_exception',
                'deps/boost/boost.gyp:boost_smart_ptr',
                'deps/boost/boost.gyp:boost_system',
                'deps/boost/boost.gyp:boost_thread'
            ]
        }
    ]
}