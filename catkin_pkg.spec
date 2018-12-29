#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : catkin_pkg
Version  : 0.4.9
Release  : 24
URL      : https://files.pythonhosted.org/packages/bb/d3/8ac1edf6c039124079b362a992175880d043d01d8995013c40e256a45046/catkin_pkg-0.4.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/bb/d3/8ac1edf6c039124079b362a992175880d043d01d8995013c40e256a45046/catkin_pkg-0.4.9.tar.gz
Summary  : catkin package library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: catkin_pkg-bin = %{version}-%{release}
Requires: catkin_pkg-python = %{version}-%{release}
Requires: catkin_pkg-python3 = %{version}-%{release}
Requires: docutils
Requires: pyparsing
Requires: python-dateutil
BuildRequires : buildreq-distutils3
BuildRequires : docutils
BuildRequires : pyparsing
BuildRequires : python-dateutil

%description
catkin_pkg
----------
Standalone Python library for the `Catkin package system <http://ros.org/wiki/catkin>`_.

%package bin
Summary: bin components for the catkin_pkg package.
Group: Binaries

%description bin
bin components for the catkin_pkg package.


%package python
Summary: python components for the catkin_pkg package.
Group: Default
Requires: catkin_pkg-python3 = %{version}-%{release}

%description python
python components for the catkin_pkg package.


%package python3
Summary: python3 components for the catkin_pkg package.
Group: Default
Requires: python3-core

%description python3
python3 components for the catkin_pkg package.


%prep
%setup -q -n catkin_pkg-0.4.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539730948
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
/usr/bin/catkin_package_version
/usr/bin/catkin_prepare_release
/usr/bin/catkin_tag_changelog
/usr/bin/catkin_test_changelog

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
