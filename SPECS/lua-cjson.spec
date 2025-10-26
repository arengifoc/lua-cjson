Name:           lua-cjson
Version:        2.1.0.10
Release:        1%{?dist}
Summary:        Lua CJSON module (precompiled)
License:        MIT
URL:            https://github.com/openresty/lua-cjson
BuildArch:      x86_64
Requires:       luajit >= 2.1.0

%description
Precompiled Lua CJSON shared library for LuaJIT.
Provides JSON encode/decode functions for Lua scripts and Fluent Bit Lua filters.

%install
mkdir -p %{buildroot}/usr/local/lib/lua/5.1
install -m 0755 %{_sourcedir}/cjson.so %{buildroot}/usr/local/lib/lua/5.1

%files
/usr/local/lib/lua/5.1/cjson.so

%changelog
- Initial build of precompiled lua-cjson module