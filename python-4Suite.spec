%define short_name 4Suite
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)

Summary:	XML processing tools
Summary(pl):	Narz�dzia do przetwarzania XML
Name:		python-%{short_name}
Version:	0.11.1
Release:	1
License:	Custom
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Source0:	ftp://ftp.fourthought.com/pub/%{short_name}/%{short_name}-%{version}.tar.gz
URL:		http://4suite.org/
BuildRequires:	python >= 2.0
BuildRequires:	python-PyXML
Requires:	python-PyXML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
4Suite is a collection of Python tools for XML processing and object
database management. It provides support for XML parsing, several
transient and persistent DOM implementations, XPath expressions,
XPointer, XSLT transforms, XLink, RDF and ODMG object databases

%description -l pl
4Suite do zestaw narz�dzi Python'a do przetwarzania XML i zarz�dzania
baz� danych obiekt�w. Dostarcza wsparcie dla parsowania XML, kilku
implementacji DOM, wyra�e� XPath, XPointer, przekszta�ce� XSLT, baz
danych obiekt�w RDF i ODMG.

%package examples
Summary:	4Suite examples
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����

%description examples
Examples of 4Suite.

%description examples
Przyk�ady u�ycia 4Suite.

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

%{python_sitepkgsdir}/_xmlplus/*
%{python_sitepkgsdir}/Ft/
%attr(755,root,root) %{_bindir}/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
