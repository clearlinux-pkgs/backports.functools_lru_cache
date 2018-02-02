#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : backports.functools_lru_cache
Version  : 1.4
Release  : 5
URL      : http://pypi.debian.net/backports.functools_lru_cache/backports.functools_lru_cache-1.4.tar.gz
Source0  : http://pypi.debian.net/backports.functools_lru_cache/backports.functools_lru_cache-1.4.tar.gz
Summary  : backports.functools_lru_cache
Group    : Development/Tools
License  : MIT
Requires: backports.functools_lru_cache-legacypython
Requires: backports.functools_lru_cache-python3
Requires: backports.functools_lru_cache-python
Requires: Sphinx
Requires: pytest
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/backports.functools_lru_cache.svg
:target: https://pypi.org/project/backports.functools_lru_cache

%package legacypython
Summary: legacypython components for the backports.functools_lru_cache package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the backports.functools_lru_cache package.


%package python
Summary: python components for the backports.functools_lru_cache package.
Group: Default
Requires: backports.functools_lru_cache-legacypython
Requires: backports.functools_lru_cache-python3

%description python
python components for the backports.functools_lru_cache package.


%package python3
Summary: python3 components for the backports.functools_lru_cache package.
Group: Default
Requires: python3-core

%description python3
python3 components for the backports.functools_lru_cache package.


%prep
%setup -q -n backports.functools_lru_cache-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507572757
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507572757
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/backports/__init__.py
%exclude /usr/lib/python2.7/site-packages/backports/__init__.pyc
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.6/site-packages/backports/__init__.py
%exclude /usr/lib/python3.6/site-packages/backports/__pycache__/__init__.cpython-36.pyc
/usr/lib/python3*/*
