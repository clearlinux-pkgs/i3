#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : i3
Version  : 4.15
Release  : 3
URL      : https://github.com/i3/i3/archive/4.15.tar.gz
Source0  : https://github.com/i3/i3/archive/4.15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: i3-bin
Requires: i3-data
BuildRequires : libev-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-cursor)
BuildRequires : pkgconfig(xcb-event)
BuildRequires : pkgconfig(xcb-icccm)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xcb-randr)
BuildRequires : pkgconfig(xcb-util)
BuildRequires : pkgconfig(xcb-xinerama)
BuildRequires : pkgconfig(xcb-xkb)
BuildRequires : pkgconfig(xcb-xrm)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xkbcommon-x11)
BuildRequires : pkgconfig(yajl)

%description
Introduction
============
libi3 is an *INTERNAL* library which contains functions that i3 and related
tools (i3-msg, i3-input, i3-nagbar, i3-config-wizard, i3bar) use.

%package bin
Summary: bin components for the i3 package.
Group: Binaries
Requires: i3-data

%description bin
bin components for the i3 package.


%package data
Summary: data components for the i3 package.
Group: Data

%description data
data components for the i3 package.


%package dev
Summary: dev components for the i3 package.
Group: Development
Requires: i3-bin
Requires: i3-data
Provides: i3-devel

%description dev
dev components for the i3 package.


%prep
%setup -q -n i3-4.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525295887
%reconfigure --disable-static
make  %{?_smp_mflags} || ( sed -i 's/TEST_LOGS:/TEST_LOGS):/' Makefile && make %{?_smp_mflags} CPPFLAGS="-I/usr/include/libev/" )

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1525295887
rm -rf %{buildroot}
%make_install
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/xdg/i3
install -m 644 etc/config %{buildroot}/usr/share/xdg/i3/
install -m 644 etc/config.keycodes %{buildroot}/usr/share/xdg/i3/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/i3
/usr/bin/i3-config-wizard
/usr/bin/i3-dmenu-desktop
/usr/bin/i3-dump-log
/usr/bin/i3-input
/usr/bin/i3-migrate-config-to-v4
/usr/bin/i3-msg
/usr/bin/i3-nagbar
/usr/bin/i3-save-tree
/usr/bin/i3-sensible-editor
/usr/bin/i3-sensible-pager
/usr/bin/i3-sensible-terminal
/usr/bin/i3-with-shmlog
/usr/bin/i3bar

%files data
%defattr(-,root,root,-)
/usr/share/applications/i3.desktop
/usr/share/xdg/i3/config
/usr/share/xdg/i3/config.keycodes
/usr/share/xsessions/i3-with-shmlog.desktop
/usr/share/xsessions/i3.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/i3/ipc.h
