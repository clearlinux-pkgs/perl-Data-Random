#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Random
Version  : 0.13
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/B/BA/BAREFOOT/Data-Random-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BA/BAREFOOT/Data-Random-0.13.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-random-perl/libdata-random-perl_0.12-1.debian.tar.xz
Summary  : 'Perl module to generate random data'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Random-license = %{version}-%{release}
Requires: perl-Data-Random-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(Test::MockTime)

%description
INSTALLATION:
The standard perl module install process:
perl Makefile.PL
make
make test (optional)
make install

%package dev
Summary: dev components for the perl-Data-Random package.
Group: Development
Provides: perl-Data-Random-devel = %{version}-%{release}
Requires: perl-Data-Random = %{version}-%{release}

%description dev
dev components for the perl-Data-Random package.


%package license
Summary: license components for the perl-Data-Random package.
Group: Default

%description license
license components for the perl-Data-Random package.


%package perl
Summary: perl components for the perl-Data-Random package.
Group: Default
Requires: perl-Data-Random = %{version}-%{release}

%description perl
perl components for the perl-Data-Random package.


%prep
%setup -q -n Data-Random-0.13
cd %{_builddir}
tar xf %{_sourcedir}/libdata-random-perl_0.12-1.debian.tar.xz
cd %{_builddir}/Data-Random-0.13
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Random-0.13/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Random
cp %{_builddir}/Data-Random-0.13/LICENSE %{buildroot}/usr/share/package-licenses/perl-Data-Random/52319b44b32ad515e948b5efe0767928780cb8f2
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Random/ac2ab31a23a88a078fb8c9c9410e29d330ab15f1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Random.3
/usr/share/man/man3/Data::Random::WordList.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Random/52319b44b32ad515e948b5efe0767928780cb8f2
/usr/share/package-licenses/perl-Data-Random/ac2ab31a23a88a078fb8c9c9410e29d330ab15f1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Data/Random.pm
/usr/lib/perl5/vendor_perl/5.30.2/Data/Random/WordList.pm
/usr/lib/perl5/vendor_perl/5.30.2/Data/Random/dict
/usr/lib/perl5/vendor_perl/5.30.2/auto/share/dist/Data-Random/README.linux.words
/usr/lib/perl5/vendor_perl/5.30.2/auto/share/dist/Data-Random/README2.linux.words
