#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : catkin_pkg
Version  : 0.2.10
Release  : 2
URL      : http://pypi.debian.net/catkin_pkg/catkin_pkg-0.2.10.tar.gz
Source0  : http://pypi.debian.net/catkin_pkg/catkin_pkg-0.2.10.tar.gz
Summary  : catkin package library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: catkin_pkg-bin
Requires: catkin_pkg-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
No detailed description available

%package bin
Summary: bin components for the catkin_pkg package.
Group: Binaries

%description bin
bin components for the catkin_pkg package.


%package python
Summary: python components for the catkin_pkg package.
Group: Default

%description python
python components for the catkin_pkg package.


%prep
%setup -q -n catkin_pkg-0.2.10

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/catkin_create_pkg
/usr/bin/catkin_find_pkg
/usr/bin/catkin_generate_changelog
/usr/bin/catkin_tag_changelog
/usr/bin/catkin_test_changelog

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
