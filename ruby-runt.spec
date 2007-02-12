Summary:	Ruby Temporal Expressions
Summary(pl.UTF-8):	Wyrażenia czasowe dla języka Ruby
Name:		ruby-runt
Version:	0.2.0
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/614/runt-%{version}.tgz
# Source0-md5:	2bf595823d47d998183b18a4b2a1cac1
URL:		http://runt.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
#BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runt is an implementation of select temporal patterns by Martin Fowler
in the super-fantastic Ruby language.

%description -l pl.UTF-8
Runt to implementacja wybranych wyrażeń czasowych Martina Fowlera w
języku Ruby.

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
%defattr(644,root,root,755)
%doc rdoc README TODO CHANGES
%{ruby_rubylibdir}/runt
%{ruby_rubylibdir}/runt.rb
