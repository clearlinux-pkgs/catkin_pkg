#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : catkin_pkg
Version  : 0.2.10
Release  : 7
URL      : http://pypi.debian.net/catkin_pkg/catkin_pkg-0.2.10.tar.gz
Source0  : http://pypi.debian.net/catkin_pkg/catkin_pkg-0.2.10.tar.gz
Summary  : catkin package library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: catkin_pkg-bin
Requires: catkin_pkg-legacypython
Requires: catkin_pkg-python3
Requires: catkin_pkg-python
Requires: argparse
Requires: docutils
Requires: python-dateutil
BuildRequires : argparse
BuildRequires : docutils
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dateutil
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package bin
Summary: bin components for the catkin_pkg package.
Group: Binaries

%description bin
bin components for the catkin_pkg package.


%package legacypython
Summary: legacypython components for the catkin_pkg package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the catkin_pkg package.


%package python
Summary: python components for the catkin_pkg package.
Group: Default
Requires: catkin_pkg-legacypython
Requires: catkin_pkg-python3

%description python
python components for the catkin_pkg package.


%package python3
Summary: python3 components for the catkin_pkg package.
Group: Default
Requires: python3-core

%description python3
python3 components for the catkin_pkg package.


%prep
%setup -q -n catkin_pkg-0.2.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511380652
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1511380652
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/catkin_create_pkg
/usr/bin/catkin_find_pkg
/usr/bin/catkin_generate_changelog
/usr/bin/catkin_tag_changelog
/usr/bin/catkin_test_changelog

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
