#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : i3
Version  : 4.20.1
Release  : 20
URL      : https://github.com/i3/i3/archive/4.20.1/i3-4.20.1.tar.gz
Source0  : https://github.com/i3/i3/archive/4.20.1/i3-4.20.1.tar.gz
Summary  : A tiling window manager for X11
Group    : Development/Tools
License  : BSD-3-Clause
Requires: i3-bin = %{version}-%{release}
Requires: i3-data = %{version}-%{release}
Requires: i3-filemap = %{version}-%{release}
Requires: i3-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : buildreq-meson
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
Patch1: 0001-Stateless-i3-and-i3-config-wizard.patch
Patch2: include.patch

%description
i3 is a tiling window manager, completely written from scratch. The target
platforms are GNU/Linux and BSD operating systems, our code is Free and Open
Source Software (FOSS) under the BSD license. i3 is primarily targeted at
advanced users and developers.

%package bin
Summary: bin components for the i3 package.
Group: Binaries
Requires: i3-data = %{version}-%{release}
Requires: i3-license = %{version}-%{release}
Requires: i3-filemap = %{version}-%{release}

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
Requires: i3-bin = %{version}-%{release}
Requires: i3-data = %{version}-%{release}
Provides: i3-devel = %{version}-%{release}
Requires: i3 = %{version}-%{release}

%description dev
dev components for the i3 package.


%package doc
Summary: doc components for the i3 package.
Group: Documentation

%description doc
doc components for the i3 package.


%package filemap
Summary: filemap components for the i3 package.
Group: Default

%description filemap
filemap components for the i3 package.


%package license
Summary: license components for the i3 package.
Group: Default

%description license
license components for the i3 package.


%prep
%setup -q -n i3-4.20.1
cd %{_builddir}/i3-4.20.1
%patch1 -p1
%patch2 -p1
pushd ..
cp -a i3-4.20.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635952257
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain --sysconfdir=/usr/share/defaults/i3  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain --sysconfdir=/usr/share/defaults/i3  builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/i3
cp %{_builddir}/i3-4.20.1/LICENSE %{buildroot}/usr/share/package-licenses/i3/3884a0d877db89ec2bad44adcb129ee4878458e2
cp %{_builddir}/i3-4.20.1/debian/copyright %{buildroot}/usr/share/package-licenses/i3/8289e87adc66e6622c0801c873dd5793ca4bda0a
cp %{_builddir}/i3-4.20.1/i3bar/LICENSE %{buildroot}/usr/share/package-licenses/i3/af3376079066b36e94bd0b123e61c632cf5e4fe8
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
install -d -m 755 %{buildroot}/usr/share/xdg/i3
install -m 644 etc/config %{buildroot}/usr/share/xdg/i3/
install -m 644 etc/config.keycodes %{buildroot}/usr/share/xdg/i3/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/applications/i3.desktop
/usr/share/defaults/i3/i3/config
/usr/share/defaults/i3/i3/config.keycodes
/usr/share/xdg/i3/config
/usr/share/xdg/i3/config.keycodes
/usr/share/xsessions/i3-with-shmlog.desktop
/usr/share/xsessions/i3.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/i3/ipc.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/i3/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-i3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/i3/3884a0d877db89ec2bad44adcb129ee4878458e2
/usr/share/package-licenses/i3/8289e87adc66e6622c0801c873dd5793ca4bda0a
/usr/share/package-licenses/i3/af3376079066b36e94bd0b123e61c632cf5e4fe8
