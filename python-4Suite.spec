# TODO:
# - external expat
%define		short_name	4Suite
%define	_rc	b3
Summary:	XML processing tools
Summary(pl.UTF-8):	Narzędzia przetwarzania XML-a
Name:		python-%{short_name}
Version:	1.0
Release:	0.%{_rc}.1
License:	Custom
Group:		Libraries/Python
Source0:	ftp://ftp.4suite.org/pub/4Suite/%{short_name}-XML-%{version}%{_rc}.tar.bz2
# Source0-md5:	9decb8b1032415ae155fe9a917fe8126
Patch0:		%{name}-root.patch
URL:		http://4suite.org/
BuildRequires:	pydoc
BuildRequires:	python-devel >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Obsoletes:	4Suite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
4Suite is a collection of Python tools for XML processing and object
database management. It provides support for XML parsing, several
transient and persistent DOM implementations, XPath expressions,
XPointer, XSLT transforms, XLink, RDF and ODMG object databases

%description -l pl.UTF-8
4Suite jest zestawem narzędzi języka Python do przetwarzania XML-a i
zarządzania bazą danych obiektów. Dostarcza wsparcie dla analizy
składniowej XML-a, kilku implementacji DOM, wyrażeń XPath, XPointer,
przekształceń XSLT, baz danych obiektów RDF i ODMG.

%package examples
Summary:	4Suite examples
Summary(pl.UTF-8):	Przykłady użycia 4Suite
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples of 4Suite.

%description examples -l pl.UTF-8
Przykłady użycia 4Suite.

%prep
%setup -q -n %{short_name}-%{version}%{_rc}
%patch0 -p1

python -c 'from distutils.util import get_platform; import sys; print "[%s-%.3s]" % (get_platform(), sys.version)' > config.cache
cat >> config.cache <<EOF
docdir = %{_datadir}/doc/%{name}-%{version}
mandir = %{_mandir}
pythonlibdir = %{py_sitedir}
sysconfdir = %{_sysconfdir}
exec_prefix =
libdir = %{_libdir}/%{short_name}
datadir = %{_datadir}/%{short_name}
localedir = %{_datadir}/locale
localstatedir = %{_var}/lib/%{short_name}
prefix =
bindir = %{_bindir}
EOF

%build
CFLAGS="%{rpmcflags}" python setup.py build
grep -q "/usr/local" config.cache && exit 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT
%py_comp $RPM_BUILD_ROOT
%py_postclean

cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -a profile $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -a test $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/xml
%{py_sitedir}/Ft
%attr(755,root,root) %{_bindir}/*
#%{_sysconfdir}/4ss.conf
%{_libdir}/4Suite
%{_datadir}/4Suite
#%{_var}/lib/4Suite

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
