%include	/usr/lib/rpm/macros.perl
Summary:	CDDB perl module
Summary(pl):	Modu³ perla do CDDB
Name:		perl-CDDB
Version:	1.08
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/CDDB/CDDB-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module/script gets the CDDB info for an audio cd.

%description -l pl
Ten modu³/skrypt zbiera informacje z bazy CDDB dla p³yt audio CD.

%prep
%setup -q -n CDDB-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/CDDB.pm
%{_mandir}/man3/*
