#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	IntRange
Summary:	Set::IntRange - Sets of Integers Easy manipulation of sets of integers
Summary(pl):	Moduł Set::IntRange - ułatwiający operacje na zbiorach liczb całkowitych
Name:		perl-Set-IntRange
Version:	5.1
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a0cd165114eda0ab48128e670823066a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Bit-Vector >= 5.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class lets you dynamically create sets of arbitrary intervals of
integers and perform all the basic operations for sets on them.

%description -l pl
Ta klasa pozwala dynamicznie tworzyć zbiory dowolnych przedziałów
liczb całkowitych i przeprowadzać na nich wszystkie podstawowe
operacje dla zbiorów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Set/IntRange.pm
%{_mandir}/man3/*
