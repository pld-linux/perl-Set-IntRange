%include	/usr/lib/rpm/macros.perl
Summary:	Set-IntRange perl module
Summary(pl):	Modu³ perla Set-IntRange
Name:		perl-Set-IntRange
Version:	5.0
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Set/Set-IntRange-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Bit-Vector
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set-IntRange perl module.

%description -l pl
Modu³ perla Set-IntRange.

%prep
%setup -q -n Set-IntRange-%{version}

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
