%define upstream_name    MooseX-Traits-Pluggable%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	An extension to MooseX::Traits
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::Traits)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch
Requires:	perl(MooseX::Traits)

%description
See the MooseX::Traits manpage for usage information.

Adds support for class precedence search for traits and some extra
attributes, described below.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 655124
- rebuild for updated spec-helper

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 561945
- update to 0.10

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 502105
- update to 0.09

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 421831
- update to 0.08

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 399267
- update to 0.07

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 398852
- update to 0.06
- fixed license field

* Wed Jun 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-2mdv2010.0
+ Revision: 388823
- fix dependencies

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 387835
- import perl-MooseX-Traits-Pluggable


* Sun Jun 21 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist


