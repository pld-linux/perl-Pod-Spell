#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Spell
Summary:	Pod::Spell -- a formatter for spellchecking Pod
Summary(pl.UTF-8):	Pod::Spell - moduł formatujący do kontroli pisowni dokumentacji Pod
Name:		perl-Pod-Spell
Version:	1.20
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5e4d4c2b74e3cb780c5531cb8bfb04d4
URL:		http://search.cpan.org/dist/Pod-Spell/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-File-ShareDir-Install >= 0.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Tiny
BuildRequires:	perl-File-ShareDir
BuildRequires:	perl-Lingua-EN-Inflect
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::Spell is a Pod formatter whose output is good for spellchecking.
Pod::Spell rather like Pod::Text, except that it doesn't put much
effort into actual formatting, and it suppresses things that look like
Perl symbols or Perl jargon (so that your spellchecking program won't
complain about mystery words like "$thing" or "Foo::Bar" or
"hashref").

%description -l pl.UTF-8
Pod::Spell to moduł formatujący dokumentację Pod, którego wyjście
dobrze nadaje się do sprawdzania pisowni. Zachowuje się podobnie do
Pod::Text, ale nie wkłada wiele wysiłku we właściwe formatowanie, za
to pomija elementy wyglądające na symbole Perla lub perlowy żargon
(dzięki czemu narzędzie do kontroli pisowni nie będzie skarżył się na
tajemnicze słowa takie jak "$coś", "Foo::Bar" czy "hashref".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING Changes
%attr(755,root,root) %{_bindir}/podspell
%{perl_vendorlib}/Pod/Spell.pm
%{perl_vendorlib}/Pod/Wordlist.pm
%{perl_vendorlib}/auto/share/dist/Pod-Spell
%{_mandir}/man1/podspell.1p*
%{_mandir}/man3/Pod::Spell.3pm*
%{_mandir}/man3/Pod::Wordlist.3pm*
