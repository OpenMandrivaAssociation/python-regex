%define oname   regex
%define ver 2019.3.12

Name:           python-%{oname}
Version:        2019.03.12
Release:        1
Summary:        Alternative regular expression module, to replace re

Source0:        https://files.pythonhosted.org/packages/a3/d5/7dca7f9a629f8cfb06232bc23b4ce1bb5daa2115cbeee7f6868c57f2beb3/regex-%{version}.tar.gz
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
%{py_platsitedir}/regex-%{ver}-*.egg-info
%{py_platsitedir}/regex*

%files -n python2-regex
%doc python2/README
%{py2_platsitedir}/regex-%{ver}-*.egg-info
%{py2_platsitedir}/regex*
