%include /usr/lib/rpm/macros.python

%define		short_name	4Suite
%define		snap_y	2003
%define		snap_m	08
%define		snap_d	08
%define		snap	%{snap_y}%{snap_m}%{snap_d}
Summary:	XML processing tools
Summary(pl):	Narzêdzia do przetwarzania XML
Name:		python-%{short_name}
Version:	1.0
Release:	0.%{snap}.1
License:	Custom
Group:		Development/Libraries
#Source0:	ftp://ftp.fourthought.com/pub/%{short_name}/%{short_name}-%{version}.tar.gz
Source0:	ftp://ftp.4suite.org/pub/cvs-snapshots/%{snap_y}-%{snap_m}-%{snap_d}-%{short_name}.tar.gz
# Source0-md5:	bd8400a0468f18523b99078febbf9cd9
URL:		http://4suite.org/
BuildRequires:	python-devel >= 2.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	4Suite

%description
4Suite is a collection of Python tools for XML processing and object
database management. It provides support for XML parsing, several
transient and persistent DOM implementations, XPath expressions,
XPointer, XSLT transforms, XLink, RDF and ODMG object databases

%description -l pl
4Suite do zestaw narzêdzi Python'a do przetwarzania XML i zarz±dzania
baz± danych obiektów. Dostarcza wsparcie dla parsowania XML, kilku
implementacji DOM, wyra¿eñ XPath, XPointer, przekszta³ceñ XSLT, baz
danych obiektów RDF i ODMG.

%package examples
Summary:	4Suite examples
Summary(pl):	Przyk³ady u¿ycia 4Suite
Group:		Development/Libraries
%pyrequires_eq	python
Requires:	%{name} = %{version}

%description examples
Examples of 4Suite.

%description examples -l pl
Przyk³ady u¿ycia 4Suite.

%prep
%setup -q -n %{short_name}
cat > config.cache <<EOF
[linux-i686-2.3]
docdir = %{_datadir}/doc/%{name}-%{version}
pythonlibdir = %{py_sitedir}
sysconfdir = %{_sysconfdir}
exec_prefix =
libdir = %{_libdir}/%{short_name}
datadir = %{_datadir}/%{short_name}
localstatedir = %{_var}/lib/%{short_name}
prefix =
bindir = %{_bindir}
EOF

%build
CFLAGS="%{rpmcflags}" python setup.py build --with-docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

mv config.cache cc
cat cc | sed -e "s#/usr/local#/usr#" > config.cache

python setup.py install --root=$RPM_BUILD_ROOT --with-docs
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
