%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	IntRange
Summary:	Set::IntRange - Sets of Integers Easy manipulation of sets of integers
Name:		perl-Set-IntRange
Version:	5.0
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Bit-Vector
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class lets you dynamically create sets of arbitrary intervals of
integers and perform all the basic operations for sets on them (for a
list of available methods and operators, see above).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Set/IntRange.pm
%{_mandir}/man3/*
