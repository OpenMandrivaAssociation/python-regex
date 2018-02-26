%define oname   regex
%define ver 2018.2.21

Name:           python-%{oname}
Version:        2018.02.21
Release:        1
Summary:        Alternative regular expression module, to replace re

Source0:        http://pypi.python.org/packages/source/p/regex/regex-%{version}.tar.gz
License:        Python
Group:          Development/Python
Url:            https://bitbucket.org/mrabarnett/mrab-regex
BuildRequires:  python2-devel
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools

%description
This regex implementation is backwards-compatible with the standard 're' module,
but offers additional functionality.

%package -n python2-regex
Summary: %{summary}

BuildRequires: python2-devel

%prep
%setup -qc 
mv %{oname}-%{version} python2
cp -a python2 python3

%build
pushd python2
%{__python2} setup.py build
popd

pushd python3
python3 setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python} setup.py install --root=%{buildroot}
popd

%files
%doc python3/README
%{py_platsitedir}/regex-%{ver}-*.egg-info
%{py_platsitedir}/_regex*
%{py_platsitedir}/test_regex.py
%{py_platsitedir}/regex.py

%files -n python2-regex
%doc python2/README
%{py2_platsitedir}/regex-%{ver}-*.egg-info
%{py2_platsitedir}/_regex*
%{py2_platsitedir}/test_regex.py
%{py2_platsitedir}/regex.py

