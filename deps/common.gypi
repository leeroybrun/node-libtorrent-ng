{
    'variables': {
        # We define default cflags & defines so we can use them in targets, to force overhidding of existing settings
        'default_cflags': [
            #'-fPIC', # TODO: enable PIC ?
            '-Wno-parentheses-equality',
            '-Wno-unused-value',
            '-Wno-unused-private-field',
            '-Wno-sign-compare',
            '-ftemplate-depth-128',
            '-O0',
            '-fno-inline',
            '-Wall',
            '-g',
            '-gdwarf-2',
            '-fexceptions',
            '-ftrapv'
        ],
        'default_defines': [
            #'PIC',
            '_LARGEFILE_SOURCE',
            'UNICODE',
            '_UNICODE',
            '_FILE_OFFSET_BITS=64',
            'NDEBUG',

            # Boost defines
            'BOOST_ALL_NO_LIB=1',
            'BOOST_ATOMIC_STATIC_LINK=1',
            'BOOST_ATOMIC_SOURCE', # ?
            'BOOST_ASIO_ENABLE_CANCELIO',
            'BOOST_ASIO_HASH_MAP_BUCKETS=1021',
            'BOOST_ASIO_HEADER_ONLY=1',
            'BOOST_EXCEPTION_DISABLE',
            'BOOST_DATE_TIME_STATIC_LINK',
            'BOOST_SYSTEM_STATIC_LINK=1',
            'BOOST_THREAD_STATIC_LINK=1',
            'BOOST_THREAD_BUILD_LIB=1',
            'BOOST_THREAD_USE_LIB=1',
            'BOOST_THREAD_DONT_USE_CHRONO',
            'BOOST_FILESYSTEM_VERSION=2',

            # Libtorrent defines
            'TORRENT_PRODUCTION_ASSERTS=1',
            'TORRENT_RELEASE_ASSERTS=1',
            'TORRENT_DISABLE_INVARIANT_C',
            'TORRENT_DEBUG',
            'TORRENT_USE_I2P=1',

            # TODO: enable GeoIP ?
            'TORRENT_DISABLE_GEO_IP', 

            # TODO: enable optional OpenSSL support
            'TORRENT_USE_TOMMATH'
        ]
    },
    'target_defaults': {
        'default_configuration': 'Debug',
        'configurations': {
            'Debug': {
                'defines': [ 'DEBUG', '_DEBUG' ],
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'RuntimeLibrary': 1, # static debug
                    },
                },
            },
            'Release': {
                'defines': [ 'NDEBUG' ],
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'RuntimeLibrary': 0, # static release
                    },
                },
            }
        },
        'msvs_settings': {
            'VCLinkerTool': {
                'GenerateDebugInformation': 'true',
            },
        },
        'xcode_settings': {
            "OTHER_CFLAGS": [
                '<@(default_cflags)'
            ],
            'OTHER_CPLUSPLUSFLAGS':[
                '<@(default_cflags)'
            ],
            'GCC_ENABLE_CPP_RTTI': 'YES',
            'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
        },
        'defines': [
            '<@(default_defines)'
        ],
        'include_dirs': [
            '/usr/local/include',
            '/usr/sfw/include'
        ],
        "cflags": [
            '<@(default_cflags)'
        ],
        "cflags_cc!": ["-fno-exceptions"],
        'cflags!': [ '-fno-exceptions' ],
    }
}