
%define short_name 4Suite

Summary:	XML processing tools
Summary(pl):	Narzêdzia do przetwarzania XML
Name:		python-%{short_name}
Version:	0.11.1
Release:	1
License:	Custom
Group:		Development/Libraries
Source0:	ftp://ftp.fourthought.com/pub/%{short_name}/%{short_name}-%{version}.tar.gz
URL:		http://4suite.org/
BuildRequires:	python-devel >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	python-PyXML
Requires:	python-PyXML
%requires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%include /usr/lib/rpm/macros.python

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
Group:		Development/Libraries
%requires_eq	python
Requires:	%{name} = %{version}

%description examples
Examples of 4Suite.

%description examples -l pl
Przyk³ady u¿ycia 4Suite.

%prep
%setup -q -n %{short_name}-%{version}

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_examplesdir}/%{name}

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
cp -a demos $RPM_BUILD_ROOT/%{_examplesdir}/%{name}
cp -a profile $RPM_BUILD_ROOT/%{_examplesdir}/%{name}
cp -a test_suite $RPM_BUILD_ROOT/%{_examplesdir}/%{name}

gzip -9fn COPYRIGHT PKG-INFO README ReleaseNotes \
	docs/text/{COPYRIGHT,CREDITS,PACKAGES,README,ReleaseNotes,TODO} \
	docs/text/howto/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs

%{py_sitedir}/_xmlplus/*
%{py_sitedir}/Ft/
%attr(755,root,root) %{_bindir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
