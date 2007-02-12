#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CDDB
Summary:	CDDB - high-level interface to databases based on the Compact Disc DataBase protocol
Summary(pl.UTF-8):   CDDB - wysokopoziomowy interfejs do baz danych opartych o protokół CDDB
Name:		perl-CDDB
Version:	1.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CDDB/CDDB-%{version}.tar.gz
# Source0-md5:	b026752a6d25f70ed87a6854b15e93f7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDDB is a high-level interface to cddb protocol servers (freedb and
CDDB). CDDB protocol (cddbp) servers provide compact disc information
for programs that need it. This allows such programs to display disc
and track titles automatically, and it provides extended information
like liner notes and lyrics.

%description -l pl.UTF-8
CDDB jest wysokopoziomowym interfejsem do baz danych opartych o
protokół CDDB (Compact Disc DataBase). Serwery protokołu CDDB (cddbp)
udostępniają programom, które tego potrzebują, informacje o dyskach
CD. Umożliwia to takim programom automatyczne wyświetlanie tytułów
dysków i ścieżek, a także dodatkowych informacji, takich jak
komentarze czy słowa piosenek.

%prep
%setup -q -n CDDB-%{version}

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
%{perl_vendorlib}/CDDB.pm
%{_mandir}/man3/*
