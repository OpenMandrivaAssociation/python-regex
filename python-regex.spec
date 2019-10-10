%define oname   regex

Name:           python-%{oname}
Version:	2019.08.19
Release:	1
Summary:        Alternative regular expression module, to replace re

Source0:	https://files.pythonhosted.org/packages/6f/a6/99eeb5904ab763db87af4bd71d9b1dfdd9792681240657a4c0a599c10a81/regex-2019.08.19.tar.gz
License:        Python
Group:          Development/Python
Url:            https://bitbucket.org/mrabarnett/mrab-regex
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools

%description
This regex implementation is backwards-compatible with
the standard 're' module, but offers additional
functionality.

%package -n python2-regex
Summary: %{summary}

BuildRequires: python2-devel

%description -n python2-regex
This regex implementation is backwards-compatible with
the standard 're' module, but offers additional
functionality.

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
%{py_platsitedir}/regex-*-*.egg-info
%{py_platsitedir}/regex*

%files -n python2-regex
%doc python2/README
%{py2_platsitedir}/regex-*-*.egg-info
%{py2_platsitedir}/regex*
