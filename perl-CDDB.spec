#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CDDB
Summary:	CDDB - high-level interface to databases based on the Compact Disc DataBase protocol
Summary(pl):	CDDB - wysokopoziomowy interfejs do baz danych opartych o protokó³ CDDB
Name:		perl-CDDB
Version:	1.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CDDB/CDDB-%{version}.tar.gz
# Source0-md5:	4753c73ac7162ab18d1508ae02d40014
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

%description -l pl
CDDB jest wysokopoziomowym interfejsem do baz danych opartych o
protokó³ CDDB (Compact Disc DataBase). Serwery protoko³u CDDB (cddbp)
udostêpniaj± programom, które tego potrzebuj±, informacje o dyskach
CD. Umo¿liwia to takim programom automatyczne wy¶wietlanie tytu³ów
dysków i ¶cie¿ek, a tak¿e dodatkowych informacji, takich jak
komentarze czy s³owa piosenek.

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
