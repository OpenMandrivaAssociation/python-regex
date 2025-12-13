%define module	regex

Name:		python-%{module}
Version:	2025.11.3
Release:	1
Summary:	Alternative regular expression module, to replace re

#Source0:	https://files.pythonhosted.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/r/%{module}/%{module}-%{version}.tar.gz
License:	Python
Group:		Development/Python
Url:		https://bitbucket.org/mrabarnett/mrab-regex
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python

%description
This regex implementation is backwards-compatible with
the standard 're' module, but offers additional
functionality.

%files
%doc README.rst
%{py_platsitedir}/%{module}/
%{py_platsitedir}/%{module}-%{version}.dist-info
