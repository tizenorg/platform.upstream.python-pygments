%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-pygments
Version:        1.1.1
Release:        1
Summary:        A syntax highlighting engine written in Python

Group:          Development/Libraries
License:        BSD
URL:            http://pygments.org/
Source0:        %{name}-%{version}.tar.gz
Source1001: python-pygments.manifest 

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
Requires:       python-setuptools


%description
Pygments is a syntax highlighting engine written in Python. That means, it 
will take source code (or other markup) in a supported language and output 
a processed version (in different formats) containing syntax highlighting 
markup.


%prep
%setup -q


%build
cp %{SOURCE1001} .
%{__python} setup.py build
%{__sed} -i 's/\r//' LICENSE


%install

%{__python} setup.py install -O1 --skip-build --root %{buildroot} --prefix=%{_prefix}

%files
%manifest %{name}.manifest
%{python_sitelib}/*
# For noarch packages: sitelib
%{_bindir}/pygmentize


