#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Time
%define	pnam	Warp
Summary:	Time::Warp - control over the flow of time
Summary(pl.UTF-8):	Time::Warp - kontrola nad upływem czasu
Name:		perl-Time-Warp
Version:	0.5
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JP/JPRIT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	33652a9dfdc11366ddba95efe6432a51
URL:		http://search.cpan.org/dist/Time-Warp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Our external experience unfolds in 3 1/2 dimensions (time has a
dimensionality of 1/2). The Time::Warp module offers developers
control over the measurement of time.

%description -l pl.UTF-8
Nasze zewnętrzne doświadczenie odsłania się w 3.5 wymiarach (czas ma
pół wymiaru). Moduł Time::Warp oferuje programistom kontrolę nad
pomiarem czasu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Time/*.pm
%dir %{perl_vendorarch}/auto/Time/Warp
%attr(755,root,root) %{perl_vendorarch}/auto/Time/Warp/*.so
%{_mandir}/man3/*
