#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Spell
Summary:	Pod::Spell -- a formatter for spellchecking Pod
#Summary(pl):	
Name:		perl-Pod-Spell
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SB/SBURKE/Pod-Spell-1.01.tar.gz
# Source0-md5:	aa4964844da2586562aae5208e2dbe61
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::Spell is a Pod formatter whose output is good for
spellchecking.  Pod::Spell rather like Pod::Text, except that
it doesn't put much effort into actual formatting, and it suppresses things
that look like Perl symbols or Perl jargon (so that your spellchecking
program won't complain about mystery words like "$thing" 
or "Foo::Bar" or "hashref").

This class provides no new public methods.  All methods of interest are
inherited from Pod::Parser (which see).  The especially
interesting ones are parse_from_filehandle (which without arguments
takes from STDIN and sends to STDOUT) and parse_from_file.  But you
can probably just make do with the examples in the synopsis though.

This class works by filtering out words that look like Perl or any
form of computerese (like "$thing" or "@{$foo}{'bar','baz'}", anything in
C<...> or F<...> codes, anything in verbatim paragraphs (codeblocks), and
anything in the stopword list.  The default stopword list for a document starts
out from the stopword list defined by Pod::Wordlist, and can be supplemented
(on a per-document basis) by having "=for stopwords" / "=for :stopwords"
region(s) in a document.


# %description -l pl
# TODO

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
%doc ChangeLog README
%{perl_vendorlib}/Pod/*.pm
# some people like to be able to use perldoc not only man (like me)
%{perl_vendorlib}/Pod/Wordlist.pod
#%%{perl_vendorlib}/Pod/Spell
%{_mandir}/man3/*
%{_bindir}/podspell
