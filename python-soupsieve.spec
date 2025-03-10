# TODO: doc (requires mkdocs-material)
#
# Conditional build:
%bcond_with	doc	# API documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Modern CSS selector implementation for Beautiful Soup
Summary(pl.UTF-8):	Współczesna implementacja wybierania CSS dla Beautiful Soup
Name:		python-soupsieve
# keep 1.x here for python2 support
Version:	1.9.6
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/soupsieve/
Source0:	https://files.pythonhosted.org/packages/source/s/soupsieve/soupsieve-%{version}.tar.gz
# Source0-md5:	056fc893f7e6d4df64c136e07c426342
URL:		https://pypi.org/project/soupsieve/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-backports.functools_lru_cache
BuildRequires:	python-bs4 >= 4.9
BuildRequires:	python-html5lib
BuildRequires:	python-lxml
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-bs4 >= 4.9
BuildRequires:	python3-html5lib
BuildRequires:	python3-lxml
BuildRequires:	python3-pytest
%endif
%endif
%if %{with doc}
BuildRequires:	python-backports.functools_lru_cache
BuildRequires:	python-mkdocs-material >= 2.2.5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Soup Sieve is a CSS selector library designed to be used with
Beautiful Soup 4 (bs4). It aims to provide selecting, matching, and
filtering using modern CSS selectors. Soup Sieve currently provides
selectors from the CSS level 1 specifications up through the latest
CSS level 4 drafts and beyond (though some are not yet implemented).

%description -l pl.UTF-8
Soup Sieve to biblioteka wybierania CSS zaprojektowana z myślą o
używaniu w Beautiful Soup 4 (bs4). Celem jest zapewnienie wyboru,
dopasowywania i filtrowania przy użyciu współczesnego wybierania CSS.
Soup Sieve obecnie zawiera wybieranie ze specyfikacji od CSS poziomu 1
do najnowszych szkiców CSS poziomu 4 i nowszych (ale nie wszystkie są
zaimplementowane).

%package -n python3-soupsieve
Summary:	Modern CSS selector implementation for Beautiful Soup
Summary(pl.UTF-8):	Współczesna implementacja wybierania CSS dla Beautiful Soup
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-soupsieve
Soup Sieve is a CSS selector library designed to be used with
Beautiful Soup 4 (bs4). It aims to provide selecting, matching, and
filtering using modern CSS selectors. Soup Sieve currently provides
selectors from the CSS level 1 specifications up through the latest
CSS level 4 drafts and beyond (though some are not yet implemented).

%description -n python3-soupsieve -l pl.UTF-8
Soup Sieve to biblioteka wybierania CSS zaprojektowana z myślą o
używaniu w Beautiful Soup 4 (bs4). Celem jest zapewnienie wyboru,
dopasowywania i filtrowania przy użyciu współczesnego wybierania CSS.
Soup Sieve obecnie zawiera wybieranie ze specyfikacji od CSS poziomu 1
do najnowszych szkiców CSS poziomu 4 i nowszych (ale nie wszystkie są
zaimplementowane).

%package apidocs
Summary:	API documentation for Python soupsieve module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona soupsieve
Group:		Documentation

%description apidocs
API documentation for Python soupsieve module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona soupsieve.

%prep
%setup -q -n soupsieve-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
mkdocs build --clean --verbose --strict
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py_sitescriptdir}/soupsieve
%{py_sitescriptdir}/soupsieve-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-soupsieve
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{py3_sitescriptdir}/soupsieve
%{py3_sitescriptdir}/soupsieve-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
