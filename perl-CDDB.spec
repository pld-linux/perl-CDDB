%include	/usr/lib/rpm/macros.perl
Summary:	CDDB perl module
Summary(pl):	Modu� perla do CDDB
Name:		perl-CDDB
Version:	1.12
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CDDB/CDDB-%{version}.tar.gz
# Source0-md5:	e426a8ad306748e53fd644862a05e989
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module/script gets the CDDB info for an audio cd.

%description -l pl
Ten modu�/skrypt zbiera informacje z bazy CDDB dla p�yt audio CD.

%prep
%setup -q -n CDDB-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/CDDB.pm
%{_mandir}/man3/*
