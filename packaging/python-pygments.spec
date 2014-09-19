Name:           python-pygments
Version:        1.1.1
Release:        0
Summary:        A syntax highlighting engine written in Python
Group:          Development/Libraries
License:        BSD-2-Clause
URL:            http://pygments.org/
Source0:        %{name}-%{version}.tar.gz
Source1001:     python-pygments.manifest

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-setuptools

BuildRequires:  fdupes

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
%if 0%{?suse_version}
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot} --record-rpm=INSTALLED_FILES  
%else
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --prefix=%{_prefix}
%endif
%fdupes %{buildroot}

%if 0%{?suse_version}
%files -f INSTALLED_FILES
%manifest %{name}.manifest
%else
%files
%manifest %{name}.manifest
%{python_sitelib}/*
%endif
# For noarch packages: sitelib
%{_bindir}/pygmentize
