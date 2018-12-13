#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostContainerConan(base.BoostBaseConan):
    name = "boost_container_hash"
    url = "https://github.com/bincrafters/conan-boost_container_hash"
    lib_short_names = ["container_hash"]
    header_only_libs = ["container_hash"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_detail",
        "boost_integer",
        "boost_static_assert",
        "boost_type_traits"
    ]
