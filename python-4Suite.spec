# TODO:
# - external expat
# - egg-info
# - -devel package
# - remove -root patch after full release
%define		short_name	4Suite
#
Summary:	XML processing tools
Summary(pl.UTF-8):	Narzędzia przetwarzania XML-a
Name:		python-%{short_name}
Version:	1.0.2
Release:	0.1
License:	Custom
Group:		Libraries/Python
Source0:	ftp://ftp.4suite.org/pub/4Suite/%{short_name}-XML-%{version}.tar.bz2
# Source0-md5:	b3e976a666899113d58f333518205968
URL:		http://4suite.org/
BuildRequires:	pydoc
BuildRequires:	python-devel >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
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

%package -n %{short_name}-tools
Summary:	4Suite tools
Summary(pl.UTF-8):	Narzędzia 4Suite
Group:		Applications
%pyrequires_eq	python
Requires:	%{name} = %{version}-%{release}

%description -n %{short_name}-tools
4Suite command-line tools:

   * 4xml: XML document parsing and reserialization.
   * 4xpath: XPath expression evaluation.
   * 4xslt: XSLT processing engine.
   * 4xupdate: XUpdate processing.

%description -n %{short_name}-tools -l pl.UTF-8
Narzędzia CLI 4Suite:

   * 4xml: analiza i reserializacja dokumentów XML.
   * 4xpath: rozwiązywanie wyrażeń XPath.
   * 4xslt: silnik przetwarzania XSLT.
   * 4xupdate: Przetwarzanie XUpdate.

%prep
%setup -q -n %{short_name}-XML-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install \
	--install-docs=%{_datadir}/doc/%{name}-%{version} \
	--install-headers=%{_includedir}/4Suite \
	--system
find $RPM_BUILD_ROOT/%{_bindir} -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%py_postclean

cp -a profile $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a test $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/%{name}-%{version}
%{py_sitedir}/Ft
#%{_sysconfdir}/4ss.conf
%{_libdir}/4Suite
%{_datadir}/4Suite
#%{_var}/lib/4Suite

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files -n %{short_name}-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
