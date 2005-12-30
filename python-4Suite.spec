# TODO:
# - external expat

%define		short_name	4Suite
Summary:	XML processing tools
Summary(pl):	Narz�dzia do przetwarzania XML-a
Name:		python-%{short_name}
Version:	1.0
%define	_rc	b1
Release:	0.%{_rc}.1
License:	Custom
Group:		Development/Libraries
Source0:	ftp://ftp.4suite.org/pub/4Suite/%{short_name}-%{version}%{_rc}.tar.bz2
# Source0-md5:	d512d79dcbe08584d0b5ba4c9704a820
URL:		http://4suite.org/
BuildRequires:	python-devel >= 2.0
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	4Suite

%description
4Suite is a collection of Python tools for XML processing and object
database management. It provides support for XML parsing, several
transient and persistent DOM implementations, XPath expressions,
XPointer, XSLT transforms, XLink, RDF and ODMG object databases

%description -l pl
4Suite do zestaw narz�dzi Python'a do przetwarzania XML-a i
zarz�dzania baz� danych obiekt�w. Dostarcza wsparcie dla analizy
sk�adniowej XML-a, kilku implementacji DOM, wyra�e� XPath, XPointer,
przekszta�ce� XSLT, baz danych obiekt�w RDF i ODMG.

%package examples
Summary:	4Suite examples
Summary(pl):	Przyk�ady u�ycia 4Suite
Group:		Development/Libraries
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description examples
Examples of 4Suite.

%description examples -l pl
Przyk�ady u�ycia 4Suite.

%prep
%setup -q -n %{short_name}-%{version}%{_rc}

cat > config.cache <<EOF
[linux-%{_target_cpu}-%{py_ver}]
docdir = %{_datadir}/doc/%{name}-%{version}
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
%{_sysconfdir}/4ss.conf
%{_libdir}/4Suite
%{_datadir}/4Suite
%{_var}/lib/4Suite

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
