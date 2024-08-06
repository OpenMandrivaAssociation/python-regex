%define module	regex

# python2 is not more supported bt regex
%bcond_with python2

Name:		python-%{module}
Version:	2024.7.24
Release:	1
Summary:	Alternative regular expression module, to replace re

#Source0:	https://files.pythonhosted.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/r/%{module}/%{module}-%{version}.tar.gz
License:	Python
Group:		Development/Python
Url:		https://bitbucket.org/mrabarnett/mrab-regex
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

%description
This regex implementation is backwards-compatible with
the standard 're' module, but offers additional
functionality.

%files
%doc python3/README.rst
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%if %{with python2}
%package -n python2-regex
Summary: %{summary}
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2dist(setuptools)

%description -n python2-regex
This regex implementation is backwards-compatible with
the standard 're' module, but offers additional
functionality.

%files -n python2-regex
%doc python2/README.rst
%{py2_platsitedir}/%{module}/
%{py2_platsitedir}/%{module}-%{version}-py%{python_version}.egg-info/
%endif

#----------------------------------------------------------------------------

%prep
%setup -qc 
mv %{module}-%{version} python2
cp -a python2 python3

%build
%if %{with python2}
pushd python2
%{__python2} setup.py build
popd
%endif

pushd python3
python3 setup.py build
popd

%install
%if %{with python2}
pushd python2
%{__python2} setup.py install --root=%{buildroot}
popd
%endif

pushd python3
%{__python} setup.py install --root=%{buildroot}
popd

