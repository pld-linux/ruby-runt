%define pkgname runt
Summary:	Runt is a Ruby implementation of select temporal patterns
Name:		ruby-%{pkgname}
Version:	0.7.0
Release:	3
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	15c36c030d985091b927f2a1f390fff0
URL:		http://runt.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runt is a Ruby implementation of select temporal patterns by Martin
Fowler.

%package rdoc
Summary:	HTML documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_vendorlibdir}/runt.rb
%{ruby_vendorlibdir}/runt
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Date
%{ruby_ridir}/ExpressionBuilder
%{ruby_ridir}/Runt
%{ruby_ridir}/Time
