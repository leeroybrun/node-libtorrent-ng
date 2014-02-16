{
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
        '-fPIC',
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
      'OTHER_CPLUSPLUSFLAGS':[
        '-fPIC',
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
      'GCC_ENABLE_CPP_RTTI': 'YES',
      'GCC_ENABLE_CPP_EXCEPTIONS': 'NO'
    },
    'defines': [
      'PIC',
      '_LARGEFILE_SOURCE',
      'BOOST_ALL_NO_LIB',
      'BOOST_ASIO_ENABLE_CANCELIO',
      'BOOST_ASIO_HASH_MAP_BUCKETS=1021',
      'BOOST_ASIO_HEADER_ONLY=1',
      #'BOOST_ASIO_SEPARATE_COMPILATION',
      'BOOST_EXCEPTION_DISABLE',
      'BOOST_ATOMIC_STATIC_LINK=1',
      'BOOST_DATE_TIME_STATIC_LINK',
      'BOOST_SYSTEM_STATIC_LINK=1',
      'BOOST_THREAD_STATIC_LINK=1',
      'BOOST_THREAD_BUILD_LIB=1',
      'BOOST_THREAD_DONT_USE_CHRONO',
      'TORRENT_DEBUG',
      'TORRENT_DISABLE_GEO_IP',
      'TORRENT_USE_I2P=1',
      'TORRENT_USE_TOMMATH',
      'UNICODE',
      '_FILE_OFFSET_BITS=64',
      '_UNICODE',
      '_WIN32_WINNT=0x0500',
    ],
    'include_dirs': [
      '/usr/local/include',
      '/usr/sfw/include'
    ],
    "cflags": [
      '-fPIC',
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
    "cflags_cc!": [
      "-fno-exceptions"
    ],
    'cflags!': [ '-fno-exceptions' ],
    'target_conditions': [
      ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          },
      }],
      [ 'OS=="win"', {
        'conditions': [
          # "openssl_root" is the directory on Windows of the OpenSSL files
          # http://slproweb.com/products/Win32OpenSSL.html
          ['target_arch=="x64"', {
            'variables': {
              'openssl_root%': 'C:/OpenSSL-Win64'
            },
          }, {
            'variables': {
              'openssl_root%': 'C:/OpenSSL-Win32'
            },
          }],
        ],
        'defines': [
          'uint=unsigned int',
        ],
        'libraries': [ 
          '-l<(openssl_root)/lib/libeay32.lib',
        ],
        'include_dirs': [
          '<(openssl_root)/include',
        ],
      }, { # OS!="win"
        'include_dirs': [
          # use node's bundled openssl headers on Unix platforms
          '<(node_root_dir)/deps/openssl/openssl/include'
        ],
        "conditions" : [
          ["target_arch=='ia32'", {
            "include_dirs": [ "<(node_root_dir)/deps/openssl/config/piii" ]
          }],
          ["target_arch=='x64'", {
            "include_dirs": [ "<(node_root_dir)/deps/openssl/config/k8" ]
          }],
          ["target_arch=='arm'", {
            "include_dirs": [ "<(node_root_dir)/deps/openssl/config/arm" ]
          }]
        ],
      }],
    ],
    'conditions': [
      ['clang==1', {
        'cflags': [
          '-Wno-parentheses-equality',
          '-Wno-unused-value',
          '-Wno-unused-private-field',
          '-Wno-sign-compare'
        ]
      }, { # Not clang. Disable all warnings.
        'cflags': [
          '-w',
        ],
      }]
    ],
  }
}