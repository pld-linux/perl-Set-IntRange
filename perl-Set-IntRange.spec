#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Set
%define		pnam	IntRange
Summary:	Set::IntRange Perl module - easy manipulation of sets of integers
Summary(pl.UTF-8):	Moduł Perla Set::IntRange - ułatwienie operacji na zbiorach liczb całkowitych
Name:		perl-Set-IntRange
Version:	5.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0c885f01cdcfe624e648f8feb2123297
URL:		http://search.cpan.org/dist/Set-IntRange/
BuildRequires:	perl-Bit-Vector >= 7.1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class lets you dynamically create sets of arbitrary intervals of
integers and perform all the basic operations for sets on them.

%description -l pl.UTF-8
Ta klasa pozwala dynamicznie tworzyć zbiory dowolnych przedziałów
liczb całkowitych i przeprowadzać na nich wszystkie podstawowe
operacje dla zbiorów.

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
%doc README*
%{perl_vendorlib}/Set/IntRange.pm
%{_mandir}/man3/*
