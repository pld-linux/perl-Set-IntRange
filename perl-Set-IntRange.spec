#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	IntRange
Summary:	Set::IntRange - Sets of Integers Easy manipulation of sets of integers
Summary(pl):	Modu³ Set::IntRange - u³atwiaj±cy operacje na zbiorach liczb ca³kowitych
Name:		perl-Set-IntRange
Version:	5.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Bit-Vector >= 5.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class lets you dynamically create sets of arbitrary intervals of
integers and perform all the basic operations for sets on them.

%description -l pl
Ta klasa pozwala dynamicznie tworzyæ zbiory dowolnych przedzia³ów
liczb ca³kowitych i przeprowadzaæ na nich wszystkie podstawowe
operacje dla zbiorów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%{perl_sitelib}/Set/IntRange.pm
%{_mandir}/man3/*
