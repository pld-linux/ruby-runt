%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby Temporal Expressions
Summary(pl):	Wyra¿enia czasowe dla jêzyka Ruby
Name:		ruby-runt
Version:	0.2.0
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/614/runt-0.2.0.tgz
# Source0-md5:	2bf595823d47d998183b18a4b2a1cac1
URL:		http://runt.rubyforge.org/
BuildRequires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runt is an implementation of select temporal patterns by Martin Fowler
in the super-fantastic Ruby language.

%description -l pl
Runt to implementacja wybranych wyra¿eñ czasowych Martina Fowlera w
jêzyku Ruby.

%prep
%setup -q -n runt-%{version}

%build
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc doc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc rdoc README TODO CHANGES
%defattr(644,root,root,755)
%{ruby_rubylibdir}/runt
%{ruby_rubylibdir}/runt.rb
