{
  "includes": [ "../common.gypi" ],
  'variables': { 'target_arch%': 'ia32' },
  'target_defaults': {
    'include_dirs': [
      './', 
      './boost/'     
    ],
    'direct_dependent_settings': {
      'variables': { 'target_arch%': 'ia32' },
      'include_dirs': [
        './', 
        './boost/'
      ],
    },
    'defines': [
      '_LIB'
    ],
    "conditions": [
      ["OS == 'win'", {
        'defines': [
        ]
      }],
      ["OS == 'mac'", {
        'xcode_settings': {
        }
      }],
      ["OS=='linux'", {  
        'defines': [
        ]
      }]
    ],
  },
  "targets": [
    {
      'target_name': 'boost_atomic',
      'product_prefix': 'lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'sources': [
        "libs/atomic/src/lockpool.cpp",
      ],
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
      
    },
    {
      'target_name': 'boost_date_time',
      'product_prefix': 'lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'sources': [
        "libs/date_time/src/gregorian/date_generators.cpp",
        "libs/date_time/src/gregorian/greg_month.cpp",
        "libs/date_time/src/gregorian/greg_weekday.cpp",
        "libs/date_time/src/gregorian/gregorian_types.cpp",
        "libs/date_time/src/posix_time/posix_time_types.cpp",
      ],
      "conditions": [
        ["OS == 'mac'", {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ],
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
    },
    {
      'target_name': 'boost_exception',
      'product_prefix': 'lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'sources': [
        "libs/exception/src/clone_current_exception_non_intrusive.cpp",
      ],
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
    },
    {
      'target_name': 'boost_smart_ptr',
      'product_prefix': 'lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'sources': [
        "libs/smart_ptr/src/sp_collector.cpp",
        "libs/smart_ptr/src/sp_debug_hooks.cpp",
      ],
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
    },
    {
      'target_name': 'boost_system',
      'product_prefix': 'lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'sources': [
        "libs/system/src/error_code.cpp",
      ],
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
    },
    {
      'target_name': 'boost_thread',
      'product_prefix': 'lib',
      'type': 'static_library',
      'hard_dependency': 1,
      'sources': [
        "libs/thread/build/has_atomic_flag_lockfree_test.cpp",
        "libs/thread/src/future.cpp",
        "libs/thread/src/tss_null.cpp"
      ],
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
      'dependencies': [
        'boost_date_time',
        'boost_system'
      ],
      "conditions": [
         ["OS == 'win'", {
            'sources': [
              "libs/thread/src/win32/thread.cpp",
              "libs/thread/src/win32/tss_dll.cpp",
              "libs/thread/src/win32/tss_pe.cpp",
            ],
            'defines': [
            ]
          }],
         ["OS == 'mac'", {
            'include_dirs': [
              "libs/thread/src/pthread/once.cpp",
              "libs/thread/src/pthread/once_atomic.cpp",
              "libs/thread/src/pthread/thread.cpp",
            ],
            'defines': [
            ],
            "libraries": [
              "-lpthread"
            ]
          }],
          ["OS=='linux'", {  
            'include_dirs': [
              "libs/thread/src/pthread/once.cpp",
              "libs/thread/src/pthread/once_atomic.cpp",
              "libs/thread/src/pthread/thread.cpp",
            ],
            'defines': [
            ],
            "libraries": [
              "-lpthread"
            ]
          }]
      ]
    }
  ]
}
